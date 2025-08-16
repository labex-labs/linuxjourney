---
lang: "pt"
title: "Threads de Processo"
description: "Aprenda sobre threads de processo Linux, conceitos single-threaded vs. multi-threaded e como visualizá-los usando 'ps m'. Entenda processos leves de forma eficiente!"
keywords: "threads Linux, threads de processo, comando ps m, multi-threaded, single-threaded, processos Linux, Linux para iniciantes, tutorial Linux"
---

## Lesson Content

Você pode ter ouvido falar dos termos processos single-threaded e multi-threaded. Threads são muito semelhantes a processos, pois são usados para executar o mesmo programa; eles são frequentemente referidos como processos leves. Se um processo tem uma thread, ele é single-threaded, e se um processo tem mais de uma thread, ele é multi-threaded. No entanto, todos os processos têm pelo menos uma thread.

Processos operam com seus próprios recursos de sistema isolados; no entanto, threads podem compartilhar esses recursos entre si facilmente, tornando a comunicação mais fácil. Às vezes, é mais eficiente ter uma aplicação multi-threaded do que uma aplicação multi-processo.

Basicamente, digamos que você abra o LibreOffice Writer e o Chrome; cada um é seu próprio processo separado. Agora você entra no Writer e começa a editar texto. Quando você edita o texto, ele é salvo automaticamente. Esses dois "processos leves" paralelos de salvar e editar são threads.

Para visualizar as threads de um processo, você pode usar:

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

Os processos são denotados por cada PID, e abaixo dos processos estão suas threads (denotadas por um `--`). Assim, você pode ver que os processos acima são ambos single-threaded.

## Exercise

Execute o comando `ps m` e veja quais processos em execução são multi-threaded.

## Quiz Question

Verdadeiro ou falso, todos os processos começam como single-threaded.

## Quiz Answer

True
