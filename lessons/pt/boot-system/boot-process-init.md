---
lesson_id: "boot-process-init"
course_id: "boot-system"
lang: "pt"
order_index: 5
title: "Processo de Inicialização: Init"
description: "Aprenda como o PID 1 inicializa o espaço do usuário, supervisiona serviços, recolhe processos-filhos e coordena o desligamento."
meta_title: "Processo de Inicialização: Init - Inicialize o Sistema"
meta_description: "Explore o núcleo do processo de inicialização do Linux neste guia para iniciantes. Aprenda sobre os diferentes sistemas init do Linux, incluindo o tradicional System V, Upstart e o padrão moderno, systemd. Entenda como esses sistemas iniciam e gerenciam serviços em sua máquina."
meta_keywords: "init Linux, systemd, System V init, Upstart, processo de inicialização Linux, tutorial Linux, Linux para iniciantes, guia Linux"
---

O kernel inicia o primeiro processo do espaço do usuário como PID 1 em um namespace de PIDs. Em um sistema Linux completo, esse processo init estabelece o ambiente de serviços. Em um container, o PID 1 pode ser um pequeno wrapper de init ou o próprio aplicativo, mas ainda tem responsabilidades especiais sobre sinais e processos-filhos.

## Responsabilidades do PID 1

Um sistema init geralmente:

- inicia e supervisiona serviços, logins, montagens e outras unidades de trabalho
- ordena o trabalho conforme dependências e o estado de destino configurado
- adota e recolhe processos-filhos órfãos
- reage a falhas de serviços conforme a política
- coordena desligamentos e reinicializações ordenados

O limite exato varia. Gerenciamento de dispositivos, rede, logs e tarefas agendadas podem ser programas separados supervisionados pelo init, não código incorporado ao PID 1.

:::single-choice{#boot-init-pid-one-role}
Qual responsabilidade é especial para o PID 1 em seu namespace?

::option[Compilar todos os aplicativos a cada boot.]{#boot-init-compile-apps explanation="A inicialização normal usa programas instalados, em vez de recompilar todo o software."}
::option[Definir o tamanho físico dos setores do disco.]{#boot-init-sector-size explanation="O hardware e os drivers expõem a geometria do armazenamento antes que o init gerencie serviços."}
::option[Adotar e recolher processos-filhos órfãos.]{#boot-init-reap-orphans .correct explanation="O PID 1 é o pai final e precisa recolher o estado de término para evitar o acúmulo de processos zumbis."}
:::

## System V init e runlevels

O sysvinit tradicional usa configurações como `/etc/inittab` e scripts de inicialização e desligamento específicos de cada runlevel. Um runlevel representa um modo de operação, mas o significado dos níveis numerados pode variar entre distribuições. A ordem dos scripts segue convenções e pode ser ampliada ou paralelizada pelas ferramentas da distribuição.

Não deduza o init ativo apenas porque `/etc/init.d/` existe; scripts de compatibilidade podem permanecer em sistemas cujo PID 1 usa outra implementação.

:::single-choice{#boot-init-sysv-runlevel}
O que representa um runlevel do System V?

::option[Uma versão do kernel escolhida pelo carregador.]{#boot-init-runlevel-kernel explanation="A escolha do kernel pertence ao carregador e não é codificada por um runlevel."}
::option[Um modo de operação configurado associado a ações de serviços.]{#boot-init-runlevel-mode .correct explanation="Layouts SysV associam níveis a conjuntos e ordens de scripts de inicialização ou desligamento."}
::option[A porcentagem atual de inodes usados em um sistema de arquivos.]{#boot-init-runlevel-inodes explanation="A capacidade de metadados do sistema de arquivos não tem relação com modos de serviços."}
:::

## Sistemas baseados em eventos e dependências

O Upstart introduziu um modelo de jobs orientado a eventos e foi usado em versões antigas do Ubuntu e em outros sistemas. Hoje, ele tem interesse principalmente histórico ou para operação de sistemas legados.

O systemd é amplamente usado por distribuições atuais de uso geral. Ele modela serviços, sockets, montagens, temporizadores, dispositivos, targets e outros recursos como units. Dependências declarativas e mecanismos de ativação permitem que trabalhos independentes avancem em paralelo sem perder a ordem necessária.

Outros projetos ativos incluem OpenRC, runit, s6 e BusyBox init. “Mais recente” não é uma regra útil de compatibilidade; identifique o sistema realmente em execução e consulte sua documentação.

:::single-choice{#boot-init-systemd-unit-model}
Como o systemd representa recursos gerenciados, como serviços e montagens?

::option[Como entradas de partição primária do MBR.]{#boot-init-systemd-partitions explanation="Metadados de partição não têm relação com units do gerenciador de serviços."}
::option[Como meros links físicos para o executável do PID 1.]{#boot-init-systemd-hard-links explanation="Units são objetos de configuração e execução, não simples aliases de inode."}
::option[Como units com dependências e relações de ativação.]{#boot-init-systemd-units .correct explanation="Os tipos de unit fornecem um modelo comum para ordem, estado e supervisão."}
:::

## Identificação do init em execução

Examine o PID 1 em vez de adivinhar pelos arquivos instalados:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

Permissões, containers e namespaces afetam o que você vê. Um comando dentro de um container informa o PID 1 daquele namespace, não necessariamente o init do host. Depois de identificá-lo, use suas ferramentas nativas de estado e logs.

:::single-choice{#boot-init-detect-running}
Por que examinar o PID 1 é melhor que verificar se existe um diretório de scripts legados?

::option[O PID 1 sempre tem o mesmo nome em todo sistema Linux.]{#boot-init-same-name explanation="Systemd, sysvinit, BusyBox, programas init de containers e outros podem ocupar o PID 1."}
::option[Arquivos de compatibilidade podem existir mesmo quando outro init está em execução.]{#boot-init-compatibility-files .correct explanation="O executável ativo como PID 1 é uma evidência mais forte do sistema init em uso."}
::option[Diretórios legados são apagados automaticamente a cada boot.]{#boot-init-directories-deleted explanation="Arquivos de compatibilidade instalados podem persistir entre reinicializações."}
:::

## Resumo

Agora você consegue explicar init como um papel, não como uma implementação obrigatória.

1. Relacionar o PID 1 à inicialização de serviços, coleta de filhos e desligamento.
2. Reconhecer runlevels do System V como modos definidos pela distribuição.
3. Relacionar recursos e dependências do systemd a units.
4. Examinar o PID 1 ativo no namespace relevante antes de escolher ferramentas.
