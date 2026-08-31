---
lesson_id: "systemd-overview"
course_id: "init"
lang: "pt"
order_index: 5
title: "Visão geral do systemd"
description: "Aprenda como o systemd carrega unidades, resolve dependências, ativa alvos e gerencia recursos do sistema e do usuário."
meta_title: "Visão geral do systemd - Init"
meta_description: "Aprenda os fundamentos do sistema de init systemd. Este guia aborda como o systemd (ou system d) usa unidades e alvos para gerenciar o processo de inicialização do Linux e os serviços do sistema. Entenda os conceitos centrais do padrão moderno de inicialização do Linux."
meta_keywords: "systemd, system d, sistema init, unidades systemd, alvos systemd, processo de inicialização do linux, serviços linux, gerenciamento de sistema, iniciante, tutorial"
---

O systemd é o sistema de init com PID 1 e o gerenciador de serviços usado por muitas distribuições Linux atuais. O projeto systemd também fornece componentes de registro, dispositivos, login, rede, horário e outros, mas as distribuições podem escolher quais partes implantar.

## Confirmando o gerenciador em execução

Inspecione o estado ativo em vez de verificar a existência de diretórios instalados:

```bash
$ ps -p 1 -o pid,comm,args=
$ systemctl is-system-running
```

`/usr/lib/systemd/` pode existir em um sistema no qual outro programa é o PID 1, e um contêiner pode expor seu próprio namespace de PID. O `systemctl` também possui modos para gerenciador de usuário e para sistemas remotos ou contêineres; portanto, identifique qual gerenciador é o destino de uma operação.

