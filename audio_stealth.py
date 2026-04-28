import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import os
import numpy as np

def run_layer1_audio_engine():
    """
    MODERN AUDIO ENGINE (v4.0)
    Optimized for Python 3.14 + Windows.
    Bypasses PyAudio issues using sounddevice chunking.
    """
    print("\n" + "="*50)
    print("🛡️ [LAYER 1] INITIALIZING AUDIO STEALTH SENSOR")
    print("="*50)
    
    fs = 44100  # High-quality sample rate
    seconds = 5  # Capture window
    filename = "temp_stealth.wav"
    
    print(">>> 🟢 Microphone Armed. System is actively monitoring...")
    print(">>> (Speak trigger: 'server is timing out')")
    
    try:
        # 1. Capture the audio buffer
        # This records in a clean 5-second chunk
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait for recording to finish
        
        # 2. Write to a temporary hidden file
        write(filename, fs, myrecording)
        print(">>> ⏳ Audio chunk captured. Running AI transcription...")
        
        # 3. Use SpeechRecognition to analyze the temp file
        recognizer = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)
            
        # 4. Transcribe using Google's Cloud Engine
        recognized_text = recognizer.recognize_google(audio_data)
        print(f">>> 🗣️ Detected Speech: \"{recognized_text}\"")
        
        # 5. Silently delete the temp file (Cleaning the evidence)
        if os.path.exists(filename):
            os.remove(filename)
            
        # --- THE STEALTH TRIGGER LOGIC ---
        text_lower = recognized_text.lower()
        
        # We check for both the full phrase and the keyword "server issue"
        if "server is timing out" in text_lower or "server issue" in text_lower:
            print("\n🚨 [ALERT] STEALTH TRIGGER DETECTED!")
            print(">>> PROTOCOL: HIGH_STRESS_COERCION CONFIRMED.")
            return "HIGH_STRESS_COERCION"
        else:
            print("🟢 [STATUS] Normal speech. System remaining in stealth.")
            return "SAFE"
            
    except sr.UnknownValueError:
        print(">>> 🤷 Speech was not clear enough to analyze. Rescanning...")
        if os.path.exists(filename): os.remove(filename)
        return "SAFE"
    except Exception as e:
        print(f">>> ❌ Engine Error: {e}")
        if os.path.exists(filename): os.remove(filename)
        return "SAFE"

if __name__ == "__main__":
    # Test block to verify the engine without running the full dashboard
    print("Testing Audio Engine independently...")
    run_layer1_audio_engine()