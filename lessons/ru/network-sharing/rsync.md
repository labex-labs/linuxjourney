---
lang: "ru"
title: "rsync"
description: "Изучите rsync для эффективной синхронизации файлов и резервного копирования в Linux. Разберитесь в удаленной и локальной передаче данных с помощью команд и опций rsync. Улучшите свои навыки работы с Linux!"
keywords: "rsync, передача файлов Linux, резервное копирование данных, синхронизация файлов, учебник Linux, команды rsync, для начинающих, руководство"
---

## Lesson Content

Еще один инструмент, используемый для копирования данных с разных хостов, — это rsync (сокращение от remote synchronization). Rsync очень похож на scp, но имеет существенное отличие. Rsync использует специальный алгоритм, который заранее проверяет, есть ли уже данные, которые вы копируете, и копирует только различия. Например, если вы копировали файл и ваше сетевое соединение прервалось; таким образом, ваше копирование остановилось на полпути. Вместо того чтобы копировать все заново с самого начала, rsync скопирует только те части, которые не были скопированы.

Он также проверяет целостность копируемого файла с помощью контрольных сумм. Эти небольшие оптимизации обеспечивают большую гибкость передачи файлов и делают rsync идеальным для синхронизации каталогов удаленно и локально, резервного копирования данных, передачи больших объемов данных и многого другого.

Некоторые часто используемые опции rsync:

- v - verbose output
- r - recursive into directories
- h - human-readable output
- z - compressed for easier transfer, great for slow connections

### Copy/sync files on the same host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copy/sync files to local host from a remote host

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copy/sync files to a remote host from a local host

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

Используйте rsync для синхронизации одного каталога с другим. Убедитесь, что вы не перезапишете важный каталог!

## Quiz Question

Какая команда будет полезна для резервного копирования данных?

## Quiz Answer

rsync
