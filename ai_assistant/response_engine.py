import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
import wikipedia

class EnhancedResponseEngine:
    def __init__(self):
        # Rule-based responses with patterns
        self.rules = {
            r"hello|hi|hey": "Hello! How can I assist you today?",
            r"weather in (.+)": self.get_weather,
            r"what is (.+)": self.search_definition,
            r"who is (.+)": self.search_person,
            r"latest news about (.+)": self.get_news,
            r"tell me about (.+)": self.wikipedia_search,
            r"search (.+)": self.web_search,
            r"bye|goodbye": "Goodbye! Have a great day!"
        }
    
    def generate_response(self, user_input):
        import re
        
        # Check against rules
        for pattern, response in self.rules.items():
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                if callable(response):
                    return response(match)
                return response
        
        # Default web search if no rules match
        return self.web_search(user_input)
    
    def get_weather(self, match):
        location = match.group(1)
        # Using OpenWeatherMap API (get free API key)
        api_key = "YOUR_OPENWEATHER_API_KEY"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()
            if data["cod"] == 200:
                weather = data["weather"][0]["description"]
                temp = data["main"]["temp"]
                return f"The weather in {location} is {weather} with a temperature of {temp}°C"
            else:
                return f"Sorry, I couldn't find weather information for {location}"
        except:
            return "Weather service is currently unavailable"
    
    def search_definition(self, match):
        term = match.group(1)
        try:
            # Try Wikipedia first
            summary = wikipedia.summary(term, sentences=2)
            return f"According to Wikipedia: {summary}"
        except:
            # Fallback to web search
            return self.web_search(f"definition of {term}")
    
    def get_news(self, match):
        topic = match.group(1)
        # Using NewsAPI (get free API key)
        api_key = "YOUR_NEWSAPI_KEY"
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}&pageSize=3"
        
        try:
            response = requests.get(url)
            data = response.json()
            if data["status"] == "ok":
                articles = data["articles"]
                news = []
                for article in articles:
                    news.append(f"{article['title']}: {article['description']}")
                return "\n\n".join(news)
            else:
                return f"Sorry, I couldn't find news about {topic}"
        except:
            return "News service is currently unavailable"
    
    def wikipedia_search(self, match):
        topic = match.group(1)
        try:
            summary = wikipedia.summary(topic, sentences=3)
            return summary
        except:
            return f"Sorry, I couldn't find information about {topic} on Wikipedia"
    
    def web_search(self, query):
        try:
            # Using DuckDuckGo (no API key required)
            with DDGS() as ddgs:
                results = [r for r, _ in zip(ddgs.text(query, region='wt-wt', max_results=3), range(3))]
            
            if results:
                response = "I found these results:\n\n"
                for i, result in enumerate(results, 1):
                    response += f"{i}. {result['title']}\n{result['body']}\n\n"
                return response
            else:
                return "Sorry, I couldn't find any results for your search"
        except Exception as e:
            return f"Search error: {str(e)}"