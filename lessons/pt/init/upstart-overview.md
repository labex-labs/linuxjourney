---
index: 3
lang: "pt"
title: "Visão Geral do Upstart"
meta_title: "Visão Geral do Upstart - Init"
meta_description: "Aprenda sobre o Upstart, seu modelo orientado a eventos e como ele gerencia serviços no Linux. Entenda as configurações de job do Upstart e seu papel como um sistema init."
meta_keywords: "Upstart, sistema init, serviços Linux, Ubuntu, SysV, tutorial para iniciantes, guia Linux"
---

## Lesson Content

O Upstart foi desenvolvido pela Canonical, então foi a implementação init no Ubuntu por um tempo; no entanto, nas instalações modernas do Ubuntu, o systemd é agora usado. O Upstart foi criado para melhorar os problemas com o SysV, como processos de inicialização rigorosos, bloqueio de tarefas, etc. O modelo orientado a eventos e tarefas do Upstart permite que ele responda aos eventos à medida que eles acontecem.

Para descobrir se você está usando o Upstart, se você tem um diretório `/usr/share/upstart`, isso é um bom indicador.

Jobs são as ações que o Upstart executa, e eventos são mensagens que são recebidas de outros processos para acionar jobs. Para ver uma lista de jobs e suas configurações:

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

Dentro dessas configurações de job, você encontrará informações sobre como e quando iniciar os jobs.

Por exemplo, no arquivo `networking.conf`, pode dizer algo tão simples como:

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

Isso significa que ele começará a configurar a rede nos runlevels 2, 3 ou 5 e interromperá a rede no runlevel 0. Existem muitas maneiras de escrever o arquivo de configuração, e você descobrirá isso ao olhar as diferentes configurações de job disponíveis.

A forma como o Upstart funciona é que:

1. Primeiro, ele carrega as configurações de job de `/etc/init`.
2. Uma vez que um evento de inicialização ocorre, ele executará os jobs acionados por esse evento.
3. Esses jobs criarão novos eventos, e então esses eventos acionarão mais jobs.
4. O Upstart continua a fazer isso até completar todos os jobs necessários.

## Exercise

Se você estiver executando o Upstart, veja se consegue entender as configurações de job em `/etc/init`.

## Quiz Question

Qual é a implementação init usada pelo Ubuntu?

## Quiz Answer

upstart
