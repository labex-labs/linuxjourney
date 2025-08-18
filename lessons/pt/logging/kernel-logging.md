---
lang: "pt"
title: "Registro do Kernel"
meta_title: "Registro do Kernel - Registro de Logs"
meta_description: "Aprenda sobre o registro do kernel Linux com dmesg e kern.log. Entenda as mensagens de inicialização e problemas de hardware. Explore os logs do kernel para insights do sistema."
meta_keywords: "dmesg, kern.log, registro Linux, mensagens do kernel, log de inicialização, tutorial Linux, guia para iniciantes"
---

## Lesson Content

### /var/log/dmesg

No momento da inicialização, seu sistema registra informações sobre o buffer circular do kernel. Isso nos mostra informações sobre drivers de hardware, informações do kernel e status durante a inicialização, entre outras coisas. Este arquivo de log pode ser encontrado em `/var/log/dmesg` e é redefinido a cada inicialização. Você pode não ver nenhum uso nele agora, mas se você tiver problemas com algo durante a inicialização ou um problema de hardware, `dmesg` é o melhor lugar para procurar. Você também pode visualizar este log usando o comando `dmesg`.

### /var/log/kern.log

Outro log que você pode usar para visualizar informações do kernel é o arquivo `/var/log/kern.log`. Este registra informações e eventos do kernel em seu sistema; ele também registra a saída do `dmesg`.

## Exercise

Observe seus logs `dmesg` e `kern`. Que diferenças você nota?

## Quiz Question

Qual comando pode ser usado para visualizar as mensagens de inicialização do kernel?

## Quiz Answer

dmesg
