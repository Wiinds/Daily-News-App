import requests
import smtplib, ssl
import os 
from send_emailv2 import send_email 

api_key = os.getenv("Daily_News_API")


url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"

# make request
response = requests.get(url)

#Get a dictionary with data 
content = response.json()

# Access each article titles 
body = ""
for article in content["articles"][:12]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" \
            + article["description"] + "\n"\
            + article["url"] + 2*"\n"


send_email(body)
    
    

    
    
    
    
    


