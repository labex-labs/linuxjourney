---
lesson_id: "print-working-directory-pwd-command"
course_id: "command-line"
lang: "pt"
order_index: 2
title: "pwd (Exibir o Diretório de Trabalho)"
description: "Aprenda a usar pwd para identificar sua localização atual no sistema de arquivos do Linux."
meta_title: "pwd (Exibir o Diretório de Trabalho) - Linha de Comando"
meta_description: "Aprenda o comando pwd do Linux, o significado de print working directory e como caminhos absolutos mostram sua localização atual no sistema de arquivos."
meta_keywords: "comando pwd, pwd Linux, exibir diretório de trabalho, diretório atual Linux, caminho absoluto, sistema de arquivos Linux, árvore de diretórios"
---

No Linux, arquivos e diretórios são organizados em uma hierarquia chamada sistema de arquivos. Antes de navegar com confiança, você precisa saber onde está. O comando `pwd` responde a essa pergunta exibindo seu diretório de trabalho atual.

## A Árvore de Diretórios no Linux

Todo o sistema de arquivos começa em um único diretório de nível superior chamado diretório raiz, representado por uma barra (`/`). A partir da raiz, a árvore se ramifica em subdiretórios, que podem conter arquivos e outros subdiretórios.

Veja um exemplo simplificado dessa estrutura:

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

:::single-choice{#identify-root-subdirectories}
Na árvore de diretórios acima, qual é a relação de `home` e `etc` com `/`?

::option[Eles são subdiretórios que se ramificam a partir de `/`.]{#root-subdirectories .correct explanation="Os dois diretórios aparecem diretamente abaixo de `/` na árvore. O sistema de arquivos se ramifica em subdiretórios a partir da raiz."}
::option[Eles são arquivos armazenados dentro do diretório `bin`.]{#files-inside-bin explanation="A árvore coloca `home` e `etc` ao lado de `bin`, não dentro dele. Neste exemplo, eles são diretórios, e não arquivos."}
::option[Eles são nomes alternativos para o diretório raiz.]{#alternate-root-names explanation="O Linux tem uma única raiz do sistema de arquivos, representada por `/`. `home` e `etc` são diretórios abaixo dela."}
:::

## Compreensão dos Caminhos de Arquivos

A localização de qualquer arquivo ou diretório é descrita por seu caminho. Um caminho é uma sequência de diretórios que leva de um ponto inicial até um destino específico.

Por exemplo, se houver uma pasta chamada `pete` dentro de `/home` e uma pasta `Movies` dentro de `pete`, o caminho completo será:

```plaintext
/home/pete/Movies
```

Um caminho que começa com `/` é absoluto porque parte do diretório raiz. Um caminho como `Movies` é relativo porque depende da sua localização atual.

:::single-choice{#recognize-absolute-path}
O que torna `/home/pete/Movies` um caminho absoluto?

::option[Ele contém vários nomes de diretórios separados por `/`.]{#contains-directories explanation="Tanto caminhos absolutos quanto relativos podem conter vários nomes de diretórios. O ponto inicial, e não a quantidade de nomes, determina o tipo do caminho."}
::option[Ele termina em um diretório chamado `Movies`.]{#ends-with-movies explanation="O nome do destino não determina se um caminho é absoluto. Um caminho absoluto é identificado por seu ponto inicial na raiz."}
::option[Ele começa na raiz com uma `/` inicial.]{#starts-at-root .correct explanation="Um caminho absoluto começa no diretório raiz. A `/` inicial mostra esse ponto de partida."}
:::

## Qual É o Significado de PWD no Linux?

`pwd` significa “print working directory”, ou “exibir o diretório de trabalho”. Seu diretório de trabalho é aquele em que o shell se encontra no momento. Os comandos que usam caminhos relativos partem dessa localização.

:::single-choice{#expand-pwd-name}
O que significa `pwd`?

::option[Print working directory]{#print-working-directory .correct explanation="O nome descreve exatamente o que o comando faz: exibe o diretório de trabalho atual do shell."}
::option[Present working directory]{#present-working-directory explanation="Na linguagem comum, a localização atual pode ser chamada de diretório presente, mas essa não é a expansão de `pwd`."}
::option[Print whole directory]{#print-whole-directory explanation="`pwd` informa o caminho do diretório atual. Ele não exibe todo o conteúdo desse diretório."}
:::

## Uso do Comando pwd

Para descobrir seu diretório atual, digite `pwd` e pressione Enter.

```bash
$ pwd
/home/pete
```

A saída é um caminho absoluto. Neste exemplo, o shell está no diretório pessoal do usuário `pete`.

A saída exata pode ser diferente em seu sistema porque o nome do usuário, o diretório pessoal e a localização atual podem variar. O comando `pwd` apenas exibe informações; ele não altera o diretório de trabalho. Já `cd` muda o diretório em que o shell se encontra.

:::single-choice{#check-location-without-changing-it}
Qual ação verifica seu diretório atual sem alterá-lo?

::option[Executar `cd` e ler o diretório para o qual ele muda.]{#run-cd explanation="O comando `cd` altera o diretório de trabalho. Ele não atende ao requisito de verificar a localização sem modificá-la."}
::option[Inserir `/home/pete` e usar o caminho como um comando.]{#run-path explanation="Um caminho absoluto identifica uma localização, mas o caminho sozinho não é o comando que informa seu diretório atual."}
::option[Executar `pwd` e ler o caminho absoluto exibido.]{#run-pwd .correct explanation="`pwd` informa a localização atual do shell sem mudá-la. Por isso, você pode usá-lo com segurança sempre que precisar confirmar onde está."}
:::

## Por que pwd É Útil

Use `pwd` quando:

- estiver seguindo instruções e precisar confirmar sua localização;
- um comando falhar porque o caminho de um arquivo está errado;
- tiver percorrido vários diretórios e perdido a noção de onde está;
- quiser copiar o caminho do diretório atual para outro comando.

Por exemplo:

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

Isso mostra que `app.py` e `README.md` estão localizados em `/home/pete/projects`.

Para reforçar sua compreensão sobre a navegação no sistema de arquivos do Linux e a identificação da localização atual, experimente estes laboratórios práticos:

1. **[Comando pwd do Linux: Exibição de Diretórios](https://labex.io/labs/linux-linux-pwd-command-directory-displaying-209734)** — Este laboratório oferece uma visão geral focada e o uso prático do comando `pwd`, em correspondência direta com a identificação do diretório atual apresentada nesta lição.
2. **[Navegação em Diretórios no Linux](https://labex.io/labs/linux-directory-navigation-387844)** — Teste suas habilidades básicas na linha de comando navegando por vários diretórios e consolide sua compreensão sobre caminhos e a estrutura do sistema de arquivos.
3. **[Comando cd do Linux: Mudança de Diretórios](https://labex.io/labs/linux-linux-cd-command-directory-changing-209733)** — Aprenda a navegar com eficiência pelo sistema de arquivos usando `cd`, conhecendo diferentes técnicas para mudar de diretório e explorar sua estrutura.

## Resumo

Agora você sabe usar `pwd` para identificar sua localização atual no sistema de arquivos do Linux.

1. Reconheça a raiz da árvore de diretórios.
2. Diferencie um caminho absoluto de um caminho relativo.
3. Explique o significado de `pwd` e o que ele informa.
4. Verifique seu diretório de trabalho sem alterá-lo.
