from bs4 import BeautifulSoup
# import lxml
# Sometimes you need to use the lxml parser

with open("website.html", mode="r") as data:
    contents = data.read()

soup = BeautifulSoup(markup=contents, features="html.parser")
# soup = BeautifulSoup(markup=contents, parser="lxml")

# Entire element and string
# print(soup.title)
# Name of the title tag
# print(soup.title.name)
# String inside of title tag
# print(soup.title.string)

# Get hold of entire html file
# print(soup.prettify())

# Get the first "a" tag
# print(soup.a)

# Get all the "a" tags
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # Get element
    # print(tag.getText())
    # Get value of attribute
    print(tag.get("href"))

# Get by id. Find to return one or find_all
heading = soup.find(name="h1", id="name")
print(f"heading: {heading}")

# Get by class. Find to return one or find_all
section_heading = soup.find(name="h3", class_="heading")
print(f"section_heading: {section_heading}")
print(f"section_heading: {section_heading.get_text()}")
print(f"section_heading: {section_heading.name}")

# How to drill down into a specific element
# This anchor tag sits inside a paragraph code

# select() all matching items
# select_one() returns the first one
# Selector is the css selector
company_url = soup.select_one(selector="p a")
name_heading = soup.select_one(selector="#name")
headings = soup.select(selector=".heading")

