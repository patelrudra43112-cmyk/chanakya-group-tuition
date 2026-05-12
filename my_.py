import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# 1. Voice Engine Setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 for Male, 1 for Female

def speak(audio):
    print(f"Jarvis: {audio}")
    engine.say(audio)
    engine.runAndWait()

# 2. Command Sunne ke liye function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSuna raha hoon (Listening)...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Pehchan raha hoon (Recognizing)...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User ne kaha: {query}\n")
    except Exception as e:
        print("Dubara boliye please...")
        return "None"
    return query.lower()

# 3. Main Logic Loop
if __name__ == "__main__":
    .")
    
    while True:
        query = takeCommand()

        # Logic for tasks
        if 'wikipedia' in query:
            speak('Wikipedia par dhoond raha hoon...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Wikipedia ke mutabik")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("YouTube khul gaya hai")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Google khul gaya hai")

        elif 'the time' in query or 'samay' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, abhi {strTime} ho rahe hain")

        elif 'open code' in query:
            codePath = "C:\\Users\\YourName\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # Apna path yahan dalein
            os.startfile(codePath)

        elif 'exit' in query or 'stop' in query or 'bye' in query:
            speak("Goodbye Rudra Sir! Have a productive day.")
            exit()
            
        elif 'none' in query:
            continue
            
        else:
            speak("tare maa no lodo")