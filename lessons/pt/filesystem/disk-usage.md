---
lesson_id: "disk-usage"
course_id: "filesystem"
lang: "pt"
order_index: 9
title: "Uso do Disco"
description: "Aprenda como `df` e `du` medem diferentes perspectivas do consumo de blocos e inodes do sistema de arquivos."
meta_title: "Uso do Disco - O Sistema de Arquivos"
meta_description: "Aprenda a verificar o uso e o espaço livre em discos Linux com os comandos df e du. Este guia aborda como analisar espaço em disco, incluindo o uso de inodes com df -i, e localizar os arquivos que ocupam espaço."
meta_keywords: "comando df, comando du, uso de disco Linux, verificar espaço livre, df -i Linux, gerenciamento de discos, tutorial Linux, utilização do disco, uso do sistema de arquivos"
---

A capacidade de um sistema de arquivos possui pelo menos dois limites: blocos de dados e objetos de metadados, como inodes. `df` informa a alocação pela perspectiva do sistema de arquivos, enquanto `du` percorre caminhos acessíveis e soma o uso atribuído a eles. Os valores respondem a perguntas diferentes e não precisam coincidir.

## Capacidade do Sistema de Arquivos com `df`

Mostre o tipo do sistema de arquivos montado e os valores de blocos em formato legível com:

```bash
$ df -hT
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda1      ext4  6.2G  2.3G  3.6G  40% /
```

`Size`, `Used` e `Avail` vêm da contabilidade do sistema de arquivos. O espaço disponível pode ser menor que o total menos o usado por causa de blocos reservados, metadados, políticas de alocação, cotas ou arredondamentos. Execute `df` em um caminho para informar o sistema de arquivos que contém esse caminho:

```bash
$ df -hT /var/log
```

