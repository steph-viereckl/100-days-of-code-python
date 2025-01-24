# HTML Boilerplate


DOCTYPE declaration tells the browser which html version it is using
```html
<!DOCTYPE html>
```

Language of text content is lang = "en". This is important for assistive technologies-->
```html
<html lang="en">
...
</html>
```

`head` section shows important things about the website so it renders correctly. You should always have a `meta` tag. This ensure that the characters are rendered correctly.

```html
<head>
    <meta charset="UTF-8">
    <title>My Website</title>
</head>
```

`title` should also be in the `meta` section.

There are a lot more things that can go into the `head` section.

After `head` element is the `body` element

```html
<body>
    <h1>All content and structure go inside here</h1>
</body>

## Lists

```html
<!-- Unordered List will give us bullets-->
<ul>
    <!-- List items -->
    <li>Harry</li>
    <li>Ron</li>
    <li>Hermoine</li>
</ul>

<!-- Ordered List will give us numbers-->
<ol>
    <!-- List items -->
    <li>Harry</li>
    <li>Ron</li>
    <li>Hermoine</li>
</ol>
```

## Anchor

```html
<a href="www.google.com">This is a link</a>
```

## Global Attribute

Can be set to any html attribute.