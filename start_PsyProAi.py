import customtkinter as ctk
import threading
import pyperclip
import time

# --- IMPORTING YOUR PSYPROAI LAYERS ---
from audio_stealth import run_layer1_audio_engine 
from Layer2_Brain.brain import LinguisticHeartbeat  
from layer4_Deception.decoy import ActiveHallucination 
from call_interceptor import CallInterceptor  # 👈 NEW: Importing your ear!

# Set the premium dark mode theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class PsyProDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.title("PsyProAi - Neural Defense System.")
        self.geometry("900x600")
        self.resizable(True, True)
        self.after(0, lambda: self.state('zoomed'))

        # Initialize the AI Brain
        self.brain = LinguisticHeartbeat()
        
        # 🎙️ Initialize the Interceptor (Linking it to the UI console)
        self.interceptor = CallInterceptor(callback_function=self.log_to_console)

        # --- GRID LAYOUT ---
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR (Controls) ---
        self.sidebar = ctk.CTkFrame(self, width=280, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(6, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar, text="🛡️ PsyProAi", font=ctk.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 20))

        self.btn_audio = ctk.CTkButton(self.sidebar, text="🎙️ Arm Physical Trap", command=self.start_audio_thread, height=50, width=220, corner_radius=8)
        self.btn_audio.grid(row=1, column=0, padx=20, pady=15, sticky="ew")

        self.btn_scan = ctk.CTkButton(self.sidebar, text="📋 Scan Copied Text", command=self.start_scan_thread, height=50, width=220, corner_radius=8)
        self.btn_scan.grid(row=2, column=0, padx=20, pady=10)

        self.btn_scambait = ctk.CTkButton(self.sidebar, text="🎣 Generate Scam-Bait", command=self.start_scambait_thread, height=50, width=220, corner_radius=8)
        self.btn_scambait.grid(row=3, column=0, padx=20, pady=10)

        # 📞 CONNECTED: Now triggers the real Interceptor thread
        self.btn_call = ctk.CTkButton(self.sidebar, text="📞 Live Call Interceptor", command=self.interceptor.start_interception_thread, height=50, width=220, corner_radius=8)
        self.btn_call.grid(row=4, column=0, padx=20, pady=10)

        self.status_label = ctk.CTkLabel(self.sidebar, text="System Status: STANDBY", text_color="#4caf50", font=ctk.CTkFont(weight="bold"))
        self.status_label.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # --- MAIN CONTENT AREA (Console Output) ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.console_label = ctk.CTkLabel(self.main_frame, text="LIVE THREAT INTELLIGENCE FEED", font=ctk.CTkFont(size=14, weight="bold"))
        self.console_label.pack(pady=(15, 5))

        self.console_box = ctk.CTkTextbox(self.main_frame, width=600, height=500, font=ctk.CTkFont(family="Consolas", size=13))
        self.console_box.pack(padx=20, pady=10, fill="both", expand=True)
        self.log_to_console("System Booted. Awaiting commands...\n")

    # --- HELPER FUNCTION: Log to the UI Console ---
    def log_to_console(self, text):
        # We use a schedule so the thread doesn't crash the main UI
        self.after(0, lambda: self._update_ui_log(text))

    def _update_ui_log(self, text):
        self.console_box.insert("end", text + "\n")
        self.console_box.see("end")

    # --- FEATURE 1: AUDIO TRAP ---
    def start_audio_thread(self):
        self.log_to_console("\n[SYSTEM] Microphone armed. Listening for coercion triggers...")
        self.status_label.configure(text="Status: LISTENING 🎙️", text_color="#ff9800")
        threading.Thread(target=self.run_audio_trap, daemon=True).start()

    def run_audio_trap(self):
        stress_signal = run_layer1_audio_engine()
        if stress_signal == "HIGH_STRESS_COERCION":
            self.log_to_console("🚨 COERCION CONFIRMED. DEPLOYING HDFC DECOY!")
            self.status_label.configure(text="Status: DECOY ACTIVE", text_color="#f44336")
            ActiveHallucination.deploy_decoy()
            self.status_label.configure(text="Status: STANDBY", text_color="#4caf50")

    # --- FEATURE 2: TEXT SCANNER ---
    def start_scan_thread(self):
        threading.Thread(target=self.run_text_scan, daemon=True).start()

    def run_text_scan(self):
        copied_text = pyperclip.paste()
        if not copied_text or len(copied_text) < 10:
            self.log_to_console("\n[ERROR] Clipboard empty. Copy a suspicious message first!")
            return
        
        self.log_to_console(f"\n📋 Analyzing: \"{copied_text[:50]}...\"")
        self.status_label.configure(text="Status: ANALYZING 🧠", text_color="#2196f3")
        
        report = self.brain.analyze_text_threat(copied_text)
        self.log_to_console("-" * 40)
        self.log_to_console(report)
        self.log_to_console("-" * 40)
        self.status_label.configure(text="Status: STANDBY", text_color="#4caf50")

    # --- FEATURE 3: SCAM-BAITER ---
    def start_scambait_thread(self):
        threading.Thread(target=self.run_scambait, daemon=True).start()

    def run_scambait(self):
        copied_text = pyperclip.paste()
        if not copied_text or len(copied_text) < 10:
            self.log_to_console("\n[ERROR] Clipboard empty. Copy the scammer's message first!")
            return
        
        self.log_to_console("\n🎣 Generating decoy reply to waste hacker's time...")
        reply = self.brain.generate_scambait_reply(copied_text)
        self.log_to_console("-" * 40)
        self.log_to_console(reply)
        self.log_to_console("-" * 40)

if __name__ == "__main__":
    app = PsyProDashboard()
    app.mainloop()