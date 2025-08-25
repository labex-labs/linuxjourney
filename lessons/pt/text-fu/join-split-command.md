---
index: 11
lang: "pt"
title: "join e split"
meta_title: "join e split - Text-Fu"
meta_description: "Aprenda a usar os comandos 'join' e 'split' do Linux para manipulação de arquivos. Entenda como combinar arquivos por campos comuns e dividir arquivos grandes de forma eficiente. Obtenha exemplos práticos e dicas."
meta_keywords: "comando join Linux, comando split Linux, manipulação de arquivos, tutorial Linux, linha de comando, Linux para iniciantes, guia Linux"
---

## Lesson Content

O comando `join` permite que você junte vários arquivos por um campo comum:

Digamos que eu tivesse dois arquivos que eu queria juntar:

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

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Veja como ele juntou meus arquivos? Eles são unidos pelo primeiro campo por padrão, e os campos precisam ser idênticos. Se não forem, você pode classificá-los. Neste caso, os arquivos são unidos via 1, 2, 3.

Como faríamos para juntar os seguintes arquivos?

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

Para juntar este arquivo, você precisa especificar quais campos você está juntando. Neste caso, queremos o campo 2 em `file1.txt` e o campo 1 em `file2.txt`, então o comando ficaria assim:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1` refere-se a `file1.txt` e `-2` refere-se a `file2.txt`. Muito legal. Você também pode dividir um arquivo em diferentes arquivos com o comando `split`:

```bash
split somefile
```

Isso o dividirá em diferentes arquivos. Por padrão, ele os dividirá assim que atingirem um limite de 1000 linhas. Os arquivos são nomeados `x**` por padrão.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre como juntar e manipular arquivos de texto:

1. **[Comando Linux join: Junção de Arquivos](https://labex.io/pt/labs/linux-linux-join-command-file-joining-219193)** - Este laboratório oferece uma introdução direta e prática ao comando `join`, permitindo que você pratique a fusão de linhas de dois arquivos de texto classificados com base em um campo comum, exatamente como discutido na lição.
2. **[Processando Dados de Funcionários](https://labex.io/pt/labs/linux-processing-employees-data-388132)** - Aplique seu conhecimento de `join` e outros poderosos utilitários de linha de comando Linux como `awk` para combinar e processar dados de múltiplas fontes, simulando um cenário de análise de dados do mundo real.
3. **[Controle de Sequência e Pipeline](https://labex.io/pt/labs/linux-sequence-control-and-pipeline-17994)** - Aprimore sua eficiência na linha de comando e suas habilidades de manipulação de dados aprendendo a controlar sequências de execução de comandos, utilizar pipelines e aproveitar ferramentas poderosas de processamento de texto, o que complementa as capacidades de combinação de dados do `join`.

Esses laboratórios o ajudarão a aplicar os conceitos de manipulação de arquivos de texto e combinação de dados em cenários reais e a construir confiança com as ferramentas de linha de comando do Linux.

## Quiz Question

Qual comando você usaria para juntar arquivos chamados `cat`, `dog`, `cow`?

## Quiz Answer

join cat dog cow
