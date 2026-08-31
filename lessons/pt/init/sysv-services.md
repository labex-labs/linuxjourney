---
lesson_id: "sysv-services"
course_id: "init"
lang: "pt"
order_index: 2
title: "Serviço System V"
description: "Aprenda a inspecionar e operar scripts legados de serviços SysV pela interface compatível do sistema ativo."
meta_title: "Serviço System V - Init"
meta_description: "Aprenda a gerenciar serviços tradicionais System V (SysV) no Linux. Este guia aborda o uso do comando `service` para listar, iniciar, interromper e reiniciar serviços."
meta_keywords: "System V, SysV init, serviços Linux, comando service, gerenciar serviços Linux, iniciar serviço, parar serviço, reiniciar serviço, Linux System V"
---

Os serviços SysV normalmente são representados por scripts executáveis em `/etc/init.d/`. Um script aceita ações como `start`, `stop`, `restart` ou `status`, conforme sua implementação e as convenções da distribuição. O comando `service` oferece uma interface que executa determinado script em um ambiente mais controlado.

## Descoberta dos Serviços e das Ações

Liste primeiro os nomes dos scripts:

```bash
$ ls -1 /etc/init.d/
```

Algumas implementações oferecem:

```bash
$ service --status-all
```

Seus marcadores entre colchetes e status de saída são específicos da interface, e um script pode informar um estado desconhecido. Para um serviço, inspecione a saída de uso do script ou sua documentação, em vez de presumir que todas as ações existam.

:::single-choice{#sysv-services-wrapper-purpose}
O que o comando `service` normalmente encapsula?

::option[Um editor de partições de disco executado em cada arquivo de serviço.]{#sysv-services-partition-editor explanation="O controle de serviços não tem relação com o particionamento do armazenamento."}
::option[Uma chamada de sistema do kernel acrescentada dinamicamente pelo script.]{#sysv-services-new-syscall explanation="Os scripts init são programas de controle de processos no espaço do usuário."}
::option[Um script init nomeado e uma de suas ações compatíveis.]{#sysv-services-script-action .correct explanation="A interface localiza um script de serviço legado e o invoca com um ambiente normalizado."}
:::

## Início e Interrupção

Em um host realmente gerenciado pelo SysV, estas formas são comuns:

```bash
$ sudo service SERVICE_NAME start
$ sudo service SERVICE_NAME stop
```

Substitua o marcador somente depois de identificar o serviço, seus dependentes, o estado atual e o impacto operacional. Interromper a rede, o acesso remoto, o armazenamento ou a autenticação a partir de uma sessão remota pode bloquear seu acesso ou corromper trabalhos ativos.

A forma direta `/etc/init.d/SERVICE_NAME ACTION` pode existir, mas, em um host cujo gerenciador ativo oferece compatibilidade, use o comando voltado ao gerenciador para que ele acompanhe o estado e as dependências.

:::single-choice{#sysv-services-stop-peanut}
Qual comando solicita a interrupção do serviço SysV `peanut`?

::option[`sudo service stop peanut`]{#sysv-services-stop-first explanation="A ordem convencional dos operandos coloca o nome do serviço antes da ação."}
::option[`sudo stop --partition peanut`]{#sysv-services-partition-stop explanation="Essa não é a sintaxe da interface de serviços SysV."}
::option[`sudo service peanut stop`]{#sysv-services-peanut-stop .correct explanation="A interface recebe o nome do serviço seguido pela ação de parada solicitada."}
:::

## Recarga, Reinicialização e Estado

`restart` normalmente interrompe e depois inicia um serviço, causando uma indisponibilidade. `reload` pode solicitar que um serviço releia a configuração sem uma reinicialização completa, mas apenas quando o script e o daemon oferecerem suporte. Alguns scripts oferecem `force-reload`, com um comportamento alternativo definido pela distribuição.

Valide a configuração antes de qualquer recarga ou reinicialização, preserve uma segunda conexão administrativa ao alterar o acesso remoto e depois verifique o serviço por seu endpoint real e pelos logs — não apenas por um estado “running”.

```bash
$ sudo service SERVICE_NAME status
$ sudo service SERVICE_NAME reload
```

:::single-choice{#sysv-services-reload-versus-restart}
Por que não se deve presumir que `reload` seja equivalente a `restart`?

::option[Reload sempre desliga todo o sistema operacional.]{#sysv-services-reload-shutdown explanation="Esse não é o significado normal de uma ação de recarga de serviço."}
::option[Restart apenas imprime a configuração e nunca altera o estado dos processos.]{#sysv-services-restart-readonly explanation="Restart normalmente interrompe e inicia o serviço."}
::option[Reload é específico do serviço e pode reler a configuração sem interromper o processo.]{#sysv-services-reload-specific .correct explanation="O suporte e a semântica pertencem ao script init e ao daemon, enquanto restart normalmente causa uma interrupção do ciclo de vida."}
:::

## Controle em Tempo de Execução e Ativação no Boot

Iniciar um serviço agora não necessariamente o habilita para runlevels futuros. A ativação no boot é representada pelos links de runlevels e gerenciada por ferramentas específicas da distribuição, como `update-rc.d`, `chkconfig` ou geradores de compatibilidade do gerenciador de serviços.

Não crie links `S` e `K` manualmente antes de compreender os metadados de dependências e a ferramenta de gerenciamento da distribuição; links manuais podem ser sobrescritos ou ordenados incorretamente.

:::single-choice{#sysv-services-start-versus-enable}
`service SERVICE start` necessariamente habilita o serviço nos boots futuros?

::option[Sim; toda ação start cria automaticamente todos os links de runlevels.]{#sysv-services-start-links explanation="A interface não altera universalmente a ativação persistente."}
::option[Não; o estado em tempo de execução e a ativação nos runlevels são separados.]{#sysv-services-runtime-separate .correct explanation="Os links de boot ou a política do gerenciador determinam a ativação futura independentemente do início atual do processo."}
::option[Sim; um PID em execução é armazenado permanentemente no setor de boot.]{#sysv-services-pid-boot-sector explanation="PIDs são identificadores de tempo de execução, não metadados de ativação no boot."}
:::

## Resumo

Agora você sabe operar um serviço legado sem confundir o controle em tempo de execução com a política de boot.

1. Descubra o script real e as ações compatíveis.
2. Use o nome do serviço antes da ação na sintaxe da interface.
3. Valide e verifique o comportamento de recarga ou reinicialização.
4. Gerencie a ativação futura nos runlevels por meio das ferramentas da distribuição.
