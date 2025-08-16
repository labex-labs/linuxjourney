# less

## Lesson Content

If you are viewing text files larger than a simple output, less is more. (There is actually a command called more that does something similar, so this is ironic.) The text is displayed in a paged manner, so you can navigate through a text file page by page.

Go ahead and look at the contents of a file with less. Once you’re in the less command, you can actually use other keyboard commands to navigate in the file.

<pre>$ less /home/pete/Documents/text1</pre>

Use the following command to navigate through less:

<ul>
<li>q - Used to quit out of less and go back to your shell.</li>
<li>Page up, Page down, Up and Down - Navigate using the arrow keys and page keys.</li>
<li>g - Moves to beginning of the text file.</li>
<li>G - Moves to the end of the text file.</li>
<li>/search - You can search for specific text inside the text document. Prefacing the words you want to search with /</li>
<li>h - If you need a little help about how to use less while you’re in less, use help.</li>
</ul>

## Exercise

Run less on a file, then page up and around the file. Try searching for a specific word. Quickly navigate to the beginning or the end of the file.

## Quiz Question

How do you quit out of a less command?

## Quiz Answer

q
