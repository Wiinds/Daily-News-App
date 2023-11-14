import requests



api_key = "5dc27eea6fef477a92581918563993b8"

url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5dc27eea6fef477a92581918563993b8"

# make request
request = requests.get(url)

#Get a dictionary with data 
content = request.json()

# Access each article titles 
for article in content["articles"]:
    print(article["title"])
    





