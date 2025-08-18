---
lang: "pt"
title: "Controle de Jobs"
meta_title: "Controle de Jobs - Processos"
meta_description: "Aprenda o controle de jobs do Linux para gerenciar processos em segundo plano. Entenda os comandos 'jobs', 'bg', 'fg' e 'kill' para uso eficiente do shell. Comece sua jornada no Linux!"
meta_keywords: "controle de jobs Linux, processos em segundo plano, comando jobs, comando bg, comando fg, comando kill, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

Digamos que você esteja trabalhando em uma única janela de terminal e executando um comando que está demorando uma eternidade. Você não pode interagir com o shell até que ele seja concluído. No entanto, queremos continuar trabalhando em nossas máquinas, então precisamos que o shell esteja aberto. Felizmente, podemos controlar como nossos processos são executados com jobs:

### Enviando um job para o background

Adicionar um e comercial (`&`) ao comando o executará em segundo plano para que você ainda possa usar seu shell. Vejamos um exemplo:

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### Visualizar todos os jobs em segundo plano

Agora você pode visualizar os jobs que acabou de enviar para o background.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

Isso mostrará o ID do job na primeira coluna, depois o status e o comando que foi executado. O **+** ao lado do ID do job significa que é o job em segundo plano mais recente que foi iniciado. O job com o **-** é o segundo comando mais recente.

### Enviando um job para o background em um job existente

Se você já executou um job e deseja enviá-lo para o background, não precisa terminá-lo e começar de novo. Primeiro, suspenda o job com Ctrl-Z e, em seguida, execute o comando **bg** para enviá-lo para o background.

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

### Movendo um job do background para o foreground

Para mover um job para fora do background, basta especificar o ID do job que você deseja. Se você executar `fg` sem nenhuma opção, ele trará de volta o job em segundo plano mais recente (o job com o sinal de + ao lado).

```bash
fg %1
```

### Matar jobs em segundo plano

Semelhante a mover jobs para fora do background, você pode usar a mesma forma para matar os processos usando seus Job IDs.

```bash
kill %1
```

## Exercise

Mova alguns jobs entre o background e o foreground.

## Quiz Question

Qual comando é usado para listar jobs em segundo plano?

## Quiz Answer

jobs
