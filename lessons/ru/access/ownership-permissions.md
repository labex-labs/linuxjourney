---
lang: "ru"
title: "Разрешения владения"
meta_title: "Разрешения владения - Разрешения"
meta_description: "Узнайте, как изменять владение файлами в Linux с помощью команд chown и chgrp. Разберитесь с разрешениями пользователей и групп с помощью этого руководства по Linux для начинающих."
meta_keywords: "chown, chgrp, владение файлами Linux, разрешения Linux, команды Linux, Linux для начинающих, руководство по Linux, учебник по Linux"
---

## Lesson Content

В дополнение к изменению разрешений на файлы, вы также можете изменять владение файлом группой и пользователем.

### Modify user ownership

```bash
sudo chown patty myfile
```

Эта команда установит владельцем `myfile` пользователя `patty`.

### Modify group ownership

```bash
sudo chgrp whales myfile
```

Эта команда установит группу `myfile` в `whales`.

### Modify both user and group ownership at the same time

Если вы добавите двоеточие и имя группы после пользователя, вы сможете установить и пользователя, и группу одновременно.

```bash
sudo chown patty:whales myfile
```

## Exercise

Измените группу и пользователя некоторых тестовых файлов. После этого посмотрите на разрешения с помощью `ls -l`.

## Quiz Question

Какую команду вы используете для изменения владения пользователем?

## Quiz Answer

chown
