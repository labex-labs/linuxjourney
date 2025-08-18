---
index: 10
lang: "pt"
title: "Sistema de arquivos /proc"
meta_title: "Sistema de arquivos /proc - Processos"
meta_description: "Aprenda sobre o sistema de arquivos /proc no Linux, como ele armazena informações de processo e sua estrutura. Explore detalhes de processo com este guia essencial do Linux."
meta_keywords: "sistema de arquivos /proc, processos Linux, informações de processo, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Lembre-se, tudo no Linux é um arquivo, até mesmo os processos. As informações do processo são armazenadas em um sistema de arquivos especial conhecido como sistema de arquivos `/proc`.

```bash
ls /proc
```

Você deve ver vários valores aqui; existem subdiretórios para cada PID. Se você olhasse um PID na saída do `ps`, você seria capaz de encontrá-lo no diretório `/proc`.

Vá em frente e entre em um dos processos e olhe para esse arquivo:

```bash
cat /proc/12345/status
```

Você deve ver informações sobre o estado do processo, bem como informações mais detalhadas. O diretório `/proc` é como o kernel vê o sistema, então há muito mais informações aqui do que você veria em `ps`.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual sistema de arquivos armazena informações de processo?

## Quiz Answer

/proc
