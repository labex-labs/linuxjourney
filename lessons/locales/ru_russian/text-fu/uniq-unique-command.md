# uniq (Unique)

## Lesson Content

Команда uniq (unique / уникальный) - другой полезный иструмент для обработки текста.

Давайте скажем, что у нас есть файл с множеством дубликатов:

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

И вы хотите удалить эти дубликаты, давайте применим команду uniq:

<pre>$ uniq reading.txt
book
paper
article
magazine</pre>

Давайте получим количество копий для каждой строки в файле:

<pre>$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine</pre>

Давайте просто получим уникальные значения:

<pre>$ uniq -u reading.txt
magazine</pre>

Давайте просто получим дублирующиеся значения:

<pre>$ uniq -d reading.txt
book
paper
article
</pre>

<b>Примечание</b> : uniq не обнаруживает дублирующиеся линии, если они не соседи. Например:

Давайте скажем, что у вас есть файл с дубликатами, которые не соседствуют:

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

Результат, возвращенный uniq содержит все значения, в отличии от первого примера.

Чтобы обойти это ограничение, мы можем использовать uniq вместе с sort:

<pre>
$ sort reading.txt | uniq
article
book
magazine
paper</pre>

## Exercise

Какой результат вы получите, если попробуете выполнить uniq -uc?

## Quiz Question

Какая команда используется для удаления дубликатов в файле?

## Quiz Answer

uniq
