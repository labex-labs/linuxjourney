---
index: 11
lang: "pt"
title: "juntar e dividir"
meta_title: "juntar e dividir - Text-Fu"
meta_description: "Domine o uso dos comandos Linux join e split. Aprenda a juntar arquivos eficientemente com base em campos comuns e dividir arquivos grandes em partes menores. Este guia aborda qual comando usar para juntar arquivos como cat, dog, cow e outros exemplos práticos."
meta_keywords: "linux juntar arquivos, qual comando usar para juntar arquivos, comando join linux, comando split linux, manipulação de arquivos, linha de comando, processamento de texto"
---

## Lesson Content

No Linux, gerenciar e manipular arquivos de texto é uma tarefa comum. Dois utilitários poderosos para isso são `join` e `split`. O comando `join` mescla linhas de dois arquivos com base em um campo comum, enquanto `split` divide um arquivo grande em pedaços menores e mais gerenciáveis.

### Juntando Arquivos por um Campo Comum

O comando `join` é uma ferramenta fundamental quando você precisa **linux join files** (juntar arquivos linux). Por padrão, ele combina linhas de dois arquivos ordenados com base no primeiro campo idêntico.

Por exemplo, imagine que você tem dois arquivos que deseja mesclar:

```plaintext
file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue
```

Usando o comando `join`, você pode combiná-los facilmente:

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Como você pode ver, os arquivos foram unidos usando o primeiro campo comum (1, 2, 3). Para que o `join` funcione corretamente, os campos de junção em ambos os arquivos devem estar ordenados.

### Especificando Campos de Junção Diferentes

E se o campo comum não for a primeira coluna? Você pode dizer ao `join` quais campos usar. Considere estes arquivos:

```plaintext
file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
```

Aqui, precisamos juntar no segundo campo de `file1.txt` e no primeiro campo de `file2.txt`. O comando seria:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

A flag `-1 2` especifica o campo 2 do primeiro arquivo, e `-2 1` especifica o campo 1 do segundo arquivo.

### Dividindo Arquivos Grandes

O comando `split` faz o oposto de juntar; ele divide um arquivo grande em arquivos menores.

```bash
$ split somefile
```

Por padrão, este comando divide `somefile` em novos arquivos assim que um limite de 1000 linhas é atingido. Os arquivos de saída são nomeados `xaa`, `xab`, e assim por diante. Você pode personalizar esse comportamento, por exemplo, especificando uma contagem de linhas diferente com a flag `-l` ou dividindo por tamanho de arquivo com a flag `-b`.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre junção e manipulação de arquivos de texto:

1. **[Comando Linux join: Junção de Arquivos](https://labex.io/pt/labs/linux-linux-join-command-file-joining-219193)** - Este laboratório oferece uma introdução prática e direta ao comando `join`, permitindo que você pratique a mesclagem de linhas de dois arquivos de texto ordenados com base em um campo comum, assim como discutido na lição.
2. **[Processamento de Dados de Funcionários](https://labex.io/pt/labs/linux-processing-employees-data-388132)** - Aplique seu conhecimento de `join` e outras poderosas utilidades de linha de comando Linux, como `awk`, para combinar e processar dados de múltiplas fontes, simulando um cenário de análise de dados do mundo real.
3. **[Controle de Sequência e Pipeline](https://labex.io/pt/labs/linux-sequence-control-and-pipeline-17994)** - Aumente sua eficiência na linha de comando e suas habilidades de manipulação de dados aprendendo a controlar sequências de execução de comandos, utilizar pipelines e aproveitar ferramentas poderosas de processamento de texto, o que complementa as capacidades de combinação de dados do `join`.

Estes laboratórios ajudarão você a aplicar os conceitos de manipulação de arquivos de texto e combinação de dados em cenários reais e a construir confiança com as ferramentas de linha de comando do Linux.

## Quiz Question

Qual comando você usaria para juntar arquivos chamados `cat`, `dog`, `cow`? Por favor, forneça o comando completo em inglês. O comando e os nomes dos arquivos devem estar em minúsculas.

## Quiz Answer

join cat dog cow
