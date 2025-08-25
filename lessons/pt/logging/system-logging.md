---
index: 1
lang: "pt"
title: "Registro de Sistema"
meta_title: "Registro de Sistema - Logging"
meta_description: "Aprenda sobre o registro de sistema Linux, syslog e como visualizar arquivos de log em /var/log. Entenda rsyslogd e monitore eventos do sistema com este guia para iniciantes."
meta_keywords: "Registro Linux, syslog, rsyslogd, var log, logs do sistema, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Os serviços, kernel, daemons, etc., em seu sistema estão constantemente fazendo algo. Esses dados são realmente enviados para serem salvos em seu sistema na forma de logs. Isso nos permite ter um diário legível por humanos dos eventos que estão acontecendo em nosso sistema. Esses dados geralmente são mantidos no diretório `/var`; o diretório `/var` é onde mantemos nossos dados variáveis, como logs!

Como essas mensagens são recebidas em seu sistema? Existe um serviço chamado syslog que envia essas informações para o registrador do sistema.

syslog na verdade contém muitos componentes. Um dos importantes é um daemon em execução chamado `syslogd` (distribuições Linux mais recentes usam `rsyslogd`), que espera que mensagens de evento ocorram e filtra as que deseja saber. Dependendo do que ele deve fazer com essa mensagem, ele a enviará para um arquivo, para o seu console ou não fará nada com ela.

Você pensaria que este registrador de sistema é o local centralizado para gerenciar logs, mas, infelizmente, não é. Você verá muitos aplicativos que escrevem suas próprias regras de log e geram diferentes arquivos de log. No entanto, em geral, o formato dos logs deve incluir um carimbo de data/hora e os detalhes do evento.

Aqui está um exemplo de uma linha do syslog:

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Aqui podemos ver que em 27 de janeiro às 07:41:32, nosso serviço cron executou o trabalho `cron.weekly`. Você pode visualizar todas as mensagens de evento que o syslog coleta no arquivo `/var/log/syslog`.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão dos logs do Linux e da visualização de arquivos:

1. **[Visualizando Arquivos de Log e Configuração no Linux](https://labex.io/pt/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Aprenda habilidades essenciais da linha de comando Linux para visualizar e navegar eficientemente em arquivos de texto, incluindo logs do sistema e arquivos de configuração. Pratique o uso de comandos como `cat`, `more` e `less` para extrair informações críticas de vários tipos de arquivo.
2. **[Comando Linux tail: Exibição do Final do Arquivo](https://labex.io/pt/labs/linux-linux-tail-command-file-end-display-214303)** - Aprenda o comando Linux `tail` para visualizar e monitorar o final dos arquivos de texto. Isso é particularmente útil para análise de log em tempo real.
3. **[Pesquisar Texto com grep no Linux](https://labex.io/pt/labs/comptia-search-text-with-grep-in-linux-590841)** - Neste laboratório, você aprenderá a pesquisar texto em arquivos em um sistema Linux usando o comando `grep`. Isso é inestimável para encontrar entradas específicas em grandes arquivos de log.

Esses laboratórios o ajudarão a aplicar os conceitos de gerenciamento e análise de arquivos de log em cenários reais e a construir confiança com o monitoramento do sistema Linux.

## Quiz Question

Qual é o daemon que gerencia logs em sistemas Linux mais recentes?

## Quiz Answer

rsyslogd
