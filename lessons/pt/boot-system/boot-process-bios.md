---
lesson_id: "boot-process-bios"
course_id: "boot-system"
lang: "pt"
order_index: 2
title: "Processo de Boot: BIOS"
description: "Aprenda como o BIOS legado e o firmware UEFI moderno localizam e autorizam a próxima etapa do boot."
meta_title: "Processo de Boot: BIOS - Inicializando o Sistema"
meta_description: "Descubra o primeiro passo do processo de boot do Linux: a BIOS. Aprenda como ela encontra o carregador de boot via MBR ou GPT e entenda o papel da UEFI. Este guia explica a inicialização do sistema e aborda como entrar na BIOS para configuração."
meta_keywords: "processo de boot linux, BIOS, MBR, UEFI, bios no linux, bios linux, como entrar na bios, carregador de boot, inicialização do sistema"
---

O firmware é executado antes do kernel Linux. Em hardware da classe PC, as duas principais interfaces são BIOS legado e UEFI. Elas usam modelos diferentes para descobrir o boot; portanto, “o BIOS lê o carregador” descreve apenas um dos caminhos.

## Boot com BIOS legado

Depois da inicialização inicial da plataforma e da escolha do dispositivo, o BIOS legado normalmente lê o primeiro setor de 512 bytes do disco escolhido e transfere o controle ao código ali presente se encontrar a assinatura esperada.

Em um layout MBR, esse setor contém uma pequena região de código, quatro entradas de partição e uma assinatura. O espaço é insuficiente para um carregador completo, por isso o código costuma localizar outra etapa no disco ou em um sistema de arquivos.

É possível iniciar por BIOS em um disco GPT, mas o MBR protetor sozinho não contém as etapas posteriores. O GRUB costuma usar uma pequena BIOS Boot Partition no GPT para seu código central incorporado. A organização exata depende do carregador instalado.

:::single-choice{#boot-bios-legacy-first-sector}
O que o BIOS legado normalmente carrega primeiro do disco de boot escolhido?

::option[O setor inicial de boot que contém um pequeno código.]{#boot-bios-boot-sector .correct explanation="O caminho de disco legado do firmware transfere o controle ao código no primeiro setor do disco escolhido."}
::option[Todo o sistema de arquivos raiz Linux na memória do firmware.]{#boot-bios-entire-root explanation="O setor inicial é minúsculo; softwares posteriores localizam o kernel e o armazenamento raiz."}
::option[Toda configuração de serviços de usuário em `/etc`.]{#boot-bios-etc-config explanation="O firmware não interpreta toda a configuração de serviços do sistema instalado."}
:::

## Boot com UEFI

O firmware UEFI compreende um sistema de arquivos definido em uma Partição de Sistema EFI (ESP) e pode carregar executáveis EFI. Entradas de boot guardadas em variáveis não voláteis normalmente identificam disco, partição e caminho do executável. Um caminho alternativo padronizado pode ser usado em mídias removíveis ou recuperação.

A ESP contém aplicativos de boot e arquivos de apoio, não “todas as informações de inicialização”. Kernel, initramfs e configuração do carregador podem ficar nela ou em outro lugar. GPT é convencional em UEFI, mas a interface do firmware e a tabela de partições continuam sendo camadas distintas.

:::single-choice{#boot-bios-uefi-esp}
O que o UEFI normalmente carrega de uma Partição de Sistema EFI?

::option[Um executável EFI escolhido por uma entrada de boot do firmware.]{#boot-bios-efi-executable .correct explanation="O gerenciamento de boot UEFI aponta o firmware para um arquivo executável em uma partição de sistema compatível."}
::option[Um script de shell POSIX de qualquer diretório pessoal ext4.]{#boot-bios-shell-script explanation="O firmware carrega formatos executáveis definidos em caminhos compatíveis, em vez de executar um shell de usuário."}
::option[Uma partição estendida MBR que contém contas de usuário.]{#boot-bios-extended-users explanation="Dados de contas não participam da descoberta de executáveis UEFI."}
:::

## Secure Boot e confiança

Com o Secure Boot ativado, o UEFI verifica as assinaturas da cadeia de boot conforme as chaves e a política cadastradas. Uma distribuição Linux pode usar shim, carregador e kernel assinados, além de uma política para módulos, para estender essa cadeia.

Secure Boot não criptografa o disco nem prova que todo programa é seguro. Ele ajuda a impedir que código de pré-boot não autorizado seja aceito pela política de confiança configurada.

:::single-choice{#boot-bios-secure-boot-purpose}
O que o UEFI Secure Boot impõe principalmente?

::option[Criptografia automática de todos os arquivos em todos os discos.]{#boot-bios-secure-encryption explanation="A confidencialidade dos discos exige um sistema de criptografia separado."}
::option[Autorização por assinatura dos executáveis da cadeia de boot.]{#boot-bios-secure-signatures .correct explanation="O firmware e os componentes verificados posteriores aceitam código conforme as chaves e a política cadastradas."}
::option[Ausência garantida de vulnerabilidades em software assinado.]{#boot-bios-secure-no-vulnerabilities explanation="Uma assinatura válida prova autorização e integridade, não que o código seja perfeito."}
:::

## Entrada na configuração do firmware

As teclas variam por fabricante e modelo, incluindo Delete, Escape ou teclas de função durante o início. Consulte a documentação do dispositivo. Alguns sistemas UEFI também permitem que o sistema operacional solicite uma reinicialização para a configuração.

Registre os valores existentes e as chaves de recuperação antes de mudar Secure Boot, modo do controlador de armazenamento, TPM, virtualização ou ordem de boot. Uma alteração pode tornar volumes criptografados ou o sistema temporariamente inacessíveis.

:::single-choice{#boot-bios-setup-key}
Por que não existe uma tecla universal para entrar na configuração do firmware?

::option[O Linux escolhe uma tecla aleatória após cada boot.]{#boot-bios-random-key explanation="O sistema operacional não define aleatoriamente a tecla inicial do firmware."}
::option[A tecla e o momento são definidos pelo fabricante do sistema.]{#boot-bios-vendor-key .correct explanation="As interfaces variam entre modelos, por isso é preciso consultar a documentação oficial do dispositivo."}
::option[Só é possível entrar na configuração apagando o carregador.]{#boot-bios-delete-loader explanation="A configuração do firmware independe da destruição dos arquivos de boot instalados."}
:::

## Resumo

Agora você consegue distinguir os modelos de descoberta de boot do BIOS legado e do UEFI.

1. Relacionar o BIOS legado ao primeiro setor e às etapas posteriores do carregador.
2. Relacionar entradas UEFI a executáveis EFI em uma ESP.
3. Tratar GPT, interface do firmware e layout do carregador como escolhas distintas.
4. Alterar configurações de confiança e armazenamento apenas com um caminho de recuperação.
