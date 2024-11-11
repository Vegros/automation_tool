import speech_recognition as sr
import pyttsx3
import time


def listen_for_a_word():
    
    recogniser = sr.Recognizer()
    
    try:
        with sr.Microphone() as mic:
            
            recogniser.adjust_for_ambient_noise(mic, duration=1.0)

        
            full_text = ""
            listening = True

            print("Start speaking. I am listening...")

            while listening:
                try:
                    audio = recogniser.listen(mic, timeout=5, phrase_time_limit=5)

                    text = recogniser.recognize_google(audio)
                    full_text += " " + text.lower()
                    print(f"Partial recognition: {text}")

                except sr.WaitTimeoutError:
                    print("Timeout: No speech detected. Listening again...")
                    continue
                except sr.UnknownValueError:
                    print("Couldn't understand. Please try again.")
                    continue

                
                time.sleep(1)  
                listening = False 
                
                print(f"Final recognized sentence: {full_text.strip()}")
                return full_text.strip()
        

    except sr.RequestError:
        print("API unavailable or quota exceeded.")
        return None

