from openai import OpenAI
import yaml
import click
from pathlib import Path
from yaml import load, CLoader as Loader

# Path to your openai.yaml in your home directory
openaipath = "/.private/openai.yaml"
chat_logfile = "/.private/chatlog.txt"
home = str(Path.home())

# Load apikey
with open(home + openaipath, "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=Loader)

# Set up the OpenAI API client
client = OpenAI(api_key=cfg["openai"]["api-key"])

@click.command()
def send_request():
    prompt = input("Hello, how can I help you? ")

    # Chat API call
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a succint assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        temperature=0.5,
        n=1
    )

    response = completion.choices[0].message.content
    print(response)

if __name__ == '__main__':
    send_request()

