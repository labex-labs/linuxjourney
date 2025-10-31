---
index: 4
lang: "pt"
title: "NFS"
meta_title: "NFS - Compartilhamento de Rede"
meta_description: "Descubra como usar o Sistema de Arquivos de Rede (NFS) no Linux. Esta lição aborda a configuração de um cliente NFS, o uso do comando mount e a configuração do automount para acesso contínuo a compartilhamentos de rede."
meta_keywords: "NFS, cliente NFS, automount, Sistema de Arquivos de Rede, rede Linux, comando mount, tutorial Linux, iniciante"
---

## Lesson Content

O protocolo mais padrão para compartilhamento de arquivos em rede no Linux é o NFS, que significa **Network File System** (Sistema de Arquivos de Rede). O NFS permite que um servidor compartilhe seus diretórios e arquivos com uma ou mais máquinas clientes através de uma rede, fazendo com que pareçam recursos locais.

Esta lição focará na configuração de um **cliente NFS**, pois a configuração de um servidor NFS pode ser um processo mais complexo.

### Montando um Compartilhamento NFS

Para se conectar a um compartilhamento NFS, você primeiro precisa garantir que o serviço cliente NFS esteja em execução. Em seguida, você pode usar o comando `mount` para anexar o diretório remoto a um ponto de montagem local no seu sistema.

```bash
sudo service nfsclient start
sudo mount servidor:/diretorio /diretorio_montagem
```

Neste exemplo, `servidor:/diretorio` é o compartilhamento remoto que você deseja acessar, e `/diretorio_montagem` é o diretório local onde o compartilhamento será montado.

### Usando Automount para NFS

Se você acessa frequentemente um compartilhamento NFS, pode considerar tornar a montagem permanente. Embora adicionar uma entrada ao arquivo `/etc/fstab` seja um método comum para unidades locais, isso pode causar atrasos significativos na inicialização ou até falhas se a conexão de rede ou o servidor NFS não estiverem disponíveis durante a inicialização.

A melhor solução para compartilhamentos de rede é o **automount**. Este serviço, gerenciado pela ferramenta `automount` ou sua implementação moderna `amd`, monta dinamicamente um sistema de arquivos sob demanda. Quando um arquivo ou diretório dentro de um caminho especificado é acessado, o automount conecta-se automaticamente ao servidor remoto e monta o compartilhamento. Isso garante acesso contínuo quando necessário, sem impactar o processo de inicialização do sistema.

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Trilha de Aprendizagem Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual ferramenta é usada para gerenciar pontos de montagem automaticamente? Por favor, responda em inglês, e observe que a resposta diferencia maiúsculas de minúsculas.

## Quiz Answer

automount
