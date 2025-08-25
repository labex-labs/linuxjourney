---
index: 2
lang: "pt"
title: "rsync"
meta_title: "rsync - Compartilhamento de Rede"
meta_description: "Aprenda rsync para sincronização e backups eficientes de arquivos Linux. Entenda a transferência de dados remota e local com comandos e opções rsync. Melhore suas habilidades em Linux!"
meta_keywords: "rsync, transferência de arquivos Linux, backup de dados, sincronização de arquivos, tutorial Linux, comandos rsync, iniciante, guia"
---

## Lesson Content

Outra ferramenta usada para copiar dados de diferentes hosts é o rsync (abreviação de sincronização remota). O Rsync é muito semelhante ao scp, mas tem uma grande diferença. O Rsync usa um algoritmo especial que verifica antecipadamente se já existem dados para os quais você está copiando e copiará apenas as diferenças. Por exemplo, digamos que você estivesse copiando um arquivo e sua rede fosse interrompida; portanto, sua cópia parou no meio do caminho. Em vez de copiar tudo novamente desde o início, o rsync copiará apenas as partes que não foram copiadas.

Ele também verifica a integridade de um arquivo que você está copiando com somas de verificação (checksums). Essas pequenas otimizações permitem maior flexibilidade na transferência de arquivos e tornam o rsync ideal para sincronização de diretórios remotamente e localmente, backups de dados, grandes transferências de dados e muito mais.

Algumas opções de rsync comumente usadas:

- v - saída detalhada (verbose output)
- r - recursivo em diretórios
- h - saída legível por humanos (human-readable output)
- z - compactado para facilitar a transferência, ótimo para conexões lentas

### Copiar/sincronizar arquivos no mesmo host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copiar/sincronizar arquivos para o host local a partir de um host remoto

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copiar/sincronizar arquivos para um host remoto a partir de um host local

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Caminho de Aprendizagem Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual comando seria útil para backups de dados?

## Quiz Answer

rsync
