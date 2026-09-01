---
lesson_id: "stdin-standard-in-redirect"
course_id: "text-fu"
lang: "pt"
order_index: 2
title: "stdin (Entrada Padrão)"
description: "Aprenda como os programas leem a entrada padrão e como o Bash conecta esse fluxo a um arquivo."
meta_title: "stdin (Entrada Padrão) - Text-Fu"
meta_description: "Domine o redirecionamento da entrada padrão, ou stdin, no Linux. Entenda sua relação com stdout, use o operador < e aprenda a controlar fluxos de dados."
meta_keywords: "stdin, entrada padrão, redirecionar stdin, cat stdin, stdin e stdout, redirecionamento Linux, linha de comando, fluxo de entrada"
---

A entrada padrão, abreviada como **stdin**, é o fluxo que um programa normalmente lê para receber dados. Em um terminal interativo, o shell geralmente conecta stdin à entrada do terminal, permitindo que um programa leia o que você digita.

## Entrada Padrão e o Descritor de Arquivo 0

Por convenção, os três fluxos padrão usam estes números de descritores de arquivo:

- `0`: entrada padrão (`stdin`)
- `1`: saída padrão (`stdout`)
- `2`: erro padrão (`stderr`)

Um programa pode escolher se e como usará esses fluxos. Um comando projetado para ler stdin costuma aguardar a entrada do terminal quando não recebe um operando de arquivo nem outra fonte de entrada.

:::single-choice{#stdin-descriptor-number} Qual descritor de arquivo representa convencionalmente a entrada padrão?

::option[`0`]{#stdin-fd-zero .correct explanation="A entrada padrão é convencionalmente o descritor de arquivo 0."}
::option[`1`]{#stdin-fd-one explanation="O descritor de arquivo 1 representa convencionalmente a saída padrão, o fluxo dos resultados comuns."}
::option[`2`]{#stdin-fd-two explanation="O descritor de arquivo 2 representa convencionalmente o erro padrão, não a entrada padrão."}
:::

## Redirecionamento de um Arquivo para stdin

O operador `<` instrui o Bash a abrir um arquivo para leitura e conectá-lo à stdin do comando:

```bash
$ cat < peanuts.txt
Hello World
```

O shell trata `< peanuts.txt`; `cat` simplesmente lê o descritor de arquivo 0. O caminho não é fornecido a `cat` como um operando comum de arquivo.

Se o arquivo de entrada não existir ou não puder ser aberto, o shell informará o erro de redirecionamento e não iniciará o comando com essa entrada.

:::single-choice{#stdin-from-file} Qual comando faz `sort` ler sua entrada padrão de `names.txt`?

::option[`sort < names.txt`]{#sort-stdin-file .correct explanation="O Bash abre `names.txt` para leitura e o conecta a `sort` no descritor de arquivo 0."}
::option[`sort > names.txt`]{#stdout-to-names explanation="O operador de maior redireciona stdout para o arquivo e pode truncá-lo. Ele não fornece o arquivo como entrada."}
::option[`sort names.txt >`]{#incomplete-sort-output explanation="Essa forma inclui um redirecionamento de saída incompleto. Ela não representa a conexão de stdin solicitada."}
:::

## Operando de Arquivo versus Redirecionamento de Entrada

Alguns comandos aceitam tanto um nome de arquivo como operando quanto stdin, mas os resultados podem ser ligeiramente diferentes. Por exemplo:

```bash
$ wc -l peanuts.txt
1 peanuts.txt
$ wc -l < peanuts.txt
1
```

As duas formas contam as linhas nos mesmos dados. Na primeira, `wc` conhece o nome do arquivo porque o recebeu como argumento. Na segunda, ele recebe apenas um fluxo em stdin e, portanto, não possui um nome de arquivo para mostrar.

:::single-choice{#stdin-not-command-argument} Por que `wc -l < peanuts.txt` normalmente omite `peanuts.txt` da saída?

::option[`wc` exclui o nome do arquivo depois de terminar a contagem das linhas.]{#stdin-delete-name explanation="O comando não renomeia nem exclui o arquivo de origem. Apenas sua conexão de entrada é diferente."}
::option[O operador `<` oculta todas as palavras mostradas pelo comando.]{#stdin-hide-words explanation="O redirecionamento de entrada não filtra stdout. O nome está ausente porque `wc` nunca o recebeu como argumento."}
::option[O Bash fornece o arquivo como stdin, não como um argumento de nome de arquivo.]{#stdin-no-filename .correct explanation="O shell consome o redirecionamento e conecta o arquivo ao descritor 0; portanto, `wc` não recebe o caminho como operando."}
:::

## Combinação dos Redirecionamentos de Entrada e Saída

Uma única linha de comando pode redirecionar mais de um fluxo:

```bash
$ cat < peanuts.txt > banana.txt
```

O shell realiza duas conexões independentes:

1. `< peanuts.txt` abre `peanuts.txt` como stdin de `cat`.
2. `> banana.txt` cria ou trunca `banana.txt` e o conecta à stdout de `cat`.

`cat` lê bytes de stdin e os grava em stdout; assim, `banana.txt` recebe o conteúdo da origem. Para uma cópia comum de arquivo, `cp peanuts.txt banana.txt` comunica a intenção mais diretamente; este exemplo trata das conexões entre fluxos.

:::single-choice{#stdin-and-stdout-files} Em `cat < input.txt > output.txt`, qual arquivo fornece stdin e qual recebe stdout?

::option[`output.txt` fornece stdin; `input.txt` recebe stdout.]{#stdin-output-stdout-input explanation="Essa resposta inverte os significados dos operadores. As setas apontam para o comando na entrada e para o arquivo na saída."}
::option[`input.txt` fornece stdin; `output.txt` recebe stdout.]{#stdin-input-stdout-output .correct explanation="O redirecionamento `<` abre `input.txt` para o descritor 0, e `>` abre `output.txt` para o descritor 1."}
::option[Os dois arquivos fornecem stdin, e stdout permanece no terminal.]{#both-stdin explanation="Os dois operadores afetam fluxos padrão diferentes. `>` redireciona stdout para fora do terminal."}
:::

Para praticar o redirecionamento de entrada e saída, experimente estes laboratórios:

1. **[Redirecionamento de Entrada e Saída no Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** — Pratique o controle do fluxo de dados dos comandos manipulando saída padrão (stdout), erro padrão (stderr) e entrada padrão (stdin) com operadores como `>`, `>>`, `2>` e o comando `tee`.
2. **[Redirecionamento de Fluxos de Dados](https://labex.io/labs/linux-data-stream-redirection-17995)** — Aprenda a manipular os fluxos de entrada, saída e erro, combinar saídas e usar `/dev/null` em operações avançadas com arquivos.

## Resumo

Agora você sabe conectar a entrada padrão de um comando a um arquivo por meio do shell.

1. Reconheça stdin como o descritor de arquivo 0.
2. Redirecione um arquivo legível com `<`.
3. Diferencie um operando de nome de arquivo de uma entrada redirecionada.
4. Combine conscientemente os redirecionamentos de stdin e stdout.
