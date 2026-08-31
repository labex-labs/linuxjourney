---
lesson_id: "kernel-logging"
course_id: "logging"
lang: "pt"
order_index: 4
title: "Registro do Kernel"
description: "Aprenda a consultar mensagens atuais e retidas do kernel Linux com dmesg e journalctl."
meta_title: "Registro do Kernel - Logging"
meta_description: "Explore o log do kernel Linux, incluindo /var/log/kern.log e dmesg. Aprenda a verificar o log kern para mensagens de inicialização, informações de drivers de hardware e solucionar problemas do sistema. Um guia para arquivos de log do kernel Linux."
meta_keywords: "log do kernel, kern.log, /var/log/kern.log, log kernel linux, log kern, dmesg, logging linux, mensagens de inicialização, eventos do kernel"
---

O kernel emite mensagens sobre boot, drivers, dispositivos, sistemas de arquivos, rede, memória e falhas. Esses registros explicam sintomas de baixo nível, mas um aviso isolado não prova defeito no hardware.

## Leitura do buffer circular do kernel

`dmesg` lê mensagens do buffer circular:

```bash
$ dmesg --human
```

O buffer tem capacidade finita, portanto mensagens novas podem sobrescrever antigas. O acesso também pode exigir privilégio. `dmesg --follow` acompanha novas mensagens quando compatível; interrompa depois de uma reprodução limitada.

:::single-choice{#kernel-log-ring-buffer-limit}
Por que um evento antigo pode não aparecer no `dmesg` atual?

::option[Eventos do kernel só podem conter um caractere.]{#kernel-log-one-character explanation="Mensagens podem conter texto normal de diagnóstico e metadados."}
::option[`dmesg` apaga permanentemente toda linha exibida.]{#kernel-log-display-deletes explanation="Uma leitura normal não consome as mensagens mostradas."}
::option[O buffer finito pode tê-lo sobrescrito.]{#kernel-log-overwritten .correct explanation="O buffer em memória retém uma quantidade limitada de dados."}
:::

## Uso de horários legíveis

Horários brutos do kernel costumam ser relativos ao boot. `dmesg --ctime` ou `--human` pode convertê-los para hora do relógio, mas o resultado depende do histórico do relógio e pode ficar impreciso após mudanças. Preserve o tempo relativo quando a sequência exata importar.

:::single-choice{#kernel-log-timestamp-caution}
Por que horários convertidos do `dmesg` exigem cuidado?

::option[Eles sempre se referem a outra máquina.]{#kernel-log-other-machine explanation="Eles são derivados localmente, embora mudanças do relógio afetem a conversão."}
::option[Eles mapeiam o tempo relativo a um relógio que pode mudar.]{#kernel-log-clock-change .correct explanation="Sincronização ou ajustes manuais podem tornar a hora exibida enganosa."}
::option[Eles mostram espaço livre em vez de tempo.]{#kernel-log-free-space explanation="As opções continuam exibindo horários, não capacidade."}
:::

## Consulta de registros persistentes

Em systemd, consulte o kernel do boot atual com:

```bash
$ journalctl -k -b
```

Se boots anteriores foram retidos:

```bash
$ journalctl --list-boots
$ journalctl -k -b -1
```

O roteamento tradicional do syslog pode criar `/var/log/kern.log` ou outro arquivo, mas isso depende da configuração. Um arquivo `/var/log/dmesg` salvo também não é universal e pode representar apenas um snapshot do momento da inicialização.

:::single-choice{#kernel-log-previous-boot}
Qual comando solicita mensagens do kernel no boot anterior retido?

::option[`journalctl -u kernel -f`]{#kernel-log-unit-follow explanation="Mensagens do kernel usam `-k`, e acompanhar não escolhe o boot anterior."}
::option[`dmesg --clear`]{#kernel-log-clear explanation="Limpar altera o buffer e não recupera um boot anterior."}
::option[`journalctl -k -b -1`]{#kernel-log-previous .correct explanation="O filtro de kernel com deslocamento menos um escolhe o boot anterior retido."}
:::

## Investigação de um evento

Identifique a inicialização, o registro de horário, o dispositivo, o subsistema e a ação que ocorria naquele momento. Consulte os registros próximos do kernel e dos serviços e, em seguida, compare o inventário de hardware e o estado atual:

```bash
$ journalctl -k -b --since '10 minutes ago'
$ lspci -k
$ lsblk
```

Use apenas ferramentas relevantes. Antes de recarregar driver, desvincular dispositivo ou reiniciar, avalie impacto em armazenamento, rede, console e serviços e preserve o acesso de recuperação.

:::single-choice{#kernel-log-warning-response}
Qual é a melhor resposta a uma única linha de aviso do kernel?

::option[Descarregar imediatamente todos os drivers.]{#kernel-log-unload-all explanation="Isso pode interromper dispositivos críticos sem isolar a causa."}
::option[Presumir que toda a máquina precisa ser substituída.]{#kernel-log-replace-machine explanation="Um registro isolado é evidência insuficiente."}
::option[Correlacioná-la com eventos próximos e o estado atual.]{#kernel-log-correlate .correct explanation="Contexto e impacto reproduzível são necessários antes de corrigir."}
:::

## Resumo

Agora você consegue distinguir mensagens ativas do buffer de logs retidos do kernel.

1. Ler o buffer finito com `dmesg`.
2. Interpretar cuidadosamente horários relativos e convertidos.
3. Consultar boots atuais ou anteriores com `journalctl -k`.
4. Correlacionar mensagens antes de mudanças disruptivas.
