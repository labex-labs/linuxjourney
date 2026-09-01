---
lesson_id: "exit-command"
course_id: "command-line"
lang: "pt"
order_index: 19
title: "exit"
description: "Aprenda a sair do shell atual e escolher o status que ele devolve ao processo chamador."
meta_title: "exit - Linha de Comando"
meta_description: "Aprenda o comando exit do Linux, como encerrar uma sessão do shell, a diferença entre logout e exit e como funcionam os códigos de saída."
meta_keywords: "comando exit, exit Linux, comando logout, sessão shell, sair terminal, status de saída, exit Bash"
---

Os shells podem ser aninhados: um terminal gráfico inicia um shell, uma conexão SSH inicia um shell remoto e um shell pode iniciar outro shell. Sair de um deles normalmente devolve o controle ao processo que iniciou o shell atual.

## Saída do Shell Atual

O comando `exit` solicita que o shell atual seja encerrado:

```bash
$ exit
```

Se esse shell for o processo principal de uma aba do terminal gráfico, a aba poderá ser fechada de acordo com as configurações do terminal. Em uma sessão SSH, sair do shell remoto normalmente leva você de volta ao shell local. Se você iniciou um shell aninhado, `exit` retorna ao shell pai.

:::single-choice{#leave-current-shell} Você iniciou o Bash dentro de outro shell e agora quer retornar ao shell pai. Qual comando deve executar na sessão aninhada do Bash?

::option[`clear`]{#clear-nested explanation="`clear` atualiza a área visível do terminal, mas mantém o shell atual em execução."}
::option[`exit`]{#exit-nested .correct explanation="`exit` encerra o shell atual, permitindo que o shell pai retome o controle."}
::option[`history -c`]{#clear-nested-history explanation="Esse comando limpa a lista do histórico do Bash na memória. Ele não encerra o shell atual."}
:::

## Retorno de um Status de Saída

Um argumento numérico opcional define o status devolvido ao processo chamador do shell:

```bash
$ exit 0
```

Por convenção, `0` significa sucesso, e um valor diferente de zero representa falha ou outra condição definida pelo programa. Se o Bash não receber um argumento numérico, ele sairá com o status do último comando executado antes de `exit`.

:::single-choice{#return-success-status} Qual comando encerra o shell atual e informa explicitamente sucesso ao processo chamador?

::option[`exit 0`]{#exit-zero .correct explanation="Por convenção, o status `0` informa ao chamador uma conclusão bem-sucedida."}
::option[`exit 1`]{#exit-one explanation="Por convenção, um status diferente de zero indica falha ou outro resultado excepcional, não sucesso."}
::option[`logout 0`]{#logout-zero explanation="O `logout` do Bash serve para um shell de login e não usa essa forma para definir o status solicitado."}
:::

:::single-choice{#exit-without-number} No Bash, qual status `exit` devolve quando você não fornece um número?

::option[Ele sempre devolve o status de sucesso `0`.]{#always-zero explanation="A convenção de sucesso não obriga um `exit` sem argumento a retornar zero. Nesse caso, o Bash preserva um status anterior."}
::option[Ele sempre devolve o status de falha `1`.]{#always-one explanation="O Bash não atribui o status de falha `1` a todo `exit` sem argumento. O comando anterior determina o valor."}
::option[Ele devolve o status de saída do comando anterior.]{#last-command-status .correct explanation="Sem um argumento numérico explícito, o Bash sai usando o status do comando mais recente."}
:::

## Uso de logout em um Shell de Login

O comando interno `logout` do Bash encerra um shell de login:

```bash
$ logout
```

Em um shell do Bash que não seja de login, `logout` informa que ele não é um shell de login; nesse caso, use `exit`.

:::single-choice{#leave-login-shell} Qual comando interno do Bash se destina especificamente a sair de um shell de login?

::option[`logout`]{#logout-login .correct explanation="O Bash fornece `logout` para encerrar um shell de login."}
::option[`unalias`]{#unalias-login explanation="`unalias` remove definições de aliases do shell atual. Ele não encerra a sessão."}
::option[`source`]{#source-login explanation="`source` lê comandos de um arquivo no shell atual. Ele não encerra esse shell."}
:::

## Uso de Ctrl+D ou Fechamento de um Terminal

Em um prompt interativo vazio, pressionar `Ctrl+D` normalmente fornece o caractere de fim de arquivo do terminal. O Bash costuma interpretar essa condição como uma solicitação para sair. Isso não é um sinal, e configurações do shell como `ignoreeof` do Bash podem alterar o comportamento.

Fechar uma janela de terminal gráfico solicita que o aplicativo encerre seus processos e pode afetar tarefas em execução. Quando for possível, prefira uma saída organizada com `exit` e verifique se há trabalhos ativos antes de fechar a sessão.

## Resumo

Agora você sabe sair do shell atual e comunicar seu status de conclusão.

1. Use `exit` para retornar ao processo chamador do shell atual.
2. Forneça `0` para sucesso ou um status definido diferente de zero nos outros casos.
3. Entenda qual status é usado por `exit` sem argumento.
4. Use `logout` apenas em um shell de login.
5. Reconheça `Ctrl+D` como entrada de fim de arquivo, não como sinal.
