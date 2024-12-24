from fastapi import APIRouter, Request
import requests

router2 = APIRouter(tags=["User_Data"])


def get_location_from_ip(ip_address: str):
    access_token = "your_ipinfo_api_token"  # Get your token from https://ipinfo.io/
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    return response.json()
@router2.get("/user")
async def get_user_ip(request: Request):
    # Get the real client IP address from the 'X-Forwarded-For' header
    client_ip = request.headers.get('X-Forwarded-For', '').split(',')[0]  # Get the first IP address
    print("I got the user IP now I am getting the location : " + client_ip)
    client_address = get_location_from_ip(client_ip)
    return {"client_address": client_address}