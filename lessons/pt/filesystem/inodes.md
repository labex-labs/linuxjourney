---
lesson_id: "inodes"
course_id: "filesystem"
lang: "pt"
order_index: 11
title: "Inodes"
description: "Aprenda como os números de inodes conectam os nomes dos diretórios aos metadados e dados dos objetos do sistema de arquivos."
meta_title: "Inodes - O Sistema de Arquivos"
meta_description: "Conheça o conceito de inode no Linux. Aprenda o que é um i-node, como os inodes gerenciam metadados de arquivos e como verificar seu uso com `df -i` e `ls -li`."
meta_keywords: "inode Linux, inode no Linux, i-node, inode, número de inode, sistema de arquivos, df -i, ls -li, stat"
---

Em sistemas de arquivos Unix baseados em inodes, um diretório mapeia o nome de cada entrada para um número de inode. O inode representa o objeto do sistema de arquivos e registra os metadados necessários para localizar e interpretar seus dados. Portanto, o caminho não é armazenado como a identidade principal do próprio objeto.

## Metadados Armazenados com um Inode

Os metadados normalmente associados a um inode incluem:

- tipo do objeto e modo de permissão
- propriedade de usuário e grupo
- tamanho lógico e contabilização dos blocos alocados
- contagem de links físicos
- timestamps de acesso, modificação e alteração de estado
- referências aos dados do arquivo ou a estruturas de extensões específicas do sistema de arquivos

Normalmente, o inode não armazena o nome da entrada do diretório. Um sistema de arquivos também pode armazenar atributos estendidos, listas de controle de acesso, horário de criação, dados inline ou outras informações por meio de estruturas específicas do formato.

`ctime` é o horário de alteração do estado do inode, não necessariamente o horário de criação do arquivo. Um timestamp separado de nascimento ou criação é opcional e pode não estar disponível.

