class F1Agent:
    def __init__(self):
        # Initialize any models or data sources you need here.
        pass

    def get_response(self, query):
        # Here, implement the logic for generating an F1-related answer
        # For example, you could call a machine learning model or a database of F1 stats.
        
        # Placeholder response logic (replace with actual logic)
        if "race winner" in query.lower():
            return "The last race winner was Max Verstappen."
        elif "fastest lap" in query.lower():
            return "The fastest lap time in the last race was 1:14.5."
        else:
            return "Sorry, I couldn't find an answer for that query."