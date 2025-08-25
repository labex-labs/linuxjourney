---
index: 14
lang: "pt"
title: "find"
meta_title: "find - Linha de Comando"
meta_description: "Aprenda como usar o comando 'find' do Linux para localizar arquivos e diretórios. Descubra opções básicas de pesquisa e melhore suas habilidades de gerenciamento de arquivos no Linux."
meta_keywords: "comando find Linux, encontrar arquivos Linux, pesquisa de diretório Linux, tutorial comando find, gerenciamento de arquivos Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Com todos esses arquivos que temos no sistema, pode ser um pouco caótico tentar encontrar um específico. Bem, existe um comando que podemos usar para isso: `find`!

```bash
find /home -name puppies.jpg
```

Com `find`, você terá que especificar o diretório onde você estará pesquisando e o que você está procurando. Neste caso, estamos tentando encontrar um arquivo com o nome de `puppies.jpg`.

Você pode especificar o tipo de arquivo que você está tentando encontrar.

```bash
find /home -type d -name MyFolder
```

Você pode ver que eu defini o tipo de arquivo que estou tentando encontrar como `d` para diretório, e ainda estou pesquisando pelo nome de `MyFolder`.

Uma coisa legal a notar é que `find` não para no diretório que você está pesquisando; ele também procurará dentro de quaisquer subdiretórios que esse diretório possa ter.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre como encontrar arquivos e diretórios no Linux:

1. **[Comando find do Linux: Pesquisa de Arquivos](https://labex.io/pt/labs/linux-linux-find-command-file-searching-219191)** - Este laboratório fornece uma introdução ao comando `find`, um utilitário versátil para pesquisar e localizar arquivos e diretórios com base em vários critérios. Você praticará o uso de `find` para localizar arquivos específicos.
2. **[Descobrir Recursos Críticos do Sistema](https://labex.io/pt/labs/linux-discover-critical-system-resources-388032)** - Aprenda comandos essenciais do Linux para localizar arquivos e executáveis, incluindo `find`. Você praticará a navegação eficiente no sistema de arquivos e a descoberta de recursos críticos do sistema.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança no uso eficaz do comando `find`.

## Quiz Question

Qual opção devo especificar para `find` se eu quiser pesquisar por nome?

## Quiz Answer

-name
