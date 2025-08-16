# uniq (Unique)

## Lesson Content

The uniq (unique) command is another useful tool for parsing text.

Let's say you had a file with lots of duplicates:

<pre>
reading.txt
book
book
paper
paper
article
article
magazine
</pre>

And you wanted to remove the duplicates, well you can use the uniq command:

<pre>$ uniq reading.txt
book
paper
article
magazine</pre>

Let's get the count of how many occurrences of a line:

<pre>$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine</pre>

Let's just get unique values:

<pre>$ uniq -u reading.txt
magazine</pre>

Let's just get duplicate values:

<pre>$ uniq -d reading.txt
book
paper
article
</pre>

<b>Note</b> : uniq does not detect duplicate lines unless they are adjacent. For eg:

Let's say you had a file with duplicates which are not adjacent:

<pre>
reading.txt
book
paper
book
paper
article
magazine
article
</pre>

<pre>$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article</pre>

The result returned by uniq will contain all the entries unlike the very first
example.

To overcome this limitation of uniq we can use sort in combination with uniq:

<pre>
$ sort reading.txt | uniq
article
book
magazine
paper</pre>

## Exercise

What result would you get if you tried uniq -uc?

## Quiz Question

What command would you use to remove duplicates in a file?

## Quiz Answer

uniq
