from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")

yc_Web_page = response.text

soup = BeautifulSoup(yc_Web_page, "html.parser")

article_tag = soup.find_all(name="a", class_="titlelink")

article_texts = []
article_links = []

for article in article_tag:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvote)

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvote[largest_index])

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_anchor_tags = soup.findAll(name='a')
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h3", class_="heading")
# print(heading.getText())
