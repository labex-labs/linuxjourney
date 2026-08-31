---
lesson_id: "swap-space"
course_id: "filesystem"
lang: "pt"
order_index: 8
title: "swap"
description: "Aprenda como o Linux usa, inicializa, ativa, dimensiona e desativa com segurança o espaço de swap."
meta_title: "swap - O Sistema de Arquivos"
meta_description: "Aprenda sobre o espaço de swap do Linux, como ele funciona e como criar e gerenciar partições de swap. Otimize o uso da memória do sistema com este guia."
meta_keywords: "swap Linux, mkswap, swapon, swapoff, /etc/fstab, memória virtual, Linux para iniciantes, tutorial Linux"
---

O Linux pode mover páginas selecionadas de memória anônima entre a RAM e um armazenamento apoiado por swap. Isso permite manter memória inativa enquanto libera RAM para cargas de trabalho ativas e para o cache do sistema de arquivos, mas o armazenamento é muito mais lento que a RAM. O swap é uma ferramenta de capacidade e gerenciamento de memória, não um substituto para uma quantidade suficiente de memória nem um limite para a memória das aplicações.

## Participação do Swap no Gerenciamento de Memória

O kernel pode usar o swap antes que a RAM se esgote completamente, dependendo da carga de trabalho, da pressão de memória, dos cgroups e de parâmetros ajustáveis como swappiness. Páginas limpas apoiadas por arquivos muitas vezes podem ser descartadas e relidas de seus arquivos, enquanto páginas anônimas precisam do swap ou devem permanecer na RAM.

Uma atividade intensa e contínua de swap pode causar grande latência ou thrashing. Diagnostique a demanda de memória, os conjuntos de trabalho, a pressão e os limites das aplicações, em vez de tratar uma área de swap maior como uma solução universal de desempenho.

