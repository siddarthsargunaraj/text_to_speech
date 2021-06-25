import text_to_speech as speech
import speech_recognition as sr
import quote

def main():
    r = sr.Recognizer()
    understand = False
    speech.speak("Hello User!", "en")
    print("List of commands:")
    print("Exit / Quit: Exit from the voice assistant")
    print("Quote      : Get the positive quote of the day")
    print("Credit     : Obtain the credits")
    speech.speak("The available commands are shown on the screen", "en")
    with sr.Microphone() as source:
        speech.speak("Initializing", "en")
        print("Initialize...")
        r.adjust_for_ambient_noise(source, duration=5)
        r.pause_threshold = 0.8
        while understand is False:
            speech.speak("Listening", "en")
            print("Listening...")
            audio = r.listen(source)
            try:
                converter = r.recognize_google(audio)
                if "exit" in converter:
                    understand = True
                    speech.speak("Have a nice day User", "en")
                elif "quote" in converter:
                    quote.main()
                    understand = True
                elif "credit" in converter:
                    understand = True
                    print("Idea by: Siddarth Sargunaraj")
                    print("Code written by: Siddarth Sargunaraj")
                    print("Quotes obtained from:\n'365 Daily Quotes for Inspired Living' written by Gail Lynne Goodwin")
                else:
                    print("Unknown command")
                    speech.speak("I could not understand. Try again!", "en")
            except sr.UnknownValueError:
                print("Unknown command")
                speech.speak("I could not understand the command. Terminating. Have a nice day user", "en")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

if __name__ == '__main__':
    main()