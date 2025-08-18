---
index: 4
lang: "pt"
title: "NFS"
meta_title: "NFS - Compartilhamento de Rede"
meta_description: "Aprenda sobre a configuração do cliente NFS e automounting no Linux. Entenda como se conectar a compartilhamentos de arquivos de rede e usar o automount para acesso contínuo."
meta_keywords: "cliente NFS, automount, Network File System, rede Linux, comando mount, tutorial Linux, iniciante"
---

## Lesson Content

O compartilhamento de arquivos de rede mais padrão para Linux é o NFS (Network File System). O NFS permite que um servidor compartilhe diretórios e arquivos com um ou mais clientes pela rede.

Não entraremos nos detalhes de como criar um servidor NFS, pois pode ser complexo; no entanto, discutiremos a configuração de clientes NFS.

### Setting up NFS client

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### Automounting

Digamos que você use o servidor NFS com bastante frequência e queira mantê-lo montado permanentemente. Normalmente, você pode pensar em editar o arquivo `/etc/fstab`, mas nem sempre você pode conseguir uma conexão com o servidor, e isso pode causar problemas na inicialização. Em vez disso, o que você deseja fazer é configurar o automounting para que você possa se conectar ao servidor NFS quando precisar. Isso é feito com a ferramenta **automount** ou, em versões recentes do Linux, **amd**. Quando um arquivo é acessado em um diretório especificado, o automount procurará o servidor remoto e o montará automaticamente.

## Exercise

Leia a manpage para NFS para saber mais.

## Quiz Question

Qual ferramenta é usada para gerenciar pontos de montagem automaticamente?

## Quiz Answer

automount
