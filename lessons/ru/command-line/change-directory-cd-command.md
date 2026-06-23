---
index: 3
lang: "ru"
title: "cd (Смена каталога)"
meta_title: "cd (Смена каталога) - Командная строка"
meta_description: "Изучите команду Linux cd с примерами абсолютных и относительных путей, ярлыков домашнего каталога, перехода к родительским и предыдущим каталогам."
meta_keywords: "команда cd, linux команда cd, смена каталога, cd родительский каталог, cd домой, cd предыдущий каталог, абсолютный путь, относительный путь"
---

## Lesson Content

Чтобы перемещаться по файловой системе Linux, вы используете пути для указания места назначения. Основным инструментом для этого является команда `cd`, сокращение от change directory (сменить каталог). Она изменяет текущий рабочий каталог оболочки.

Основной синтаксис:

```bash
cd [DIRECTORY]
```

### Понимание путей

Существует два способа указать путь: абсолютный и относительный.

- **Абсолютный путь**: полный путь, начинающийся с корневого каталога (`/`). Например: `/home/pete/Desktop`.

- **Относительный путь**: путь, основанный на вашем текущем расположении. Если вы находитесь в `/home/pete/Documents` и хотите получить доступ к подкаталогу с именем `taxes`, вы можете использовать `taxes/`.

### Использование команды cd

Чтобы перейти в конкретный каталог, используя абсолютный путь, введите:

```bash
$ cd /home/pete/Pictures
```

Эта команда переместит вас непосредственно в каталог `Pictures`.

Вы можете проверить своё местоположение с помощью `pwd`:

```bash
$ pwd
/home/pete/Pictures
```

### Переход в подкаталог

Если вы уже находитесь в каталоге и хотите перейти в подкаталог, используйте относительный путь. Например, если ваше текущее расположение `/home/pete/Pictures` и в нем есть папка с именем `Hawaii`, вы можете перейти в неё так:

```bash
$ cd Hawaii
```

Обратите внимание, что мы использовали только имя папки. Это потому, что мы уже находились в её родительском каталоге `/home/pete/Pictures`.

### Важные ярлыки для навигации

Навигация с помощью полных путей может быть утомительной. К счастью, оболочка предоставляет несколько ярлыков, которые делают перемещение гораздо быстрее.

- `.` (текущий каталог): представляет каталог, в котором вы находитесь в данный момент.
- `..` (родительский каталог): поднимает вас на один уровень выше, в каталог, содержащий текущий.
- `~` (домашний каталог): ярлык для вашего личного домашнего каталога, например `/home/pete`.
- `-` (предыдущий каталог): возвращает вас в последний каталог, в котором вы были.

Вы можете использовать эти ярлыки с командой `cd`:

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

Попробуйте эти ярлыки, чтобы стать более эффективным при работе с командной строкой.

### Практические примеры cd

Перейти в домашний каталог:

```bash
$ cd
```

Подняться на два уровня вверх:

```bash
$ cd ../..
```

Перейти в каталог с пробелами в имени, заключив его в кавычки:

```bash
$ cd "Vacation Photos"
```

Вернуться в предыдущий каталог:

```bash
$ cd -
/home/pete/Documents
```

### Часто задаваемые вопросы

**Почему команда cd выводит "No such file or directory"?** Путь не существует относительно вашего текущего расположения, или имя было введено неправильно. Используйте `ls` для просмотра доступных каталогов.

**Почему команда cd выводит "Permission denied"?** У вас нет прав на вход в этот каталог.

**Что происходит, если запустить cd без аргументов?** Вы переходите в свой домашний каталог.

**Работает ли cd с файлами?** Нет. `cd` меняет только каталоги, а не обычные файлы.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux directory navigation:

1. **[Linux cd Command: Directory Changing](https://labex.io/ru/labs/linux-linux-cd-command-directory-changing-209733)** - Learn the Linux `cd` command to efficiently navigate your file system, including various techniques for changing directories, understanding paths, and exploring the file structure.
2. **[Linux Directory Navigation](https://labex.io/ru/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through directories using essential commands.
3. **[Setting Up a New Project Structure](https://labex.io/ru/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts in real scenarios and build confidence with navigating the Linux filesystem.

## Quiz Question

If you are in `/home/pete/Pictures` and want to navigate to the parent directory (`/home/pete`), what is the full command you should use? Please answer in English, paying attention to case and spacing.

## Quiz Answer

cd ..
