from django.test import TestCase
from .response_engine import EnhancedResponseEngine

class ResponseEngineTests(TestCase):
    def setUp(self):
        self.engine = EnhancedResponseEngine()
    
    def test_greeting(self):
        response = self.engine.generate_response("Hello")
        self.assertIn("Hello", response)
    
    def test_weather(self):
        response = self.engine.generate_response("weather in London")
        self.assertIn("London", response)
    
    def test_web_search(self):
        response = self.engine.generate_response("search python programming")
        self.assertIn("python", response.lower())
    
    def test_unknown_query(self):
        response = self.engine.generate_response("xyz123")
        self.assertIn("results", response)