import sounddevice as sd
import numpy as np
import threading
from scipy.io import wavfile
import io
import speech_recognition as sr
from Layer2_Brain.brain import LinguisticHeartbeat

class CallInterceptor:
    def __init__(self, callback_function):
        self.brain = LinguisticHeartbeat()
        self.callback = callback_function
        self.is_running = False
        self.fs = 44100  # Sample rate

    def listen_and_process(self):
        try:
            self.callback("🎙️ [LISTENING] Recording 10 seconds of audio...")
            
            # Record audio using sounddevice (No PyAudio needed!)
            duration = 10  # seconds
            recording = sd.rec(int(duration * self.fs), samplerate=self.fs, channels=1, dtype='int16')
            sd.wait()  # Wait until recording is finished
            
            self.callback("📡 [PROCESSING] Analyzing captured audio...")

            # Convert to buffer for SpeechRecognition
            byte_io = io.BytesIO()
            wavfile.write(byte_io, self.fs, recording)
            byte_io.seek(0)
            
            # Use SpeechRecognition to read the buffer
            recognizer = sr.Recognizer()
            with sr.AudioFile(byte_io) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
                
            self.callback(f"📝 [INTERCEPTED]: {text}")
            
            # Send to AI
            analysis = self.brain.analyze_text_threat(text)
            self.callback(analysis)

        except Exception as e:
            self.callback(f"⚠️ Interceptor Error: {str(e)}")
        finally:
            self.is_running = False

    def start_interception_thread(self):
        if not self.is_running:
            self.is_running = True
            threading.Thread(target=self.listen_and_process, daemon=True).start()