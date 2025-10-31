---
index: 18
lang: "pt"
title: "alias"
meta_title: "alias - Linha de Comando"
meta_description: "Aprenda a criar e gerenciar um alias de comando no Linux para otimizar seu fluxo de trabalho. Este guia aborda a criação de aliases temporários e permanentes usando o comando alias e o arquivo .bashrc."
meta_keywords: "alias linux, comando alias linux, alias de comando no linux, alias de comando linux, alias bash, comando unalias, .bashrc, linha de comando, tutorial linux"
---

## Lesson Content

Digitar comandos longos ou repetitivos pode ser cansativo. Felizmente, você pode criar um atalho, ou um **alias do Linux**, para tornar sua experiência na linha de comando mais eficiente. O comando `alias` permite que você defina um nome personalizado para qualquer comando ou sequência de comandos.

### Criando um Alias Temporário

Para criar um alias temporário que dure apenas para sua sessão de terminal atual, você simplesmente especifica um nome e o define como igual à string do comando.

Por exemplo, para criar um alias chamado `ll` para o comando `ls -la`, você usaria a sintaxe do `alias command linux` desta forma:

```bash
alias ll='ls -la'
```

Agora, em vez de digitar `ls -la`, você pode simplesmente digitar `ll`, e ele executará o mesmo comando. Esta é uma maneira simples, mas poderosa, de personalizar seu shell.

### Tornando um Alias Permanente

Um alias temporário desaparecerá assim que você fechar o terminal ou reiniciar o sistema. Para tornar um `command alias in linux` permanente, você precisa adicioná-lo ao arquivo de configuração do seu shell. Para o shell Bash, este arquivo é tipicamente `~/.bashrc`.

1. Abra o arquivo em um editor de texto: `nano ~/.bashrc`
2. Adicione sua definição de alias ao arquivo, exatamente como você a digitou na linha de comando:

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. Salve o arquivo e saia do editor.

Para que as alterações entrem em vigor, você deve fechar e reabrir seu terminal ou instruir o shell a recarregar o arquivo de configuração usando o comando `source`:

```bash
source ~/.bashrc
```

Seu **linux command alias** agora estará disponível toda vez que você iniciar uma nova sessão de terminal.

### Removendo um Alias

Se você não precisar mais de um alias, pode removê-lo com o comando `unalias`. Isso o removerá da sua sessão atual.

```bash
unalias ll
```

Para remover um alias permanente, você também deve excluir sua definição do seu arquivo `~/.bashrc`.

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar a abrangente [Trilha de Aprendizagem do Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual comando é usado para criar um alias? Por favor, responda em inglês minúsculo.

## Quiz Answer

alias
