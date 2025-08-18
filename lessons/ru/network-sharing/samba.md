---
lang: "ru"
title: "Samba"
meta_title: "Samba - Совместное использование сети"
meta_description: "Узнайте, как настроить общие файловые ресурсы Samba в Linux для Windows и macOS. Это руководство для начинающих охватывает установку, настройку и доступ к общим ресурсам. Начните прямо сейчас!"
meta_keywords: "Samba, общий доступ к файлам Linux, smb.conf, CIFS, smbclient, учебник Linux, руководство для начинающих"
---

## Lesson Content

В первые дни развития вычислительной техники возникла необходимость обмена файлами между машинами Windows и Linux; так родился протокол Server Message Block (SMB). SMB использовался для обмена файлами между операционными системами Windows (macOS также имеет общий доступ к файлам с помощью SMB) и позже был доработан и оптимизирован в форме протокола Common Internet File System (CIFS).

Samba — это набор утилит Linux для работы с CIFS в Linux. Помимо обмена файлами, вы также можете обмениваться такими ресурсами, как принтеры.

### Создание сетевого ресурса с помощью Samba

Давайте рассмотрим основные шаги по созданию сетевого ресурса, к которому может получить доступ машина Windows:

### Install Samba

```bash
sudo apt update
sudo apt install samba
```

### Setup smb.conf

Файл конфигурации для Samba находится по адресу `/etc/samba/smb.conf`. Этот файл должен указывать системе, какие каталоги должны быть общими, их права доступа и другие параметры. По умолчанию `smb.conf` уже содержит много закомментированного кода, и вы можете использовать его в качестве примера для написания собственных конфигураций.

```bash
sudo vi /etc/samba/smb.conf
```

### Set up a password for Samba

```bash
sudo smbpasswd -a [username]
```

### Create a shared directory

```bash
mkdir /my/directory/to/share
```

### Restart the Samba service

```bash
sudo service smbd restart
```

### Accessing a Samba share via Windows

В Windows просто введите сетевое подключение в командной строке Run: `\\HOST\sharename`.

### Accessing a Samba/Windows share via Linux

```bash
smbclient //HOST/directory -U user
```

Пакет Samba включает инструмент командной строки под названием **smbclient**, который вы можете использовать для доступа к любому серверу Windows или Samba. После подключения к общему ресурсу вы можете перемещаться и передавать файлы.

### Attach a Samba share to your system

Вместо того чтобы передавать файлы по одному, вы можете просто смонтировать сетевой ресурс в своей системе.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Настройте общий ресурс Samba. Если у вас его нет, откройте `smb.conf` и ознакомьтесь с параметрами в файле конфигурации.

## Quiz Question

Какой протокол является последним, используемым для передачи файлов между Windows и Linux?

## Quiz Answer

CIFS
