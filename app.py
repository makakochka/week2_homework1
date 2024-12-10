import requests
import time

# response = requests.get("https://news.ycombinator.com/")

r = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
ids = r.json()

top30_stories = []
for id in ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    response = requests.get(url)
    data = response.json()
    top30_stories.append({"title": data.get("title", "No Title"), "url": data.get("url", "No URL")})

for story in top30_stories:
    time.sleep(1)
    print("{" + f"Title: {story['title']} URL: {story['url']}" + "}")
