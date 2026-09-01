---
lesson_id: "process-signals"
course_id: "processes"
lang: "pt"
order_index: 6
title: "Sinais"
description: "Aprenda como o Linux gera, bloqueia, entrega e trata sinais para controle de processos e notificação de eventos."
meta_title: "Sinais - Processos"
meta_description: "Conheça os fundamentos dos sinais Linux, um mecanismo essencial do gerenciamento de processos. Aprenda como sinais como SIGTERM e SIGKILL funcionam e entenda seus códigos no sistema operacional."
meta_keywords: "sinais Linux, sinais de processos Linux, sinal 15 Linux, código de sinal SO, SIGKILL, SIGTERM, SIGINT, gerenciamento de processos, tutorial Linux"
---

Um sinal é uma notificação assíncrona entregue a um processo ou a uma thread específica. Os sinais informam eventos e solicitam ações, mas transportam apenas informações limitadas em comparação com mecanismos de comunicação entre processos voltados a dados.

## Origens dos Sinais

Os sinais podem vir de vários lugares:

- Um terminal pode gerar `SIGINT` para `Ctrl-C` ou `SIGTSTP` para `Ctrl-Z` e direcioná-lo ao grupo de processos em primeiro plano.
- O kernel pode gerar um sinal síncrono, como `SIGSEGV`, quando uma thread faz uma referência inválida à memória.
- Um processo pode enviar um sinal autorizado para outro processo ou grupo de processos.
- Temporizadores, alterações no estado de filhos e hangups de terminais podem gerar outros sinais.

O remetente precisa possuir as permissões adequadas, normalmente baseadas em credenciais ou capacidades. Portanto, os sinais são uma interface de controle intermediada pelo kernel, não mensagens irrestritas entre usuários arbitrários.

:::single-choice{#process-signals-ctrl-c} Qual sinal um terminal normalmente gera para `Ctrl-C`?

::option[`SIGTSTP`]{#process-signals-ctrl-c-tstp explanation="`SIGTSTP` normalmente está associado ao caractere de suspensão do terminal, como `Ctrl-Z`."}
::option[`SIGCONT`]{#process-signals-ctrl-c-cont explanation="`SIGCONT` retoma um processo interrompido, em vez de representar uma interrupção pelo teclado."}
::option[`SIGINT`]{#process-signals-ctrl-c-int .correct explanation="O caractere de interrupção do terminal normalmente gera `SIGINT` para o grupo de processos em primeiro plano."}
:::

## Disposições e Ações Padrão

A maioria dos sinais possui uma disposição válida para todo o processo que seleciona uma de três respostas:

- realizar a ação padrão definida pelo sinal
- ignorar o sinal
- invocar um manipulador instalado pelo usuário

As ações padrão variam: um sinal pode encerrar, encerrar e criar um core dump, interromper, continuar ou ser ignorado. Capturar `SIGTERM` pode permitir que um programa inicie um encerramento ordenado, mas um manipulador deve seguir regras rígidas de segurança assíncrona de sinais, e o programa ainda pode adiar ou se recusar a terminar.

Os nomes dos sinais são mais portáveis e legíveis que os números. Embora arquiteturas Linux comuns usem 15 para `SIGTERM`, não presuma que todos os números de sinais, exceto os garantidos pelo padrão relevante, sejam idênticos em todos os lugares. Use `kill -l` para inspecionar o mapeamento local.

:::single-choice{#process-signals-term-behavior} Por que um processo pode responder de forma ordenada a `SIGTERM`?

::option[Ele pode instalar um manipulador para esse sinal.]{#process-signals-term-handler .correct explanation="Ao contrário de `SIGKILL`, `SIGTERM` pode ser capturado para que um programa inicie sua própria lógica de encerramento."}
::option[O kernel sempre salva automaticamente todos os documentos abertos.]{#process-signals-term-kernel-save explanation="A limpeza da aplicação depende do código do programa; o kernel não compreende nem salva estados arbitrários de documentos."}
::option[`SIGTERM` não pode causar o encerramento por padrão.]{#process-signals-term-no-default explanation="Sua ação padrão é encerrar quando o processo não altera a disposição."}
:::

## Sinais Bloqueados e Pendentes

As threads possuem máscaras de sinais que podem bloquear temporariamente a entrega dos sinais selecionados. Um sinal bloqueado que foi gerado permanece pendente até que possa ser entregue, sujeito às regras dos sinais padrão e de tempo real. Sinais padrão do mesmo tipo podem ser combinados, em vez de enfileirados uma vez por ocorrência.

Em um processo multithread, um sinal direcionado ao processo pode ser entregue a uma thread elegível que não o bloqueie; um sinal direcionado a uma thread tem como destino a thread especificada. Portanto, um projeto correto de sinais exige mais que verificar se “o processo o bloqueou”.

:::single-choice{#process-signals-blocked-state} O que normalmente acontece quando um sinal bloqueável é gerado enquanto seu destino o bloqueia?

::option[Ele permanece pendente até que a entrega se torne possível.]{#process-signals-pending .correct explanation="O bloqueio adia o tratamento; o sinal pendente pode ser entregue depois que for desbloqueado."}
::option[Ele é convertido automaticamente em `SIGKILL`.]{#process-signals-convert-kill explanation="O kernel não transforma um sinal comum bloqueado em um sinal que não pode ser capturado."}
::option[Ele altera o ID de usuário do processo de destino.]{#process-signals-change-uid explanation="As máscaras de sinais afetam a entrega e não alteram as credenciais do processo."}
:::

## Sinais que Não Podem Ser Tratados

`SIGKILL` encerra um processo, e `SIGSTOP` o interrompe. Nenhum deles pode ser capturado, ignorado ou bloqueado. Isso garante que o kernel mantenha o controle definitivo, mas também significa que `SIGKILL` não oferece oportunidade para a limpeza no nível da aplicação.

Até mesmo `SIGKILL` pode não fazer uma tarefa desaparecer instantaneamente da perspectiva de um observador. Uma tarefa pode estar aguardando uma operação ininterruptível do kernel e, depois do encerramento, seu pai ainda precisa coletar seu status.

:::single-choice{#process-signals-uncatchable-pair} Qual par não pode ser capturado, ignorado nem bloqueado?

::option[`SIGKILL` e `SIGSTOP`]{#process-signals-kill-stop .correct explanation="O kernel reserva esses dois sinais para que um processo não possa substituir nem adiar suas ações fundamentais."}
::option[`SIGINT` e `SIGTERM`]{#process-signals-int-term explanation="Os dois podem ter manipuladores instalados pelo usuário e podem ser bloqueados."}
::option[`SIGHUP` e `SIGCONT`]{#process-signals-hup-cont explanation="Esses sinais possuem semânticas especiais, mas não são o par que não pode ser capturado."}
:::

## Resumo

Agora você sabe explicar as principais etapas e restrições do tratamento de sinais no Linux.

1. Identifique sinais gerados pelo terminal, pelo kernel e por processos.
2. Diferencie ações padrão, sinais ignorados e manipuladores.
3. Relacione o bloqueio à entrega pendente e às máscaras das threads.
4. Lembre-se de que `SIGKILL` e `SIGSTOP` não podem ser tratados nem bloqueados.
