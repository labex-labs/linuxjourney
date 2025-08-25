---
index: 3
lang: "pt"
title: "Registro Geral"
meta_title: "Registro Geral - Logs"
meta_description: "Aprenda sobre arquivos de log do Linux como /var/log/messages e syslog. Entenda suas diferenças para uma solução de problemas eficaz do sistema. Comece sua jornada no Linux!"
meta_keywords: "logs Linux, syslog, var/log/messages, solução de problemas Linux, Linux para iniciantes, guia Linux, logs do sistema"
---

## Lesson Content

Existem muitos arquivos de log que você pode visualizar em seu sistema; muitos importantes podem ser encontrados em `/var/log`. Não vamos abordar todos eles, mas discutiremos alguns dos principais.

Existem dois arquivos de log gerais que você pode visualizar para ter uma ideia do que seu sistema está fazendo:

### `/var/log/messages`

Este log contém todas as mensagens não críticas e não de depuração, incluindo mensagens registradas durante a inicialização (dmesg), autenticação, cron, daemon, etc. É muito útil para ter uma ideia de como sua máquina está se comportando.

### `/var/log/syslog`

Este registra tudo, exceto mensagens de autenticação; é extremamente útil para depurar erros em sua máquina.

Esses dois logs devem ser mais do que suficientes ao solucionar problemas com seu sistema. No entanto, se você quiser apenas visualizar um componente de log específico, também existem logs separados para eles.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre a visualização e análise de arquivos de log:

1. **[Comando Linux tail: Exibição do Final do Arquivo](https://labex.io/pt/labs/linux-linux-tail-command-file-end-display-214303)** - Aprenda o comando Linux `tail` para visualizar e monitorar o final de arquivos de texto, essencial para a análise de logs.
2. **[Comando Linux head: Exibição do Início do Arquivo](https://labex.io/pt/labs/linux-linux-head-command-file-beginning-display-214302)** - Explore o comando `head` para exibir as linhas iniciais de arquivos de texto, útil para verificar rapidamente os cabeçalhos de log.
3. **[Detecção Rápida de Ameaças](https://labex.io/pt/labs/linux-rapid-threat-detection-387930)** - Pratique habilidades essenciais da linha de comando Linux para análise de cibersegurança, usando `tail` e `head` para extrair e analisar rapidamente entradas de log recentes.

Esses laboratórios o ajudarão a aplicar os conceitos de visualização de arquivos de log em cenários reais e a construir confiança com o monitoramento do sistema.

## Quiz Question

Qual arquivo de log registra tudo, exceto as mensagens de autenticação?

## Quiz Answer

syslog
