from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)
website_html = response.text
# We want titles and links

soup = BeautifulSoup(markup=website_html, features="html.parser")
# print(f"soup.title: {soup.title}")
#
# article_tag = soup.select_one(selector=".titleline a")
# print(f"Article Tag: {article_tag}")
#
# article_text = article_tag.text
# print(f"Article Text: {article_text}")
#
# article_link = article_tag.get("href")
# print(f"Article link: {article_link}")
#
# # article_score = soup.select_one(selector=".score").text
# article_score = soup.find(name="span", class_="score").getText()
# print(f"Article Score: {article_score}")

story_links = soup.select(selector=".titleline a")
print(f"story_links: {story_links}")

article_texts = []
article_links = []

for link in story_links:

    # The live site has 2 anchor tags inslide the titleline class.
    # Only get the one with the https link
    if "https" in link.get("href"):
        article_links.append(link.get("href"))
        article_texts.append(link.getText())

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(f"article_texts: {article_texts}")
print(f"article_links: {article_links}")
print(f"article_upvotes: {article_upvotes}")

max_upvote_score = max(article_upvotes)
print(f"max_upvote_score: {max_upvote_score}")
max_upvote_index = article_upvotes.index(max_upvote_score)
highest_voted_title = article_texts[max_upvote_index]
highest_voted_link = article_links[max_upvote_index]

print(f"highest_voted_title: {highest_voted_title}")
print(f"highest_voted_link: {highest_voted_link}")



