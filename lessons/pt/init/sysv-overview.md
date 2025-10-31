---
index: 1
lang: "pt"
title: "Visão Geral do System V"
meta_title: "Visão Geral do System V - Init"
meta_description: "Explore o sistema init tradicional System V, também conhecido como SysV ou init v. Este guia aborda como o systemv gerencia processos, sua inicialização sequencial e o papel dos níveis de execução (runlevels) no Linux. Aprenda os fundamentos do processo clássico initv."
meta_keywords: "System V, systemv, SysV init, systemv init, init v, initv, níveis de execução Linux, sistema init, gerenciamento de processos, tutorial Linux"
---

## Lesson Content

O papel principal de um sistema init é iniciar e parar processos essenciais. O Linux viu três grandes implementações de init: System V, Upstart e systemd. Esta lição foca na versão mais tradicional, **System V init**, frequentemente referida como **SysV** ou simplesmente **systemv** (pronuncia-se 'System Five').

Para determinar se o seu sistema usa a implementação **systemv**, verifique a existência de um arquivo `/etc/inittab`. Se este arquivo existir, você está muito provavelmente executando uma distribuição baseada em SysV.

### Como o System V Gerencia Processos

O processo **systemv init** inicia e para serviços sequencialmente. Por exemplo, se um serviço chamado `foo-b` depende de `foo-a`, `foo-b` não pode iniciar até que `foo-a` esteja totalmente em execução. O sistema **initv** consegue isso usando scripts shell. Esses scripts, localizados em diretórios específicos, lidam com a inicialização e o desligamento de serviços. Embora você possa escrever scripts personalizados, a maioria dos sistemas depende dos scripts pré-configurados que gerenciam os serviços essenciais do SO.

### Vantagens e Desvantagens

A principal vantagem dessa abordagem sequencial é sua simplicidade e previsibilidade. A solução de problemas de dependências é direta porque você sabe que `foo-a` sempre inicia antes de `foo-b`. No entanto, a principal desvantagem do modelo **init v** é o desempenho, pois os serviços são tipicamente iniciados um de cada vez, resultando em tempos de inicialização mais lentos em comparação com sistemas paralelos modernos.

### Entendendo os Níveis de Execução (Runlevels) no System V

Em um ambiente **systemv**, o estado da máquina é definido por **runlevels** (níveis de execução), numerados de 0 a 6. Esses modos podem variar ligeiramente entre as distribuições Linux, mas geralmente seguem esta convenção padrão:

- 0: Desligamento (Shutdown)
- 1: Modo de Usuário Único (Single User Mode)
- 2: Modo multiusuário sem rede
- 3: Modo multiusuário com rede
- 4: Não utilizado
- 5: Modo multiusuário com rede e GUI
- 6: Reinicialização (Reboot)

### Scripts e Diretórios Init

Quando o sistema é inicializado, ele verifica seu nível de execução configurado e executa os scripts correspondentes. Esses scripts são tipicamente encontrados em diretórios como **/etc/rc.d/rc[runlevel].d/** ou dentro de um diretório central **/etc/init.d**. Scripts que começam com `S` (Start/Iniciar) são executados durante a inicialização, enquanto aqueles que começam com `K` (Kill/Matar) são executados durante o desligamento. Os números que seguem `S` ou `K` ditam a ordem de execução.

Por exemplo:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Neste exemplo, a mudança para o nível de execução 0 (desligamento) executará primeiro o script para matar o serviço de atualizações, seguido pelo script para OpenVPN. Você pode encontrar o nível de execução padrão da sua máquina no arquivo `/etc/inittab`, onde também pode alterá-lo.

É importante notar que o **System V** foi amplamente substituído pelo `systemd` na maioria das distribuições Linux modernas. No entanto, você ainda pode encontrar o conceito de níveis de execução em sistemas init mais novos, pois eles frequentemente fornecem uma camada de compatibilidade para suportar serviços legados que dependem de scripts **systemv init**.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de processos Linux e configuração do sistema, que são fundamentais para o funcionamento dos sistemas init:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro plano e em segundo plano, inspecionando-os com `ps`, monitorando recursos com `top` e terminando-os com `kill`. Isso se relaciona diretamente com o aspecto de 'iniciar e parar processos essenciais' do init.
2. **[Agendar Tarefas com at e cron no Linux](https://labex.io/pt/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Aprenda a agendar tarefas únicas e recorrentes, o que se baseia no conceito de execução automatizada, semelhante à forma como os scripts init gerenciam serviços.
3. **[Gerenciar Permissões de Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Entenda como gerenciar permissões de arquivos e diretórios, uma habilidade crítica para trabalhar com arquivos de configuração do sistema e scripts como os encontrados em `/etc/init.d`.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança com tarefas fundamentais de administração de sistemas Linux.

## Quiz Question

Qual nível de execução é geralmente usado para desligamento?

## Quiz Answer

0
