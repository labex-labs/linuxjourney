---
lesson_id: "system-logging"
course_id: "logging"
lang: "pt"
order_index: 1
title: "Registro de Sistema"
description: "Aprenda como fontes, coletores, armazenamento e ferramentas de consulta de logs Linux se relacionam."
meta_title: "Registro de Sistema - Logging"
meta_description: "Descubra a melhor forma de aprender Linux entendendo o registro de sistema. Este guia cobre syslog, rsyslogd e como encontrar e ler arquivos de log em /var/log. Uma parte essencial de qualquer curso Linux online gratuito."
meta_keywords: "como aprender linux, melhor forma de aprender linux, registro de sistema linux, syslog, rsyslogd, var log, logs do sistema, aprender linha de comando linux, melhores recursos para aprender linux"
---

Logs registram eventos emitidos pelo kernel, serviços, aplicativos e componentes de segurança. Eles ajudam no diagnóstico e na auditoria, mas apenas quando a coleta funciona, os horários são compreendidos e a fonte relevante está incluída.

## Caminho de uma mensagem de log

Um caminho de logging tem partes distintas:

1. Uma fonte emite um evento.
2. Um coletor o recebe e enriquece.
3. Regras de roteamento e retenção escolhem armazenamento ou encaminhamento.
4. Uma ferramenta consulta os registros armazenados.

Em hosts systemd, `systemd-journald` costuma coletar saída de serviços, mensagens do kernel e mensagens nativas do journal ou syslog. Um daemon como rsyslog também pode receber mensagens, gravar arquivos de texto ou encaminhá-las. Aplicativos podem manter arquivos próprios ou telemetria externa.

:::single-choice{#system-logging-distinct-roles}
Qual componente decide onde mensagens aceitas são armazenadas ou encaminhadas?

::option[O diretório de trabalho atual do terminal.]{#system-logging-cwd explanation="Um diretório do shell não define rotas de logging do sistema."}
::option[O nome do arquivo da imagem de kernel.]{#system-logging-kernel-file explanation="O kernel emite mensagens, mas o nome de sua imagem não é a política de roteamento."}
::option[A configuração de roteamento e retenção.]{#system-logging-routing .correct explanation="As regras entre coleta e armazenamento determinam destinos e retenção."}
:::

## Descoberta dos logs disponíveis

Não presuma que todo host tenha os mesmos arquivos. Examine serviços ativos e configuração local:

```bash
$ systemctl --type=service --state=running | grep -E 'journal|syslog'
$ ls -la /var/log
$ journalctl --disk-usage
```

`/var/log/syslog` é comum na família Debian com roteamento compatível, enquanto `/var/log/messages` aparece em outros sistemas. Ambos podem faltar em um host apenas com journal. A documentação do aplicativo e a unit podem revelar destinos adicionais.

:::single-choice{#system-logging-file-absence}
O que a ausência de `/var/log/syslog` significa necessariamente?

::option[O host pode usar outro destino configurado.]{#system-logging-other-destination .correct explanation="Sistemas apenas com journal e políticas diferentes não precisam criar esse arquivo."}
::option[O kernel nunca produziu uma mensagem.]{#system-logging-no-kernel explanation="Registros do kernel podem estar no journal ou em outro destino."}
::option[Todos os aplicativos pararam.]{#system-logging-apps-stopped explanation="Não se deduz o estado dos aplicativos pela ausência de um caminho."}
:::

## Consulta do journal

Comece por uma consulta limitada:

```bash
$ journalctl -b -p warning
$ journalctl -u ssh.service --since '1 hour ago'
```

`-b` seleciona o boot atual, `-p` filtra prioridade e `-u` filtra uma unit. Nomes e boots retidos variam. Use `journalctl --list-boots` para listar boots e `journalctl -f` para acompanhar novos registros ao reproduzir um problema.

:::single-choice{#system-logging-current-boot}
Qual opção limita uma consulta `journalctl` ao boot atual?

::option[`-b`]{#system-logging-boot-option .correct explanation="Sem argumento, o seletor escolhe o boot atual."}
::option[`-u`]{#system-logging-unit-option explanation="Essa opção filtra por unit do systemd."}
::option[`-f`]{#system-logging-follow-option explanation="Essa opção acompanha novos registros."}
:::

## Leitura dos registros em contexto

Uma linha tradicional pode ser:

```text
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Ela contém horário, host, programa e PID, depois a mensagem. Trate o texto como saída do aplicativo, não como fato estruturado garantido. Confira fuso, sincronização do relógio, ID do boot, reutilização do PID e eventos próximos. Campos do journal podem fornecer identificadores mais fortes.

Logs podem conter usuários, endereços, caminhos, tokens e outros dados sensíveis. Aplique privilégio mínimo, remova dados de exportações e preserve originais e horários numa investigação.

:::single-choice{#system-logging-export-safety}
O que fazer antes de compartilhar externamente um trecho de log?

::option[Substituir cada horário por um valor aleatório.]{#system-logging-random-time explanation="Destruir horários impede correlação e não é uma boa forma de anonimização."}
::option[Revisá-lo em busca de segredos e identificadores sensíveis.]{#system-logging-review-sensitive .correct explanation="Logs frequentemente contêm dados operacionais ou pessoais que exigem remoção controlada."}
::option[Tornar o log original gravável por todos.]{#system-logging-world-writable explanation="Reduzir controles pode comprometer a integridade e expor mais dados."}
:::

## Resumo

Agora você consegue localizar e consultar logs Linux sem presumir um caminho universal.

1. Separar fontes, coletores, roteamento, armazenamento e visualizadores.
2. Descobrir a configuração ativa do host.
3. Usar consultas limitadas por unit, boot, tempo ou prioridade.
4. Correlacionar registros no contexto e proteger dados sensíveis.
