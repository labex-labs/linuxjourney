---
index: 4
lang: "pt"
title: "NFS"
meta_title: "NFS - Compartilhamento de Rede"
meta_description: "Aprenda sobre a configuração do cliente NFS e a montagem automática no Linux. Entenda como se conectar a compartilhamentos de arquivos de rede e usar a montagem automática para acesso contínuo."
meta_keywords: "cliente NFS, automount, Network File System, rede Linux, comando mount, tutorial Linux, iniciante"
---

## Lesson Content

O compartilhamento de arquivos de rede mais padrão para Linux é o NFS (Network File System). O NFS permite que um servidor compartilhe diretórios e arquivos com um ou mais clientes pela rede.

Não entraremos em detalhes sobre como criar um servidor NFS, pois pode ser complexo; no entanto, discutiremos a configuração de clientes NFS.

### Configurando o cliente NFS

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### Montagem Automática

Digamos que você use o servidor NFS com bastante frequência e queira mantê-lo montado permanentemente. Normalmente, você pode pensar em editar o arquivo `/etc/fstab`, mas nem sempre você pode conseguir uma conexão com o servidor, e isso pode causar problemas na inicialização. Em vez disso, o que você deseja fazer é configurar a montagem automática para que você possa se conectar ao servidor NFS quando precisar. Isso é feito com a ferramenta **automount** ou, em versões recentes do Linux, **amd**. Quando um arquivo é acessado em um diretório especificado, o automount procurará o servidor remoto e o montará automaticamente.

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Caminho de Aprendizagem Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual ferramenta é usada para gerenciar pontos de montagem automaticamente?

## Quiz Answer

automount
