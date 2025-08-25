---
index: 1
lang: "pt"
title: "ps (Processos)"
meta_title: "ps (Processos) - Processos"
meta_description: "Aprenda sobre o comando 'ps' do Linux para visualizar processos em execução e entender os IDs de processo (PIDs). Obtenha um guia para iniciantes sobre gerenciamento de processos."
meta_keywords: "comando ps, processos Linux, ID de processo, PID, tutorial Linux, iniciante, guia, comando top"
---

## Lesson Content

Processos são os programas que estão sendo executados em sua máquina. Eles são gerenciados pelo kernel, e cada processo tem um ID associado a ele chamado **ID do processo (PID)**. Este PID é atribuído na ordem em que os processos são criados.

Execute o comando `ps` para ver uma lista de processos em execução:

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

Isso mostra um rápido instantâneo dos processos atuais:

- PID: ID do Processo
- TTY: Terminal de controle associado ao processo (entraremos em detalhes sobre isso mais tarde)
- STAT: Código de status do processo
- TIME: Tempo total de uso da CPU
- CMD: Nome do executável/comando

Se você olhar a página man para `ps`, verá que há muitas opções de comando que você pode passar. Elas variarão dependendo das opções que você deseja usar — BSD, GNU ou Unix. Na minha opinião, o estilo BSD é mais popular de usar, então vamos com ele. Se você estiver curioso, a diferença entre os estilos é a quantidade de hífens que você usa e as flags.

```bash
ps aux
```

O **a** exibe todos os processos em execução, incluindo os que estão sendo executados por outros usuários. O **u** mostra mais detalhes sobre os processos. E, finalmente, o **x** lista todos os processos que não têm um TTY associado a eles. Esses programas mostrarão um `?` no campo TTY; eles são mais comuns em processos daemon que são iniciados como parte da inicialização do sistema.

Você notará que está vendo muito mais campos agora. Não há necessidade de memorizá-los todos; em um curso posterior sobre processos avançados, revisaremos alguns deles novamente:

- USER: O usuário efetivo (aquele cujo acesso estamos usando)
- PID: ID do Processo
- %CPU: Tempo de CPU usado dividido pelo tempo em que o processo está em execução
- %MEM: Razão do tamanho do conjunto residente do processo para a memória física na máquina
- VSZ: Uso de memória virtual de todo o processo
- RSS: Tamanho do conjunto residente, a memória física não trocada que uma tarefa usou
- TTY: Terminal de controle associado ao processo
- STAT: Código de status do processo
- START: Hora de início do processo
- TIME: Tempo total de uso da CPU
- COMMAND: Nome do executável/comando

O comando `ps` pode ficar um pouco confuso de se olhar. Por enquanto, os campos que mais veremos são PID, STAT e COMMAND.

Outro comando muito útil é o comando **top**. `top` fornece informações em tempo real sobre os processos em execução em seu sistema, em vez de um instantâneo. Por padrão, você terá uma atualização a cada 10 segundos. `top` é uma ferramenta extremamente útil para ver quais processos estão consumindo muitos de seus recursos.

```bash
top
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão dos processos Linux e seu monitoramento:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique habilidades essenciais para gerenciar e monitorar processos em um sistema Linux, incluindo interação com processos em primeiro/segundo plano, inspeção com `ps`, monitoramento com `top` e encerramento com `kill`.
2. **[Comando Linux top: Monitoramento de Sistema em Tempo Real](https://labex.io/pt/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a usar o comando Linux `top` para monitoramento de sistema em tempo real, incluindo classificação de processos, ajuste de intervalos de atualização e filtragem por usuário.

Esses laboratórios o ajudarão a aplicar os conceitos de identificação e monitoramento de processos em cenários reais e a construir confiança com a administração de sistemas Linux.

## Quiz Question

Qual flag do `ps` é usado para visualizar informações detalhadas sobre os processos?

## Quiz Answer

u
