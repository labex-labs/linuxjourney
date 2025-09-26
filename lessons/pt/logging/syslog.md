---
index: 2
lang: "pt"
title: "syslog"
meta_title: "syslog - Registro de Logs"
meta_description: "Aprenda sobre syslog e rsyslog no Linux, como gerenciar logs do sistema e usar o comando logger. Comece com este tutorial amigável para iniciantes!"
meta_keywords: "syslog, rsyslog, logs Linux, comando logger, /var/log/syslog, tutorial Linux, Linux para iniciantes, registro de sistema"
---

## Lesson Content

O serviço syslog gerencia e envia logs para o registrador do sistema. O Rsyslog é uma versão avançada do syslog; a maioria das distribuições Linux deve estar usando esta nova versão. A saída de todos os logs que o serviço syslog coleta pode ser encontrada em `/var/log/syslog` (todas as mensagens, exceto as de autenticação).

Para descobrir quais arquivos são mantidos pelo nosso registrador do sistema, verifique os arquivos de configuração em `/etc/rsyslog.d`:

```plaintext
pete@icebox:~$ less /etc/rsyslog.d/50-default.conf
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log
```

Estas regras para arquivos de log são denotadas pelo seletor na coluna da esquerda e pela ação na coluna da direita. A ação nos diz para onde enviar a informação do log: para um arquivo, console, etc. Lembre-se, nem todo aplicativo e serviço usa rsyslog para gerenciar seus logs, então, se você quiser saber especificamente o que está sendo registrado, terá que olhar dentro deste diretório.

Vamos ver o registro de logs em ação; você pode enviar um log manualmente com o comando `logger`:

```bash
logger -s Hello
```

Agora olhe dentro do seu `/var/log/syslog`, e você deverá ver esta entrada em seus logs.

## Exercise

Praticar leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre registro de logs do Linux e visualização de arquivos:

1. **[Visualizando Arquivos de Log e Configuração no Linux](https://labex.io/pt/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Pratique habilidades essenciais de linha de comando do Linux para visualizar e navegar eficientemente em arquivos de texto, incluindo logs do sistema e arquivos de configuração.
2. **[Comando tail do Linux: Exibição do Final do Arquivo](https://labex.io/pt/labs/linux-linux-tail-command-file-end-display-214303)** - Aprenda o comando `tail` do Linux para visualizar e monitorar o final de arquivos de texto, o que é particularmente útil para análise de logs em tempo real.
3. **[Pesquisar Texto com grep no Linux](https://labex.io/pt/labs/comptia-search-text-with-grep-in-linux-590841)** - Aprenda a procurar por padrões de texto específicos dentro de arquivos, uma habilidade inestimável para peneirar entradas de log em busca de informações críticas.

Estes laboratórios ajudarão você a aplicar os conceitos de gerenciamento de logs e inspeção de arquivos em cenários reais e a construir confiança com a administração do sistema Linux.

## Quiz Question

Qual comando você pode usar para registrar manualmente uma mensagem?

## Quiz Answer

logger
