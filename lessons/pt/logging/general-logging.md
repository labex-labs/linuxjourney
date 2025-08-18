---
lang: "pt"
title: "Registro Geral"
meta_description: "Aprenda sobre arquivos de log do Linux como /var/log/messages e syslog. Entenda suas diferenças para uma solução de problemas eficaz do sistema. Comece sua jornada no Linux!"
meta_keywords: "Logs do Linux, syslog, var/log/messages, solução de problemas do Linux, iniciante em Linux, guia do Linux, logs do sistema"
---

## Lesson Content

Existem muitos arquivos de log que você pode visualizar em seu sistema; muitos importantes podem ser encontrados em `/var/log`. Não abordaremos todos, mas discutiremos alguns dos principais.

Existem dois arquivos de log gerais que você pode visualizar para ter uma ideia do que seu sistema está fazendo:

### `/var/log/messages`

Este log contém todas as mensagens não críticas e não de depuração, incluindo mensagens registradas durante a inicialização (dmesg), auth, cron, daemon, etc. É muito útil para ter uma ideia de como sua máquina está se comportando.

### `/var/log/syslog`

Este registra tudo, exceto as mensagens de auth; é extremamente útil para depurar erros em sua máquina.

Esses dois logs devem ser mais do que suficientes ao solucionar problemas com seu sistema. No entanto, se você quiser apenas visualizar um componente de log específico, também existem logs separados para eles.

## Exercise

Look at your `/var/log/messages` and `/var/log/syslog` files and see what the differences are.

## Quiz Question

Qual arquivo de log registra tudo, exceto as mensagens de auth?

## Quiz Answer

syslog