:::single-choice{#systemd-overview-detection}
O que identifica mais diretamente o systemd como o gerenciador de init do sistema?

::option[Existe um diretório chamado `/usr/lib/systemd`.]{#systemd-overview-directory explanation="Bibliotecas e arquivos de unidade podem permanecer instalados sem que o systemd atue como PID 1."}
::option[Um usuário executou um comando chamado `systemctl`.]{#systemd-overview-command-executed explanation="Um binário cliente pode existir mesmo quando nenhum gerenciador systemd do sistema está disponível."}
::option[O PID 1 do host é o systemd.]{#systemd-overview-pid-one .correct explanation="O primeiro processo em execução é uma evidência mais forte do que arquivos instalados ou nomes de pacotes."}
:::

## Unidades como objetos gerenciados

Uma unidade é o modelo nomeado do systemd para um recurso ou uma atividade. Entre os tipos comuns de unidade estão:

- `.service` para processos e daemons
- `.socket` para ativação por socket
- `.mount` e `.automount` para sistemas de arquivos
- `.timer` e `.path` para ativação orientada a eventos
- `.target` para agrupamento e sincronização
- `.device`, `.swap`, `.slice` e `.scope` para outros recursos gerenciados

O estado de uma unidade nem sempre é “em execução”. Uma montagem pode estar montada, um temporizador pode estar aguardando, um dispositivo pode estar presente e um alvo pode estar ativo depois que suas dependências são alcançadas.

:::single-choice{#systemd-overview-group-unit}
Qual tipo de unidade geralmente agrupa outras unidades e fornece um ponto de sincronização?

::option[`.socket`]{#systemd-overview-socket explanation="Unidades de socket expõem pontos de extremidade de IPC ou rede e podem ativar serviços."}
::option[`.target`]{#systemd-overview-target .correct explanation="Unidades de alvo reúnem dependências e representam marcos de inicialização ou operação."}
::option[`.timer`]{#systemd-overview-timer explanation="Unidades de temporizador agendam a ativação com base no calendário ou no tempo monotônico."}
:::

## Caminhos de carregamento e substituições de unidades

Unidades do sistema podem ser carregadas de caminhos da distribuição e do administrador, como:

- `/usr/lib/systemd/system/` para unidades fornecidas por pacotes em muitas distribuições
- `/run/systemd/system/` para configurações geradas em tempo de execução ou transitórias
- `/etc/systemd/system/` para configurações e substituições locais persistentes do administrador

Os caminhos exatos dos fornecedores podem variar. Configurações locais de prioridade mais alta substituem arquivos de prioridade mais baixa com o mesmo nome de unidade. Prefira substituições complementares criadas com `systemctl edit UNIT` a copiar e modificar um arquivo completo do fornecedor, para que as atualizações de pacotes continuem visíveis.

:::single-choice{#systemd-overview-local-override}
Onde normalmente devem ficar as substituições locais persistentes de unidades do sistema?

::option[Dentro de `/proc/systemd/`.]{#systemd-overview-proc-systemd explanation="O procfs é uma interface do kernel em tempo de execução, não uma configuração persistente de unidades."}
::option[Em `/etc/systemd/system/`.]{#systemd-overview-etc-system .correct explanation="A camada de configuração do administrador tem precedência sobre as unidades empacotadas pelo fornecedor."}
::option[Nos bytes de código de inicialização do MBR do disco.]{#systemd-overview-mbr-units explanation="Unidades de serviço são arquivos de configuração no espaço do usuário."}
:::

## Dependências e ordenação

O systemd cria uma transação com base nos relacionamentos de dependência. `Wants=` e `Requires=` incluem outras unidades em uma transação com intensidades diferentes. `Before=` e `After=` especificam a ordem quando ambas as unidades estão agendadas; por si só, eles não fazem outra unidade iniciar.

Uma linha `After=network.target` não comprova que uma conectividade utilizável, o DNS ou um ponto de extremidade remoto específico estejam prontos. Os serviços devem usar a integração apropriada com o estado de rede online ou implementar seu próprio comportamento de repetição e prontidão.

:::single-choice{#systemd-overview-after-semantics}
O que `After=other.service` especifica por si só?

::option[Uma garantia de que o ponto de extremidade da aplicação do outro serviço está íntegro.]{#systemd-overview-after-health explanation="A conclusão da ordenação e a prontidão da aplicação são conceitos diferentes."}
::option[A ordenação caso ambas as unidades façam parte da transação.]{#systemd-overview-after-ordering .correct explanation="Um requisito separado, como Wants ou Requires, é necessário para incluir a outra unidade."}
::option[A habilitação automática de ambas as unidades em toda inicialização futura.]{#systemd-overview-after-enable explanation="A habilitação é um metadado de instalação e não está implícita na ordenação."}
:::

## Alvos e a transação de inicialização padrão

`default.target` normalmente é um alias para um alvo como `multi-user.target` ou `graphical.target`. O systemd inicia uma transação para esse alvo e suas dependências, permitindo que trabalhos não relacionados prossigam simultaneamente enquanto aplica a ordenação explícita.

Os alvos se assemelham aos níveis de execução apenas em um sentido amplo de compatibilidade. Vários alvos podem estar ativos ao mesmo tempo, alvos personalizados podem ser criados, e a atividade de um alvo não significa que todos os serviços da máquina estejam íntegros.

:::single-choice{#systemd-overview-default-target}
O que `default.target` normalmente seleciona?

::option[O dispositivo de bloco padrão que `mkfs` deve apagar.]{#systemd-overview-default-disk explanation="Alvos descrevem a ativação de unidades, não a seleção destrutiva de armazenamento."}
::option[O único alvo que pode estar ativo.]{#systemd-overview-only-target explanation="Alvos são agrupamentos, e muitos podem estar ativos em uma mesma inicialização."}
::option[A transação de alvo usada para uma inicialização normal do sistema.]{#systemd-overview-normal-boot .correct explanation="Ele normalmente é um alias para o alvo de inicialização multiusuário ou gráfico selecionado pelo administrador."}
:::

## Resumo

Agora você pode descrever o systemd em termos de gerenciadores ativos, unidades e transações.

1. Confirme o systemd por meio do PID 1 relevante e da conexão com o gerenciador.
2. Associe os tipos de recurso aos sufixos das unidades.
3. Posicione as substituições locais acima da configuração do fornecedor.
4. Diferencie a intensidade da dependência, a ordenação e a prontidão da aplicação.
5. Trate os alvos como agrupamentos e marcos, não como estados exclusivos.
