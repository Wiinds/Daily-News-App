import requests
#import smtplib, ssl
#import os 
from send_email import send_email 


api_key = "5dc27eea6fef477a92581918563993b8"

url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5dc27eea6fef477a92581918563993b8"

# make request
request = requests.get(url)

#Get a dictionary with data 
content = request.json()

# Access each article titles 
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"
        send_email(body)
    
    
    #print(article["title"])
    
    
    
    
    


