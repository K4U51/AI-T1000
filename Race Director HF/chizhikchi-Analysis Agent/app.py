from smolagents import CodeAgent,DuckDuckGoSearchTool, HfApiModel,load_tool,tool
import datetime
import requests
import pytz
import yaml
from tools.final_answer import FinalAnswerTool
import pandas as pd
from huggingface_hub import InferenceClient


from Gradio_UI import GradioUI

final_answer = FinalAnswerTool()

# If the agent does not answer, the model is overloaded, please use another model or the following Hugging Face Endpoint that also contains qwen2.5 coder:
# model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud' 

model = HfApiModel(
max_tokens=2096,
temperature=0.5,
model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
custom_role_conversions=None,
)

@tool
def f1_tackinfo_getter(country: str)-> str: #it's import to specify the return type
    """
    Returns data for a specified race
    Args:
        country: A string respresenting a valid country name from the 2024 F1 calendar.
    Returns:
        A string with information about the given race
    """
    df = pd.read_csv('./Formula1_2024season_raceResults.csv')
    # Select only few relevant columns
    df = df[['Track', 'Position', 'Driver', 'Team']]
    info =  str(df.groupby('Track').get_group(country).iloc[:10])
    client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct")
    system_prompt = "You are an expert in F1 race analysis. You will be given data about a race and your goal is to provide a very concise analysis of these results. Your answer should be no more that 5 sentences long. Your answer should only be based on the provided information, do not add anything that is not in the data"
    output = client.chat.completions.create(
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': f'Here is the data about the race: {info}'}
        ]
    )
    return output.choices[0].message.content

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)


agent = CodeAgent(
    model=model,
    tools=[f1_tackinfo_getter, final_answer], ## add your tools here (don't remove final answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name='PitBot',
    description="A Formula 1 race analysis assistant that provides detailed insights about the 2024 F1 season races.", 
    prompt_templates=prompt_templates
)


GradioUI(agent).launch()