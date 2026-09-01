---
lesson_id: "boot-process-kernel"
course_id: "boot-system"
lang: "pt"
order_index: 4
title: "Processo de Inicialização: Kernel"
description: "Aprenda como o kernel Linux usa o espaço inicial do usuário para alcançar a raiz real e iniciar o PID 1."
meta_title: "Processo de Inicialização: Kernel - Inicializando o Sistema"
meta_description: "Explore o processo de inicialização do kernel Linux. Aprenda como o initramfs carrega drivers de um sistema de arquivos temporário para montar a partição raiz final. Entenda as etapas desde o carregamento do kernel até a execução do init."
meta_keywords: "raiz de inicialização, initramfs, inicialização do kernel, partição de boot, initramfs ubuntu, /etc/default/grub, processo de boot Linux, sistema de arquivos raiz, inicialização do kernel"
---

Depois que o controle chega ao kernel Linux, ele inicializa gerenciamento de memória, escalonamento, interrupções, drivers incorporados, estruturas de segurança e outros subsistemas centrais. Em seguida, interpreta a linha de comando e se prepara para iniciar o primeiro processo do espaço do usuário.

## Por que existe o espaço inicial do usuário

Às vezes, um sistema de arquivos raiz simples pode ser montado com drivers incorporados ao kernel. Sistemas mais complexos precisam de módulos e ferramentas antes que a raiz real possa ser alcançada. Exemplos:

- módulos do controlador de armazenamento ou sistema de arquivos
- desbloqueio de uma raiz criptografada
- montagem de LVM ou RAID
- configuração de rede para uma raiz remota
- descoberta de dispositivos e resolução de identificadores persistentes

Um initramfs reúne esses componentes em um ambiente inicial do espaço do usuário fornecido junto com o kernel.

:::single-choice{#boot-kernel-initramfs-purpose} Que problema um initramfs costuma resolver?

::option[Ele fornece ferramentas e módulos iniciais necessários antes que a raiz real esteja disponível.]{#boot-kernel-early-tools .correct explanation="O espaço inicial pode descobrir e montar armazenamento que o kernel não acessa apenas com o suporte incorporado."}
::option[Ele guarda permanentemente no firmware o diretório pessoal de cada usuário.]{#boot-kernel-home-firmware explanation="Esse arquivo é um artefato de boot, não armazenamento permanente de dados do usuário."}
::option[Ele substitui o kernel Linux depois do primeiro login.]{#boot-kernel-replace-kernel explanation="O kernel continua ativo enquanto o código do initramfs é executado no espaço do usuário."}
:::

## Initramfs e initrd legado

Um initramfs moderno normalmente consiste em um ou mais arquivos cpio, muitas vezes comprimidos, que o kernel descompacta em seu sistema de arquivos raiz inicial. O kernel executa o programa `/init` desse ambiente.

Um initrd legado é, conceitualmente, uma imagem de sistema de arquivos carregada em um dispositivo de bloco baseado em RAM e montada. Os termos são usados de modo impreciso em nomes de arquivo e comandos; examine as ferramentas reais em vez de deduzir o formato apenas pelo nome.

O initramfs deve corresponder ao kernel e ao projeto de boot. Módulos ausentes, identificadores antigos ou ferramentas de criptografia e LVM omitidas podem tornar um kernel novo incapaz de iniciar, mesmo que sua imagem seja válida.

:::single-choice{#boot-kernel-initramfs-format} Como um initramfs moderno costuma ser apresentado ao kernel?

::option[Como um repositório interativo de pacotes apenas por HTTP.]{#boot-kernel-http-repository explanation="A rede pode ser configurada no espaço inicial, mas não define o formato do initramfs."}
::option[Como um arquivo baseado em cpio, descompactado na raiz inicial.]{#boot-kernel-cpio-archive .correct explanation="O kernel expande o arquivo e executa seu programa de inicialização do espaço inicial do usuário."}
::option[Como o cabeçalho GPT de backup do disco.]{#boot-kernel-gpt-header explanation="A redundância da tabela de partições independe do arquivo do espaço inicial."}
:::

## Chegada à raiz real

O espaço inicial interpreta parâmetros como `root=`, espera pelos dispositivos, ativa camadas de armazenamento e monta a raiz pretendida. Depois, usa uma operação de troca de raiz para tornar esse sistema de arquivos o novo `/` e liberar o ambiente temporário quando possível.

A solicitação inicial `ro` pode permitir verificações de consistência e uma inicialização controlada, mas a sequência exata depende da distribuição. Verificações de sistema de arquivos são operações do espaço do usuário, e o initramfs ou o sistema init posterior pode remontar a raiz para leitura e escrita quando permitido.

:::single-choice{#boot-kernel-root-switch} O que acontece depois que o espaço inicial monta com êxito a raiz real pretendida?

::option[A tabela de partições é recriada em todos os discos.]{#boot-kernel-recreate-tables explanation="A troca de raiz não reparticiona o armazenamento."}
::option[O kernel termina e o firmware volta a escalonar processos.]{#boot-kernel-firmware-schedules explanation="O kernel Linux continua responsável por processos e hardware depois da transferência."}
::option[O boot troca a visão da raiz para esse sistema de arquivos e continua a inicialização.]{#boot-kernel-switch-root .correct explanation="A raiz inicial temporária transfere o controle à hierarquia raiz do sistema instalado."}
:::

## Inicialização do PID 1

O kernel executa o programa init configurado, normalmente acessado por um caminho como `/sbin/init` ou escolhido com `init=`. Esse processo recebe o PID 1 e assume a responsabilidade pelo principal ambiente de serviços do espaço do usuário.

Se nenhum programa init utilizável puder ser executado, o kernel não consegue chegar a um sistema normal e costuma relatar falha ou panic. Investigue a primeira camada que falhou: kernel e linha de comando, conteúdo do initramfs, descoberta e montagem da raiz ou execução do PID 1.

:::single-choice{#boot-kernel-pid-one} Qual é a última grande transferência do kernel nessa etapa simplificada?

::option[Executar o primeiro programa do espaço do usuário como PID 1.]{#boot-kernel-exec-init .correct explanation="Depois disso, o PID 1 inicia os serviços e o estado configurado do sistema."}
::option[Transformar `/proc` em um banco persistente de pacotes.]{#boot-kernel-proc-package explanation="Procfs continua sendo uma interface de tempo de execução do kernel."}
::option[Atribuir o mesmo PID a todos os processos posteriores.]{#boot-kernel-same-pid explanation="Cada processo ativo recebe seu próprio PID dentro de um namespace."}
:::

## Resumo

Agora você consegue acompanhar o boot do kernel pelo espaço inicial até o PID 1.

1. Separar a inicialização incorporada ao kernel dos módulos iniciais carregáveis.
2. Relacionar initramfs a uma raiz temporária baseada em cpio e a `/init`.
3. Acompanhar a montagem do armazenamento e a troca para a raiz real.
4. Identificar a execução do PID 1 como transferência ao espaço do usuário.
