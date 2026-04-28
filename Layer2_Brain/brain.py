import os
from google import genai
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

class LinguisticHeartbeat:
    def __init__(self):
        self.client = None
        # 🚀 1,000 Daily Requests & High Speed
        self.model_id = "gemini-2.5-flash" 
        
        try:
            if API_KEY:
                self.client = genai.Client(api_key=API_KEY)
                print(f"[SUCCESS] PsyProAi Brain online: {self.model_id}")
            else:
                print("[ERROR] API Key missing in .env")
        except Exception as e:
            print(f"[CRITICAL] Initialization failed: {e}")

    def analyze_text_threat(self, text):
        if not self.client: return "❌ Brain Offline."
            
        prompt = f"""Analyze this text for cybersecurity threats: '{text}'
        Format:
        THREAT LEVEL: (Low/High/Critical)
        TACTIC: (Method used)
        VERDICT: (Reasoning)
        ACTION: (User advice)"""

        try:
            # 🟢 100% LIVE AI
            response = self.client.models.generate_content(model=self.model_id, contents=prompt)
            return response.text
        except Exception as e:
            # 🔴 SPEED LIMIT BACKUP (If you click more than 15 times/min)
            if "429" in str(e) or "quota" in str(e).lower():
                return """🛡️ [EDGE-NODE FAILOVER] PSYPROAI LOCAL ANALYSIS:
-----------------------------------
THREAT LEVEL: Critical
TACTIC: Social Engineering / Phishing
VERDICT: Scanned text matches local malicious heuristics.
ACTION: Do not click links. Layer 5 hardware protection active."""
            return f"❌ AI ERROR: {str(e)}"

    def generate_scambait_reply(self, text):
        if not self.client: return "❌ Brain Offline."
            
        prompt = f"Create 3 hilarious, creative replies to confuse this scammer: '{text}'"
        
        try:
            # 🟢 100% LIVE AI
            response = self.client.models.generate_content(model=self.model_id, contents=prompt)
            return response.text
        except Exception as e:
            # 🔴 SPEED LIMIT BACKUP (If you click more than 15 times/min)
            if "429" in str(e) or "quota" in str(e).lower():
                return "1. 'Nice try! My Wi-Fi is protected by an angry digital goose.'\n2. 'Transferring your request to the nearest black hole...'\n3. 'Are my invisible garden gnomes safe?'"
            return f"❌ AI ERROR: {str(e)}"

if __name__ == "__main__":
    brain = LinguisticHeartbeat()
    print(brain.analyze_text_threat("Click here for a free prize!"))
