---
lesson_id: "remove-rm-command"
course_id: "command-line"
lang: "pt"
order_index: 13
title: "rm (Remover)"
description: "Aprenda a remover arquivos e diretórios verificando os destinos e escolhendo opções mais seguras de rm."
meta_title: "rm (Remover) - Linha de Comando"
meta_description: "Aprenda o comando rm do Linux com exemplos seguros para excluir arquivos e diretórios, usar rm -r e rm -i e evitar erros com rm -rf."
meta_keywords: "comando rm Linux, comando rm, rm -r, rm -i, rm -f, rm -rf, excluir arquivos Linux, remover diretório Linux, rmdir"
---

O comando `rm` remove entradas do sistema de arquivos. A remoção pela linha de comando normalmente não envia os itens para a lixeira do ambiente gráfico, e `rm` não possui uma função integrada para desfazer a ação; portanto, confirme todos os destinos antes de executá-lo.

A sintaxe básica é:

```bash
rm [OPTIONS] FILE...
```

## Remoção de Arquivos

Forneça um ou mais caminhos de arquivos a `rm`:

```bash
$ rm file1
```

```bash
$ rm notes.txt old-report.txt draft.md
```

Verifique a grafia e a localização antes de pressionar Enter. Um backup ou uma cópia no controle de versão oferece um plano de recuperação mais confiável do que ferramentas de recuperação do sistema de arquivos após a exclusão.

