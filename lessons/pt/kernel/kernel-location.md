---
lesson_id: "kernel-location"
course_id: "kernel"
lang: "pt"
order_index: 5
title: "Localização do Kernel"
description: "Aprenda onde as distribuições armazenam imagens do kernel, initramfs, configurações, símbolos e módulos versionados."
meta_title: "Localização do Kernel - Kernel"
meta_description: "Descubra onde o kernel é armazenado no Linux. Este guia explica a localização do kernel Linux no diretório /boot, detalhando arquivos chave como vmlinuz e initrd."
meta_keywords: "localização kernel linux, onde está o kernel, localização kernel, onde o kernel está localizado, onde o kernel é armazenado no linux, vmlinuz, diretório /boot"
---

As distribuições normalmente guardam artefatos inicializáveis em `/boot`, mas layouts UEFI e Boot Loader Specification também podem colocá-los em uma Partição de Sistema EFI ou partição de boot estendida montada em `/boot`, `/boot/efi` ou `/efi`. Examine montagens e a configuração do carregador, sem presumir um caminho universal.

## Arquivos versionados em `/boot`

Um layout tradicional pode conter:

- `vmlinuz-KERNEL_RELEASE`: imagem inicializável do kernel Linux
- `initrd.img-KERNEL_RELEASE` ou `initramfs-KERNEL_RELEASE.img`: imagem do espaço inicial do usuário
- `config-KERNEL_RELEASE`: configuração usada na compilação do kernel empacotado
- `System.map-KERNEL_RELEASE`: mapa de endereços de símbolos da compilação

Os nomes variam. Um arquivo chamado `initrd` em uma distribuição moderna costuma conter um initramfs. O nome `vmlinuz` não informa a compactação interna exata nem o formato de boot; use as ferramentas da distribuição para inspecioná-lo.

:::single-choice{#kernel-location-vmlinuz} O que um arquivo versionado `vmlinuz-*` normalmente contém?

::option[Uma imagem inicializável do kernel Linux.]{#kernel-location-kernel-image .correct explanation="O carregador ou firmware carrega esse artefato de kernel específico da arquitetura."}
::option[Todos os módulos de todos os kernels instalados.]{#kernel-location-all-modules explanation="Os módulos ficam separados em uma árvore específica da versão."}
::option[O histórico do shell do usuário no boot anterior.]{#kernel-location-shell-history explanation="Imagens de kernel não contêm histórico pessoal de comandos."}
:::

## Sistema de arquivos RAM inicial e metadados

O initramfs deve conter módulos e ferramentas iniciais exigidos pelo kernel correspondente e pelo projeto de armazenamento raiz. Um nome compatível não basta: uma geração antiga ou mal-sucedida ainda pode produzir uma entrada inutilizável.

`config-*` mostra recursos incorporados, modulares ou omitidos. `System.map-*` pode ajudar na simbolização e depuração, embora randomização, informações de debug separadas e ferramentas da distribuição influenciem seu uso. São artefatos de apoio, não kernels alternativos.

:::single-choice{#kernel-location-initramfs-match} Por que um initramfs está ligado a uma versão do kernel e a uma configuração do sistema?

::option[Ele armazena permanentemente todo sistema de arquivos montado.]{#kernel-location-all-filesystems explanation="Um initramfs é um pequeno ambiente inicial, não um backup completo."}
::option[Ele atribui novos UIDs aos usuários a cada boot.]{#kernel-location-user-ids explanation="O gerenciamento de identidades não faz parte de seu papel normal."}
::option[Ele contém módulos e ferramentas iniciais necessários ao caminho de boot.]{#kernel-location-early-modules .correct explanation="A ABI dos módulos e os componentes de armazenamento precisam corresponder ao kernel escolhido."}
:::

## Módulos versionados do kernel

Módulos carregáveis da versão em execução normalmente ficam em:

```bash
$ printf '/lib/modules/%s\n' "$(uname -r)"
```

Em layouts unificados, isso pode apontar para `/usr/lib/modules/KERNEL_RELEASE`. Cada kernel precisa de uma árvore compatível e índices de dependência. `modprobe` usa metadados específicos da versão, não procura arquivos `.ko` arbitrários pelo disco.

:::single-choice{#kernel-location-module-tree} Qual diretório normalmente guarda módulos do kernel em execução?

::option[`/home/modules/current/`]{#kernel-location-home-modules explanation="Diretórios pessoais não são a árvore padrão de módulos do sistema."}
::option[`/lib/modules/$(uname -r)/`]{#kernel-location-lib-modules .correct explanation="A versão separa a ABI e as dependências dos módulos de cada kernel instalado."}
::option[`/proc/modules/files/`]{#kernel-location-proc-files explanation="`/proc/modules` informa módulos carregados; não é um diretório de binários."}
:::

## Imagens unificadas e caminhos do firmware

Uma Unified Kernel Image (UKI) é um único executável EFI assinado que pode reunir kernel, initrd, linha de comando e metadados. UKIs ficam em um local acessível ao EFI, em vez de arquivos separados `vmlinuz` e initramfs.

Assim, um `/boot` tradicional aparentemente vazio não prova que nenhum kernel está instalado. Use `findmnt`, o banco de pacotes, ferramentas do gerenciador de boot e sua configuração para mapear os artefatos ativos.

:::single-choice{#kernel-location-uki} O que uma Unified Kernel Image pode combinar?

::option[Todos os diretórios pessoais em um cabeçalho GPT.]{#kernel-location-uki-homes explanation="Uma UKI é um executável de boot, não contêiner de dados nem tabela de partições."}
::option[Todos os pacotes instalados em um script de shell.]{#kernel-location-uki-packages explanation="Ela reúne componentes de boot, não todo o repositório do sistema."}
::option[Kernel, initrd, linha de comando e metadados em um executável EFI.]{#kernel-location-uki-components .correct explanation="O artefato combinado pode participar de um fluxo UEFI assinado."}
:::

## Gerenciamento seguro do espaço

Se o sistema de arquivos de boot estiver cheio, mapeie os caminhos montados e identifique o pacote proprietário de cada artefato. Use o fluxo de limpeza de kernels do gerenciador, preserve o kernel em execução e uma alternativa funcional, regenere ou confira as entradas e verifique o espaço.

Não apague manualmente `vmlinuz`, initramfs, UKI ou árvores de módulos apenas pela idade. Um arquivo pode ser a única entrada de recuperação inicializável.

## Resumo

Agora você consegue mapear um pacote de kernel a seus artefatos de boot e módulos.

1. Inspecionar montagens reais de `/boot` e EFI.
2. Distinguir imagem, initramfs, configuração e mapa de símbolos.
3. Vincular árvores de módulos à versão exata do kernel.
4. Considerar UKIs e layouts específicos da distribuição.
5. Liberar espaço apenas com plano verificado de pacotes e fallback.
