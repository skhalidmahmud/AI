import keyboard  # Import the keyboard module

print("Press any key to stop the loop.")

while True:
    if keyboard.is_pressed():  # Check if any key is pressed
        print("Key pressed, exiting the loop.")
        break  # Exit the loop when any key is pressed


# import speech_recognition as sr

# u = ''

# def test_microphone():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Adjusting for ambient noise...")
#         r.adjust_for_ambient_noise(source)
#         print("Please say something...")
#         audio = r.listen(source, timeout=5, phrase_time_limit=5)
#     try:
#         text = r.recognize_google(audio)
#         print(f"You said: {text}")
#         u = text
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     test_microphone()



# import pyttsx3

# def test_tts():
#     engine = pyttsx3.init()
#     engine.say("Hello, I am your voice assistant.")
#     engine.runAndWait()

# if __name__ == "__main__":
#     test_tts()



# def generate_response(user_input):
#     responses = {
#         "hello": "Hello! How can I help?",
#         "how are you": "I'm doing well, thank you!",
#         "bye": "Goodbye!"
#     }
#     return responses.get(user_input.lower(), "I didn't understand that.")

# def test_response():
#     # user_input = input("You: ")
#     print(f"You: {u}")
#     user_input = u
#     response = generate_response(user_input)
#     print(f"AI: {response}")

# if __name__ == "__main__":
#     test_response()