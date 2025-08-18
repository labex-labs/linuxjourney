---
lang: "pt"
title: "cut"
meta_description: "Aprenda como usar o comando `cut` do Linux para extrair texto de arquivos. Este tutorial para iniciantes aborda o corte de caracteres e campos. Melhore suas habilidades de processamento de texto no Linux!"
meta_keywords: "comando cut, processamento de texto Linux, extrair texto, tutorial Linux, Linux para iniciantes, exemplos de cut, guia Linux"
---

## Lesson Content

Vamos aprender alguns comandos úteis que você pode usar para processar texto. Antes de começarmos, vamos criar um arquivo com o qual trabalharemos. Copie e cole o seguinte comando; depois de fazer isso, adicione um TAB entre "lazy" e "dog" (segure Ctrl-v + TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

O primeiro comando que aprenderemos é o comando `cut`. Ele extrai partes de texto de um arquivo.

Para extrair conteúdo por uma lista de caracteres:

```bash
cut -c 5 sample.txt
```

Isso exibe o 5º caractere em cada linha do arquivo. Neste caso, é "q"; observe que o espaço também conta como um caractere.

Para extrair o conteúdo por um campo, precisaremos fazer uma pequena modificação:

```bash
cut -f 2 sample.txt
```

A flag `-f` ou field corta o texto com base em campos. Por padrão, ele usa TABs como delimitadores, então tudo separado por um TAB é considerado um campo. Você deve ver "dog" como sua saída.

Você pode combinar a flag de campo com a flag de delimitador para extrair o conteúdo por um delimitador personalizado:

```bash
cut -f 1 -d ";" sample.txt
```

Isso mudará o delimitador TAB para um delimitador ";", e como estamos cortando o primeiro campo, o resultado deve ser "The quick brown".

## Exercise

O que o seguinte comando faz? Por quê?

```bash
cut -c 5-10 sample.txt
cut -c 5- sample.txt
cut -c -5 sample.txt
```

## Quiz Question

Qual comando você usaria para obter o primeiro caractere de cada linha em um arquivo?

## Quiz Answer

cut -c 1
