---
lesson_id: "systemd-goals"
course_id: "init"
lang: "pt"
order_index: 6
title: "Objetivos do systemd"
description: "Aprenda a inspecionar, substituir, validar, iniciar, habilitar e solucionar problemas de unidades de serviço do systemd."
meta_title: "Objetivos do systemd - Init"
meta_description: "Explore os objetivos do systemd e aprenda a gerenciar serviços Linux usando comandos essenciais do systemctl. Este guia aborda os fundamentos dos arquivos de unidade do systemd, como iniciar, parar e habilitar serviços e consultar seus estados."
meta_keywords: "systemd, systemctl, serviços Linux, arquivos de unidade, objetivos do systemd, gerenciamento de serviços, unidades systemd, iniciante, tutorial, guia, comandos Linux"
---

`systemctl` envia solicitações a um gerenciador systemd. Esta lição se concentra nas unidades de serviço do sistema. Confirme o nome exato da unidade, o escopo do gerenciador, as dependências e o impacto operacional antes de alterar o estado.

## Lendo uma unidade de serviço

Uma unidade ilustrativa mínima pode ter esta aparência:

```ini
[Unit]
Description=Example worker
Wants=network-online.target
After=network-online.target

[Service]
Type=exec
ExecStart=/usr/local/bin/example-worker
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `[Unit]` contém a descrição e os relacionamentos de dependência.
- `[Service]` define o ciclo de vida do processo e o comportamento específico do serviço.
- `[Install]` informa aos comandos de habilitação quais aliases ou links de dependência devem ser criados; ela não é automaticamente uma dependência ativa em tempo de execução.

`ExecStart=` não é passado por um shell por padrão. Pipelines, redirecionamentos, variáveis e aspas do shell não se comportam como em uma linha de comando interativa, a menos que um shell explícito seja invocado intencionalmente.

:::single-choice{#systemd-goals-install-section}
Qual é a finalidade principal das diretivas de `[Install]`, como `WantedBy=`?

::option[Garantir que o processo do serviço já esteja em execução.]{#systemd-goals-install-running explanation="A ativação em tempo de execução exige start ou outra dependência acionadora."}
::option[Descrever links ou relacionamentos criados quando a unidade é habilitada.]{#systemd-goals-enable-links .correct explanation="Os metadados de instalação são interpretados pelas operações de habilitação e são separados do estado atual do processo."}
::option[Executar todos os comandos pelo shell interativo do usuário.]{#systemd-goals-install-shell explanation="A análise de comandos da unidade não usa um shell interativo por padrão."}
:::

## Inspecionando a configuração efetiva

Liste as unidades carregadas com:

```bash
$ systemctl list-units --type=service
```

Liste os arquivos de unidade instalados e seus estados de habilitação com:

```bash
$ systemctl list-unit-files --type=service
```

Essas são visualizações diferentes: um arquivo de unidade pode estar habilitado, mas inativo; ativo, mas desabilitado; estático; gerado; transitório; mascarado; ou ausente em uma das listas. Inspecione o conteúdo combinado do fornecedor e dos complementos com:

```bash
$ systemctl cat UNIT.service
$ systemctl show UNIT.service
```

:::single-choice{#systemd-goals-list-units-versus-files}
O que `list-unit-files` mostra que não é o foco principal de `list-units`?

::option[Apenas os processos que consomem mais CPU.]{#systemd-goals-cpu-processes explanation="A classificação do uso de recursos por processos não faz parte desses comandos de inventário de unidades."}
::option[Os estados de habilitação dos arquivos de unidade instalados.]{#systemd-goals-unit-file-state .correct explanation="Ele informa se os arquivos de unidade estão habilitados, desabilitados, estáticos, mascarados e outros estados relacionados à instalação."}
::option[Todas as linhas já gravadas no journal.]{#systemd-goals-all-journal explanation="Consultas ao journal usam `journalctl`."}
:::

## Criando uma substituição local

Use um complemento em vez de editar uma unidade empacotada:

```bash
$ sudo systemctl edit UNIT.service
```

Após salvar, nas implementações atuais, o systemctl normalmente solicita que o gerenciador recarregue como parte desse fluxo de edição. Porém, quando os arquivos forem alterados por outro método, execute:

```bash
$ sudo systemctl daemon-reload
```

`daemon-reload` relê as definições de unidade e reconstrói as dependências. Ele não recarrega a configuração da aplicação nem reinicia os serviços em execução. Quando apropriado, valide a sintaxe e as dependências da unidade com `systemd-analyze verify` e depois revise a unidade efetiva combinada.

:::single-choice{#systemd-goals-daemon-reload}
O que `systemctl daemon-reload` faz?

::option[Obriga todos os daemons a reler suas configurações de aplicação.]{#systemd-goals-reload-all-apps explanation="O recarregamento da aplicação é específico do serviço e separado da configuração do gerenciador."}
::option[Reinicializa o kernel em uma nova versão.]{#systemd-goals-reload-kernel explanation="A ativação do kernel exige uma inicialização, não o recarregamento das definições de unidade."}
::option[Recarrega as definições de unidade e as informações de dependência do systemd.]{#systemd-goals-reload-manager .correct explanation="Ele atualiza a visão de configuração do gerenciador sem reiniciar serviços inerentemente."}
:::

## Estado do serviço em tempo de execução

Depois de validar a configuração do serviço e preservar um acesso de recuperação:

```bash
$ sudo systemctl start peanut.service
$ sudo systemctl stop peanut.service
$ sudo systemctl restart peanut.service
$ sudo systemctl reload peanut.service
```

`reload` só funciona quando a unidade define ou oferece suporte a uma ação de recarregamento. `restart` interrompe o processo e pode não conseguir restaurar o serviço. Para acesso remoto, rede, armazenamento ou autenticação, mantenha um caminho de console separado e verifique a configuração antes de agir.

Verifique o estado e os logs com:

```bash
$ systemctl status peanut.service
$ systemctl is-active peanut.service
$ journalctl -u peanut.service -b
```

“Ativo” é um estado do gerenciador, não uma prova de que todos os pontos de extremidade da aplicação estão íntegros.

:::single-choice{#systemd-goals-start-peanut}
Qual comando inicia `peanut.service` agora sem alterar por si só sua habilitação futura?

::option[`sudo systemctl enable peanut.service`]{#systemd-goals-enable-only explanation="Enable altera os links de instalação, mas não inicia o serviço, a menos que seja combinado com `--now`."}
::option[`sudo systemctl start peanut.service`]{#systemd-goals-start-command .correct explanation="Start solicita a ativação atual em tempo de execução e é separado da habilitação."}
::option[`sudo systemctl daemon-reload peanut.service`]{#systemd-goals-daemon-reload-unit explanation="Daemon-reload não recebe um operando de ativação de unidade e não inicia esse serviço."}
:::

## Habilitação, desabilitação e mascaramento

Gerencie os links de dependência futuros com:

```bash
$ sudo systemctl enable peanut.service
$ sudo systemctl disable peanut.service
```

Enable não inicia a unidade, a menos que `--now` seja adicionado. Disable não para uma unidade em execução, a menos que `--now` seja adicionado. Uma unidade estática pode não ter metadados de instalação e ainda assim ser ativada como dependência de outra unidade.

O mascaramento vincula a unidade a `/dev/null` e bloqueia a ativação comum, inclusive por dependência, até que ela seja desmascarada. Ele é mais forte que disable e pode interromper dependentes; inspecione as dependências reversas antes de usá-lo.

:::single-choice{#systemd-goals-disable-runtime}
O que acontece com um serviço que já está em execução depois de `systemctl disable UNIT` sem `--now`?

::option[Ele é encerrado imediatamente com `SIGKILL`.]{#systemd-goals-disable-kills explanation="Disable por si só não solicita uma parada imediata."}
::option[Seu executável é excluído do sistema de arquivos.]{#systemd-goals-disable-deletes explanation="As operações de habilitação gerenciam links, não os arquivos de programa dos pacotes."}
::option[Normalmente, ele continua em execução enquanto os links de habilitação futura são removidos.]{#systemd-goals-disable-keeps-running .correct explanation="O estado em tempo de execução e o estado de instalação são dimensões separadas."}
:::

## Verifique o resultado do serviço

Após uma alteração, verifique o estado do processo, os logs recentes, os pontos de extremidade em escuta, as unidades dependentes, a integridade da aplicação e o comportamento após uma reinicialização controlada caso a habilitação de inicialização tenha mudado. Use `systemctl is-failed`, `systemctl list-dependencies` e verificações próprias da aplicação conforme apropriado.

## Resumo

Agora você pode gerenciar um serviço do systemd sem confundir configuração, execução e habilitação.

1. Leia `[Unit]`, `[Service]` e `[Install]` de acordo com suas funções distintas.
2. Compare o estado das unidades carregadas com o estado dos arquivos de unidade instalados.
3. Use complementos e recarregue o gerenciador após alterações externas nos arquivos.
4. Inicie, pare, recarregue ou reinicie somente após revisar o impacto.
5. Trate enable, disable e mask como controles distintos de persistência.
