---
index: 5
lang: "pt"
title: "Samba"
meta_title: "Samba - Compartilhamento de Rede"
meta_description: "Aprenda a configurar compartilhamentos de arquivos Samba no Linux para Windows e macOS. Este guia para iniciantes abrange instalação, configuração e acesso a compartilhamentos. Comece já!"
meta_keywords: "Samba, compartilhamento de arquivos Linux, smb.conf, CIFS, smbclient, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Nos primórdios da computação, tornou-se necessário que as máquinas Windows compartilhassem arquivos com as máquinas Linux; assim, nasceu o protocolo Server Message Block (SMB). O SMB era usado para compartilhar arquivos entre sistemas operacionais Windows (o macOS também tem compartilhamento de arquivos com SMB) e foi posteriormente limpo e otimizado na forma do protocolo Common Internet File System (CIFS).

Samba é o que chamamos de utilitários Linux para trabalhar com CIFS no Linux. Além do compartilhamento de arquivos, você também pode compartilhar recursos como impressoras.

### Criar um compartilhamento de rede com Samba

Vamos seguir os passos básicos para criar um compartilhamento de rede que uma máquina Windows pode acessar:

### Instalar Samba

```bash
sudo apt update
sudo apt install samba
```

### Configurar smb.conf

O arquivo de configuração para o Samba é encontrado em `/etc/samba/smb.conf`. Este arquivo deve informar ao sistema quais diretórios devem ser compartilhados, suas permissões de acesso e mais opções. O `smb.conf` padrão já vem com muito código comentado, e você pode usá-los como exemplo para escrever suas próprias configurações.

```bash
sudo vi /etc/samba/smb.conf
```

### Configurar uma senha para o Samba

```bash
sudo smbpasswd -a [username]
```

### Criar um diretório compartilhado

```bash
mkdir /my/directory/to/share
```

### Reiniciar o serviço Samba

```bash
sudo service smbd restart
```

### Acessando um compartilhamento Samba via Windows

No Windows, basta digitar a conexão de rede no prompt Executar: `\\HOST\sharename`.

### Acessando um compartilhamento Samba/Windows via Linux

```bash
smbclient //HOST/directory -U user
```

O pacote Samba inclui uma ferramenta de linha de comando chamada **smbclient** que você pode usar para acessar qualquer servidor Windows ou Samba. Uma vez conectado ao compartilhamento, você pode navegar e transferir arquivos.

### Anexar um compartilhamento Samba ao seu sistema

Em vez de transferir arquivos um por um, você pode simplesmente montar o compartilhamento de rede em seu sistema.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Caminho de Aprendizagem Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual é o protocolo mais recente usado para transferência de arquivos entre Windows e Linux?

## Quiz Answer

CIFS
