---
lang: "pt"
title: "Visão Geral do Systemd"
description: "Aprenda os conceitos básicos do Systemd: entenda unidades, alvos e o processo de inicialização. Descubra como o Systemd gerencia serviços e estados do sistema no Linux. Comece sua jornada!"
keywords: "Systemd, unidades Systemd, alvos Systemd, processo de inicialização Linux, serviços Linux, iniciante, tutorial, guia"
---

## Lesson Content

Systemd está lentamente se tornando o padrão emergente para init. Se você tem um diretório `/usr/lib/systemd`, é muito provável que esteja usando systemd.

Systemd usa metas para colocar seu sistema em funcionamento. Basicamente, você tem um alvo que deseja alcançar, e esse alvo também tem dependências que precisam ser atendidas. Systemd é extremamente flexível e robusto; ele não segue uma sequência estrita para iniciar processos. Veja o que acontece durante uma inicialização típica do systemd:

1. Primeiro, o systemd carrega seus arquivos de configuração, geralmente localizados em `/etc/systemd/system` ou `/usr/lib/systemd/system`.
2. Em seguida, ele determina seu objetivo de inicialização, que geralmente é `default.target`.
3. O Systemd descobre as dependências do alvo de inicialização e as ativa.

Semelhante aos runlevels do SysV, o systemd inicializa em diferentes alvos:

- `poweroff.target` - desliga o sistema
- `rescue.target` - modo de usuário único
- `multi-user.target` - multiusuário com rede
- `graphical.target` - multiusuário com rede e GUI
- `reboot.target` - reinicia

O objetivo de inicialização padrão de `default.target` geralmente aponta para o `graphical.target`.

Os principais objetos com os quais o systemd trabalha são conhecidos como unidades. O Systemd não apenas para e inicia serviços; ele pode montar sistemas de arquivos, monitorar seus sockets de rede, etc. Por causa dessa robustez, ele tem diferentes tipos de unidades com as quais opera. As unidades mais comuns são:

- Service units - estes são os serviços que temos iniciado e parado; esses arquivos de unidade terminam em `.service`.
- Mount units - Estes montam sistemas de arquivos; esses arquivos de unidade terminam em `.mount`.
- Target units - Estes agrupam outras unidades; os arquivos terminam em `.target`.

Por exemplo, digamos que inicializamos em nosso `default.target`. Este alvo agrupa a unidade `networking.service`, a unidade `crond.service`, etc., então, uma vez que ativamos uma única unidade, tudo abaixo dessa unidade também é ativado.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual unidade é usada para agrupar outras unidades?

## Quiz Answer

target
