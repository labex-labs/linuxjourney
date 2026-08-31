---
lesson_id: "boot-process-bootloader"
course_id: "boot-system"
lang: "pt"
order_index: 3
title: "Processo de Boot: Carregador de Boot"
description: "Aprenda como um carregador de boot seleciona artefatos Linux, constrói a linha de comando do kernel e transfere o controle."
meta_title: "Processo de Boot: Carregador de Boot - Inicialize o Sistema"
meta_description: "Um guia sobre o carregador de boot (bootloader) no Linux. Aprenda o que é um carregador de boot Linux, suas funções principais e como o GRUB usa parâmetros de kernel como initrd e root para iniciar o sistema."
meta_keywords: "carregador de boot linux, bootloader no linux, bootloader linux, grub, o que é bootloader no linux, parâmetros de kernel, initrd, sistema de arquivos root, processo de boot linux"
---

Um carregador de boot faz a ponte entre a descoberta realizada pelo firmware e a execução do kernel. O GRUB é comum em PCs Linux, mas systemd-boot, U-Boot, o carregamento de um kernel EFI-stub pelo firmware e outros projetos implementam partes diferentes desse papel.

## Seleção dos artefatos de boot

Uma entrada do carregador pode identificar:

- uma imagem do kernel Linux
- uma imagem initramfs opcional ou um initrd legado
- uma linha de comando do kernel
- metadados específicos da plataforma ou o carregador de outro sistema operacional

O GRUB pode apresentar vários kernels e entradas de recuperação. Um kernel alternativo só é útil quando seus módulos e initramfs correspondentes continuam disponíveis e testados. O carregador lê arquivos por seus próprios módulos de armazenamento e sistema de arquivos; ele não depende do VFS do Linux, que ainda não está em execução.

