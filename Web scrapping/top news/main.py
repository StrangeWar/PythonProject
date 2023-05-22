from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
content = response.text

soup = BeautifulSoup(content, 'html.parser')

article_text = []
article_link = []

articles = soup.find_all(name="a", class_="titlelink")
for article in articles:
    link = article.get("href")
    article_link.append(link)
    text = article.get_text()
    article_text.append(text)

article_upvote = [int(vote.getText().split()[0]) for vote in soup.find_all(name="span", class_="score")]

max_vote = max(article_upvote)
index = article_upvote.index(max_vote)
print(article_text[index])
print(article_link[index])