:::single-choice{#inodes-name-location} Onde o componente do caminho de um arquivo comum normalmente é associado ao número de seu inode?

::option[No escalonador de processos.]{#inodes-scheduler-name explanation="O estado de escalonamento da CPU não implementa a resolução de caminhos do sistema de arquivos."}
::option[Em uma entrada de diretório.]{#inodes-directory-entry .correct explanation="Um diretório mapeia um nome para um número de inode dentro daquele sistema de arquivos."}
::option[Na tabela de partições do disco.]{#inodes-partition-name explanation="Uma tabela de partições mapeia regiões de armazenamento, não nomes de arquivos individuais."}
:::

## Números de Inodes e o Escopo do Sistema de Arquivos

Exiba os números de inodes com:

```bash
$ ls -li
```

O primeiro campo é o número do inode. Inspecione um objeto com mais detalhes usando:

```bash
$ stat path
```

Um número de inode é exclusivo apenas dentro de um sistema de arquivos em determinado momento. O mesmo número pode existir em outro sistema de arquivos e pode ser reutilizado depois que um inode é liberado. Identifique um objeto de forma confiável tanto pela identidade do sistema de arquivos quanto pelo número do inode, não apenas pelo número.

:::single-choice{#inodes-number-scope} Em qual escopo um número de inode identifica um objeto?

::option[Em todos os sistemas Linux do mundo, para sempre.]{#inodes-global-forever explanation="A alocação de inodes é local ao sistema de arquivos, e os identificadores podem ser reutilizados."}
::option[Em um sistema de arquivos, em determinado momento.]{#inodes-one-filesystem .correct explanation="Outros sistemas de arquivos podem usar o mesmo número, e os números de inodes liberados podem ser reutilizados mais tarde."}
::option[Somente no processo do shell que criou o arquivo.]{#inodes-shell-scope explanation="O sistema de arquivos, não um único shell, mantém a identidade do inode."}
:::

## Links Físicos e Referências Abertas

Várias entradas de diretório podem apontar para o mesmo inode; elas são links físicos. Criar outro link físico incrementa a contagem de links do objeto. Remover um nome reduz a contagem sem excluir os dados enquanto outro link permanecer.

Mesmo depois que a última entrada de diretório é removida, um arquivo aberto continua alocado até que a última referência de processo seja fechada. Sua contagem de links pode ser zero enquanto um descritor ainda o acessa. Isso explica por que excluir um log grande e aberto pode não reduzir imediatamente o uso informado por `df`.

:::single-choice{#inodes-unlinked-open-file} Quando os recursos de um arquivo sem links normalmente são liberados?

::option[Imediatamente após a remoção de qualquer um dos nomes de links físicos.]{#inodes-one-link-removed explanation="Outros links físicos ou referências abertas podem manter o objeto existente."}
::option[Somente quando todo o sistema de arquivos é reformatado.]{#inodes-reformat-only explanation="As operações comuns de unlink e close recuperam inodes e blocos que deixaram de ser usados."}
::option[Depois que a contagem de links chega a zero e a última referência aberta é fechada.]{#inodes-zero-links-no-opens .correct explanation="Os nomes dos diretórios e os descritores de arquivos dos processos são referências independentes ao inode."}
:::

## Capacidade de Inodes

Em sistemas de arquivos com um conjunto finito ou informado de inodes, milhões de arquivos pequenos podem esgotar a capacidade de metadados antes que os blocos de dados sejam preenchidos. Inspecione a contabilidade de inodes dos sistemas de arquivos montados com:

```bash
$ df -i
```

Se não houver inodes livres, a criação de outro arquivo pode falhar mesmo que `df -h` informe blocos disponíveis. As estratégias de alocação variam: alguns sistemas de arquivos pré-alocam estruturas de inodes durante a criação, enquanto outros gerenciam os metadados dinamicamente e podem informar sua capacidade de forma diferente.

:::single-choice{#inodes-df-i-purpose} O que `df -i` informa quando o sistema de arquivos oferece contabilidade de inodes?

::option[O conteúdo de todos os arquivos na ordem dos inodes.]{#inodes-df-i-content explanation="Df informa estatísticas agregadas do sistema de arquivos e não lê o conteúdo dos arquivos."}
::option[A capacidade de inodes usada e disponível.]{#inodes-df-i-capacity .correct explanation="A visualização de inodes ajuda a diagnosticar o esgotamento de objetos de metadados independentemente dos blocos de dados."}
::option[A revisão do firmware do disco.]{#inodes-df-i-firmware explanation="O inventário de firmware não tem relação com o uso de inodes."}
:::

## Mapeamento de Dados Específico do Sistema de Arquivos

Não presuma que todo inode possua exatamente 12 ponteiros diretos e três indiretos. Essa é uma descrição útil de alguns layouts clássicos, mas o ext4 moderno pode usar extensões, e XFS, Btrfs e outros sistemas empregam estruturas diferentes. Dados inline e extensões comprimidas ou copy-on-write alteram ainda mais essa relação.

Use ferramentas de diagnóstico específicas do sistema de arquivos apenas em modos somente para leitura ou documentados quando o mapeamento interno for importante. Para a administração comum, `stat`, `find -inum`, `df -i` e ferramentas que consideram links fornecem abstrações mais seguras.

:::single-choice{#inodes-layout-portability} Por que você não deve presumir um único layout fixo de ponteiros para todos os inodes?

::option[Inodes nunca fazem referência aos dados dos arquivos de nenhuma forma.]{#inodes-no-data-reference explanation="O sistema de arquivos precisa associar o objeto ao seu conteúdo, embora o mecanismo varie."}
::option[As implementações de sistemas de arquivos usam diferentes estruturas de extensões, árvores e dados inline.]{#inodes-format-specific-layout .correct explanation="O mapeamento em disco do inode para o conteúdo faz parte do formato de cada sistema de arquivos."}
::option[Cada proprietário de arquivo escolhe separadamente o layout de cada inode.]{#inodes-owner-layout explanation="A implementação e o formato do sistema de arquivos determinam a estrutura dos metadados."}
:::

Use o laboratório [Gerenciamento de Arquivos e Diretórios no Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835) para comparar números de inodes e contagens de links em arquivos descartáveis.

## Resumo

Agora você sabe relacionar caminhos, inodes, links e a capacidade do sistema de arquivos.

1. Trate as entradas dos diretórios como mapeamentos de nomes para números de inodes.
2. Leia metadados e timestamps sem confundir ctime com o horário de criação.
3. Restrinja o escopo dos números de inodes a um sistema de arquivos e momento.
4. Considere tanto links físicos quanto descritores de arquivos abertos.
5. Use modelos específicos de cada sistema de arquivos, não um único layout universal de ponteiros.
