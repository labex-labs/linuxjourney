---
lesson_id: "move-mv-command"
course_id: "command-line"
lang: "ru"
order_index: 11
title: "mv (Перемещение)"
description: "Научитесь переименовывать и перемещать файлы и каталоги, избегая нежелательной перезаписи."
meta_title: "mv (Перемещение) - Командная строка"
meta_description: "Изучите команду Linux mv с примерами перемещения файлов, переименования файлов и каталогов, перемещения нескольких файлов и предотвращения перезаписи."
meta_keywords: "linux mv команда, команда mv, перемещение файлов linux, переименование файла linux, переименование каталога linux, mv -i, mv -n, mv -t"
---

Команда `mv` переименовывает файл или каталог либо перемещает его. В отличие от `cp`, после успешной операции исходный путь не остаётся на месте.

Базовый синтаксис:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

## Переименование файлов и каталогов

Сначала укажите текущий путь, затем новый.

Переименование файла:

```bash
$ mv oldfile newfile
```

В том же порядке переименовывается каталог:

```bash
$ mv old_directory_name new_directory_name
```

:::single-choice{#rename-file-with-mv} Какая команда переименовывает `cat` в `dog` в текущем каталоге?

::option[`mv cat dog`]{#rename-cat .correct explanation="`mv` воспринимает `cat` как источник, а `dog` — как новый путь назначения."}
::option[`mv dog cat`]{#rename-dog explanation="Аргументы переставлены: команда попытается переименовать существующий `dog` в `cat`."}
::option[`cp cat dog`]{#copy-cat explanation="`cp` создаст копию `dog`, сохранив `cat`, а не выполнит переименование."}
:::

## Перемещение в каталог

Если последний аргумент — существующий каталог, `mv` помещает источник внутрь:

```bash
$ mv file2 /home/pete/Documents
```

Для нескольких источников перечислите их, а целевой каталог поставьте последним:

```bash
$ mv file_1 file_2 somedirectory/
```

GNU `mv` также поддерживает `-t`, чтобы указать целевой каталог раньше источников:

```bash
$ mv -t somedirectory/ file_1 file_2
```

В отличие от `cp`, для каталога `mv` не нужен рекурсивный параметр.

:::single-choice{#move-multiple-files} Какая команда перемещает `file_1` и `file_2` в существующий `archive/`?

::option[`mv archive/ file_1 file_2`]{#target-first-without-option explanation="Без GNU `-t` при нескольких источниках целевой каталог должен стоять последним."}
::option[`mv -r file_1 file_2 archive/`]{#recursive-move explanation="`mv` не использует `-r` для файлов или каталогов; обычная форма уже выполняет нужное перемещение."}
::option[`mv file_1 file_2 archive/`]{#target-last .correct explanation="При нескольких источниках последний существующий каталог служит назначением для обоих файлов."}
:::

## Управление существующим назначением

По умолчанию `mv` может заменить существующее назначение. Проверьте пути и при необходимости выберите политику:

- `-i`: спросить перед заменой.

  ```bash
  $ mv -i source_file destination_directory
  ```

- `-n`: не перезаписывать существующее назначение.

  ```bash
  $ mv -n source_file destination_directory
  ```

- `-b`: в GNU/Linux создать резервную копию заменяемого назначения, обычно с суффиксом `~`.

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- `-v`: показывать каждое перемещение.

```bash
$ mv -v file1 file2 somedirectory/
```

:::single-choice{#move-without-overwriting} Какая команда перемещает `draft.txt` в `finished/` только если не произойдёт перезапись?

::option[`mv -i draft.txt finished/`]{#interactive-draft explanation="`-i` задаёт вопрос, но при подтверждении перезапись всё же произойдёт."}
::option[`mv -b draft.txt finished/`]{#backup-draft explanation="`-b` разрешает замену, сохраняя резервную копию прежнего назначения, а не запрещает её."}
::option[`mv -n draft.txt finished/`]{#no-clobber-draft .correct explanation="`-n` пропускает перемещение, если оно перезаписало бы существующее назначение."}
:::

## Перемещение каталогов и совпадений шаблона

Каталог перемещается без `-r`:

```bash
$ mv project /home/pete/Documents/
```

Шаблоны оболочки выбирают несколько источников:

```bash
$ ls *.txt
$ mv *.txt notes/
```

Предварительный `ls` помогает заметить слишком широкий шаблон до изменения путей.

:::single-choice{#move-directory-without-recursion} Какая команда перемещает каталог `project/` в `/srv/archive/`?

::option[`mv -r project/ /srv/archive/`]{#recursive-project explanation="Для этой цели `mv` не нужен и не поддерживается `-r`; каталоги обрабатываются обычным перемещением."}
::option[`mv project/ /srv/archive/`]{#move-project .correct explanation="Обычный синтаксис `mv` перемещает каталог в существующее назначение без рекурсивного флага."}
::option[`cp project/ /srv/archive/`]{#copy-project explanation="Обычная `cp` не перемещает каталог и для копирования потребовала бы рекурсии; источник также остался бы."}
:::

:::single-choice{#preview-text-file-move} Перед `mv *.txt notes/` какая команда показывает пути, выбранные тем же шаблоном?

::option[`ls '*.txt'`]{#literal-text-pattern explanation="Кавычки запрещают раскрытие `*`, и команда ищет буквальное имя со звёздочкой."}
::option[`ls *.txt`]{#list-text-matches .correct explanation="Оболочка раскрывает `*.txt` для `ls` так же, как для `mv`, позволяя сначала увидеть нескрытые имена."}
::option[`mv -v *.txt notes/`]{#verbose-text-move explanation="Подробный режим сообщает о перемещениях во время выполнения, а не даёт просмотр без изменений."}
:::

Для практики:

1. **[Команда Linux mv: перемещение и переименование](https://labex.io/ru/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** — перемещайте и переименовывайте файлы и каталоги.
2. **[Организация файлов и каталогов](https://labex.io/ru/labs/linux-organizing-files-and-directories-387877)** — примените `mv`, `cp` и `rm` к структуре проекта.

## Итоги

Теперь вы умеете переименовывать и перемещать пути, защищая существующие назначения.

1. Ставить источник перед новым путём.
2. Размещать целевой каталог после нескольких источников.
3. Спрашивать, пропускать или создавать резервную копию перед заменой.
4. Перемещать каталоги без рекурсивного параметра.
5. Проверять совпадения шаблона перед массовой операцией.
