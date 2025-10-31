---
index: 3
lang: "pt"
title: "Chamadas de Sistema"
meta_title: "Chamadas de Sistema - Kernel"
meta_description: "Explore os fundamentos de uma chamada de sistema no Linux. Aprenda como processos em espaço de usuário usam chamadas de sistema (syscalls) para solicitar serviços do kernel, mudar de modo e como a tabela de syscalls funciona. Use `strace` para ver chamadas de sistema em ação."
meta_keywords: "chamada de sistema linux, chamadas de sistema, tabela syscall, modo kernel, modo usuário, strace, kernel linux, API syscall"
---

## Lesson Content

Imagine que você está em um grande show. Para ir da área da plateia geral para os bastidores exclusivos, você não pode simplesmente entrar. Você precisa de um passe especial que lhe conceda acesso através de uma porta específica e vigiada. No mundo da computação, as **chamadas de sistema** (system calls) são esses passes especiais.

### O Que São Chamadas de Sistema?

Chamadas de sistema, frequentemente abreviadas como syscalls, fornecem uma maneira para processos em espaço do usuário solicitarem serviços diretamente do kernel. O kernel expõe um conjunto de serviços através da API de chamadas de sistema. Esses serviços são essenciais para operações como ler ou escrever em um arquivo, gerenciar memória ou lidar com conexões de rede. O número de chamadas de sistema disponíveis é fixo; você não pode adicionar novas arbitrariamente. Seu sistema mantém uma `tabela de chamadas de sistema` (syscall table) onde cada chamada de sistema é registrada com um ID exclusivo.

### O Mecanismo de Chamada de Sistema no Linux

Quando você executa um programa como `ls`, o código dentro dele não executa o comando **system call linux** diretamente. Em vez disso, ele usa uma função de biblioteca, que atua como um invólucro (wrapper). Essa função wrapper configura os parâmetros necessários e, em seguida, aciona uma interrupção de software, ou um "trap".

Esse trap sinaliza ao processador para mudar do modo de usuário não privilegiado para o modo de kernel privilegiado. Uma vez no modo kernel, um manipulador de chamada de sistema assume o controle. Ele usa o ID exclusivo para procurar a função solicitada na `tabela de chamadas de sistema` e então a executa. Por exemplo, a chamada de sistema `stat()`, usada para consultar o status de um arquivo, é encontrada e executada dessa maneira. Após o kernel concluir a tarefa, ele alterna o contexto de volta para o modo de usuário e retorna um código de status para o seu processo, indicando sucesso ou erro.

### Visualizando Chamadas de Sistema com strace

Você pode observar as chamadas de sistema que um processo faz em tempo real usando o comando `strace`. Esta ferramenta é incrivelmente útil para depuração e para entender como um programa interage com o kernel.

Para ver as chamadas de sistema feitas pelo comando `ls`, você executaria:

```bash
strace ls
```

Isso gerará uma lista detalhada de cada chamada de sistema que `ls` realiza durante sua execução.

## Exercise

Prática leva à perfeição! Embora o funcionamento interno das chamadas de sistema seja complexo, entender como os programas em espaço do usuário interagem com o kernel é fundamental. A melhor maneira de compreender essa interação é praticando com comandos que realizam essas operações subjacentes. Aqui estão alguns laboratórios práticos para reforçar sua compreensão das interações com o sistema de arquivos, que dependem fortemente de chamadas de sistema:

1. **[Navegue pelo Sistema de Arquivos no Linux](https://labex.io/pt/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Pratique comandos essenciais como `ls`, `cd` e `pwd` para se mover e inspecionar seu sistema de arquivos Linux, engajando-se diretamente com os serviços de sistema de arquivos do kernel.
2. **[Gerencie Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-files-and-directories-in-linux-590835)** - Aprenda a criar, remover, copiar e mover arquivos e diretórios usando comandos como `mkdir`, `rm`, `cp` e `mv`, todos os quais envolvem chamadas de sistema para realizar suas ações.
3. **[Encontre Arquivos e Comandos no Linux](https://labex.io/pt/labs/comptia-find-files-and-commands-in-linux-590834)** - Domine técnicas para localizar arquivos e comandos usando `find`, `whereis` e `which`, ilustrando ainda mais como os comandos do usuário alavancam os serviços do kernel para interagir com o sistema de arquivos.

Esses laboratórios ajudarão você a aplicar os conceitos de interação com o sistema de arquivos em cenários reais e a ganhar confiança com operações fundamentais do Linux que dependem implicitamente de chamadas de sistema.

## Quiz Question

O que é usado para mudar do modo de usuário para o modo kernel? Por favor, responda em inglês, usando duas palavras.

## Quiz Answer

System call
