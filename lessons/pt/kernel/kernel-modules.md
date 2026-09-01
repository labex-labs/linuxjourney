---
lesson_id: "kernel-modules"
course_id: "kernel"
lang: "pt"
order_index: 6
title: "Módulos do Kernel"
description: "Aprenda a inspecionar, carregar, configurar e remover com segurança módulos específicos da versão do kernel Linux."
meta_title: "Módulos do Kernel - Kernel"
meta_description: "Descubra o que são módulos de kernel no Linux e como eles estendem a funcionalidade do kernel. Esta lição aborda o uso de lsmod e modprobe para listar, carregar e descarregar módulos sob demanda."
meta_keywords: "o que são módulos de kernel, módulos de kernel Linux, modprobe, lsmod, gerenciamento de kernel, tutorial Linux, Linux para iniciantes, guia Linux"
---

Um módulo carregável é código privilegiado que amplia o kernel em execução com um driver, sistema de arquivos, recurso de rede ou outro subsistema. Os módulos evitam incorporar todo recurso opcional à imagem principal, mas cada módulo carregado aumenta a superfície confiável de ataque.

## Listagem e inspeção de módulos

Liste os módulos carregados:

```bash
$ lsmod
```

A saída deriva do estado do kernel, como `/proc/modules`, e inclui nome, tamanho e contagem de uso ou dependências. Uma contagem aparentemente zero não prova que a remoção é segura; um driver ainda pode controlar dispositivos ativos ou participar do estado de um subsistema.

Inspecione um módulo disponível para o kernel atual com:

```bash
$ modinfo MODULE_NAME
```

`modinfo` pode mostrar arquivo, aliases, parâmetros, licença, descrição e assinatura. Esses metadados são descritivos, não prova de confiança ou compatibilidade com a carga de trabalho.

