# regex (Regular Expressions)

## Lesson Content

Regular expressions are a powerful tool to do pattern based selection. It uses special notations similar to those we've encountered already such as the * wildcard. 

We'll go through a couple of the most common regular expressions, these are almost universal with any programming language.

Well use this phrase as our test string:
<pre>
sally sells seashells 
by the seashore
</pre>

<b>1. Beginning of a line with ^</b>

<pre>
<b>^</b>by
would match the line "by the seashore"
</pre>

<b>2. End of a line with $</b>

<pre>
seashore<b>$</b>
would match the line "by the seashore"
</pre>

<b>3. Matching any single character with .</b>

<pre>
b<b>.</b>
would match by
</pre>

<b>4. Bracket notation with [] and ()</b>

This can be a little tricky, brackets allow us to specify characters found within the bracket. 

<pre>
d<b>[iou]</b>g
would match: dig, dog, dug
</pre>

The previous anchor tag ^ when used in a bracket means anything except the characters within the bracket. 

<pre>
d<b>[^i]</b>g
would match: dog and dug but not dig
</pre>

Brackets can also use ranges to increase the amount of characters you want to use. 

<pre>
d<b>[a-c]</b>g
will match patterns like dag, dbg, and dcg
</pre>

Be careful though as brackets are case sensitive:

<pre>
d<b>[A-C]</b>g
will match dAg, dBg and dCg but not dag, dbg and dcg
</pre>

And those are some basic regular expressions.

## Exercise

Try to combine regular expressions with grep and search through some files.

<pre>
grep [regular expression here] [file]

## Quiz Question

What regular expression would you use to match a single character?

## Quiz Answer

.