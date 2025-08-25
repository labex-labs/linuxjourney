---
index: 8
lang: "pt"
title: "niceness"
meta_title: "niceness - Processos"
meta_description: "Aprenda sobre niceness no Linux e prioridade de processo. Entenda os comandos nice e renice para gerenciar o tempo de CPU para processos. Melhore o desempenho do sistema!"
meta_keywords: "niceness Linux, prioridade de processo, comando nice, comando renice, tutorial Linux, agendamento de CPU, Linux para iniciantes, guia Linux"
---

## Lesson Content

Quando você executa várias coisas no seu computador, como talvez Chrome, Microsoft Word ou Photoshop ao mesmo tempo, pode parecer que esses processos estão sendo executados simultaneamente, mas isso não é totalmente verdade.

Os processos usam a CPU por um pequeno período de tempo chamado fatia de tempo. Em seguida, eles pausam por milissegundos, e outro processo recebe uma pequena fatia de tempo. Por padrão, o agendamento de processos acontece dessa forma "round-robin". Cada processo recebe fatias de tempo suficientes até que termine o processamento. O kernel lida com todas essas trocas de processos, e ele faz um trabalho muito bom na maioria das vezes.

Os processos não conseguem decidir quando e por quanto tempo eles recebem tempo de CPU. Se todos os processos se comportassem normalmente, cada um deles (aproximadamente) receberia uma quantidade igual de tempo de CPU. No entanto, existe uma maneira de influenciar o algoritmo de agendamento de processos do kernel com um valor "nice". Niceness é um nome bem estranho, mas o que significa é que os processos têm um número para determinar sua prioridade para a CPU. Um número alto significa que o processo é "nice" e tem uma prioridade mais baixa para a CPU, e um número baixo ou negativo significa que o processo não é muito "nice" e quer obter o máximo de CPU possível.

```bash
top
```

Você pode ver uma coluna para `NI` agora; esse é o nível de "niceness" de um processo.

Para alterar o nível de "niceness", você pode usar os comandos `nice` e `renice`:

```bash
nice -n 5 apt upgrade
```

O comando `nice` é usado para definir a prioridade para um novo processo. O comando `renice` é usado para definir a prioridade em um processo existente.

```bash
renice 10 -p 3245
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento e agendamento de processos Linux:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro e segundo plano, inspecionando-os com `ps`, monitorando recursos com `top`, ajustando a prioridade com `renice` e encerrando-os com `kill`.

Este laboratório o ajudará a aplicar os conceitos de agendamento de processos e "niceness" em cenários reais e a construir confiança no gerenciamento de processos no Linux.

## Quiz Question

Se eu quero que um processo obtenha mais prioridade de CPU, eu uso um número "nice" menor ou maior?

## Quiz Answer

lower
