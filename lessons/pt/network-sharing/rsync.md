---
lang: "pt"
title: "rsync"
meta_description: "Aprenda rsync para sincronização e backups eficientes de arquivos Linux. Entenda a transferência de dados remota e local com comandos e opções rsync. Melhore suas habilidades em Linux!"
meta_keywords: "rsync, transferência de arquivos Linux, backup de dados, sincronização de arquivos, tutorial Linux, comandos rsync, iniciante, guia"
---

## Lesson Content

Outra ferramenta usada para copiar dados de diferentes hosts é o rsync (abreviação de remote synchronization). O rsync é muito semelhante ao scp, mas tem uma grande diferença. O rsync usa um algoritmo especial que verifica antecipadamente se já existem dados para os quais você está copiando e copiará apenas as diferenças. Por exemplo, digamos que você estivesse copiando um arquivo e sua rede fosse interrompida; portanto, sua cópia parou no meio do caminho. Em vez de copiar tudo novamente desde o início, o rsync copiará apenas as partes que não foram copiadas.

Ele também verifica a integridade de um arquivo que você está copiando com checksums. Essas pequenas otimizações permitem maior flexibilidade na transferência de arquivos e tornam o rsync ideal para sincronização de diretórios remotamente e localmente, backups de dados, grandes transferências de dados e muito mais.

Algumas opções de rsync comumente usadas:

- v - verbose output
- r - recursive into directories
- h - human-readable output
- z - compressed for easier transfer, great for slow connections

### Copy/sync files on the same host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copy/sync files to local host from a remote host

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copy/sync files to a remote host from a local host

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

Use rsync para sincronizar um diretório com outro diretório. Certifique-se de não sobrescrever um diretório importante!

## Quiz Question

Qual comando seria útil para backups de dados?

## Quiz Answer

rsync
