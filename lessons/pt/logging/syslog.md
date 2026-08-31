---
lesson_id: "syslog"
course_id: "logging"
lang: "pt"
order_index: 2
title: "syslog"
description: "Aprenda como funcionam facilities, níveis de gravidade, regras de roteamento e o comando logger do syslog."
meta_title: "syslog - Registro de Logs"
meta_description: "Aprenda sobre syslog e rsyslog no Linux, como gerenciar logs do sistema e usar o comando logger. Comece com este tutorial amigável para iniciantes!"
meta_keywords: "syslog, rsyslog, logs Linux, comando logger, /var/log/syslog, tutorial Linux, Linux para iniciantes, registro de sistema"
---

Syslog define um modelo de mensagens e convenções de transporte usadas por muitos sistemas semelhantes ao Unix. Rsyslog é uma implementação que recebe, filtra, transforma, armazena e encaminha mensagens. Ele pode coexistir com `systemd-journald`; nenhum dos nomes significa que todo aplicativo usa esse caminho.

## Facilities e níveis de gravidade

Uma mensagem syslog carrega uma facility que descreve a categoria geral da fonte e uma gravidade de emergency a debug. Facilities comuns incluem `auth`, `cron`, `daemon`, `kern`, `mail`, `user` e `local0` a `local7`.

Os níveis são ordenados. Na sintaxe clássica, `daemon.warning` normalmente seleciona mensagens warning e todas as mais graves da facility daemon, não apenas warning. Em implementações compatíveis, a correspondência exata usa `daemon.=warning`.

:::single-choice{#syslog-warning-selector}
O que um seletor clássico como `daemon.warning` normalmente seleciona?

::option[Apenas mensagens cujo texto contém a palavra daemon.]{#syslog-text-daemon explanation="A seleção usa os metadados da facility, não uma busca no texto."}
::option[Toda mensagem debug de toda facility.]{#syslog-all-debug explanation="O seletor se limita à facility daemon e a um limiar de gravidade."}
::option[Mensagens warning e mais graves da facility daemon.]{#syslog-warning-or-higher .correct explanation="O seletor inclui o nível nomeado e todos os de maior urgência."}
:::

## Leitura das regras do rsyslog

Rsyslog costuma carregar um arquivo principal e trechos de `/etc/rsyslog.d/`. Uma regra tradicional tem seletor e ação:

```text
auth,authpriv.*          /var/log/auth.log
*.*;auth,authpriv.none  -/var/log/syslog
kern.*                  /var/log/kern.log
```

A primeira envia todas as prioridades de duas facilities de autenticação. A segunda seleciona amplamente e exclui essas facilities. A terceira envia mensagens do kernel. Um `-` antes do arquivo normalmente solicita escritas assíncronas; não indica exclusão.

Examine todos os arquivos incluídos e valide a sintaxe da versão instalada antes de mudar o roteamento de produção.

:::single-choice{#syslog-selector-action}
Em uma regra tradicional do rsyslog, qual parte é a ação?

::option[A expressão de facility e gravidade à esquerda.]{#syslog-left-selector explanation="Essa parte seleciona mensagens."}
::option[O destino ou a operação à direita.]{#syslog-right-action .correct explanation="A ação determina se os registros vão para arquivo, destino remoto ou outra saída."}
::option[O comentário com a versão do pacote.]{#syslog-comment-version explanation="Comentários não fazem roteamento."}
:::

## Envio de uma mensagem de teste

Use `logger` para enviar um teste controlado com uma tag e uma prioridade identificáveis:

```bash
$ logger -p user.notice -t lesson-test 'routing check 2026-08-31T10:00'
```

Em seguida, consulte o destino esperado, por exemplo:

```bash
$ journalctl -t lesson-test --since '5 minutes ago'
```

O mesmo evento pode aparecer no journal e em um arquivo de texto, dependendo do encaminhamento e do roteamento. `logger -s` também copia a mensagem para a saída de erro padrão; isso não comprova o armazenamento durável.

:::single-choice{#syslog-logger-tag}
O que `logger -t lesson-test` acrescenta à mensagem?

::option[Um pedido para apagar registros antigos.]{#syslog-tag-delete explanation="A opção define uma tag e não gerencia retenção."}
::option[O identificador `lesson-test` como tag.]{#syslog-tag-identifier .correct explanation="Uma tag exclusiva facilita localizar o evento nos destinos configurados."}
::option[Um atraso de entrega de cinco minutos.]{#syslog-tag-delay explanation="A opção de tag não codifica intervalo de entrega."}
:::

## Alteração e verificação do roteamento

Antes de uma mudança, salve a configuração atual e identifique os consumidores posteriores. Valide a sintaxe com o modo de verificação de configuração da implementação, normalmente:

```bash
$ sudo rsyslogd -N1
```

Somente depois da validação recarregue o serviço por meio de seu gerenciador. Envie uma nova mensagem marcada, verifique todos os destinos necessários e confira o estado do serviço e os logs de erros internos. Uma regra sintaticamente válida ainda pode rotear de forma ampla demais, duplicar registros ou expor dados confidenciais.

Encaminhamento remoto deve usar transporte autenticado e criptografado em redes não confiáveis. UDP não oferece confirmação de ponta a ponta; auditoria crítica precisa considerar filas, perdas, integridade, acesso e indisponibilidade do receptor.

:::single-choice{#syslog-change-verification}
Qual evidência basta para mostrar que uma nova regra funciona?

::option[O arquivo de configuração tem data de modificação recente.]{#syslog-mtime explanation="A data não prova sintaxe válida nem entrega."}
::option[O remetente consegue executar ping no receptor.]{#syslog-ping explanation="Alcance de rede não verifica protocolo nem armazenamento."}
::option[A validação passa e um teste marcado chega a todos os destinos.]{#syslog-validate-and-test .correct explanation="São necessárias validação estática e observação de ponta a ponta."}
:::

## Resumo

Agora você consegue testar o roteamento syslog dos metadados ao destino configurado.

1. Distinguir facilities de níveis ordenados de gravidade.
2. Ler seletores separadamente de suas ações.
3. Enviar um evento marcado e priorizado com `logger`.
4. Validar a configuração e verificar a entrega de ponta a ponta.
