---
lesson_id: "copy-cp-command"
course_id: "command-line"
lang: "pt"
order_index: 10
title: "cp (Copiar)"
description: "Aprenda a copiar arquivos e árvores de diretórios controlando substituições e atributos preservados."
meta_title: "cp (Copiar) - Linha de Comando"
meta_description: "Aprenda o comando cp do Linux com exemplos para copiar arquivos, diretórios, vários arquivos, curingas e backups, além de opções como cp -r, cp -i e cp -p."
meta_keywords: "comando cp Linux, comando cp, copiar arquivos Linux, cp -r, cp -i, cp -p, cp -a, cp -u, cópia recursiva, curingas Linux"
---

O comando `cp` copia arquivos e diretórios, mantendo a origem no lugar. Sua sintaxe básica é:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

Você pode copiar um arquivo para outro caminho, copiar vários arquivos para um diretório ou copiar recursivamente uma árvore de diretórios.

## Cópia de um Arquivo

Coloque primeiro a origem e depois o destino:

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

Se `/home/pete/Documents/cooldocs` for um diretório existente, a cópia será criada dentro dele com o nome `mycoolfile`. Você também pode fornecer um novo nome no destino:

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

No segundo exemplo, os dados copiados recebem o nome `mycoolfile_backup`.

:::single-choice{#copy-file-under-new-name} Qual comando copia `draft.txt` para um arquivo chamado `final.txt`, mantendo `draft.txt`?

::option[`mv draft.txt final.txt`]{#move-draft explanation="`mv` renomeia ou move o caminho original. Ele não mantém a cópia de origem solicitada."}
::option[`cp final.txt draft.txt`]{#copy-reversed explanation="A origem e o destino estão invertidos. Esse comando copiaria de `final.txt` para `draft.txt`."}
::option[`cp draft.txt final.txt`]{#copy-draft .correct explanation="`cp` lê `draft.txt` e cria ou substitui `final.txt`, enquanto a origem continua disponível."}
:::

## Cópia de Vários Arquivos para um Diretório

Liste primeiro todas as origens e coloque o diretório de destino por último:

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

O último argumento deve ser um diretório quando você fornece mais de uma origem.

:::single-choice{#copy-multiple-files} Qual comando copia `a.txt` e `b.txt` para o diretório existente `archive/`?

::option[`cp archive/ a.txt b.txt`]{#destination-first explanation="Nessa forma de `cp`, o diretório de destino deve ficar no final. Colocá-lo primeiro altera a interpretação dos operandos."}
::option[`cp a.txt b.txt archive/`]{#destination-last .correct explanation="Com várias origens, `cp` trata o último diretório existente como destino de todos os arquivos anteriores."}
::option[`cp a.txt archive/ b.txt`]{#destination-middle explanation="Todos os operandos de origem devem vir antes do destino. O diretório existente deve ser o último operando."}
:::

## Seleção de Arquivos com Curingas

O shell pode expandir padrões curingas para vários caminhos de origem:

- `*`: corresponde a qualquer sequência de caracteres.
- `?`: corresponde a qualquer caractere individual.
- `[]`: corresponde a um dos caracteres entre colchetes.

Por exemplo, copie os nomes terminados em `.jpg` do diretório atual para `Pictures`:

```bash
$ cp *.jpg /home/pete/Pictures
```

Visualize as correspondências antes de uma cópia em massa, especialmente quando o destino contiver dados importantes:

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

:::single-choice{#preview-copy-pattern} Antes de copiar `*.jpg`, qual comando mostra os nomes não ocultos aos quais o padrão corresponde no momento?

::option[`cp *.jpg`]{#copy-no-destination explanation="Esse comando tenta realizar uma cópia sem um destino claro quando há várias correspondências. Ele não é uma operação de visualização."}
::option[`ls *.jpg`]{#list-jpg-matches .correct explanation="O shell expande o mesmo padrão para `ls`, permitindo inspecionar os nomes correspondentes antes de copiá-los."}
::option[`file '*.jpg'`]{#quoted-jpg-pattern explanation="As aspas impedem a expansão do curinga; portanto, `file` recebe os caracteres literais `*.jpg`. Isso não mostra as correspondências normais."}
:::

## Cópia de Árvores de Diretórios

Copiar um diretório e tudo abaixo dele exige uma operação recursiva. Use `-r` ou `-R`:

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

Esse comando copia o diretório `Pumpkin` e seus descendentes para `Documents`.

`-R` maiúsculo também solicita uma cópia recursiva:

```bash
$ cp -R website /home/pete/backups/
```

O modo de arquivamento, `-a`, é útil para cópias de backup. Ele copia recursivamente, preservando links e muitos atributos:

```bash
$ cp -a project/ project-backup/
```

:::single-choice{#archive-directory-tree} Você quer uma cópia recursiva de `project/` no estilo de backup, preservando links e muitos atributos. Qual comando atende a esse objetivo?

::option[`cp -p project/ project-backup/`]{#preserve-directory-only explanation="`-p` preserva determinados atributos, mas não torna a cópia de um diretório recursiva por si só."}
::option[`cp -u project/ project-backup/`]{#update-directory-only explanation="`-u` controla quando os arquivos são copiados conforme o estado do destino. Ele não ativa por si só a cópia recursiva de diretórios."}
::option[`cp -a project/ project-backup/`]{#archive-project .correct explanation="O modo de arquivamento inclui a cópia recursiva e preserva links e um conjunto amplo de atributos para um resultado no estilo de backup."}
:::

## Controle das Substituições

Por padrão, `cp` pode substituir um arquivo existente no destino. Use `-i` para solicitar confirmação antes da substituição:

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

Use `-n` quando um destino existente não deve ser sobrescrito:

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

A opção `-f` instrui o GNU `cp` a tentar remover um destino existente quando não conseguir abri-lo para gravação e depois repetir a cópia. Ela não substitui a verificação cuidadosa dos destinos. Aliases do shell também podem acrescentar opções como `-i`; portanto, investigue uma solicitação inesperada em vez de presumir uma configuração específica.

:::single-choice{#skip-existing-destination} Qual comando copia `report.txt` para `backup/`, mas ignora um destino existente com o mesmo nome?

::option[`cp -n report.txt backup/`]{#no-clobber-report .correct explanation="A opção `-n` impede que `cp` sobrescreva um arquivo existente no destino."}
::option[`cp -i report.txt backup/`]{#interactive-report explanation="`-i` pergunta antes de sobrescrever; portanto, o resultado depende da resposta. Ele não ignora automaticamente todos os destinos existentes."}
::option[`cp -f report.txt backup/`]{#force-report explanation="`-f` pode ajudar a substituir um destino que inicialmente não pôde ser aberto. Ele não impede sobrescritas."}
:::

## Preservação ou Atualização de Arquivos

Use `-p` para preservar o modo do arquivo de origem, seu proprietário quando permitido e seus carimbos de data e hora:

```bash
$ cp -p mycoolfile /home/pete/backups/
```

Use `-u` para copiar uma origem somente quando o destino estiver ausente ou a origem for mais recente:

```bash
$ cp -u *.txt /home/pete/Documents/
```

Outras opções comuns incluem:

- `-f`: força a substituição removendo primeiro o destino, se necessário.
- `-v`: mostra cada arquivo conforme ele é copiado.

Para praticar a cópia de arquivos e árvores de diretórios, experimente estes laboratórios:

1. **[Comando cp do Linux: Cópia de Arquivos](https://labex.io/labs/linux-linux-cp-command-file-copying-209744)** — Pratique o uso básico, opções avançadas como cópia recursiva e preservação de atributos, além de curingas para copiar arquivos e diretórios com eficiência.
2. **[Organização de Arquivos e Diretórios](https://labex.io/labs/linux-organizing-files-and-directories-387877)** — Pratique habilidades essenciais de gerenciamento de arquivos usando `cp`, `mv` e `rm` para organizar uma estrutura de projeto, mover arquivos e remover diretórios desnecessários.

## Resumo

Agora você sabe copiar arquivos e árvores de diretórios controlando o tratamento dos destinos.

1. Coloque os operandos de origem antes do destino.
2. Visualize as correspondências de curingas antes de uma cópia em massa.
3. Copie árvores de diretórios recursivamente ou no modo de arquivamento.
4. Confirme, ignore ou substitua conscientemente os destinos existentes.
5. Preserve atributos ou copie apenas origens mais recentes quando necessário.
