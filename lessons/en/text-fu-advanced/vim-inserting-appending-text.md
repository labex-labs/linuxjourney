# Title

## Lesson Content

This lesson covers the basics of **HTML** and its conversion to **Markdown**. We will explore common HTML tags and their Markdown equivalents.

### What is HTML?

<p>HTML (HyperText Markup Language) is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.</p>

### What is Markdown?

<p>Markdown is a lightweight markup language for creating formatted text using a plain-text editor. It is often used for writing documentation, blog posts, and README files.</p>

### Converting HTML to Markdown

Let's look at some common conversions:

- **Headings:**
  - `<h1>Heading 1</h1>` becomes `# Heading 1`
  - `<h2>Heading 2</h2>` becomes `## Heading 2`
- **Paragraphs:**
  - `<p>This is a paragraph.</p>` becomes `This is a paragraph.`
- **Bold Text:**
  - `<b>Bold Text</b>` or `<strong>Strong Text</strong>` becomes `**Bold Text**` or `**Strong Text**`
- **Italic Text:**
  - `<i>Italic Text</i>` or `<em>Emphasized Text</em>` becomes `*Italic Text*` or `*Emphasized Text*`
- **Lists:**
  - **Unordered List:**

    ```html
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
    ```

    becomes

    ```markdown
    - Item 1
    - Item 2
    ```

  - **Ordered List:**

    ```html
    <ol>
      <li>First Item</li>
      <li>Second Item</li>
    </ol>
    ```

    becomes

    ```markdown
    1. First Item
    2. Second Item
    ```

- **Code Blocks:**
  - `<pre><code>print("Hello, World!")</code></pre>` becomes

    ```python
    print("Hello, World!")
    ```

- **Links:**
  - `<a href="https://www.example.com">Example Link</a>` becomes `[Example Link](https://www.example.com)`

## Exercise

Convert the following HTML snippet into proper Markdown syntax:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Document</title>
  </head>
  <body>
    <h1>Welcome to My Page</h1>
    <p>
      This is a simple page demonstrating <b>HTML</b> to
      <i>Markdown</i> conversion.
    </p>
    <p>Here are some features:</p>
    <ul>
      <li>Feature One</li>
      <li>Feature Two</li>
      <li>Feature Three</li>
    </ul>
    <p>
      Visit <a href="https://www.google.com">Google</a> for more information.
    </p>
    <pre><code>
        function greet(name) {
            return "Hello, " + name + "!";
        }
        console.log(greet("User"));
    </code></pre>
  </body>
</html>
```

## Quiz Question

Which Markdown syntax is used to represent an unordered list?

a) `1. Item`
b) `# Item`
c) `* Item`
d) `**Item**`

## Quiz Answer

The correct answer is **c) `* Item`**.
