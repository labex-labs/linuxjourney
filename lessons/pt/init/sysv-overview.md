---
lang: "pt"
title: "Visão Geral do System V"
description: "Aprenda sobre o System V init, seus runlevels e como ele gerencia processos no Linux. Entenda os conceitos básicos do SysV para usuários iniciantes e intermediários."
keywords: "System V, SysV init, runlevels Linux, sistema init, tutorial Linux, guia para iniciantes, gerenciamento de processos"
---

## Lesson Content

O principal objetivo do init é iniciar e parar processos essenciais no sistema. Existem três implementações principais de init no Linux: System V, Upstart e systemd. Nesta lição, vamos abordar a versão mais tradicional do init, System V init ou Sys V (pronuncia-se 'System Five').

Para descobrir se você está usando a implementação Sys V init, verifique a existência de um arquivo `/etc/inittab`; se ele existir, você provavelmente está executando o Sys V.

O Sys V inicia e para processos sequencialmente. Por exemplo, se você quisesse iniciar um serviço chamado `foo-a`, `foo-b` não pode funcionar até que `foo-a` já esteja em execução. O Sys V consegue isso com scripts. Esses scripts iniciam e param serviços para nós. Podemos escrever nossos próprios scripts ou, na maioria das vezes, usar os que já vêm embutidos no sistema operacional e são usados para carregar serviços essenciais.

As vantagens de usar esta implementação de init são que é relativamente fácil resolver dependências, já que você sabe que `foo-a` vem antes de `foo-b`. No entanto, o desempenho não é ótimo porque geralmente apenas uma coisa está iniciando ou parando por vez.

Ao usar o Sys V, o estado da máquina é definido por runlevels, que são configurados de 0 a 6. Esses diferentes modos variarão dependendo da distribuição, mas na maioria das vezes serão semelhantes ao seguinte:

- 0: Desligar
- 1: Modo de Usuário Único
- 2: Modo multiusuário sem rede
- 3: Modo multiusuário com rede
- 4: Não utilizado
- 5: Modo multiusuário com rede e GUI
- 6: Reiniciar

Quando o sistema inicia, ele verifica em qual runlevel você está e executa scripts localizados dentro da configuração desse runlevel. Os scripts estão localizados em **/etc/rc.d/rc[runlevel number].d/** ou **/etc/init.d**. Scripts que começam com S (start) ou K (kill) serão executados na inicialização e no desligamento, respectivamente. Os números ao lado desses caracteres indicam a sequência em que são executados.

Por exemplo:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Vemos que, ao mudar para o runlevel 0 ou modo de desligamento, nossa máquina tentará executar um script para encerrar os serviços de atualização e, em seguida, o OpenVPN. Para descobrir em qual runlevel sua máquina está inicializando, você pode ver o runlevel padrão no arquivo `/etc/inittab`. Você também pode alterar seu runlevel padrão neste arquivo.

Uma coisa a notar: o System V está sendo lentamente substituído, talvez não hoje, ou mesmo daqui a anos. No entanto, você pode ver runlevels aparecerem em outras implementações de init. Isso é principalmente para suportar aqueles serviços que são iniciados ou parados apenas usando scripts de inicialização do System V.

## Exercise

Se você estiver executando o System V, altere o runlevel padrão da sua máquina para outra coisa e veja o que acontece.

## Quiz Question

Qual runlevel é geralmente usado para desligamento?

## Quiz Answer

0
