---
index: 1
lang: "pt"
title: "Visão Geral do System V"
meta_title: "Visão Geral do System V - Init"
meta_description: "Aprenda sobre o init System V, seus runlevels e como ele gerencia processos no Linux. Entenda os conceitos básicos do SysV para usuários iniciantes e intermediários."
meta_keywords: "System V, SysV init, runlevels Linux, sistema init, tutorial Linux, guia para iniciantes, gerenciamento de processos"
---

## Lesson Content

O principal propósito do init é iniciar e parar processos essenciais no sistema. Existem três implementações principais de init no Linux: System V, Upstart e systemd. Nesta lição, vamos analisar a versão mais tradicional do init, o System V init ou Sys V (pronunciado como 'System Five').

Para descobrir se você está usando a implementação Sys V init, verifique a existência de um arquivo `/etc/inittab`; se ele existir, você está muito provavelmente rodando Sys V.

O Sys V inicia e para processos sequencialmente. Por exemplo, se você quisesse iniciar um serviço chamado `foo-a`, o `foo-b` não poderia funcionar até que o `foo-a` já estivesse em execução. O Sys V realiza isso com scripts. Esses scripts iniciam e param serviços para nós. Podemos escrever nossos próprios scripts, ou na maioria das vezes, usar aqueles que já vêm embutidos no sistema operacional e são usados para carregar serviços essenciais.

As vantagens de usar esta implementação de init são que é relativamente fácil resolver dependências, já que você sabe que `foo-a` vem antes de `foo-b`. No entanto, o desempenho não é ótimo porque geralmente apenas uma coisa está iniciando ou parando por vez.

Ao usar o Sys V, o estado da máquina é definido por runlevels, que são definidos de 0 a 6. Esses diferentes modos variarão dependendo da distribuição, mas na maioria das vezes se parecerão com o seguinte:

- 0: Shutdown
- 1: Single User Mode
- 2: Multiuser mode without networking
- 3: Multiuser mode with networking
- 4: Unused
- 5: Multiuser mode with networking and GUI
- 6: Reboot

Quando seu sistema inicia, ele verifica em qual runlevel você está e executa os scripts localizados dentro da configuração desse runlevel. Os scripts estão localizados em **/etc/rc.d/rc[runlevel number].d/** ou **/etc/init.d**. Scripts que começam com S (start) ou K (kill) serão executados na inicialização e no desligamento, respectivamente. Os números ao lado desses caracteres indicam a sequência em que são executados.

Por exemplo:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Vemos que ao mudar para o runlevel 0 ou modo de desligamento, nossa máquina tentará executar um script para matar os serviços de atualizações e depois o OpenVPN. Para descobrir em qual runlevel sua máquina está inicializando, você pode ver o runlevel padrão no arquivo `/etc/inittab`. Você também pode alterar seu runlevel padrão neste arquivo.

Uma coisa a notar: o System V foi amplamente substituído pelo systemd na maioria das distribuições Linux modernas. No entanto, você pode ver runlevels surgirem em outras implementações de init. Isso é principalmente para suportar aqueles serviços que são iniciados ou parados usando scripts do System V init.

## Exercise

Praticar leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de processos Linux e configuração do sistema, que são fundamentais para o funcionamento dos sistemas init:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique interagir com processos em primeiro plano e em segundo plano, inspecionando-os com `ps`, monitorando recursos com `top` e terminando-os com `kill`. Isso se relaciona diretamente com o aspecto de 'iniciar e parar processos essenciais' do init.
2. **[Agendar Tarefas com at e cron no Linux](https://labex.io/pt/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Aprenda a agendar tarefas únicas e recorrentes, o que se baseia no conceito de execução automatizada, semelhante à forma como os scripts init gerenciam serviços.
3. **[Gerenciar Permissões de Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Entenda como gerenciar permissões de arquivos e diretórios, uma habilidade crítica para trabalhar com arquivos de configuração do sistema e scripts como os encontrados em `/etc/init.d`.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança com tarefas fundamentais de administração de sistemas Linux.

## Quiz Question

Qual runlevel é geralmente usado para desligamento (shutdown)?

## Quiz Answer

0
