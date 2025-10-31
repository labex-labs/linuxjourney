---
index: 5
lang: "pt"
title: "Samba"
meta_title: "Samba - Compartilhamento de Rede"
meta_description: "Aprenda a configurar um compartilhamento de rede Samba no Linux. Este guia abrange o protocolo Samba, instalação, configuração e uso de clientes smb linux para conectar-se a compartilhamentos."
meta_keywords: "Samba, smb linux, linux smb, rede samba, protocolo samba, smb samba, compartilhamento de arquivos, smb.conf, cifs, smbclient, tutorial linux"
---

## Lesson Content

Durante décadas, um desafio primordial em ambientes com sistemas operacionais mistos tem sido o compartilhamento de arquivos entre máquinas Windows e Linux. A solução que surgiu é o protocolo Server Message Block (SMB). Originalmente desenvolvido para o Windows, o **protocolo samba** foi posteriormente refinado em um dialeto conhecido como Common Internet File System (CIFS). Hoje, sistemas modernos usam versões mais recentes do SMB, mas os termos são frequentemente usados em conjunto.

Samba é o poderoso conjunto de softwares que implementa o protocolo **SMB/CIFS** no Linux e em outros sistemas do tipo Unix. É a chave para a integração **smb linux**, permitindo que um servidor Linux atue como servidor de arquivos e impressão para clientes Windows, macOS e outros clientes Linux, criando uma **rede samba** contínua. A relação entre **smb samba** é direta: Samba é o software que fala a linguagem SMB.

### Instalando o Samba no Linux

Para começar, você precisa instalar o pacote Samba. O comando varia dependendo do gerenciador de pacotes da sua distribuição Linux. Para sistemas baseados em Debian, como o Ubuntu, use o seguinte:

```bash
sudo apt update
sudo apt install samba
```

### Configurando um Compartilhamento Samba

O arquivo de configuração principal para o Samba está localizado em `/etc/samba/smb.conf`. Este arquivo dita quais diretórios são compartilhados, quem pode acessá-los e suas permissões. O arquivo padrão contém muitos exemplos comentados que servem como uma ótima referência.

Vamos percorrer as etapas para configurar um compartilhamento básico.

Primeiro, abra o arquivo de configuração em um editor de texto:

```bash
sudo nano /etc/samba/smb.conf
```

Na parte inferior do arquivo, adicione uma nova seção para o seu compartilhamento. O nome entre colchetes será o nome do compartilhamento visível na rede.

```ini
[myshare]
    comment = Meu Primeiro Compartilhamento Samba
    path = /my/directory/to/share
    read only = no
    browsable = yes
```

Em seguida, crie o diretório que você especificou na configuração:

```bash
mkdir -p /my/directory/to/share
```

Finalmente, você precisa configurar uma senha específica para o acesso Samba. O Samba mantém seu próprio banco de dados de senhas, que é separado das senhas de usuário do sistema.

```bash
sudo smbpasswd -a [username]
```

Substitua `[username]` por um usuário Linux existente no seu sistema. Você será solicitado a criar uma nova senha para esse usuário para acesso Samba.

### Gerenciando o Serviço Samba

Após fazer alterações no arquivo `smb.conf`, você deve reiniciar o serviço Samba para que elas entrem em vigor.

```bash
sudo service smbd restart
```

### Acessando Compartilhamentos Samba

Depois que seu compartilhamento estiver configurado, os clientes na rede podem acessá-lo.

**Do Windows:**
Abra o prompt Executar (Win + R) ou o Explorador de Arquivos e digite o caminho de rede: `\HOST\sharename`, onde `HOST` é o endereço IP ou nome de host da sua máquina Linux.

**Do Linux:**
O pacote Samba inclui uma ferramenta de linha de comando chamada **smbclient** que permite interagir com qualquer compartilhamento **linux smb** ou Windows.

```bash
smbclient //HOST/myshare -U username
```

Após a conexão, você obterá um prompt `smb: \>` onde poderá usar comandos como `ls`, `get` e `put` para gerenciar arquivos.

### Montando um Compartilhamento Samba

Para um acesso mais permanente, você pode montar o compartilhamento de rede diretamente no seu sistema de arquivos, fazendo-o aparecer como um diretório local.

```bash
sudo mount -t cifs //SERVER/sharename /mnt/mountpoint -o user=username,pass=password
```

Este comando usa o tipo de sistema de arquivos `cifs` para anexar o compartilhamento remoto a um ponto de montagem local.

## Exercise

Tente configurar um compartilhamento Samba simples na sua própria máquina Linux. Crie um diretório, configure-o em `smb.conf` e tente acessá-lo usando `smbclient` a partir da mesma máquina para testar a configuração. Para prática mais aprofundada, explore o abrangente [Caminho de Aprendizagem Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual é o nome do protocolo, um dialeto inicial do SMB, que foi desenvolvido para compartilhamento de arquivos? Por favor, responda em inglês, prestando atenção à capitalização.

## Quiz Answer

CIFS
