# CSS

There are 3 ways to add CSS to an html

- Inline
- Internal
- External

## Inline

In the tag `style` attribute.

```html
<html style="background: blue">
</html>
```

`background` is what you are changing and `blue` is what you are changing to.

This isn't a great solution for your entire document. Use it for very specific situations or a single element.

## Internal

Use a `style` element in your `head` section.

```html
<html>
    <head>
        <style>
            html {
                background: red;
            }
        </style>
    </head>
</html>
```

Useful to apply to single page document.

## External

Use a new file to store the css.

```html
<html>
    <head>
        <link
            rel="stylesheet"
            href="./styles.css"
        />
    </head>
</html>
```

This is the most commonly used way to implement CSS. This can target multiple webpages.

## CSS Selectors

### Element Selector

Apply to all elements with the `h1` tag.

```css
h1 {
    color: blue
}
```

### Class Selector

Define what you are styling by the class name

```css
.red-text {
    color: red
}
```

```html
<h2 class="red-text">Heading 2</h2>
<p class="red-text">This is a paragraph</p>
```

### Id Selector

```css
#main {
    color: red;
}
```

```html
<h2 id="main">Heading 2</h2>
```

What is the difference between Class and Id selector. Class Selector can be applied to many elements, where the Id should only be ONE element in an html file. There should only be 1 `class="main"`.

### Attribute Selector

Where `p` is the html element you want to select, and you only want to grab `p` elements with the `draggable` attribute and apply css to it (regardless of whether `draggable` is true or false).

```css
p[draggable]{
    color: red
}
```

You can also specifiy the state of the attribute.


```css
p[draggable="false"]{
    color: red
}
```