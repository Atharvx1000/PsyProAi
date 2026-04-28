import time

class AgenticSentinel:
    def __init__(self):
        self.system_status = "SECURE"

    def execute_defense(self, ai_decision: str):
        """
        Layer 3: Takes the text from Gemini and decides on a physical action.
        """
        print("\n🛡️ [LAYER 3] Sentinel evaluating AI report...")
        
        # Professional Logic: Search the AI report for key 'Danger' words
        ai_decision = ai_decision.upper()
        
        if "BLOCK" in ai_decision or "THREAT" in ai_decision or "DO NOT COMPLY" in ai_decision:
            self.lock_system()
        else:
            self.authorize_action()

    def lock_system(self):
        self.system_status = "LOCKED"
        print("❌ [ACTION] CRITICAL THREAT DETECTED.")
        print("❌ [ACTION] LOCKING ALL API TRANSFERS...")
        print("❌ [ACTION] ENCRYPTING LOCAL SENSITIVE DATA...")
        print("📢 [ALERT] Sending silent notification to user's secondary device.")

    def authorize_action(self):
        self.system_status = "AUTHORIZED"
        print("✅ [ACTION] Intent verified. Proceeding with request.")

# Test it
if __name__ == "__main__":
    sentinel = AgenticSentinel()
    # Simulated report from Layer 2
    mock_report = "This is a SECURITY THREAT. DO NOT COMPLY."
    sentinel.execute_defense(mock_report)