---
lang: "en"
title: "Samba"
meta_description: "Learn to set up Samba file shares on Linux for Windows and macOS. This beginner's guide covers installation, configuration, and accessing shares. Get started!"
meta_keywords: "Samba, Linux file sharing, smb.conf, CIFS, smbclient, Linux tutorial, beginner guide"
---

## Lesson Content

In the early days of computing, it became necessary for Windows machines to share files with Linux machines; thus, the Server Message Block (SMB) protocol was born. SMB was used for sharing files between Windows operating systems (macOS also has file sharing with SMB) and was later cleaned up and optimized in the form of the Common Internet File System (CIFS) protocol.

Samba is what we call the Linux utilities to work with CIFS on Linux. In addition to file sharing, you can also share resources like printers.

### Create a network share with Samba

Let's go through the basic steps to create a network share that a Windows machine can access:

### Install Samba

```bash
sudo apt update
sudo apt install samba
```

### Setup smb.conf

The configuration file for Samba is found at `/etc/samba/smb.conf`. This file should tell the system what directories should be shared, their access permissions, and more options. The default `smb.conf` comes with lots of commented code already, and you can use those as an example to write your own configurations.

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

In Windows, just type the network connection in the Run prompt: `\\HOST\sharename`.

### Accessing a Samba/Windows share via Linux

```bash
smbclient //HOST/directory -U user
```

The Samba package includes a command-line tool called **smbclient** that you can use to access any Windows or Samba server. Once you're connected to the share, you can navigate and transfer files.

### Attach a Samba share to your system

Instead of transferring files one by one, you can just mount the network share on your system.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Set up a Samba share. If you don't have one, open `smb.conf` and familiarize yourself with the options in the config file.

## Quiz Question

What is the latest protocol used for file transfer between Windows and Linux?

## Quiz Answer

CIFS