:::single-choice{#disk-usage-df-scope}
O que `df` informa principalmente?

::option[O conteúdo em bytes de cada arquivo de um diretório.]{#disk-usage-df-file-content explanation="A contabilização de árvores de diretórios é função de ferramentas como `du`."}
::option[A capacidade, o uso e o espaço disponível no nível do sistema de arquivos.]{#disk-usage-df-filesystem .correct explanation="Df consulta as estatísticas de alocação do sistema de arquivos montado, em vez de percorrer todos os caminhos."}
::option[Somente o tamanho físico impresso no rótulo de um disco.]{#disk-usage-df-physical-label explanation="Seus valores descrevem a contabilidade do sistema de arquivos, não apenas a capacidade anunciada pelo hardware."}
:::

## Capacidade de Inodes

Sistemas de arquivos que alocam objetos semelhantes a inodes podem esgotá-los mesmo quando ainda há blocos disponíveis:

```bash
$ df -i /var
```

Grandes quantidades de arquivos pequenos podem consumir os inodes disponíveis. Excluir um arquivo grande libera muitos blocos, mas geralmente apenas um inode; excluir muitos arquivos pequenos desnecessários pode aliviar a pressão sobre os inodes. Alguns sistemas de arquivos alocam metadados dinamicamente e representam esses conceitos de forma diferente.

:::single-choice{#disk-usage-inode-exhaustion}
O que pode acontecer quando um sistema de arquivos possui blocos livres, mas nenhum inode disponível?

::option[Todos os arquivos existentes dobram de tamanho automaticamente.]{#disk-usage-inode-double explanation="O esgotamento dos inodes impede a alocação de novos metadados e não aumenta o conteúdo existente."}
::option[A criação de outro arquivo pode falhar.]{#disk-usage-inode-create-fail .correct explanation="Um novo objeto do sistema de arquivos precisa de metadados, mesmo quando ainda há espaço para dados de arquivos."}
::option[O sistema de arquivos é convertido em swap.]{#disk-usage-inode-swap explanation="O esgotamento de um recurso não altera o tipo do sistema de arquivos."}
:::

## Uso de Caminhos com `du`

Resuma o espaço alocado acessível abaixo de um diretório:

```bash
$ du -sh /var/log
```

Compare os filhos imediatos permanecendo em um único sistema de arquivos:

```bash
$ sudo du -xhd1 /var | sort -h
```

As opções do GNU mostradas aqui significam saída legível, profundidade máxima de um nível e um único sistema de arquivos. As permissões podem ocultar subárvores e produzir um total incompleto. Por padrão, `du` também pode contar arquivos com links físicos apenas uma vez, diferenciar o tamanho aparente dos blocos alocados e tratar arquivos esparsos de modo diferente conforme as opções.

:::single-choice{#disk-usage-du-purpose}
Qual comando resume o uso alocado em `/var/log`?

::option[`df -i /var/log`]{#disk-usage-df-inodes explanation="Esse comando informa estatísticas de inodes do sistema de arquivos que contém o caminho."}
::option[`du -sh /var/log`]{#disk-usage-du-summary .correct explanation="Du percorre a árvore indicada, e `-s` emite um único resumo em unidades legíveis."}
::option[`mount -a /var/log`]{#disk-usage-mount-a explanation="A montagem não tem relação com um resumo somente para leitura do uso de um diretório."}
:::

## Por que `df` e `du` São Diferentes

Algumas causas comuns são:

- um processo mantém aberto um arquivo excluído, portanto seus blocos continuam alocados, mas não existe um caminho para `du`
- metadados do sistema de arquivos, espaço reservado, journals, reflinks, snapshots ou compressão afetam a contabilidade
- outro sistema de arquivos está montado dentro da árvore percorrida
- as permissões impedem `du` de ler alguns diretórios
- arquivos esparsos possuem tamanhos aparentes e alocados diferentes

Para arquivos excluídos, mas ainda abertos, inspecione os processos autorizados com uma ferramenta como `lsof +L1`; reinicie ou sinalize o serviço responsável por seu procedimento normal, em vez de truncar descritores desconhecidos.

:::single-choice{#disk-usage-deleted-open-file}
Por que `df` pode mostrar espaço em uso que `du`, baseado em caminhos, não consegue encontrar?

::option[`df` sempre multiplica por dois o tamanho de cada arquivo.]{#disk-usage-df-doubles explanation="Não existe uma regra universal de duplicação."}
::option[Um arquivo excluído pode permanecer aberto e alocado para um processo em execução.]{#disk-usage-open-deleted .correct explanation="A entrada do diretório desapareceu, mas o sistema de arquivos mantém os blocos até que a última referência aberta seja fechada."}
::option[`du` exclui automaticamente os arquivos depois de contá-los.]{#disk-usage-du-deletes explanation="Du é uma ferramenta de contabilização e não remove os arquivos percorridos."}
:::

## Investigação sem Agravar o Incidente

Comece pelo sistema de arquivos cheio informado por `df`, identifique seu destino de montagem com `findmnt` e então restrinja as buscas de `du` nesse mesmo sistema de arquivos. Considere snapshots, camadas de contêineres, logs, caches de pacotes e a política de retenção das aplicações. Não exclua arquivos somente porque são grandes; determine primeiro a propriedade, o backup, os requisitos de conformidade e o comportamento do serviço.

:::single-choice{#disk-usage-safe-investigation}
Qual é a resposta mais segura ao encontrar um arquivo grande?

::option[Excluí-lo imediatamente enquanto o serviço está gravando.]{#disk-usage-delete-immediately explanation="Isso pode causar perda de dados necessários e talvez não libere espaço se o arquivo continuar aberto."}
::option[Executar `mkfs` no dispositivo que o contém.]{#disk-usage-mkfs-device explanation="A formatação destruiria o sistema de arquivos em vez de resolver o crescimento de um único arquivo."}
::option[Identificar seu proprietário e sua função de retenção antes de alterá-lo.]{#disk-usage-review-large-file .correct explanation="O tamanho sozinho não estabelece que o arquivo seja descartável nem seguro de truncar."}
:::

## Resumo

Agora você sabe conciliar os relatórios de espaço do sistema de arquivos e os baseados em caminhos.

1. Use `df` para a capacidade de blocos dos sistemas de arquivos montados.
2. Use `df -i` para a pressão sobre inodes quando houver suporte.
3. Use percursos restritos com `du` para atribuir o uso a caminhos acessíveis.
4. Investigue arquivos excluídos ainda abertos e diferenças específicas da contabilidade do sistema de arquivos.
5. Aplique políticas de propriedade e retenção antes de excluir dados.
