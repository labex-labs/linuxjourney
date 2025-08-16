---
title: "Gerenciando Arquivos de Log"
description: "Aprenda a gerenciar arquivos de log do Linux de forma eficiente usando logrotate. Descubra a rotação de logs, compressão e configuração para economizar espaço em disco. Comece a aprender hoje!"
keywords: "logrotate, logs Linux, gerenciamento de logs, rotação de logs, tutorial Linux, iniciante, guia, espaço em disco"
---

## Lesson Content

Os arquivos de log geram muitos dados e os armazenam em seus discos rígidos. No entanto, há muitos problemas com isso. Na maioria das vezes, queremos apenas poder ver os logs mais recentes. Também queremos gerenciar nosso espaço em disco de forma eficiente. Então, como fazemos tudo isso? A resposta é com `logrotate`.

O utilitário `logrotate` realiza o gerenciamento de logs para nós. Ele possui um arquivo de configuração que nos permite especificar quantos e quais logs manter, como compactar nossos logs para economizar espaço e muito mais. A ferramenta `logrotate` geralmente é executada via cron uma vez por dia, e os arquivos de configuração podem ser encontrados em `/etc/logrotate.d`.

Existem outras ferramentas de rotação de log que você pode usar para gerenciar seus logs, mas `logrotate` é a mais comum.

## Exercise

Look at your `logrotate` configuration file and see how it manages some of your logs.

## Quiz Question

Qual utilitário é usado para gerenciar logs?

## Quiz Answer

logrotate
