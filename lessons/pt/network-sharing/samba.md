---
title: "Samba"
description: "Aprenda a configurar partilhas de ficheiros Samba no Linux para Windows e macOS. Este guia para iniciantes abrange instalação, configuração e acesso a partilhas. Comece já!"
keywords: "Samba, partilha de ficheiros Linux, smb.conf, CIFS, smbclient, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Nos primórdios da computação, tornou-se necessário que as máquinas Windows partilhassem ficheiros com as máquinas Linux; assim, nasceu o protocolo Server Message Block (SMB). O SMB era usado para partilhar ficheiros entre sistemas operativos Windows (o macOS também tem partilha de ficheiros com SMB) e foi posteriormente limpo e otimizado na forma do protocolo Common Internet File System (CIFS).

Samba é o que chamamos às utilidades Linux para trabalhar com CIFS no Linux. Além da partilha de ficheiros, também pode partilhar recursos como impressoras.

### Create a network share with Samba

Vamos percorrer os passos básicos para criar uma partilha de rede que uma máquina Windows pode aceder:

### Install Samba

```bash
sudo apt update
sudo apt install samba
```

### Setup smb.conf

O ficheiro de configuração para o Samba encontra-se em `/etc/samba/smb.conf`. Este ficheiro deve indicar ao sistema quais os diretórios a serem partilhados, as suas permissões de acesso e mais opções. O `smb.conf` padrão vem com muito código comentado, e pode usá-los como exemplo para escrever as suas próprias configurações.

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

No Windows, basta digitar a conexão de rede no prompt Executar: `\\HOST\sharename`.

### Accessing a Samba/Windows share via Linux

```bash
smbclient //HOST/directory -U user
```

O pacote Samba inclui uma ferramenta de linha de comando chamada **smbclient** que pode usar para aceder a qualquer servidor Windows ou Samba. Uma vez conectado à partilha, pode navegar e transferir ficheiros.

### Attach a Samba share to your system

Em vez de transferir ficheiros um por um, pode simplesmente montar a partilha de rede no seu sistema.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Configure uma partilha Samba. Se não tiver uma, abra `smb.conf` e familiarize-se com as opções no ficheiro de configuração.

## Quiz Question

Qual é o protocolo mais recente usado para transferência de ficheiros entre Windows e Linux?

## Quiz Answer

CIFS
