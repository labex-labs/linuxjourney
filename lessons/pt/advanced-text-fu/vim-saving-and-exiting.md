---
index: 8
lang: "pt"
title: "Salvar e Sair no Vim"
meta_title: "Vim Salvar e Sair - Domínio Avançado de Texto"
meta_description: "Aprenda a salvar no editor Vim usando comandos como :w. Domine como salvar e sair com :wq ou ZZ. Este guia cobre os comandos essenciais linux wq e vi write and quit para gerenciamento eficiente de arquivos no Vim."
meta_keywords: "vim como salvar, linux wq, vi escrever e sair, vim como salvar e sair, como salvar no editor vim, salvar arquivo vim, sair vim, comandos vim"
---

## Lesson Content

Depois de terminar de editar um arquivo, o próximo passo é salvar suas alterações e sair do editor. O Vim oferece vários comandos para esse fim, cada um com uma função específica. Todos esses comandos são executados no modo de Linha de Comando, que você pode acessar pressionando `:`.

### Como Salvar no Editor Vim

Para salvar as alterações que você fez em um arquivo sem sair, você usa o comando de escrita (write). Esta é a resposta fundamental para a pergunta "vim como salvar".

- `:w` - Escreve (salva) o estado atual do arquivo no disco.

### Saindo do Vim

Se você deseja sair do editor, você tem algumas opções dependendo se deseja salvar suas alterações ou não.

- `:q` - Sai do editor. Este comando só funciona se você não tiver alterações não salvas.
- `:q!` - Sai do editor e descarta quaisquer alterações não salvas. Isso é útil quando você cometeu erros e deseja reverter para a última versão salva do arquivo.

### Vim Como Salvar e Sair

Combinar salvar e sair é um fluxo de trabalho muito comum. O comando `linux wq` é um pilar para muitos desenvolvedores que trabalham na linha de comando.

- `:wq` - Este comando primeiro escreve (salva) o arquivo e depois sai. É uma ação dois em um para eficiência. Muitos usuários procuram por `vi write and quit` (vi escrever e sair), e este comando funciona tanto para Vi quanto para Vim.
- `ZZ` - Este é um atalho equivalente a `:wq`. Ele salva o arquivo se ele foi modificado e então sai. É um caractere mais rápido de digitar e um favorito entre os usuários experientes do Vim.

### Desfazendo e Refazendo Alterações

Durante a edição, você pode precisar reverter uma ação ou trazê-la de volta. Esses comandos são usados no modo Normal (pressione `Esc` para entrar).

- `u` - Desfaz sua última ação.
- `Ctrl-r` - Refaz a última ação que você desfez.

Dominar esses comandos básicos é o primeiro passo para a proficiência no Vim. À medida que você se sentir mais à vontade, descobrirá que essas operações se tornam automáticas. Para recursos mais avançados, a documentação oficial do Vim é um excelente recurso.

## Exercise

Para dominar esses comandos, a prática manual é essencial. O laboratório a seguir fornece um cenário do mundo real para ajudá-lo a reforçar suas habilidades de edição de texto no Vim.

1. **[Editar Arquivos de Texto no Linux com Vim e Nano](https://labex.io/pt/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Pratique a criação de arquivos, edição de texto, salvamento de arquivos e navegação com Vim e Nano. Este laboratório solidificará sua compreensão das operações básicas do Vim, incluindo como salvar e sair.

Concluir este laboratório o ajudará a aplicar esses conceitos e a construir confiança com a edição de texto em um ambiente Linux.

## Quiz Question

Como você sai do Vim sem salvar suas alterações? Por favor, forneça o comando exato em inglês, prestando atenção a maiúsculas/minúsculas e caracteres especiais.

## Quiz Answer

:q
