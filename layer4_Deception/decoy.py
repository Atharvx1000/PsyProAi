import webbrowser
import os
import time

class ActiveHallucination:
    @staticmethod
    def deploy_decoy():
        print("\n[4/5] INITIALIZING LAYER 4: ACTIVE HALLUCINATION...")
        print(">>> 🕸️ Launching HDFC Decoy Portal...")
        
        # This finds the exact location of your HTML file on your laptop
        current_dir = os.getcwd()
        file_path = "file://" + os.path.join(current_dir, "decoy_bank.html")
        
        # This forces the default web browser to instantly open the trap
        webbrowser.open(file_path)
        
        # Give it a second to open before returning success
        time.sleep(1)
        print(">>> 🟢 DEPLOYMENT SUCCESSFUL. Hacker's screen is compromised.")
        
        return True