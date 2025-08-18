---
index: 8
lang: "pt"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "Aprenda a usar o comando 'head' do Linux para visualizar o início dos arquivos. Entenda opções como -n para contagem de linhas. Tutorial essencial de comando Linux."
meta_keywords: "comando head, Linux head, visualizar início de arquivo, tutorial Linux, comandos Linux, Linux para iniciantes, head -n, guia Linux"
---

## Lesson Content

Digamos que temos um arquivo muito longo; na verdade, temos muitos para escolher. Vá em frente e `cat /var/log/syslog`. Você deve ver páginas e páginas de texto. E se eu quisesse ver apenas as primeiras linhas deste arquivo de texto? Bem, podemos fazer isso com o comando `head`. Por padrão, o comando `head` mostrará as 10 primeiras linhas de um arquivo.

```bash
head /var/log/syslog
```

Você também pode modificar a contagem de linhas para o que quiser. Digamos que eu quisesse ver as 15 primeiras linhas em vez disso.

```bash
head -n 15 /var/log/syslog
```

A flag `-n` significa "number of lines" (número de linhas).

## Exercise

O que o seguinte comando faz e por quê?

```bash
head -c 15 /var/log/syslog
```

## Quiz Question

Qual flag você usaria para alterar o número de linhas que você deseja visualizar para o comando `head`?

## Quiz Answer

-n
