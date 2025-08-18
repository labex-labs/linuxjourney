---
lang: "ru"
title: "Шаблоны поиска Vim"
meta_description: "Изучите шаблоны поиска Vim: прямой (/) и обратный (?) поиск. Перемещайтесь по результатам с помощью 'n' и 'N'. Улучшите свои навыки Vim уже сегодня!"
meta_keywords: "Поиск Vim, команды Vim, текстовый редактор Linux, учебник Vim, руководство Vim, Vim для начинающих"
---

## Lesson Content

Чтобы найти выражение, просто наберите клавишу `/`, а затем ваш поисковый запрос, находясь в сессии Vim. После нажатия Enter вы можете нажать `n` для перехода вперед или `N` для перехода назад по результатам поиска.

```plaintext
My pretty file is very pretty.

/pretty

will find the pretty words in the text file.
```

Команда поиска `?` будет искать в текстовом файле в обратном направлении. Таким образом, в предыдущем примере последнее слово "pretty" будет найдено первым.

```plaintext
My pretty file is very pretty.

?pretty

will find the pretty words in the text file.
```

## Exercise

Поиграйте с клавишей поиска. Откройте текстовый файл в Vim с помощью: `vim [textfile]` и начните поиск!

## Quiz Question

Какая клавиша используется для поиска в Vim?

## Quiz Answer

/
