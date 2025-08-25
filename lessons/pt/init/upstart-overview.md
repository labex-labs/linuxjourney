---
index: 3
lang: "pt"
title: "Visão Geral do Upstart"
meta_title: "Visão Geral do Upstart - Init"
meta_description: "Aprenda sobre o Upstart, seu modelo orientado a eventos e como ele gerencia serviços no Linux. Entenda as configurações de job do Upstart e seu papel como um sistema init."
meta_keywords: "Upstart, sistema init, serviços Linux, Ubuntu, SysV, tutorial para iniciantes, guia Linux"
---

## Lesson Content

O Upstart foi desenvolvido pela Canonical, então foi a implementação init no Ubuntu por um tempo; no entanto, em instalações modernas do Ubuntu, o systemd é agora utilizado. O Upstart foi criado para melhorar os problemas com o SysV, como processos de inicialização rígidos, bloqueio de tarefas, etc. O modelo orientado a eventos e tarefas do Upstart permite que ele responda a eventos à medida que acontecem.

Para descobrir se você está usando o Upstart, se você tiver um diretório `/usr/share/upstart`, isso é um bom indicador.

Jobs são as ações que o Upstart executa, e eventos são mensagens recebidas de outros processos para acionar jobs. Para ver uma lista de jobs e suas configurações:

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

A forma como o Upstart funciona é a seguinte:

1. Primeiro, ele carrega as configurações de job de `/etc/init`.
2. Uma vez que um evento de inicialização ocorre, ele executará os jobs acionados por esse evento.
3. Esses jobs criarão novos eventos, e então esses eventos acionarão mais jobs.
4. O Upstart continua a fazer isso até completar todos os jobs necessários.

## Exercise

A prática leva à perfeição! Embora o Upstart seja um sistema init mais antigo, entender como os processos são gerenciados e as tarefas são agendadas é crucial para qualquer administrador Linux. Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de processos e automação de tarefas, que são fundamentais para o funcionamento dos sistemas init:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro e segundo plano, inspecionando-os com `ps`, monitorando recursos com `top` e encerrando-os com `kill`. Este laboratório ajuda você a entender o ciclo de vida dos processos, que sistemas init como o Upstart gerenciam.
2. **[Agendar Tarefas com at e cron no Linux](https://labex.io/pt/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Aprenda a agendar jobs únicos com `at` e tarefas recorrentes com `cron`. Isso fornece experiência prática com a automação de tarefas, uma função central que os sistemas init facilitam para os serviços do sistema.

Esses laboratórios o ajudarão a aplicar os conceitos de controle de processos e automação de tarefas em cenários reais, construindo confiança no gerenciamento de um sistema Linux, independentemente do sistema init específico em uso.

## Quiz Question

Qual é a implementação init usada pelo Ubuntu?

## Quiz Answer

upstart