:::single-choice{#remove-one-file} Depois de confirmar o destino, qual comando remove o arquivo `old-report.txt`?

::option[`rm old-report.txt`]{#rm-report .correct explanation="`rm` remove a entrada de arquivo indicada. Normalmente, a operação não coloca o arquivo em uma lixeira."}
::option[`rmdir old-report.txt`]{#rmdir-report explanation="`rmdir` atua em diretórios vazios, não em arquivos comuns. Ele não é o comando para este destino."}
::option[`mv old-report.txt`]{#mv-report explanation="`mv` precisa de um destino e altera um caminho, em vez de excluí-lo. Esse comando incompleto não realiza a remoção solicitada."}
:::

## Visualização dos Destinos de Curingas

O shell pode expandir um curinga para vários operandos. Por exemplo, `*.tmp` seleciona os nomes não ocultos correspondentes no diretório atual:

```bash
$ rm *.tmp
```

Antes de remover qualquer coisa, visualize o mesmo padrão sem aspas usando `ls`:

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

O shell expande o padrão antes que `rm` seja iniciado. Se a visualização incluir um arquivo inesperado, corrija o padrão em vez de prosseguir.

:::single-choice{#preview-removal-pattern} Você pretende remover `*.tmp`. Qual comando mostra primeiro, sem excluí-los, os caminhos não ocultos selecionados pelo padrão?

::option[`rm -v *.tmp`]{#verbose-remove explanation="O modo detalhado informa as remoções enquanto elas acontecem. Ele ainda exclui os arquivos correspondentes e não é uma visualização somente para leitura."}
::option[`ls '*.tmp'`]{#quoted-pattern explanation="As aspas impedem a expansão do curinga; portanto, esse comando procura um nome literal com `*`, em vez de mostrar os destinos pretendidos."}
::option[`ls *.tmp`]{#list-temp-matches .correct explanation="O shell expande `*.tmp` para `ls`, permitindo inspecionar o mesmo conjunto de correspondências não ocultas antes da remoção."}
:::

## Solicitação de Confirmação

A opção `-i` pergunta antes de cada remoção:

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

A opção `-I` é uma salvaguarda menos intrusiva no GNU `rm`: ela pergunta uma vez quando um comando removeria mais de três arquivos ou atuaria recursivamente.

:::single-choice{#confirm-each-removal} Qual comando solicita confirmação antes de remover cada arquivo indicado?

::option[`rm -i important.txt`]{#interactive-important .correct explanation="A opção `-i` pergunta antes de cada remoção, oferecendo a oportunidade de rejeitar a operação."}
::option[`rm -f important.txt`]{#force-important explanation="A opção `-f` suprime perguntas e ignora um operando ausente. Ela elimina, em vez de acrescentar, a confirmação."}
::option[`rm -v important.txt`]{#verbose-important explanation="A opção `-v` informa o que foi removido, mas não pede aprovação antecipadamente."}
:::

## Como Ignorar Arquivos Ausentes com -f

A opção `-f` ignora operandos ausentes e suprime perguntas:

```bash
$ rm -f old-cache.txt
```

Isso pode tornar uma limpeza por script idempotente quando um arquivo gerado talvez já esteja ausente. Como ela remove a confirmação, não acrescente `-f` apenas para silenciar um erro que você ainda não compreendeu.

## Remoção de Diretórios

`rm` sem opções não remove um diretório:

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

Use `-r` ou `-R` apenas quando pretender remover uma árvore de diretórios e todo o seu conteúdo:

```bash
$ rm -r old-project
```

Para um diretório vazio, `rmdir` é uma alternativa mais restrita:

```bash
$ rmdir empty-directory
```

`rmdir` falha quando o diretório não está vazio, protegendo seu conteúdo contra uma exclusão recursiva.

:::single-choice{#remove-empty-directory-only} Qual comando remove `old-cache/` somente se esse diretório estiver vazio?

::option[`rm -r old-cache/`]{#recursive-cache explanation="`rm` recursivo remove o diretório e seu conteúdo. Ele não impõe a condição de diretório vazio."}
::option[`rmdir old-cache/`]{#rmdir-cache .correct explanation="`rmdir` só tem sucesso para um diretório vazio; portanto, ele não exclui recursivamente os arquivos contidos."}
::option[`rm -f old-cache/`]{#force-cache explanation="A opção `-f` não faz `rm` sem `-r` remover um diretório. Ela também suprime salvaguardas, em vez de verificar se está vazio."}
:::

## Verificação de uma Remoção Recursiva

Uma remoção recursiva pode apagar uma árvore inteira. Combinar `-r` com `-f` também elimina as perguntas; por isso, `rm -rf` exige uma validação especialmente cuidadosa do destino. Antes de qualquer remoção recursiva, verifique:

- Você está no diretório que imagina? Use `pwd`.
- `ls -ld -- TARGET` mostra o caminho superior pretendido?
- Se houver um curinga, uma visualização somente para leitura correspondeu exatamente ao esperado?
- O caminho é absoluto ou relativo? `/tmp/cache` e `tmp/cache` são muito diferentes.
- Há um espaço acidental? `rm -rf old-project` e `rm -rf old project` se referem a caminhos diferentes.

Use `--` antes de um destino que possa começar com hífen para que ele não seja interpretado como uma opção:

```bash
$ rm -- -old-name
```

Não recorra a `sudo` simplesmente porque `rm` informou um erro de permissão. Primeiro, verifique o destino e descubra por que sua conta não consegue modificar o diretório que o contém. Uma remoção recursiva com privilégios elevados pode danificar o sistema operacional ou os dados de outros usuários.

Use `-v` quando quiser que `rm` informe cada remoção bem-sucedida:

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

:::single-choice{#remove-nonempty-tree} Depois de verificar o destino completo, qual comando remove `old-project/` e tudo abaixo dele sem suprimir as perguntas normais?

::option[`rm old-project/`]{#plain-rm-project explanation="`rm` sem opção recursiva não entra em um diretório. Ele não consegue remover uma árvore não vazia."}
::option[`rm -r old-project/`]{#recursive-old-project .correct explanation="A opção `-r` remove recursivamente a árvore de diretórios. Ao contrário de `rm -rf`, essa forma não acrescenta `-f` para suprimir perguntas."}
::option[`rmdir old-project/`]{#rmdir-project explanation="`rmdir` exige um diretório vazio. Ele falha quando o projeto ainda contém entradas."}
:::

Para praticar a remoção em um ambiente controlado, experimente estes laboratórios:

1. **[Comando rm do Linux: Remoção de Arquivos](https://labex.io/labs/linux-linux-rm-command-file-removing-209741)** — Aprenda a usar `rm` para remover arquivos e diretórios, incluindo opções como `-r` e `-i`, e pratique uma exclusão segura e eficaz.
2. **[Organização de Arquivos e Diretórios](https://labex.io/labs/linux-organizing-files-and-directories-387877)** — Pratique habilidades essenciais de gerenciamento de arquivos, inclusive o uso de `rm` para eliminar diretórios desnecessários, em um desafio prático.

## Resumo

Agora você sabe remover entradas do sistema de arquivos tratando cada destino como irreversível.

1. Confirme os caminhos dos arquivos antes da remoção.
2. Visualize expansões de curingas com um comando somente para leitura.
3. Solicite confirmação com `-i` ou `-I`.
4. Prefira `rmdir` quando um diretório precisar estar vazio.
5. Valide o destino inteiro antes de usar a remoção recursiva.