:::single-choice{#kernel-modules-lsmod-purpose} O que `lsmod` exibe?

::option[Todos os pacotes de módulos disponíveis em repositórios remotos.]{#kernel-modules-repository-list explanation="O inventário dos repositórios exige consultas ao gerenciador de pacotes."}
::option[Apenas drivers incorporados diretamente à imagem do kernel.]{#kernel-modules-builtins explanation="Recursos incorporados não são módulos carregáveis e normalmente não aparecem em lsmod."}
::option[Módulos atualmente carregados no kernel em execução.]{#kernel-modules-loaded-list .correct explanation="A listagem reflete o estado ativo e informações de uso ou dependência."}
:::

## Carregamento com `modprobe`

Carregue um módulo pelo nome:

```bash
$ sudo modprobe MODULE_NAME
```

`modprobe` consulta índices de dependências, aliases e configurações do kernel atual em `/lib/modules/$(uname -r)/`. Ele carrega dependências e passa parâmetros configurados. Já `insmod` insere diretamente um arquivo específico e não oferece o mesmo fluxo de resolução.

Antes de carregar, confirme procedência, política de assinatura, compatibilidade da versão, parâmetros, vínculo esperado com hardware e rollback. Secure Boot ou lockdown podem rejeitar módulos não assinados; forçar código incompatível arrisca travamento ou comprometimento.

:::single-choice{#kernel-modules-modprobe-dependencies} Por que normalmente se prefere `modprobe` a `insmod` direto?

::option[Ele executa o módulo inteiramente no espaço do usuário.]{#kernel-modules-modprobe-userspace explanation="O módulo inserido é executado como código privilegiado do kernel."}
::option[Ele garante que todo módulo de terceiros é assinado e seguro.]{#kernel-modules-modprobe-guarantee explanation="A imposição depende da política, e assinatura válida não prova ausência de falhas."}
::option[Ele resolve aliases, dependências e configurações do módulo.]{#kernel-modules-modprobe-resolves .correct explanation="Modprobe usa a árvore indexada da versão exata em execução."}
:::

## Parâmetros e carregamento no boot

Parâmetros e aliases persistentes ficam em um arquivo `.conf` de `/etc/modprobe.d/`:

```text
options example_module mode=careful
```

Essa linha afeta como o módulo é carregado; sozinha, não solicita carregamento no boot. Uma lista simples para o boot costuma ficar em `/etc/modules-load.d/`:

```text
example_module
```

Aliases de hardware muitas vezes acionam carregamento automático sem lista explícita. Para módulos necessários no início do boot, atualize o initramfs pelo processo documentado da distribuição.

:::single-choice{#kernel-modules-options-versus-load} O que faz uma linha `options` em `/etc/modprobe.d/`?

::option[Garante sozinha que o módulo será carregado em todo boot.]{#kernel-modules-options-autoload explanation="Pedidos de carregamento usam outro mecanismo, como modules-load ou aliases de dispositivos."}
::option[Define parâmetros usados quando o módulo nomeado é carregado.]{#kernel-modules-options-parameters .correct explanation="Modprobe aplica os argumentos de chave e valor configurados durante a inserção."}
::option[Compila o módulo para toda versão instalada do kernel.]{#kernel-modules-options-compiles explanation="A configuração não compila módulos binários."}
:::

## Blacklist e suas limitações

Uma configuração pode conter:

```text
blacklist example_module
```

Isso normalmente suprime o carregamento automático pelos aliases. Não descarrega um módulo ativo, não o remove do initramfs nem necessariamente impede uma carga explícita pelo nome ou como dependência. Hardening exige uma combinação específica de disponibilidade, assinaturas, initramfs, parâmetros de boot e política.

:::single-choice{#kernel-modules-blacklist-effect} O que uma linha básica `blacklist` do modprobe suprime principalmente?

::option[O carregamento automático pelos aliases do módulo.]{#kernel-modules-blacklist-aliases .correct explanation="A diretiva não é uma proibição universal de todas as rotas pelas quais o código pode ser carregado."}
::option[A execução de todo programa de usuário com nome parecido.]{#kernel-modules-blacklist-user-programs explanation="A configuração do modprobe se aplica à resolução de módulos do kernel."}
::option[Todo código incorporado à imagem do kernel.]{#kernel-modules-blacklist-builtins explanation="Funcionalidade incorporada não pode ser bloqueada ou descarregada como módulo."}
:::

## Remoção segura de um módulo

Solicite a remoção com:

```bash
$ sudo modprobe -r MODULE_NAME
```

Modprobe pode remover dependências que ficaram sem uso. O kernel recusa quando o rastreamento comum mostra que o módulo está ocupado, mas isso não deve ser a única verificação. Pare serviços, desmonte sistemas de arquivos, desconecte dispositivos, estabilize a rede e confirme outro driver ou caminho de recuperação.

Nunca force a remoção em um sistema que precisa preservar. Falhas ou atividades pendentes podem travar o kernel ou corromper dados.

:::single-choice{#kernel-modules-remove-command} Qual comando solicita a remoção de um módulo pelo nome considerando dependências?

::option[`lsmod -r MODULE_NAME`]{#kernel-modules-lsmod-remove explanation="Lsmod apenas lista e não remove módulos."}
::option[`uname -r MODULE_NAME`]{#kernel-modules-uname-remove explanation="Uname informa dados do kernel e não gerencia módulos."}
::option[`modprobe -r MODULE_NAME`]{#kernel-modules-modprobe-remove .correct explanation="O modo de remoção considera as dependências indexadas em torno do módulo solicitado."}
:::

Use [Gerenciar Módulos do Kernel no Linux](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865) para praticar com módulos definidos como seguros pelo laboratório.

## Resumo

Agora você consegue gerenciar módulos respeitando seu risco no nível do kernel.

1. Usar `lsmod` para estado ativo e `modinfo` para metadados.
2. Usar `modprobe` para carregamento com aliases e dependências.
3. Separar parâmetros do modprobe de pedidos de carga no boot.
4. Tratar blacklist como política limitada, não bloqueio absoluto.
5. Interromper todos os consumidores antes de `modprobe -r`.
