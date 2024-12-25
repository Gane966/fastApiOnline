import os
import subprocess
import uvicorn
from fastapi import FastAPI
from routes import helloworld, user_data, mongodb_connections
from pyngrok import ngrok
from pathlib import Path
from dotenv import load_dotenv

app = FastAPI()
app.include_router(helloworld.router)
app.include_router(user_data.router2)
app.include_router(mongodb_connections.router3)

env_file_path = Path(os.getcwd()) / ".env"
load_dotenv(env_file_path)
def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    # Run the FastAPI application using uvicorn
    # Start ngrok tunnel
    NGROK_AUTHTOKEN = os.getenv("NGROK_AUTH_TOCKEN")
    try:
        subprocess.run(["ngrok", "config", "add-authtoken", NGROK_AUTHTOKEN], check=True)
        print("Successfully added auth token to ngrok tunnel")
    except subprocess.CalledProcessError as e:
        print(f"Error configuring ngrok authtoken: {e}")
        exit("Error configuring ngrok authtoken")

        ######### This is a paid version ###########
    # try:
    #     # Start the ngrok tunnel with the reserved subdomain
    #     domain = os.getenv("DOMAIN")
    #     public_url = ngrok.connect(1729, bind_tls=True, subdomain=domain)
    #     print(f"Public URL: {public_url}")  # This should now print your reserved ngrok domain
    # except subprocess.CalledProcessError as e:
    #     print(f"Error configuring ngrok authtoken: {e}")
    #     exit("Error configuring ngrok authtoken")
    public_url = ngrok.connect("8000")
    print(f"Public URL: {public_url}")

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
