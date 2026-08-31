---
lesson_id: "sysv-overview"
course_id: "init"
lang: "pt"
order_index: 1
title: "Visão Geral do System V"
description: "Aprenda como o init tradicional System V usa runlevels e links ordenados para scripts de serviços."
meta_title: "Visão Geral do System V - Init"
meta_description: "Conheça o sistema init tradicional System V, também chamado SysV ou init V. Este guia aborda como ele gerencia processos, sua inicialização ordenada e a função dos runlevels no Linux."
meta_keywords: "System V, systemv, SysV init, systemv init, init V, initv, runlevels Linux, sistema init, gerenciamento de processos, tutorial Linux"
---

O init System V, normalmente chamado de SysV init ou sysvinit, é um projeto tradicional de PID 1 e inicialização de serviços. Ele continua importante em sistemas legados e por meio de scripts de compatibilidade, mas a presença de arquivos no estilo SysV não comprova que o sysvinit seja o PID 1 em execução.

## Identificação do Sistema Init Ativo

Inspecione o PID 1 ativo:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

Um arquivo `/etc/inittab` ou diretório `/etc/init.d/` é apenas uma evidência auxiliar. O systemd e outros sistemas init podem manter esses arquivos para compatibilidade, e contêineres podem mostrar um namespace de PIDs diferente do host.

