# 100 Days of Code (Python)

### Days Completed: 49 🎉 Days Remaining: 51

___

## Best Practices

- When using methods you didn't write, use keyword parameters so it is clear what you are passing to the method
- If you only need 1 or 2 items from an imported module, use `import module_name`
  - But if you are going to be using many items from that module, be specific using the `from module_name import xyz, abc` so that you don't have to use `module_name.something` all the time
- Don't do `from module import *` because it might be confusing where you get items from
- All method names and variable names should use snake case (`hello_world`)
- All class names should use Pascal Case (`HelloWorld`)

## Class Inheritence 

```python

class Fish(Animal):

    def __init__(self):
        super().__init__()
```

The `Fish` Class inherits from the `Animal` class. To do this, pass in the `Animal` class to the `Fish` class and include `super().__init__()` in the constructor


## File Paths

### Absolute File Path
This is the file path starting from the root directory `/`

`/Stephanie/Documents/GitHub/blah-blah-blah`

### Relative File Path
This is the file path from the working directory, the location from which we are currently working from. To indicate the file path of the current folder, use a `./`

### Moving Directories
To move up in a directory use a dot `.`

For example, to move up a folder and navigate into Desired Folder you would use `../Desired_Folder/file.txt`

To move up 2 folders, do `../../Desired_Folder/file.txt`

To reference something in the same folder, you can do `./file.txt` or shorthand of `file.txt`

## Sending Email

```python
import smtplib
import os
# pip install python-dotenv
from dotenv import load_dotenv

# Object from smtp class to connect to specific provider
with (smtplib.SMTP("smtp.gmail.com") as connection):

    load_dotenv()
    # These are stored in the .env file
    from_email = os.environ.get("FROM_EMAIL", "From Email cannot be found")
    email_password = os.environ.get("PASSWORD", "Email password cannot be found")

    subject_line = f"Subject: Here is the subject line!\n\n"
    message = f"Here is the message in the body of the email"
    combined_message = subject_line + message
    # Was running into issues with encoding so ignoring some chars
    # updated_message = combined_message.encode('ascii', 'ignore').decode('ascii')
    connection.starttls()
    connection.login(user=from_email, password=email_password)
    connection.sendmail(from_addr=from_email,to_addrs=from_email,msg=combined_message.encode("utf-8"))
```

## Open File

```python
with open("file-path.txt", mode="r") as data:
    letter = data.read()
```

## Create new file

```python
new_file = "hello world"

with open("movies-to-watch.txt", "w") as file:
    file.write(new_file)
```

## Web Scraping

```python
from bs4 import BeautifulSoup
import requests

# Get full header here: # https://myhttpheader.com/
header = {
    "Accept-Language":"en-US",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}

response = requests.get(url="www.google.com", headers=header)
website_html = response.text

soup = BeautifulSoup(markup=website_html, features="html.parser")
# Find span where class is...
price = soup.find(name="span", class_="a-price-whole").getText()
decimal = soup.find(name="span", class_="a-price-fraction").getText()
movie_title_tags = soup.find_all(name="h3", class_="title")
# Find tag where element is inside an li tag, and is an h3 element with an id of "title-of-a-story"
song_tags = soup.select("li h3#title-of-a-story")

```
