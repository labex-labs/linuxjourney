---
lang: "ru"
title: "Setgid"
meta_title: "Setgid - Разрешения"
meta_description: "Узнайте о разрешениях Linux SGID (Set Group ID), как они работают и как их изменять. Разберитесь в этой важнейшей концепции безопасности Linux."
meta_keywords: "Linux SGID, Set Group ID, разрешения Linux, chmod g+s, безопасность Linux, Linux для начинающих, учебник по Linux"
---

## Lesson Content

Подобно биту разрешения set user ID, существует бит разрешения set group ID (SGID). Этот бит позволяет программе запускаться так, как если бы она была членом этой группы.

Рассмотрим один пример:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

Теперь мы видим, что бит разрешения находится в наборе разрешений группы.

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

Числовое представление для SGID — 2.

## Exercise

No exercises for this lesson.

## Quiz Question

Какое число представляет SGID?

## Quiz Answer

2