:::single-choice{#sysv-overview-detection}
Qual é a evidência mais forte de que o sysvinit está ativo?

::option[O executável ativo do PID 1 é o sysvinit ou seu programa init.]{#sysv-overview-live-pid-one .correct explanation="Inspecionar o primeiro processo em execução é mais direto que deduzir a partir de arquivos de compatibilidade."}
::option[Existe um diretório `/etc/init.d/`.]{#sysv-overview-init-d-only explanation="Outros sistemas init normalmente preservam scripts ou wrappers do SysV."}
::option[A descrição de pacote contém a palavra service.]{#sysv-overview-package-word explanation="O texto de um pacote não identifica o processo que atua atualmente como PID 1."}
:::

## Runlevels

Um runlevel é um modo operacional numérico nomeado. As configurações SysV tradicionalmente usam os níveis `0` a `6` e níveis especiais, mas seus significados são políticas da distribuição, não uma regra universal. Algumas convenções comuns são:

- `0`: transição para parada ou desligamento
- `1` ou `S`: modo de usuário único ou resgate
- `2` a `5`: modos multiusuário definidos pela distribuição
- `6`: transição para reinicialização

Historicamente, sistemas da família Debian tratam os níveis 2 a 5 de forma semelhante, enquanto as convenções da família Red Hat diferenciam os modos de texto e gráfico. Inspecione `/etc/inittab`, a documentação do init e os diretórios de runlevels no host real.

:::single-choice{#sysv-overview-shutdown-runlevel}
Qual runlevel solicita convencionalmente a parada ou o desligamento em muitos sistemas SysV?

::option[`3`]{#sysv-overview-runlevel-three explanation="Esse normalmente é um modo operacional multiusuário, não de desligamento."}
::option[`0`]{#sysv-overview-runlevel-zero .correct explanation="O nível zero é convencionalmente a transição de desligamento, embora a política local do init seja a autoridade."}
::option[`6`]{#sysv-overview-runlevel-six explanation="O nível seis solicita convencionalmente uma reinicialização."}
:::

## Scripts Init e Links de Runlevels

Os scripts de serviços normalmente ficam em `/etc/init.d/`. Diretórios de runlevels, como `/etc/rc2.d/` ou `/etc/rc.d/rc2.d/`, contêm links cujos nomes codificam a ação e a ordem da transição:

- Links `SNNname` solicitam uma ação de início.
- Links `KNNname` solicitam uma ação de parada.
- `NN` fornece uma ordenação lexical entre os links daquela transição.

O algoritmo e os diretórios exatos variam. As dependências também podem ser expressas nos cabeçalhos dos scripts e processadas por ferramentas da distribuição, e algumas implementações paralelizam o trabalho. O SysV não deve ser reduzido a uma garantia de que todos os serviços sejam iniciados estritamente um por vez.

:::single-choice{#sysv-overview-start-link}
O que um link `S20networking` solicita convencionalmente durante a entrada em um runlevel?

::option[Enviar diretamente o sinal 20 a todos os processos de rede.]{#sysv-overview-signal-twenty explanation="Os dígitos são metadados de ordenação, não um número de sinal."}
::option[Armazenar vinte backups da configuração de rede.]{#sysv-overview-twenty-backups explanation="Os links de runlevels não oferecem retenção de backups."}
::option[Executar o script de serviço apontado com sua ação start na ordenação `S`.]{#sysv-overview-start-action .correct explanation="O prefixo diferencia os links de inicialização, e o número contribui para a sequência."}
:::

## Transição entre Runlevels

Quando o init muda de runlevel, o mecanismo rc da distribuição interrompe os serviços que deixaram de ser necessários e inicia os exigidos pelo novo modo. Os scripts precisam ser suficientemente idempotentes para lidar com operações repetidas de estado ou transição e retornar status significativos.

Solicitar o runlevel 0 ou 6 é uma ação destrutiva de disponibilidade para todo o sistema. Use a interface de desligamento do sistema, notifique os usuários, preserve o trabalho ativo e verifique o acesso remoto ao console, em vez de invocar casualmente transições brutas do init.

:::single-choice{#sysv-overview-runlevel-six-meaning}
O que o runlevel `6` solicita convencionalmente?

::option[A criação de seis contas de usuário adicionais.]{#sysv-overview-six-users explanation="Os runlevels descrevem modos operacionais, não quantidades de contas."}
::option[Uma transição de reinicialização do sistema.]{#sysv-overview-reboot .correct explanation="A política clássica do SysV reserva o nível seis para interromper serviços e reiniciar o sistema."}
::option[A montagem permanente de todos os sistemas de arquivos somente para leitura.]{#sysv-overview-six-readonly explanation="Essa não é a finalidade convencional do runlevel seis."}
:::

## Limites da Compatibilidade

Em um host com systemd, os scripts SysV podem ser encapsulados como unidades geradas, mas as dependências, os timeouts, o registro e as semânticas de estado do systemd ainda se aplicam. Executar diretamente um script legado pode ignorar o acompanhamento do gerenciador de serviços. Identifique o gerenciador ativo e use sua interface nativa quando possível.

:::single-choice{#sysv-overview-compatibility-script}
Por que um script no estilo SysV em um host com systemd normalmente deve ser invocado pelo gerenciador de serviços?

::option[A execução direta pode ignorar o acompanhamento de dependências e estados.]{#sysv-overview-manager-tracking .correct explanation="O gerenciador precisa coordenar a propriedade dos processos, a ordenação, os timeouts e o estado."}
::option[Scripts de shell não podem ser executados em um sistema com systemd.]{#sysv-overview-scripts-impossible explanation="Eles podem ser executados, mas ignorar a supervisão pode criar um estado inconsistente."}
::option[O systemd converte todo script de serviço em um módulo do kernel.]{#sysv-overview-script-module explanation="As unidades de compatibilidade continuam sendo gerenciamento de serviços no espaço do usuário."}
:::

## Resumo

Agora você sabe interpretar um layout SysV tradicional sem presumir que ele esteja ativo.

1. Identifique o PID 1 ativo antes de escolher comandos do init.
2. Trate os significados dos runlevels como convenções definidas pela distribuição.
3. Leia `S`, `K` e a ordenação numérica nos links de runlevels.
4. Use procedimentos controlados de desligamento para os níveis 0 e 6.
5. Respeite o gerenciador ativo quando houver scripts de compatibilidade.
