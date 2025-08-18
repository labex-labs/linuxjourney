---
index: 12
lang: "ru"
title: "Symlinks"
meta_title: "Symlinks - Файловая система"
meta_description: "Узнайте о symlinks и hard links в Linux, включая то, как их создавать и управлять ими. Поймите их различия и варианты использования с помощью этого руководства для начинающих."
meta_keywords: "Linux symlinks, hard links, ln command, symbolic links, Linux file system, Linux tutorial, beginner Linux"
---

## Lesson Content

Давайте используем предыдущий пример информации об inode:

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Вы могли заметить, что мы упускали из виду третье поле в команде `ls`; это поле — счетчик ссылок (link count). Счетчик ссылок — это общее количество жестких ссылок, которые имеет файл. Ну, сейчас это вам ни о чем не говорит, поэтому давайте сначала обсудим ссылки.

### Symlinks

В операционной системе Windows есть так называемые ярлыки (shortcuts). Ярлыки — это просто псевдонимы для других файлов. Если вы что-то сделаете с исходным файлом, вы потенциально можете нарушить работу ярлыка. В Linux эквивалентом ярлыков являются символические ссылки (symbolic links, или soft links, или symlinks). Symlinks позволяют нам ссылаться на другой файл по его имени. Другой тип ссылок, встречающийся в Linux, — это жесткие ссылки (hard links); это фактически другой файл со ссылкой на inode. Давайте посмотрим, что я имею в виду на практике, начиная с symlinks.

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

Вы видите, что я создал символическую ссылку с именем `myfilelink`, которая указывает на `myfile`. Символические ссылки обозначаются `->`. Обратите внимание, что я получил новый номер inode; symlinks — это просто файлы, которые указывают на имена файлов. Когда вы изменяете symlink, файл также изменяется. Номера inode уникальны для файловых систем; вы не можете иметь два одинаковых номера inode в одной файловой системе, что означает, что вы не можете ссылаться на файл в другой файловой системе по его номеру inode. Однако, если вы используете symlinks, они не используют номера inode; они используют имена файлов, поэтому на них можно ссылаться в разных файловых системах.

### Hardlinks

Давайте посмотрим пример hardlink:

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

Hardlink просто создает другой файл со ссылкой на тот же inode. Так что если я изменю содержимое `myfile2` или `myhardlink`, изменение будет видно на обоих. Но если я удалю `myfile2`, файл все равно будет доступен через `myhardlink`. Вот тут-то и вступает в игру наш счетчик ссылок в команде `ls`. Счетчик ссылок — это количество жестких ссылок, которые имеет inode. Когда вы удаляете файл, это уменьшает счетчик ссылок. Inode удаляется только тогда, когда все жесткие ссылки на inode были удалены. Когда вы создаете файл, его счетчик ссылок равен 1, потому что это единственный файл, который указывает на этот inode. В отличие от symlinks, hardlinks не охватывают файловые системы, потому что inodes уникальны для файловой системы.

### Creating a symlink

```bash
ln -s myfile mylink
```

Чтобы создать символическую ссылку, вы используете команду `ln` с опцией `-s` для символической, и указываете целевой файл, а затем имя ссылки.

### Creating a hardlink

```bash
ln somefile somelink
```

Аналогично созданию symlink, за исключением того, что на этот раз вы опускаете `-s`.

## Exercise

Поэкспериментируйте с созданием symlinks и hardlinks. Удалите пару и посмотрите, что произойдет.

## Quiz Question

Какая команда используется для создания symlink?

## Quiz Answer

ln -s
