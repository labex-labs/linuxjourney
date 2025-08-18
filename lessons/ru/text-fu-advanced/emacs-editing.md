---
lang: "ru"
title: "Редактирование в Emacs"
meta_title: "Редактирование в Emacs - Продвинутый Text-Fu"
meta_description: "Изучите основы редактирования в Emacs: эффективно перемещайтесь по тексту, вырезайте и вставляйте. Это руководство для начинающих поможет вам освоить основные команды Emacs для Linux."
meta_keywords: "Emacs, Emacs учебник, команды Emacs, текстовый редактор, редактор Linux, навигация Emacs, Emacs для начинающих, руководство Emacs"
---

## Lesson Content

### Навигация по тексту

```
C-up arrow: move up one paragraph
C-down arrow: move down one paragraph
C-left arrow: move one word left
C-right arrow: move one word right
M->: move to the end of the buffer
```

При навигации по тексту ваши обычные текстовые кнопки работают как положено: Home, End, Page Up, Page Down, клавиши со стрелками и т.д.

### Вырезание и вставка

Чтобы вырезать (kill) или вставить (yank) в Emacs, вам сначала нужно уметь выделять текст. Чтобы выделить текст, переместите курсор туда, где вы хотите вырезать или вставить, и нажмите `C-space key`. Затем вы можете использовать клавиши навигации для выделения нужного текста. Теперь вы можете вырезать и вставлять следующим образом:

```
C-w: cut
C-y: yank
```

## Exercise

Поиграйте с навигацией по тексту.

## Quiz Question

Как перейти в конец буфера?

## Quiz Answer

M->