:::single-choice{#bootloader-primary-handoff}
Para onde um carregador de boot Linux normalmente transfere o controle?

::option[Para um shell interativo com todos os serviços já em execução.]{#bootloader-user-shell explanation="Shells do espaço do usuário só aparecem depois que o kernel e o sistema init são iniciados."}
::option[Para a imagem de kernel escolhida, após carregar os artefatos necessários.]{#bootloader-selected-kernel .correct explanation="O carregador prepara o kernel, seus parâmetros e, em geral, um initramfs antes de executar o ponto de entrada do kernel."}
::option[Para o gerenciador de pacotes, que resolve dependências.]{#bootloader-package-manager explanation="O gerenciamento de pacotes não é a próxima etapa de transferência do controle do processador durante o boot."}
:::

## Parâmetros da linha de comando do kernel

O carregador passa uma linha de texto que o kernel e o espaço inicial do usuário interpretam. Exemplos comuns:

- `root=...` identifica o sistema de arquivos raiz pretendido ou uma especificação para o espaço inicial
- `ro` ou `rw` solicita o modo inicial de montagem da raiz
- `quiet` reduz as mensagens do kernel no console
- `init=...` solicita outro primeiro programa de espaço do usuário para recuperação especializada
- parâmetros `rd.*` específicos da distribuição são interpretados pelas ferramentas do initramfs

`initrd` normalmente é uma diretiva do carregador que nomeia uma imagem, não um parâmetro genérico do kernel. `BOOT_IMAGE=` pode aparecer em linhas produzidas por algumas configurações do GRUB, mas não é o mecanismo que carrega o kernel.

Veja a linha usada no boot atual com:

```bash
$ cat /proc/cmdline
```

:::single-choice{#bootloader-root-parameter}
Qual é a finalidade do parâmetro `root=` na linha de comando do kernel?

::option[Identificar o sistema de arquivos raiz que o boot deve usar.]{#bootloader-root-filesystem .correct explanation="O kernel ou o initramfs interpreta esse valor para localizar e montar a raiz real."}
::option[Definir a senha de login da conta root.]{#bootloader-root-password explanation="Segredos de autenticação não devem ser passados como texto comum na linha de comando do kernel."}
::option[Renomear o PID 1 para a palavra `root`.]{#bootloader-root-pid explanation="O nome de processos não tem relação com esse parâmetro de armazenamento."}
:::

:::single-choice{#bootloader-quiet-parameter}
O que o parâmetro `quiet` normalmente solicita?

::option[Acesso somente leitura a todo sistema de arquivos montado.]{#bootloader-quiet-readonly explanation="A política inicial de escrita da raiz usa parâmetros como `ro`, não `quiet`."}
::option[Redução das mensagens do kernel exibidas durante o boot.]{#bootloader-quiet-console .correct explanation="Ele suprime muitas mensagens informativas, mas não garante silêncio de todos os componentes."}
::option[Desativação de todas as ventoinhas de refrigeração.]{#bootloader-quiet-fans explanation="O parâmetro controla a quantidade de mensagens, não o ruído do hardware."}
:::

## Edição temporária e recuperação

O GRUB normalmente permite que um usuário autorizado no console edite uma entrada por um único boot, usando uma tecla indicada no menu. Isso é útil para remover `quiet`, escolher parâmetros de recuperação ou corrigir um identificador de raiz. A interface e a autorização variam, sobretudo com Secure Boot e GRUB protegido por senha.

Parâmetros podem expor texto sensível em `/proc/cmdline`, logs de boot e relatórios de falha. Também podem enfraquecer a segurança ou impedir o boot. Nunca coloque segredos ali; preserve uma entrada funcional e um caminho de recuperação pelo console.

:::single-choice{#bootloader-temporary-edit}
Qual é uma característica comum da edição interativa de uma entrada do GRUB para um boot?

::option[Ela reescreve automaticamente todas as imagens de kernel instaladas.]{#bootloader-rewrites-kernels explanation="Alterar o texto do comando não modifica os binários do kernel."}
::option[Ela desativa permanentemente a verificação do firmware em todos os discos.]{#bootloader-disables-firmware explanation="A política do firmware é separada e não é alterada universalmente por uma edição de entrada."}
::option[A mudança vale para esse boot, a menos que seja salva separadamente na configuração.]{#bootloader-one-boot-change .correct explanation="A edição do menu normalmente altera a entrada em memória, não os arquivos persistentes de origem."}
:::

## Configuração persistente do GRUB

As distribuições costumam gerar a configuração final do GRUB a partir de modelos, padrões, scripts e kernels encontrados. Não edite diretamente o `grub.cfg` gerado, salvo quando a distribuição documentar esse fluxo; uma nova geração pode sobrescrevê-lo.

Faça uma alteração limitada na fonte, execute o comando de geração documentado pela distribuição, confira a saída e teste mantendo uma entrada antiga funcional e uma mídia de recuperação. Comando e caminho de saída variam entre Debian, Fedora, instalações UEFI e BIOS.

:::single-choice{#bootloader-generated-config}
Por que editar diretamente um `grub.cfg` gerado costuma ser pouco confiável?

::option[O arquivo nunca pode conter texto legível.]{#bootloader-config-binary explanation="A configuração do GRUB é texto, mas ainda pertence a um processo de geração."}
::option[O GRUB lê apenas arquivos no diretório pessoal de cada usuário.]{#bootloader-grub-home explanation="A configuração de boot é do sistema e precisa estar disponível antes das sessões de usuário."}
::option[Uma geração posterior pode sobrescrever a alteração manual.]{#bootloader-regeneration-overwrites .correct explanation="Configurações persistentes geralmente pertencem às fontes e ao fluxo de geração da distribuição."}
:::

Use [Personalizar o Menu de Inicialização GRUB2 no Linux](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) somente no ambiente de laboratório com recursos de recuperação.

## Resumo

Agora você consegue separar diretivas do carregador de parâmetros da linha de comando do kernel.

1. Identificar kernel, initramfs, linha de comando e entradas alternativas.
2. Usar `root=`, `ro` e `quiet` conforme seus papéis reais.
3. Inspecionar os parâmetros do boot atual em `/proc/cmdline`.
4. Tratar edições interativas como temporárias e sensíveis à segurança.
5. Alterar configurações geradas pelo fluxo documentado da distribuição.
