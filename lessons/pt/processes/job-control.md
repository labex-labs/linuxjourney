---
index: 11
lang: "pt"
title: "Controle de Jobs"
meta_title: "Controle de Jobs - Processos"
meta_description: "Aprenda o controle de jobs do Linux para gerenciar processos em segundo plano. Entenda os comandos 'jobs', 'bg', 'fg' e 'kill' para uso eficiente do shell. Comece sua jornada no Linux!"
meta_keywords: "controle de jobs Linux, processos em segundo plano, comando jobs, comando bg, comando fg, comando kill, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

Digamos que você esteja trabalhando em uma única janela de terminal e executando um comando que está demorando uma eternidade. Você não pode interagir com o shell até que ele seja concluído. No entanto, queremos continuar trabalhando em nossas máquinas, então precisamos que esse shell esteja aberto. Felizmente, podemos controlar como nossos processos são executados com os jobs:

### Enviando um job para o segundo plano

Adicionar um e comercial (`&`) ao comando o executará em segundo plano para que você ainda possa usar seu shell. Vejamos um exemplo:

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### Visualizar todos os jobs em segundo plano

Agora você pode visualizar os jobs que acabou de enviar para o segundo plano.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

Isso mostrará o ID do job na primeira coluna, depois o status e o comando que foi executado. O **+** ao lado do ID do job significa que é o job em segundo plano mais recente que foi iniciado. O job com o **-** é o segundo comando mais recente.

### Enviando um job existente para o segundo plano

Se você já executou um job e deseja enviá-lo para o segundo plano, não precisa terminá-lo e começar de novo. Primeiro, suspenda o job com Ctrl-Z, depois execute o comando **bg** para enviá-lo para o segundo plano.

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &

pete@icebox ~ $ jobs

[1]    Running     sleep 1000 &
[2]    Running     sleep 1001 &
[3]-   Running     sleep 1002 &
[4]+   Running     sleep 1003 &
```

### Movendo um job do segundo plano para o primeiro plano

Para mover um job para fora do segundo plano, basta especificar o ID do job desejado. Se você executar `fg` sem nenhuma opção, ele trará de volta o job em segundo plano mais recente (o job com o sinal + ao lado).

```bash
fg %1
```

### Matar jobs em segundo plano

Semelhante a mover jobs para fora do segundo plano, você pode usar a mesma forma para matar os processos usando seus IDs de Job.

```bash
kill %1
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre o gerenciamento de processos no Linux:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro e segundo plano, monitoramento de recursos e encerramento de processos, abordando diretamente o cenário de comandos de longa duração.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de processos.

## Quiz Question

Qual comando é usado para listar os jobs em segundo plano?

## Quiz Answer

jobs
