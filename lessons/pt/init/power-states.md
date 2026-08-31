---
lesson_id: "power-states"
course_id: "init"
lang: "pt"
order_index: 7
title: "Estados de energia"
description: "Aprenda a agendar, cancelar e verificar com segurança operações de desligamento e reinicialização do Linux."
meta_title: "Estados de energia - Init"
meta_description: "Aprenda a gerenciar os estados de energia de um sistema Linux. Este guia aborda os comandos essenciais shutdown, reboot e halt para desligar ou reiniciar seu sistema Linux com segurança. Domine esses comandos fundamentais do Linux para a administração de sistemas."
meta_keywords: "estados de energia linux, comando shutdown, comando reboot, comando halt, desligar linux, reiniciar linux, administração de sistemas linux, linux para iniciantes, comandos linux, systemd, init"
---

Desligar ou reinicializar altera a disponibilidade de todo o sistema. Antes de agir, confirme o host de destino, obtenha autorização, avise os usuários conectados e garanta que gravações, backups e tarefas de manutenção importantes possam ser concluídos. Em um sistema remoto, preserve um console independente ou um caminho de recuperação caso a máquina não volte.

## Desligando com segurança

Em uma distribuição baseada no systemd, solicite um desligamento ordenado com:

```bash
$ sudo systemctl poweroff
```

A interface tradicional `shutdown` também está amplamente disponível:

```bash
$ sudo shutdown -h now
```

Um desligamento ordenado solicita que os serviços parem, desmonta os sistemas de arquivos e então altera o estado de energia da máquina. Não trate uma reinicialização forçada nem o botão físico de energia como um atalho comum; ambos podem interromper gravações e deixar dados ou serviços inconsistentes.

