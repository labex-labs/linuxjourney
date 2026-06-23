---
index: 18
lang: "pt"
title: "alias"
meta_title: "alias - Linha de Comando"
meta_description: "Aprenda o comando alias no Linux com exemplos para criar aliases temporários, salvar aliases no .bashrc, listar aliases e removê-los com unalias."
meta_keywords: "comando alias linux, comando alias, alias bash, alias .bashrc, comando unalias, atalho de comando linux, alias shell"
---

## Lesson Content

Digitar comandos longos ou repetitivos pode ser cansativo. Um alias é um atalho do shell que permite definir um nome personalizado para um comando ou sequência de comandos.

### Criando um Alias Temporário

Para criar um alias temporário que dura apenas para a sessão atual do terminal, basta especificar um nome e defini-lo igual à string do comando.

Por exemplo, crie um alias chamado `ll` para `ls -la`:

```bash
$ alias ll='ls -la'
```

Agora, ao invés de digitar `ls -la`, você pode simplesmente digitar `ll`, e ele executará o mesmo comando. Esta é uma forma simples, mas poderosa, de personalizar seu shell.

### Tornando um Alias Permanente

Um alias temporário desaparece assim que você fecha o terminal ou reinicia o sistema. Para tornar um `alias de comando no linux` permanente, você precisa adicioná-lo ao arquivo de configuração do seu shell. Para o shell Bash, este arquivo é tipicamente `~/.bashrc`.

1. Abra o arquivo em um editor de texto: `nano ~/.bashrc`
2. Adicione sua definição de alias no arquivo, exatamente como você digitou na linha de comando:

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. Salve o arquivo e saia do editor.

Para que as mudanças tenham efeito, você deve fechar e reabrir o terminal ou pedir ao shell para recarregar o arquivo de configuração usando o comando `source`:

```bash
$ source ~/.bashrc
```

Seu alias agora estará disponível toda vez que você iniciar uma nova sessão Bash.

### Removendo um Alias

Se você não precisar mais de um alias, pode removê-lo com o comando `unalias`. Isso o removerá da sessão atual.

```bash
$ unalias ll
```

Para remover um alias permanente, você também deve deletar sua definição do arquivo `~/.bashrc`.

### Listando Aliases Existentes

Execute `alias` sem argumentos para listar os aliases no seu shell atual.

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

Use `type` para ver o que será executado quando você digitar um comando:

```bash
$ type ll
ll is aliased to 'ls -la'
```

### Exemplos Úteis de Alias

```bash
$ alias la='ls -la'
$ alias ..='cd ..'
$ alias grep='grep --color=auto'
```

Mantenha os aliases curtos e previsíveis. Evite substituir comandos destrutivos por comportamentos inesperados, a menos que tenha certeza absoluta.

### Perguntas Comuns

**Aliases funcionam em scripts?** Geralmente não, por padrão. Scripts devem usar comandos completos ou funções.

**Onde os aliases do Bash devem ser colocados?** Coloque-os em `~/.bashrc` para sessões interativas do Bash.

**E se um alias conflitar com um comando real?** O alias geralmente tem prioridade no uso interativo do shell. Use `command nome` ou `\nome` para ignorar um alias.

## Exercise

Embora não existam laboratórios específicos para este tópico, recomendamos explorar o abrangente [Linux Learning Path](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual comando é usado para criar um alias? Por favor, responda em inglês minúsculo.

## Quiz Answer

alias
