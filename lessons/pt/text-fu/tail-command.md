---
index: 9
lang: "pt"
title: "tail"
meta_title: "tail - Text-Fu"
meta_description: "Aprenda como usar o comando `tail` no Linux para visualizar o final de arquivos e monitorar logs. Descubra `tail -f` para atualizações em tempo real. Comece sua jornada no Linux!"
meta_keywords: "comando tail, Linux tail, tail -f, visualizar logs, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Assim como o comando `head`, o comando `tail` permite que você veja as últimas 10 linhas de um arquivo por padrão.

```bash
tail /var/log/syslog
```

Junto com `head`, você pode alterar o número de linhas que deseja ver.

```bash
tail -n 10 /var/log/syslog
```

Outra ótima opção que você pode usar é a flag `-f` (follow); isso seguirá o arquivo à medida que ele cresce. Experimente e veja o que acontece.

```bash
tail -f /var/log/syslog
```

Seu arquivo `syslog` estará em constante mudança enquanto você interage com seu sistema, e usando `tail -f` você pode ver tudo o que está sendo adicionado a esse arquivo.

## Exercise

Olhe a página man de `tail` e leia alguns dos outros comandos que não discutimos.

```bash
man tail
```

## Quiz Question

Qual é a flag usada para seguir um arquivo em `tail`?

## Quiz Answer

-f
