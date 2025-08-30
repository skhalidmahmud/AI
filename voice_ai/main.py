import speech_recognition as sr

def test_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source)
        print("Please say something...")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_microphone()