:::single-choice{#swap-space-anonymous-pages}
Qual memória é uma candidata principal ao armazenamento em swap?

::option[Todos os arquivos executáveis instalados em `/usr`.]{#swap-space-installed-files explanation="Os arquivos instalados permanecem em seus sistemas de arquivos; as páginas limpas mapeadas podem ser relidas dali."}
::option[Páginas inativas de memória anônima.]{#swap-space-anonymous-memory .correct explanation="As páginas anônimas não possuem um arquivo de apoio comum do qual possam simplesmente ser relidas."}
::option[As entradas da tabela de partições do disco.]{#swap-space-partition-table explanation="Os metadados das partições permanecem no dispositivo de bloco e não são memória de processos movida da RAM."}
:::

## Inspeção do Swap Ativo

Use primeiro comandos somente para leitura:

```bash
$ swapon --show
$ cat /proc/swaps
$ free -h
```

Eles mostram o swap ativo configurado e os valores agregados de memória. Um valor “used” diferente de zero não representa automaticamente um problema; relacione-o às taxas de entrada e saída do swap, à pressão de memória, à latência e ao comportamento da carga de trabalho.

:::single-choice{#swap-space-show-active}
Qual comando lista as áreas de swap ativas em uma visualização estruturada?

::option[`swapon --show`]{#swap-space-swapon-show .correct explanation="O modo show informa os arquivos ou dispositivos de swap ativos e, quando disponíveis, seu tamanho, uso e prioridade."}
::option[`mkswap --all`]{#swap-space-mkswap-all explanation="Mkswap inicializa assinaturas de swap e não é o comando somente para leitura que lista as áreas ativas."}
::option[`mkfs -t swap`]{#swap-space-mkfs-swap explanation="A ferramenta padrão de inicialização é `mkswap`, e a formatação não é uma consulta de estado."}
:::

## Inicialização e Ativação de um Dispositivo de Swap

`mkswap` grava uma assinatura de swap e destrói os metadados utilizáveis anteriores do destino. Pratique somente em um destino descartável verificado:

```bash
$ sudo mkswap /dev/VERIFIED-SWAP-TARGET
$ sudo swapon /dev/VERIFIED-SWAP-TARGET
```

Antes de executar `mkswap`, verifique modelo, número de série, tamanho, identidade persistente, assinaturas existentes, montagens, RAID, LVM, criptografia e backups, assim como faria antes de `mkfs`. Após a ativação, confirme a origem exata com `swapon --show`.

Para persistência, use o UUID do swap em `/etc/fstab` com o tipo e as opções adequados à política local:

```text
UUID=VERIFIED-SWAP-UUID none swap sw 0 0
```

:::single-choice{#swap-space-enable-command}
Qual comando ativa uma área de swap inicializada?

::option[`swapon`]{#swap-space-command-swapon .correct explanation="Swapon adiciona um dispositivo ou arquivo de swap válido ao conjunto de swap ativo do kernel."}
::option[`mkswap`]{#swap-space-command-mkswap explanation="Mkswap inicializa a assinatura, mas não ativa a área por si só."}
::option[`mount`]{#swap-space-command-mount explanation="O swap é ativado pelo subsistema de swap, não montado como um sistema de arquivos em um diretório."}
:::

## Arquivos de Swap e Outros Backends

Um arquivo de swap pode fornecer capacidade flexível sem reparticionar, mas os requisitos de criação dependem do sistema de arquivos. O arquivo deve ter permissões restritivas, uma alocação apropriada sem lacunas nem comportamentos copy-on-write incompatíveis, uma assinatura de swap e ativação. Siga a documentação do sistema de arquivos e da distribuição, em vez de copiar em todos os ambientes uma receita genérica com `fallocate`.

Dispositivos de RAM comprimida, como zram, podem fornecer outra camada de swap, com diferentes compensações entre CPU e capacidade. O swap criptografado pode proteger as páginas armazenadas, enquanto a hibernação exige uma configuração de retomada e armazenamento adequado suficiente. Esses objetivos afetam o dimensionamento e o projeto.

Não existe uma regra universal de que o swap deve ter o dobro da RAM. Dimensione-o a partir dos picos da carga de trabalho, do comportamento desejado em caso de falha, das necessidades de hibernação, da latência e durabilidade do armazenamento, do projeto de dumps de falhas e do monitoramento operacional.

:::single-choice{#swap-space-sizing-rule}
Qual é a melhor base para dimensionar o swap?

::option[Sempre exatamente o dobro da RAM instalada.]{#swap-space-twice-ram explanation="Essa regra histórica não é adequada para todas as cargas de trabalho ou tamanhos de memória modernos."}
::option[As necessidades medidas da carga de trabalho, os objetivos de hibernação e a política de falhas.]{#swap-space-sizing-requirements .correct explanation="A finalidade do sistema e o comportamento observado da memória são mais importantes que um multiplicador fixo da RAM."}
::option[Sempre zero quando o sistema possuir um SSD.]{#swap-space-zero-ssd explanation="O tipo de armazenamento sozinho não determina os requisitos de pressão de memória ou hibernação."}
:::

## Desativação Segura do Swap

Desative uma área específica verificada com:

```bash
$ sudo swapoff /dev/VERIFIED-SWAP-TARGET
```

O kernel precisa mover para outro lugar as páginas residentes naquela área. Se a RAM e o swap restante não puderem acomodá-las, a operação pode falhar ou criar uma pressão de memória perigosa. Interrompa ou limite primeiro as cargas de trabalho, monitore a memória, remova a entrada persistente do fstab somente após verificar o destino correto e confirme a desativação com `swapon --show` antes de reutilizar o armazenamento.

:::single-choice{#swap-space-swapoff-capacity}
Por que `swapoff` pode falhar ou colocar em risco um sistema com carga intensa?

::option[Swapoff sempre reformata todos os módulos de RAM.]{#swap-space-formats-ram explanation="Ele altera a configuração ativa do swap e não formata o hardware da memória física."}
::option[As páginas naquela área precisam de capacidade na RAM ou em outro swap.]{#swap-space-pages-need-capacity .correct explanation="A desativação exige realocar páginas ativas do swap enquanto o sistema continua funcionando."}
::option[Uma área de swap inativa deve permanecer montada em `/swap`.]{#swap-space-mounted-path explanation="As áreas de swap não são sistemas de arquivos montados em diretórios."}
:::

Use o laboratório [Criação e Ativação de um Arquivo de Swap no Linux](https://labex.io/labs/comptia-create-and-activate-a-swap-file-in-linux-590858) em um ambiente controlado para praticar permissões de arquivos, ativação e persistência.

## Resumo

Agora você sabe tratar o swap como um recurso explícito de gerenciamento de memória.

1. Relacione o swap principalmente à memória anônima sob pressão.
2. Inspecione o swap ativo e o comportamento da carga de trabalho antes de alterar a capacidade.
3. Inicialize somente um destino descartável verificado e ative-o com `swapon`.
4. Dimensione e proteja o swap de acordo com a carga de trabalho e os requisitos de hibernação.
5. Garanta a capacidade de realocação antes de usar `swapoff`.
