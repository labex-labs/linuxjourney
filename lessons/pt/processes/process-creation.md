---
index: 4
lang: "pt"
title: "Criação de Processos"
meta_title: "Criação de Processos - Processos"
meta_description: "Explore os fundamentos da criação de processos no Linux. Este guia abrange as chamadas de sistema fork e execve, relações pai/filho (PID e PPID) e o papel do processo init. Aprenda a criar um processo no Linux e entenda os conceitos centrais da criação de processos no sistema operacional."
meta_keywords: "criação de processos no linux, criação de processo linux, criar um processo no linux, criação de processo no sistema operacional, criação de processo, fork, execve, PID, PPID, processo init, processos Linux"
---

## Lesson Content

Esta lição explora os conceitos fundamentais de como novos processos são iniciados em um sistema Linux. Entender este mecanismo fornece uma visão sobre o funcionamento interno do sistema operacional.

### O Modelo Fork e Exec

O principal mecanismo para **criação de processos no Linux** envolve um processo existente se clonando usando a chamada de sistema `fork`. A chamada `fork` cria um processo filho quase idêntico. Este novo processo filho recebe seu próprio Identificador de Processo (PID) exclusivo, enquanto o processo original se torna seu pai, identificado por um Identificador de Processo Pai (**PPID**).

Após o fork, o processo filho pode continuar executando o mesmo programa que seu pai ou, mais comumente, usar a chamada de sistema `execve` para carregar e executar um novo programa. A chamada `execve` substitui efetivamente o espaço de memória do processo pelo do novo programa, permitindo que uma tarefa diferente comece. Este modelo de dois passos "fork-exec" é um pilar de como você **cria um processo no Linux**.

### Observando Relações Pai-Filho

Podemos observar esta relação pai-filho em ação usando o comando `ps`:

```bash
ps l
```

A opção `l` fornece uma visualização em "formato longo", mostrando mais detalhes sobre os processos em execução. Você verá uma coluna rotulada **PPID**, que significa Parent Process ID (Identificador de Processo Pai). Observe o processo do seu shell atual (por exemplo, `bash`). Quando você executa o comando `ps l`, notará que o **PID** do seu processo shell corresponde ao **PPID** do processo `ps l`. Isso ocorre porque seu shell se bifurcou para criar o processo `ps`.

### O Processo Init

Se todo processo é filho de outro, deve haver um ancestral original. Este é o processo `init`. Quando o sistema é inicializado, o kernel cria `init` como o primeiro processo em espaço de usuário, atribuindo-lhe um PID de 1. O processo `init` é o pai supremo de todos os outros processos e é executado com privilégios de root para gerenciar o sistema. Ele não pode ser encerrado até que o sistema seja desligado e é responsável por iniciar muitos dos serviços que mantêm o sistema funcionando.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão dos processos Linux e seu gerenciamento:

- **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Neste laboratório, você aprenderá habilidades essenciais para gerenciar e monitorar processos em um sistema Linux. Você explorará como interagir com processos em primeiro plano e em segundo plano, inspecioná-los com `ps`, monitorar recursos com `top`, ajustar a prioridade com `renice` e terminá-los com `kill`.

Este laboratório o ajudará a aplicar os conceitos de IDs de processo, IDs de processo pai e monitoramento de processos em um cenário real e a ganhar confiança no gerenciamento de processos.

## Quiz Question

Qual chamada de sistema cria um novo processo? (Por favor, responda em uma única palavra em inglês minúscula.)

## Quiz Answer

fork
