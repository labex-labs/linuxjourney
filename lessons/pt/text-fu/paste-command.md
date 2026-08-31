---
lesson_id: "paste-command"
course_id: "text-fu"
lang: "pt"
order_index: 7
title: "paste"
description: "Aprenda a mesclar linhas correspondentes ou serializar linhas com delimitadores configuráveis usando paste."
meta_title: "paste - Text-Fu"
meta_description: "Aprenda a usar o comando paste do Linux para mesclar linhas de arquivos, escolher delimitadores e combinar dados orientados por linhas."
meta_keywords: "comando paste Linux, tutorial paste, mesclar linhas de arquivos, comandos Linux, Linux para iniciantes, guia Linux"
---

O comando `paste` combina linhas como colunas. Por padrão, ele obtém uma linha de cada arquivo de entrada, une essas linhas com uma tabulação e repete a operação até que todas as entradas cheguem ao fim.

## Mesclagem de Arquivos Lado a Lado

Crie dois arquivos pequenos:

```bash
$ printf 'alice\nbob\n' > names.txt
$ printf 'admin\nviewer\n' > roles.txt
```

Forneça os dois arquivos a `paste`:

```bash
$ paste names.txt roles.txt
alice	admin
bob	viewer
```

O espaço visível entre as colunas é uma tabulação. Ao contrário de `cat`, que grava um arquivo completo depois do outro, `paste` combina as linhas correspondentes das entradas.

