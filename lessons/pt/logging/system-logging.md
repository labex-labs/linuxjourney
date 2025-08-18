---
lang: "pt"
title: "Registo de Sistema"
meta_title: "Registo de Sistema - Registro de Logs"
meta_description: "Aprenda sobre o registo de sistema Linux, syslog e como visualizar ficheiros de log em /var/log. Compreenda o rsyslogd e monitorize eventos do sistema com este guia para iniciantes."
meta_keywords: "Registo Linux, syslog, rsyslogd, var log, logs de sistema, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Os serviços, kernel, daemons, etc., no seu sistema estão constantemente a fazer algo. Estes dados são, na verdade, enviados para serem guardados no seu sistema na forma de logs. Isto permite-nos ter um diário legível por humanos dos eventos que estão a acontecer no nosso sistema. Estes dados são geralmente mantidos no diretório `/var`; o diretório `/var` é onde guardamos os nossos dados variáveis, como os logs!

Como é que estas mensagens são recebidas no seu sistema? Existe um serviço chamado syslog que envia esta informação para o registador de sistema.

O Syslog contém, na verdade, muitos componentes. Um dos importantes é um daemon em execução chamado `syslogd` (distribuições Linux mais recentes usam `rsyslogd`), que espera que ocorram mensagens de evento e filtra as que quer saber. Dependendo do que deve fazer com essa mensagem, ele irá enviá-la para um ficheiro, para a sua consola, ou não fazer nada com ela.

Poder-se-ia pensar que este registador de sistema é o local centralizado para gerir logs, mas infelizmente, não é. Verá muitas aplicações que escrevem as suas próprias regras de logging e geram diferentes ficheiros de log. No entanto, em geral, o formato dos logs deve incluir um carimbo de data/hora e os detalhes do evento.

Aqui está um exemplo de uma linha do syslog:

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Aqui podemos ver que a 27 de janeiro às 07:41:32, o nosso serviço cron executou a tarefa `cron.weekly`. Pode ver todas as mensagens de evento que o syslog recolhe no ficheiro `/var/log/syslog`.

## Exercise

Observe o seu ficheiro `/var/log/syslog` e veja o que mais está a acontecer na sua máquina.

## Quiz Question

Qual é o daemon que gere os logs em sistemas Linux mais recentes?

## Quiz Answer

rsyslogd
