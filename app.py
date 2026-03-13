import streamlit as st
import pandas as pd

# Title
st.title("PsyProAi - Predictive Autonomous Human-Centric Cyber Defense Platform")
st.write("Upload sample emails/messages to see AI threat detection in action.")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV with emails/messages", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(data)

    # Initialize lists
    risk_scores = []
    ai_suggestions = []

    # Simple phishing/social engineering detection
    for content in data['content']:
        content_lower = str(content).lower()
        if "click here" in content_lower or "password" in content_lower or "urgent" in content_lower:
            risk_scores.append("High")
            ai_suggestions.append("Block / Alert User")
        elif "update" in content_lower or "account" in content_lower or "verify" in content_lower:
            risk_scores.append("Medium")
            ai_suggestions.append("Review Message")
        else:
            risk_scores.append("Low")
            ai_suggestions.append("Safe")

    # Add new columns to dataframe
    data['Risk Score'] = risk_scores
    data['AI Copilot Suggestion'] = ai_suggestions

    # Display results
    st.subheader("AI Analysis Results")
    
    # Color-coded display
    def color_risk(val):
        color = 'red' if val == 'High' else 'orange' if val == 'Medium' else 'green'
        return f'background-color: {color}; color: white; font-weight: bold'

    st.dataframe(data.style.applymap(color_risk, subset=['Risk Score']))

    # Optional: Show summary chart
    st.subheader("Risk Score Summary")
    chart_data = data['Risk Score'].value_counts()
    st.bar_chart(chart_data)
else:
    st.info("Please upload a CSV file to start analysis.")