:::single-choice{#power-states-orderly-poweroff}
O que você deve fazer antes de desligar um host remoto de produção?

::option[Desconectar seu console de gerenciamento antes de emitir o comando.]{#power-states-remove-console explanation="Um console de gerenciamento é um acesso útil para recuperação e deve permanecer disponível."}
::option[Forçar o desligamento para que os serviços não possam atrasar a operação.]{#power-states-force-first explanation="Uma operação forçada pode interromper gravações e não deve ser o método normal."}
::option[Confirmar o host e preservar um caminho de acesso para recuperação.]{#power-states-confirm-and-recover .correct explanation="A confirmação do destino evita agir no host errado, enquanto o acesso de recuperação ajuda caso ele não volte."}
:::

## Agendando e cancelando um desligamento

Dê aos usuários e às cargas de trabalho tempo para se preparar agendando a operação. A forma `+m` representa uma quantidade de minutos a partir de agora:

```bash
$ sudo shutdown -h +4
```

Isso agenda uma parada ou um desligamento para daqui a quatro minutos e envia avisos aos usuários conectados. Se a manutenção for adiada, cancele o desligamento pendente antes do prazo:

```bash
$ sudo shutdown -c
```

Não presuma que um aviso torna a operação segura. Verifique as sessões ativas e as cargas de trabalho específicas do sistema e siga o procedimento documentado de drenagem do serviço ou cluster, quando houver.

:::single-choice{#power-states-four-minute-schedule}
Qual comando agenda um desligamento para daqui a quatro minutos?

::option[`sudo shutdown -h +4`]{#power-states-relative-four .correct explanation="A ação `-h` combinada com `+4` solicita o desligamento para daqui a quatro minutos."}
::option[`sudo shutdown -h 4`]{#power-states-absolute-four explanation="Sem o sinal de adição, o argumento de tempo não está na forma documentada de minutos relativos."}
::option[`sudo shutdown -c +4`]{#power-states-cancel-four explanation="A opção `-c` cancela um desligamento pendente em vez de criar um."}
:::

## Reinicializando o sistema

Use uma reinicialização ordenada quando a máquina precisar parar e iniciar novamente:

```bash
$ sudo systemctl reboot
```

Entre os comandos de compatibilidade equivalentes normalmente estão:

```bash
$ sudo shutdown -r now
$ sudo reboot
```

Antes de reinicializar, verifique se discos criptografados, a configuração de inicialização, a rede e os serviços necessários podem se recuperar sem a sessão interativa atual. Coordene primeiro o failover ou a migração da carga de trabalho quando outros sistemas dependerem do host.

:::single-choice{#power-states-reboot-action}
Qual comando solicita uma reinicialização ordenada imediata por meio de `shutdown`?

::option[`sudo shutdown -c now`]{#power-states-cancel-now explanation="A opção `-c` cancela um desligamento pendente."}
::option[`sudo shutdown -r now`]{#power-states-reboot-now .correct explanation="A opção `-r` seleciona a reinicialização, e `now` a agenda imediatamente."}
::option[`sudo shutdown -h now`]{#power-states-halt-now explanation="A ação `-h` para ou desliga, em vez de reinicializar."}
:::

## Diferenciando parada e desligamento

`halt`, `poweroff` e `reboot` podem ser interfaces de compatibilidade para o sistema de init, mas seus estados finais solicitados são diferentes. Uma parada encerra a operação normal do sistema; dependendo da plataforma e da implementação, ela pode manter a alimentação elétrica. Um desligamento também solicita que o hardware compatível corte a energia. Prefira o comando que nomeia o resultado pretendido e consulte o manual local, pois o comportamento de compatibilidade pode variar.

:::single-choice{#power-states-halt-versus-poweroff}
Por que você deve diferenciar `halt` de `poweroff`?

::option[Power-off solicita o corte da energia, enquanto halt pode mantê-la.]{#power-states-power-distinction .correct explanation="O estado final solicitado ao hardware pode ser diferente, mesmo quando ambos encerram a operação normal."}
::option[Halt sempre reinicia os serviços depois que eles param.]{#power-states-halt-restarts explanation="Halt é um estado de parada, não uma solicitação para reiniciar serviços."}
::option[Power-off apenas encerra a sessão do usuário atual do terminal.]{#power-states-power-logout explanation="Power-off é uma transição de estado de todo o sistema, não a saída de um shell."}
:::

## Verificando o resultado

Para uma operação agendada, confirme que os usuários receberam o aviso e que o trabalho crítico foi drenado. Depois de uma reinicialização, verifique o kernel e o estado de inicialização esperados, as unidades com falha, a integridade da aplicação, as montagens de armazenamento, a conectividade de rede e os logs recentes da inicialização. Apenas conseguir iniciar uma sessão não comprova que todo o serviço se recuperou.

```bash
$ uptime
$ systemctl --failed
$ journalctl -b -p warning
```

Esses são pontos de partida; use as verificações de integridade próprias da aplicação para a carga de trabalho real.

:::single-choice{#power-states-post-reboot-check}
O que fornece a evidência mais forte de que uma aplicação reinicializada está pronta?

::option[O estado do serviço, os logs e sua verificação de integridade indicam sucesso.]{#power-states-health-evidence .correct explanation="Várias verificações do sistema e da aplicação validam a carga de trabalho, não apenas o acesso ao host."}
::option[O indicador de energia do gabinete está aceso.]{#power-states-light-on explanation="A alimentação do hardware não comprova a integridade da aplicação."}
::option[Um administrador consegue iniciar uma sessão em um shell.]{#power-states-shell-open explanation="O acesso ao shell comprova apenas parte da disponibilidade do sistema."}
:::

## Resumo

Agora você pode alterar os estados de energia do Linux com preparação, intenção clara e verificação.

1. Confirme o destino, o impacto, a autorização e o caminho de recuperação.
2. Use comandos de desligamento ou reinicialização ordenados em operações normais.
3. Agende um desligamento quando usuários e cargas de trabalho precisarem de aviso.
4. Cancele um desligamento pendente quando o plano de manutenção mudar.
5. Verifique a integridade do sistema e da aplicação depois que a máquina voltar.
