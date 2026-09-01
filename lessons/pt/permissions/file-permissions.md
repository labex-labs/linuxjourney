---
lesson_id: "file-permissions"
course_id: "permissions"
lang: "pt"
order_index: 1
title: "Permissões de Arquivos"
description: "Aprenda a interpretar os tipos de arquivos Linux e os bits de permissão do proprietário, do grupo e dos outros usuários."
meta_title: "Permissões de Arquivos - Permissões"
meta_description: "Uma parte essencial do nosso tutorial completo de Linux. Aprenda sobre permissões de arquivos Linux, incluindo os bits rwx para usuário, grupo e outros. Domine a saída de `ls -l` e entenda os modos dos arquivos."
meta_keywords: "permissões de arquivos, permissões de arquivos Linux, melhor forma de aprender Linux, tutorial completo Linux, permissões rwx, comando ls -l, modos de arquivos, guia Linux"
---

O Linux representa muitos recursos por meio de interfaces semelhantes a arquivos, e cada objeto do sistema de arquivos possui metadados que controlam o acesso. Saber interpretar esses metadados é fundamental para trabalhar com arquivos e diretórios de forma segura.

## Leitura de uma Listagem Longa

Use `ls -l` para exibir uma listagem longa:

```bash
$ ls -ld Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 Desktop/
```

O primeiro campo, `drwxr-xr-x`, combina um caractere de tipo de arquivo com nove caracteres de permissão. A listagem também identifica `pete` como proprietário e `penguins` como o grupo associado ao diretório.

O caractere inicial descreve o tipo do objeto. Os valores comuns incluem:

- `-` para um arquivo comum
- `d` para um diretório
- `l` para um link simbólico

Também existem outros tipos de arquivos especiais. Os nove caracteres restantes são as permissões de acesso:

```text
d | rwx | r-x | r-x
```

:::single-choice{#file-permissions-type-character} Em `drwxr-xr-x`, o que o primeiro `d` indica?

::option[O objeto é um link simbólico.]{#file-permissions-type-link explanation="Um link simbólico normalmente é mostrado com `l` na posição do tipo de arquivo."}
::option[O objeto é um diretório.]{#file-permissions-type-directory .correct explanation="O primeiro caractere é o tipo de arquivo, e `d` identifica um diretório."}
::option[O proprietário possui permissão de exclusão.]{#file-permissions-type-delete explanation="As sequências de modos do Linux não usam `d` como permissão de exclusão; a primeira posição descreve o tipo do objeto."}
:::

## Compreensão de `r`, `w` e `x`

Cada trio de permissões usa estes caracteres:

- `r` concede permissão de leitura.
- `w` concede permissão de escrita.
- `x` concede permissão de execução.
- `-` significa que a permissão está ausente.

Para um arquivo comum, a leitura permite acessar seu conteúdo, a escrita permite modificar seu conteúdo e a execução permite que o kernel tente executá-lo como um programa. A execução ainda pode falhar se o formato do arquivo, a linha do interpretador, as opções de montagem ou outro controle de segurança não a permitirem.

Para um diretório, os significados se referem às entradas do diretório:

- A leitura permite listar os nomes no diretório.
- A escrita permite criar ou remover entradas, normalmente em conjunto com a permissão de execução.
- A execução, também chamada de permissão de busca, permite percorrer o diretório e acessar entradas pelo nome.

A exclusão de um arquivo é determinada principalmente pelas permissões do diretório pai, não pelo bit de escrita do próprio arquivo.

:::single-choice{#file-permissions-directory-execute} O que a permissão de execução em um diretório permite principalmente?

::option[Executar todos os arquivos comuns armazenados no diretório.]{#file-permissions-directory-run-files explanation="O bit de execução de um diretório não concede permissão de execução a cada arquivo contido nele."}
::option[Alterar o conteúdo de todos os arquivos do diretório.]{#file-permissions-directory-edit-files explanation="A escrita no conteúdo dos arquivos depende das permissões dos arquivos e de outros controles de acesso."}
::option[Percorrer o diretório e acessar entradas pelo nome.]{#file-permissions-directory-search .correct explanation="A permissão de execução, ou busca, do diretório permite percorrer caminhos que passem por ele."}
:::

## Classes de Proprietário, Grupo e Outros

Os nove caracteres de modo formam três trios em uma ordem fixa:

1. **Proprietário**: permissões usadas quando o ID de usuário efetivo do processo corresponde ao proprietário do arquivo.
2. **Grupo**: permissões usadas quando um ID de grupo aplicável do processo corresponde ao grupo do arquivo.
3. **Outros**: permissões usadas quando nenhuma das classes anteriores corresponde.

O kernel seleciona uma única classe aplicável; ele não combina os três trios para encontrar o resultado mais permissivo. Mecanismos adicionais, como listas de controle de acesso, opções de montagem, capacidades ou controles de acesso obrigatórios, podem afetar ainda mais a decisão final.

No exemplo, o trio do proprietário é `rwx`, enquanto os trios do grupo e dos outros são `r-x`. O proprietário pode ler, escrever e percorrer o diretório. As classes do grupo e dos outros podem ler e percorrê-lo, mas não podem criar nem remover entradas por meio dos bits de modo comuns do diretório.

:::single-choice{#file-permissions-triplet-order} Depois do caractere de tipo de arquivo, em que ordem aparecem os três trios de permissões?

::option[Grupo, proprietário e depois outros.]{#file-permissions-order-group-first explanation="O trio do grupo aparece em segundo lugar, não em primeiro."}
::option[Outros, grupo e depois proprietário.]{#file-permissions-order-other-first explanation="O trio dos outros é o último, e o do proprietário é o primeiro."}
::option[Proprietário, grupo e depois outros.]{#file-permissions-order-owner-first .correct explanation="Os nove caracteres de permissão sempre apresentam os trios do proprietário, do grupo e dos outros nessa ordem."}
:::

:::single-choice{#file-permissions-example-group} Quais permissões comuns a classe do grupo possui em `drwxr-xr-x`?

::option[Leitura e escrita.]{#file-permissions-group-read-write explanation="O trio do grupo é `r-x`, portanto sua posição de escrita contém `-`."}
::option[Escrita e execução.]{#file-permissions-group-write-execute explanation="O trio do grupo contém `r`, não `w`, em sua primeira posição."}
::option[Leitura e execução.]{#file-permissions-group-read-execute .correct explanation="O trio do meio é `r-x`, que concede leitura e execução, mas não escrita."}
:::

Para reforçar esses conceitos em um ambiente isolado, experimente o laboratório [Usuários, Grupos e Permissões de Arquivos no Linux](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002). Ele oferece prática na leitura de modos e na alteração de propriedades e permissões.

## Resumo

Agora você sabe interpretar o campo básico de permissões em uma listagem longa do Linux.

1. Separe o caractere de tipo de arquivo dos nove bits de permissão.
2. Interprete `r`, `w` e `x` de acordo com o objeto ser um arquivo ou diretório.
3. Divida o modo nos trios do proprietário, do grupo e dos outros.
4. Relacione os trios ao proprietário e ao grupo mostrados por `ls -l`.
