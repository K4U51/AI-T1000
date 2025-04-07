import gradio as gr

# Define the F1 prediction logic (use your model or function here)
def predict_f1(driver, track):
    # Logic to make prediction based on the inputs
    return f"Predicted result for {driver} at {track}"

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# F1 Prediction")
    with gr.Row():
        driver_input = gr.Dropdown(choices=["Verstappen", "Leclerc", "Hamilton"], label="Driver")
        track_input = gr.Textbox(label="Track")
    prediction = gr.Textbox(label="Prediction Result")
    
    driver_input.change(predict_f1, [driver_input, track_input], prediction)

# Launch the interface
demo.launch()