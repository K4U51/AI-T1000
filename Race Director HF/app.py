import gradio as gr
import requests

# Define the URL for the Jolpica API
API_URL = "http://localhost:8000/ergast/f1/"

def query_f1(question):
    """
    Handles user questions and fetches data from the Jolpica F1 API.
    """
    try:
        response = requests.get(API_URL, params={"query": question})
        
        if response.status_code != 200:
            return f"Error: Received status code {response.status_code}, Response: {response.text}"

        # Print raw response for debugging
        print("Raw API Response:", response.text)

        # Return response data
        try:
            data = response.json()
            return f"API Response: {data}"
        except requests.exceptions.JSONDecodeError:
            return "Error: API response is not in JSON format."

    except requests.exceptions.RequestException as e:
        return f"Network Error: {str(e)}"

# Gradio UI
iface = gr.Interface(
    fn=query_f1,
    inputs=gr.Textbox(lines=2, placeholder="Ask me about F1 races, drivers, or standings..."),
    outputs="text",
    title="F1 Chatbot",
    description="Ask me anything about Formula 1, and I'll fetch the latest race data for you!"
)

if __name__ == "__main__":
    iface.launch()
