# sort

## Lesson Content

Команда sort (сортировать) полезна для сортировки строк.

<pre>
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
</pre>

Вы также можете сделать обратную сортировку:

<pre>$ sort -r file1.txt
elephant
dog
cow
cat
bird
</pre>

А также сортировать по числовым значениям:

<pre>$ sort -n file1.txt
bird
cat
cow
elephant
dog
</pre>

## Exercise

Огромная сила sort приходит с возможностью быть комбинированным с другими командами, попробуйте следующую команду и посмотрите, что произойдет?

<pre>$ ls /etc | sort -rn</pre>

## Quiz Question

Какой флаг используется для обратной сортировки?

## Quiz Answer

-r
