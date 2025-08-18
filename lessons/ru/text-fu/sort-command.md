---
lang: "ru"
title: "sort"
meta_title: "sort - Text-Fu"
meta_description: "Узнайте, как использовать команду Linux sort для сортировки текстовых файлов. Откройте для себя такие опции, как обратная и числовая сортировка. Улучшите свои навыки работы с командной строкой Linux!"
meta_keywords: "Команда Linux sort, sort -r, sort -n, учебник Linux, командная строка, Linux для начинающих, руководство по sort"
---

## Lesson Content

Команда `sort` полезна для сортировки строк.

```plaintext
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
```

Вы также можете выполнить обратную сортировку:

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

А также сортировать по числовому значению:

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

Настоящая мощь `sort` проявляется в ее способности комбинироваться с другими командами. Попробуйте следующую команду и посмотрите, что произойдет:

```bash
ls /etc | sort -rn
```

## Quiz Question

Какой флаг вы используете для выполнения обратной сортировки?

## Quiz Answer

-r
