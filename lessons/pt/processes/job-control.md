---
index: 11
lang: "pt"
title: "Controle de Tarefas"
meta_title: "Controle de Tarefas - Processos"
meta_description: "Explore nosso tutorial Linux sobre controle de tarefas para gerenciar processos em segundo plano de forma eficaz. Aprenda a usar os comandos jobs, bg, fg e kill para multitarefas poderosas no shell."
meta_keywords: "controle de tarefas Linux, processos em segundo plano, comando jobs, comando bg, comando fg, comando kill, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

No Linux, você frequentemente encontra comandos que demoram muito para serem concluídos. Em vez de esperar e deixar seu terminal inutilizável, você pode usar o **controle de jobs do Linux** para gerenciar essas tarefas. Este recurso poderoso permite executar e gerenciar múltiplos **processos em segundo plano** dentro de uma única sessão de shell, melhorando significativamente seu fluxo de trabalho.

### Executando um Comando em Segundo Plano

Para iniciar um processo diretamente em segundo plano, basta adicionar um e comercial (`&`) ao final do seu comando. Isso retorna imediatamente o prompt do seu shell, permitindo que você continue trabalhando enquanto o comando é executado.

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### Listando Jobs em Segundo Plano

Você pode visualizar todos os jobs sendo executados em segundo plano usando o comando `jobs`.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

A saída fornece o ID do job na primeira coluna, seu status e o comando original. O símbolo `+` indica o job em segundo plano iniciado mais recentemente, enquanto o símbolo `-` marca o segundo job mais recente.

### Gerenciando Processos Ativos

E se um comando já estiver sendo executado em primeiro plano e você decidir que precisa do seu terminal de volta? Você não precisa pará-lo. Primeiro, suspenda o processo em execução pressionando `Ctrl-Z`. Em seguida, use o comando `bg` para enviar esse job suspenso para o segundo plano.

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &
```

Agora, o processo `sleep 1003` está sendo executado como um job em segundo plano, e você pode verificar isso com o comando `jobs`.

### Trazendo um Job para Primeiro Plano

Para trazer um processo em segundo plano de volta para o primeiro plano, use o comando `fg`. Você pode especificar um job específico pelo seu ID (ex: `fg %1`). Se você executar o comando `fg` sem argumentos, ele trará o job em segundo plano mais recente (aquele marcado com `+`) para o primeiro plano.

```bash
fg %1
```

### Terminando Jobs em Segundo Plano

Se você precisar parar um processo em segundo plano, pode usar o comando `kill`. Semelhante ao comando `fg`, você referencia o job usando seu ID prefixado com um sinal de porcentagem (`%`). Esta é uma função chave do controle de jobs do Linux.

```bash
kill %1
```

Dominar esses comandos é essencial para qualquer usuário Linux iniciante que deseja realizar multitarefas de forma eficiente no shell.

## Exercise

Para colocar seu conhecimento sobre controle de jobs do Linux em prática, tente este laboratório prático. Ele o ajudará a solidificar sua compreensão sobre o gerenciamento de processos em primeiro e segundo plano.

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro e segundo plano, monitoramento de recursos e terminação de processos, abordando diretamente o cenário de comandos de longa execução.

## Quiz Question

What command is used to list background jobs? (Please answer in English, using only lowercase letters.)

## Quiz Answer

jobs