:::single-choice{#paste-corresponding-lines}
`first.txt` contém `A` e depois `B`, enquanto `second.txt` contém `1` e depois `2`. O que `paste first.txt second.txt` produz por padrão?

::option[`A`, `B`, `1` e `2` em quatro linhas consecutivas.]{#paste-concatenated-files explanation="Isso se assemelha à gravação dos arquivos um após o outro. `paste` combina as linhas correspondentes."}
::option[`A`, `B`, `1` e `2` em uma única linha, sem separadores.]{#paste-one-line-no-separator explanation="A serialização em uma linha exige `-s`, e o separador padrão é uma tabulação, não a ausência de separador."}
::option[`A` com `1`, depois `B` com `2`, separados por tabulações.]{#paste-parallel-result .correct explanation="O modo paralelo padrão obtém uma linha de cada arquivo para cada linha de saída e separa os campos com uma tabulação."}
:::

## Escolha de um Delimitador

Use `-d LIST` para substituir o separador padrão de tabulação. Para usar dois-pontos:

```bash
$ paste -d ':' names.txt roles.txt
alice:admin
bob:viewer
```

Coloque entre aspas delimitadores que tenham significado para o shell. `paste` pode alternar entre vários caracteres delimitadores quando a lista contém mais de um, mas um único caractere é a opção mais simples ao criar duas colunas.

:::single-choice{#paste-colon-delimiter}
Qual comando une as linhas correspondentes de `names.txt` e `roles.txt` com dois-pontos?

::option[`paste -d ':' names.txt roles.txt`]{#paste-colon-files .correct explanation="A opção `-d` substitui a tabulação padrão pelos dois-pontos fornecidos entre cada par de campos."}
::option[`paste -s ':' names.txt roles.txt`]{#paste-serial-colon-operand explanation="A opção `-s` seleciona o modo serial, e `:` seria tratado como outro caminho de entrada, não como delimitador."}
::option[`paste names.txt ':' roles.txt`]{#paste-colon-file-operand explanation="Sem `-d`, cada operando é tratado como arquivo de entrada. Essa forma tentaria abrir um arquivo chamado `:`."}
:::

## Serialização das Linhas de um Arquivo

A opção `-s` processa cada arquivo de entrada em modo serial, unindo suas linhas em uma única linha de saída. Crie um arquivo com uma palavra por linha:

```bash
$ printf 'The\nquick\nbrown\nfox\n' > words.txt
$ paste -s words.txt
The	quick	brown	fox
```

Combine `-s` com `-d` para escolher o separador:

```bash
$ paste -s -d ' ' words.txt
The quick brown fox
```

Se vários arquivos forem fornecidos com `-s`, cada arquivo se tornará sua própria linha de saída.

:::single-choice{#paste-serialize-with-spaces}
Qual comando une todas as linhas de `words.txt` em uma única linha de saída separada por espaços?

::option[`paste -d ' ' words.txt`]{#paste-parallel-one-file explanation="No modo paralelo padrão, um único arquivo ainda produz uma linha de saída para cada linha de entrada. O delimitador não tem arquivos para unir."}
::option[`paste -s words.txt roles.txt`]{#paste-two-serial-files explanation="Essa forma serializa dois arquivos separadamente com a tabulação padrão, produzindo duas linhas, não o resultado solicitado."}
::option[`paste -s -d ' ' words.txt`]{#paste-serial-spaces .correct explanation="`-s` serializa as linhas do arquivo, e `-d ' '` usa um espaço entre elas."}
:::

## Tratamento de Entradas com Tamanhos Diferentes

Quando arquivos de entrada paralelos possuem números diferentes de linhas, `paste` continua até o final do arquivo mais longo. Os valores ausentes de um arquivo mais curto se tornam campos vazios:

```bash
$ printf 'A\nB\nC\n' > letters.txt
$ printf '1\n2\n' > numbers.txt
$ paste -d ':' letters.txt numbers.txt
A:1
B:2
C:
```

:::single-choice{#paste-unequal-files}
O que acontece quando um arquivo fornecido ao `paste` paralelo termina antes de outro?

::option[`paste` usa campos vazios para esse arquivo até o fim da entrada mais longa.]{#paste-empty-fields .correct explanation="O modo paralelo continua até que todos os arquivos terminem, representando como campos vazios as linhas ausentes das entradas mais curtas."}
::option[`paste` para imediatamente e descarta as linhas restantes.]{#paste-stop-shortest explanation="`paste` continua até o fim da entrada mais longa; portanto, as linhas restantes não são descartadas porque outro arquivo terminou."}
::option[`paste` repete o arquivo mais curto desde o começo.]{#paste-repeat-shorter explanation="O comando não reinicia os registros de entrada. Uma entrada esgotada contribui com campos vazios."}
:::

## Leitura de uma Entrada por stdin

Use `-` como operando de arquivo para ler essa posição de stdin:

```bash
$ printf 'admin\nviewer\n' | paste -d ':' names.txt -
alice:admin
bob:viewer
```

:::single-choice{#paste-stdin-operand}
Em `producer | paste names.txt -`, o que significa o operando `-`?

::option[Gravar o resultado mesclado em stderr.]{#paste-write-stderr explanation="Aqui, o hífen identifica uma fonte de entrada. Ele não redireciona um fluxo de saída."}
::option[Remover os delimitadores entre as duas colunas.]{#paste-remove-delimiter explanation="A seleção do delimitador é controlada por `-d`. O hífen não altera o separador."}
::option[Ler essa coluna de entrada de stdin.]{#paste-read-stdin .correct explanation="O hífen instrui `paste` a usar sua entrada padrão nessa posição de operando."}
:::

Para praticar a mesclagem de dados orientados por linhas, experimente este laboratório:

1. **[Processamento Simples de Texto](https://labex.io/labs/linux-simple-text-processing-18004)** — Aprenda a usar comandos como `tr`, `col`, `join` e `paste` para manipular e analisar dados textuais com eficiência.

## Resumo

Agora você sabe combinar entradas orientadas por linhas com alinhamento e delimitadores previsíveis.

1. Mescle linhas correspondentes de vários arquivos.
2. Substitua a tabulação padrão com `-d`.
3. Serialize as linhas de um arquivo com `-s`.
4. Interprete campos vazios provenientes de entradas mais curtas.
5. Use `-` quando uma entrada vier de stdin.
