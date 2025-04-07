import requests
import gradio as gr

# SportsData.io API key (replace with your actual API key)
API_KEY = 'your_api_key_here'

# Base URL for SportsData.io API
BASE_URL = 'https://api.sportsdata.io/v4/mma/scores/json'

# Headers for authentication
headers = {
    'Ocp-Apim-Subscription-Key': API_KEY
}

# Fetch Fighter Rankings
def get_fighter_rankings():
    url = f'{BASE_URL}/FighterRankings'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Failed to fetch data from API', 'status_code': response.status_code}

# Fetch Fighter Details by ID
def get_fighter_details(fighter_id):
    url = f'{BASE_URL}/Fighter/{fighter_id}'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Failed to fetch fighter details', 'status_code': response.status_code}

# Fetch Upcoming Events
def get_upcoming_events():
    url = f'{BASE_URL}/UpcomingEvents'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Failed to fetch upcoming events', 'status_code': response.status_code}

# Fetch Recent Events
def get_recent_events():
    url = f'{BASE_URL}/RecentEvents'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Failed to fetch recent events', 'status_code': response.status_code}

# Gradio Interface
def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## MMA API: Get Fighter Rankings, Details, and Events")
        
        with gr.Tab("Fighter Rankings"):
            fighter_rankings_output = gr.Textbox()
            gr.Button("Get Fighter Rankings").click(get_fighter_rankings, outputs=fighter_rankings_output)
        
        with gr.Tab("Fighter Details"):
            fighter_id_input = gr.Number(label="Enter Fighter ID")
            fighter_details_output = gr.Textbox()
            gr.Button("Get Fighter Details").click(get_fighter_details, inputs=fighter_id_input, outputs=fighter_details_output)
        
        with gr.Tab("Upcoming Events"):
            upcoming_events_output = gr.Textbox()
            gr.Button("Get Upcoming Events").click(get_upcoming_events, outputs=upcoming_events_output)
        
        with gr.Tab("Recent Events"):
            recent_events_output = gr.Textbox()
            gr.Button("Get Recent Events").click(get_recent_events, outputs=recent_events_output)
        
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(debug=True)
