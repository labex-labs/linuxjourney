---
lesson_id: "kernel-installation"
course_id: "kernel"
lang: "pt"
order_index: 4
title: "Instalação do Kernel"
description: "Aprenda a instalar, inicializar, verificar e manter um kernel da distribuição com uma alternativa testada."
meta_title: "Instalação do Kernel - Kernel"
meta_description: "Aprenda como instalar e gerenciar kernels Linux. Descubra versões de kernel, use `uname -r` e comandos apt. Comece sua jornada no kernel Linux!"
meta_keywords: "kernel Linux, instalar kernel, uname -r, apt dist-upgrade, gerenciamento de kernel, tutorial Linux, Linux para iniciantes, guia Linux"
---

As distribuições empacotam kernels com módulos, integração do initramfs, atualizações do carregador, assinaturas e política de suporte. Use esse fluxo gerenciado, salvo quando estiver desenvolvendo ou testando deliberadamente um kernel personalizado e souber recuperar a máquina.

## Kernels em execução e instalados

Veja a versão do kernel em execução:

```bash
$ uname -r
6.8.0-00-generic
```

Isso não lista todos os kernels instalados nem muda assim que um pacote novo é instalado. O sistema precisa iniciar a nova imagem antes que `uname -r` a informe. Consulte pacotes e entradas de boot com as ferramentas da distribuição.

:::single-choice{#kernel-installation-uname-release} O que `uname -r` exibe?

::option[A identificação da versão do kernel em execução.]{#kernel-installation-running-release .correct explanation="O comando informa o estado ativo, não apenas a imagem mais nova no disco."}
::option[Todos os pacotes de kernel de todos os repositórios.]{#kernel-installation-all-packages explanation="O inventário dos repositórios pertence ao gerenciador de pacotes."}
::option[A versão do firmware de cada dispositivo conectado.]{#kernel-installation-device-firmware explanation="A versão do kernel e o inventário de firmware são dados distintos."}
:::

## Prefira o pacote de acompanhamento da distribuição

Instale ou mantenha o meta-pacote de kernel compatível para continuar recebendo atualizações de segurança. Os nomes dependem da versão, arquitetura, hardware e variante. O Ubuntu costuma oferecer `linux-generic`, mas sistemas cloud, low-latency, HWE, OEM, real-time e de outras arquiteturas usam pacotes diferentes.

Não transforme diretamente uma string de versão de `uname -r` em um operando de `apt install` presumindo que ela seja válida. Consulte a documentação atual da distribuição e examine os candidatos com o gerenciador de pacotes antes da instalação.

:::single-choice{#kernel-installation-meta-package} Por que um meta-pacote de kernel compatível é útil?

::option[Ele garante que nunca será preciso reiniciar.]{#kernel-installation-no-reboot explanation="Um kernel instalado só fica ativo depois que o sistema inicia por ele, salvo o escopo limitado de live patching."}
::option[Ele converte todo driver externo em código incorporado.]{#kernel-installation-convert-drivers explanation="Módulos externos ainda exigem compilação e assinatura compatíveis."}
::option[Ele acompanha a sequência de atualizações pretendida pela distribuição.]{#kernel-installation-update-tracking .correct explanation="As dependências conduzem o sistema a novos pacotes compatíveis de imagem e módulos."}
:::

## Preparação da alteração

Antes da transação:

1. Confirme repositórios, assinaturas, ciclo de suporte e variante pretendida.
2. Garanta espaço suficiente em `/boot` ou na ESP.
3. Preserve um kernel funcional e uma entrada selecionável.
4. Verifique console, gerenciamento remoto, mídia de resgate, chaves de recuperação e rollback.
5. Confira módulos fora da árvore, drivers de armazenamento e rede, assinatura para Secure Boot, hibernação e compatibilidade com virtualização.

A transação deve gerar um initramfs correspondente e atualizar entradas pelos hooks da distribuição. Leia todo erro; o pacote constar como instalado não basta se a geração falhou.

:::single-choice{#kernel-installation-initramfs-error} Por que um erro de geração do initramfs impede considerar a instalação bem-sucedida?

::option[A geração altera a senha do shell do usuário.]{#kernel-installation-initramfs-password explanation="O arquivo de boot não tem relação com segredos de autenticação."}
::option[O novo kernel pode ficar sem módulos ou ferramentas para alcançar a raiz.]{#kernel-installation-missing-early-tools .correct explanation="A imagem pode estar instalada enquanto seu espaço inicial está ausente ou desatualizado."}
::option[O erro prova que o kernel atual já parou.]{#kernel-installation-current-stopped explanation="Os hooks são executados enquanto o kernel antigo continua ativo."}
:::

## Inicialização e validação

Agende uma reinicialização controlada, considerando as partes interessadas e as cargas de trabalho ativas. Garanta que o console possa escolher a entrada antiga caso a padrão falhe. Depois do boot:

```bash
$ uname -r
$ journalctl -k -b
$ systemctl --failed
```

Use equivalentes em sistemas sem systemd. Valide armazenamento, rede, gráficos, entrada, módulos de segurança, módulos externos, containers, VMs e aplicativos. Um prompt de login não é validação completa.

:::single-choice{#kernel-installation-activation} Quando um pacote comum de kernel recém-instalado passa a ser o kernel em execução?

::option[Assim que `uname -r` é digitado.]{#kernel-installation-uname-activates explanation="Uname é somente leitura e não troca kernels."}
::option[Depois que a máquina inicia por essa imagem.]{#kernel-installation-after-boot .correct explanation="Instalar arquivos não substitui o kernel já executado na memória."}
::option[Quando o pacote é baixado, antes da instalação.]{#kernel-installation-download-activates explanation="Um arquivo baixado não afeta a execução ativa."}
:::

## Remoção de kernels antigos

Use o fluxo de limpeza do gerenciador somente depois de validar o novo kernel. Nunca remova o kernel em execução, a única alternativa funcional nem pacotes exigidos pelo meta-pacote ativo. Revise a remoção e as entradas resultantes.

Apagar manualmente arquivos de `/boot` deixa pacotes e carregador inconsistentes. Se já não houver espaço, prepare a recuperação antes de mudar arquivos.

:::single-choice{#kernel-installation-old-kernel-removal} Qual kernel deve permanecer instalado durante a validação inicial do novo?

::option[Apenas o novo kernel ainda não testado.]{#kernel-installation-only-new explanation="Remover todas as alternativas antes do teste transforma incompatibilidade em incidente de recuperação."}
::option[Nenhum arquivo de kernel no caminho de boot.]{#kernel-installation-no-kernels explanation="A máquina precisa de um artefato carregável para iniciar Linux."}
::option[Uma alternativa funcional selecionável pelo carregador.]{#kernel-installation-known-good-fallback .correct explanation="Ela oferece recuperação caso o novo kernel falhe com o hardware ou as cargas."}
:::

O laboratório [Personalizar o Menu de Inicialização GRUB2 no Linux](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) oferece um ambiente seguro para entender várias entradas.

## Resumo

Agora você consegue tratar uma atualização do kernel como mudança na cadeia de boot e compatibilidade.

1. Distinguir versão em execução de imagens instaladas.
2. Acompanhar atualizações pelo pacote correto da distribuição.
3. Preparar espaço, initramfs, assinaturas, módulos e recuperação.
4. Inicializar e validar hardware e aplicativos.
5. Manter uma alternativa funcional até comprovar o novo kernel.
