---
lang: "pt"
title: "Detalhes do Processo"
meta_description: "Aprenda sobre os detalhes dos processos Linux, como o kernel gerencia recursos e o que são processos. Entenda os conceitos de processo para iniciantes."
meta_keywords: "processos Linux, kernel, gerenciamento de processos, ps aux, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Antes de entrarmos em aplicações mais práticas de processos, precisamos primeiro entender o que são e como funcionam. Esta parte pode ser confusa, pois estamos nos aprofundando nos detalhes, então sinta-se à vontade para retornar a esta lição se não quiser aprender sobre isso agora.

Um processo, como dissemos antes, é um programa em execução no sistema. Mais precisamente, é o sistema alocando memória, CPU e I/O para fazer o programa rodar. Um processo é uma instância de um programa em execução. Vá em frente e abra 3 janelas de terminal. Em duas janelas, execute o comando `cat` sem passar nenhuma opção (o processo `cat` permanecerá aberto como um processo porque espera stdin). Agora, na terceira janela, execute: `ps aux | grep cat`. Você verá que existem dois processos para `cat`, mesmo que estejam chamando o mesmo programa.

O kernel é o responsável pelos processos. Quando executamos um programa, o kernel carrega o código do programa na memória, determina e aloca recursos e, em seguida, monitora cada processo. Ele sabe:

- O status do processo
- Os recursos que o processo está usando e recebendo
- O proprietário do processo
- Tratamento de sinais (mais sobre isso depois)
- E basicamente todo o resto

Todos os processos estão tentando obter uma fatia daquele doce bolo de recursos. É trabalho do kernel garantir que os processos recebam a quantidade certa de recursos, dependendo das demandas do processo. Quando um processo termina, os recursos que ele usou são agora liberados para outros processos.

## Exercise

No exercises for this lesson.

## Quiz Question

O que gerencia e controla os processos?

## Quiz Answer

kernel
