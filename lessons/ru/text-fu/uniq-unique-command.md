---
lang: "ru"
title: "uniq (Уникальный)"
meta_description: "Узнайте, как использовать команду Linux `uniq` для удаления повторяющихся строк из текстовых файлов. Откройте для себя такие опции, как -c, -u, -d, и комбинируйте с `sort` для эффективной очистки данных."
meta_keywords: "команда uniq, Linux uniq, удалить дубликаты, sort uniq, учебник Linux, обработка текста, Linux для начинающих, руководство по Linux"
---

## Lesson Content

Команда `uniq` (unique) — еще один полезный инструмент для анализа текста.

Предположим, у вас есть файл с большим количеством дубликатов:

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

И вы хотите удалить дубликаты; для этого можно использовать команду `uniq`:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Давайте получим количество вхождений каждой строки:

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

Давайте получим только уникальные значения:

```bash
$ uniq -u reading.txt
magazine
```

Давайте получим только дублирующиеся значения:

```bash
$ uniq -d reading.txt
book
paper
article
```

**Примечание**: `uniq` не обнаруживает дублирующиеся строки, если они не являются смежными. Например:

Предположим, у вас есть файл с дубликатами, которые не являются смежными:

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

Результат, возвращаемый `uniq`, будет содержать все записи, в отличие от самого первого примера.

Чтобы преодолеть это ограничение `uniq`, мы можем использовать `sort` в комбинации с `uniq`:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

Какой результат вы получите, если попробуете `uniq -uc`?

## Quiz Question

Какую команду вы бы использовали для удаления дубликатов в файле?

## Quiz Answer

uniq
