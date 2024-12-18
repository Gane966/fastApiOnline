import os
import subprocess
import uvicorn
from fastapi import FastAPI
from routes import helloworld
from pyngrok import ngrok
from pathlib import Path
from dotenv import load_dotenv

app = FastAPI()
app.include_router(helloworld.router)

env_file_path = Path(os.getcwd()) / ".env"
load_dotenv(env_file_path)
def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    # Run the FastAPI application using uvicorn
    # Start ngrok tunnel
    NGROK_AUTHTOKEN = os.getenv("NGROK_AUTH_TOCKEN")
    # try:
    #     subprocess.run(["ngrok", "config", "add-authtoken", NGROK_AUTHTOKEN], check=True)
    #     print("Successfully added auth token to ngrok tunnel")
    # except subprocess.CalledProcessError as e:
    #     print(f"Error configuring ngrok authtoken: {e}")
    #     exit("Error configuring ngrok authtoken")
    public_url = ngrok.connect("8000")
    print(f"Public URL: {public_url}")

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
