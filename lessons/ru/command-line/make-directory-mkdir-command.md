---
lesson_id: "make-directory-mkdir-command"
course_id: "command-line"
lang: "ru"
order_index: 12
title: "mkdir (Создание каталога)"
description: "Научитесь создавать отдельные, несколько и вложенные каталоги с параметрами mkdir."
meta_title: "mkdir (Создание каталога) - Командная строка"
meta_description: "Изучите команду Linux mkdir с примерами создания одного каталога, нескольких каталогов, вложенных родительских каталогов и установки прав доступа."
meta_keywords: "команда mkdir, linux mkdir, создать каталог linux, make directory linux, mkdir -p, mkdir -m, создать папку linux"
---

Команда `mkdir`, сокращение от make directory, создаёт каталоги для организации файлов и других каталогов.

Базовый синтаксис:

```bash
mkdir [OPTIONS] DIRECTORY...
```

## Создание одного каталога

Передайте путь к новому каталогу. Следующий пример создаёт `documents` в текущем рабочем каталоге:

```bash
$ mkdir documents
```

Если запись `documents` уже существует, `mkdir` сообщит об ошибке и не заменит её. Исследуйте существующую запись через `ls -ld documents`.

:::single-choice{#create-one-directory} Какая команда создаёт каталог `documents` в текущем рабочем каталоге?

::option[`mkdir documents`]{#mkdir-documents .correct explanation="`mkdir` создаёт запрошенный каталог по относительному пути `documents`."}
::option[`touch documents`]{#touch-documents explanation="`touch` создаёт пустой обычный файл, если путь отсутствует, а не каталог."}
::option[`cd documents`]{#cd-documents explanation="`cd` пытается войти в существующий каталог и не создаёт отсутствующий."}
:::

## Создание нескольких каталогов

Перечислите несколько путей в одной команде:

```bash
$ mkdir books paintings
```

:::single-choice{#create-separate-directories} Какая команда создаёт два соседних каталога `books` и `paintings`?

::option[`mkdir books/paintings`]{#nested-paintings explanation="Этот путь описывает `paintings` внутри `books`, а не два соседних каталога, и без существующего `books` завершится ошибкой."}
::option[`mkdir "books paintings"`]{#spaced-directory explanation="Кавычки объединяют слова в один путь, поэтому запрашивается один каталог с пробелом в имени."}
::option[`mkdir books paintings`]{#two-directories .correct explanation="Отдельные аргументы предписывают `mkdir` создать два каталога: `books` и `paintings`."}
:::

## Создание отсутствующих родителей

Без параметров `mkdir books/hemingway/favorites` завершится ошибкой, если промежуточного каталога нет. Параметр `-p` создаёт отсутствующих родителей по пути:

```bash
$ mkdir -p books/hemingway/favorites
```

Команда создаёт недостающие части и не сообщает об ошибке только из-за уже существующего конечного каталога. Другие ошибки, например недостаток разрешений, всё равно возможны.

:::single-choice{#create-nested-path} Ни одна часть `projects/app/src` ещё не существует. Какая команда создаст весь путь?

::option[`mkdir -p projects/app/src`]{#mkdir-parents .correct explanation="Параметр `-p` создаёт каждого отсутствующего родителя перед конечным каталогом."}
::option[`mkdir projects/app/src`]{#mkdir-no-parents explanation="Без `-p` создать `src` невозможно, когда промежуточные каталоги отсутствуют."}
::option[`mkdir -m projects/app/src`]{#mkdir-mode-missing explanation="Параметр `-m` требует аргумент режима и не запрашивает создание родителей."}
:::

## Задание начального режима

Параметр `-m MODE` задаёт разрешения нового каталога:

```bash
$ mkdir -m 755 public
```

Режимы будут подробно рассмотрены позже. Здесь `755` даёт владельцу чтение, запись и поиск, а группе и остальным — чтение и поиск.

Добавьте `-v`, чтобы получать сообщение о каждом созданном каталоге:

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

:::single-choice{#set-directory-mode} Какая команда создаёт `public` с режимом разрешений `755`?

::option[`mkdir -p 755 public`]{#parents-755 explanation="`-p` воспринимает оставшиеся слова как пути и не задаёт режим `755`."}
::option[`mkdir -v 755 public`]{#verbose-755 explanation="`-v` печатает сообщения и не интерпретирует `755` как режим."}
::option[`mkdir -m 755 public`]{#mode-public .correct explanation="Параметр `-m` принимает режим, а `public` служит создаваемым путём."}
:::

Для практики:

1. **[Команда Linux mkdir: создание каталогов](https://labex.io/ru/labs/linux-linux-mkdir-command-directory-creating-209739)** — создавайте каталоги, задавайте разрешения и стройте вложенные пути.
2. **[Создание структуры нового проекта](https://labex.io/ru/labs/linux-setting-up-a-new-project-structure-387859)** — создавайте структуру с помощью `mkdir` и перемещайтесь через `cd`.

## Итоги

Теперь вы умеете осознанно создавать структуры каталогов с нужными именами, родителями и режимами.

1. Создавать один или несколько каталогов одной командой.
2. Распознавать ошибку существующего пути.
3. Строить отсутствующих родителей с `-p`.
4. Задавать режим нового каталога через `-m`.
