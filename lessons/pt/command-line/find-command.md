---
lang: "pt"
title: "find"
meta_description: "Aprenda a usar o comando 'find' do Linux para localizar arquivos e diretórios. Descubra opções básicas de pesquisa e melhore suas habilidades de gerenciamento de arquivos Linux."
meta_keywords: "comando find Linux, encontrar arquivos Linux, pesquisa de diretório Linux, tutorial do comando find, gerenciamento de arquivos Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Com todos esses arquivos que temos no sistema, pode ser um pouco caótico tentar encontrar um específico. Bem, existe um comando que podemos usar para isso: `find`!

```bash
find /home -name puppies.jpg
```

Com `find`, você terá que especificar o diretório onde você estará procurando e o que você está procurando. Neste caso, estamos tentando encontrar um arquivo com o nome de `puppies.jpg`.

Você pode especificar o tipo de arquivo que você está tentando encontrar.

```bash
find /home -type d -name MyFolder
```

Você pode ver que eu defini o tipo de arquivo que estou tentando encontrar como `d` para diretório, e ainda estou procurando pelo nome de `MyFolder`.

Uma coisa legal a notar é que `find` não para no diretório que você está procurando; ele também procurará dentro de quaisquer subdiretórios que esse diretório possa ter.

## Exercise

1. Encontre um arquivo a partir do diretório raiz que contenha a palavra "net".

## Quiz Question

Qual opção devo especificar para `find` se eu quiser pesquisar por nome?

## Quiz Answer

-name
