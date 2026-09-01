---
lesson_id: "text-editors-vim-or-emacs"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 2
title: "Editores de Texto"
description: "Aprenda a escolher e configurar um editor de texto de terminal para administração e desenvolvimento no Linux."
meta_title: "Editores de Texto - Text-Fu Avançado"
meta_description: "Conheça editores de texto do Linux como Vim e Emacs, seus modelos de interação e como escolher uma opção segura para trabalhar no terminal."
meta_keywords: "editores de texto Linux, Vim, Emacs, comandos Linux, tutorial Linux, Linux para iniciantes, guia Linux"
---

Configurações, scripts, código-fonte e logs do Linux costumam ser armazenados como texto simples. Um editor de terminal permite trabalhar nesses arquivos em um terminal local, uma sessão SSH remota ou um ambiente sem área de trabalho gráfica.

## Escolha de um Editor para o Ambiente

Nenhum editor é o melhor para todas as pessoas ou tarefas. Editores gráficos, editores de terminal e ambientes integrados de desenvolvimento podem ser adequados. Para o trabalho na linha de comando, escolha um editor instalado, do qual você saiba sair com segurança e cujo modelo básico de edição compreenda.

Não presuma que Vim ou Emacs esteja instalado. Verifique a resolução dos comandos no shell atual:

```bash
$ command -v vim
/usr/bin/vim
$ command -v emacs
/usr/bin/emacs
```

Um resultado vazio com status diferente de zero significa que o nome não foi encontrado pela pesquisa de comandos atual. Sistemas mínimos podem fornecer `vi`, enquanto outros incluem Nano ou nenhum editor interativo.

:::single-choice{#editors-check-availability} Qual comando verifica se o shell atual consegue resolver um executável chamado `vim`?

::option[`vim --install`]{#editors-vim-install explanation="O Vim não usa esse comando como verificação portável de instalação, e a instalação de pacotes depende da distribuição."}
::option[`file ~/.vimrc`]{#editors-file-vimrc explanation="Esse comando classifica um caminho de configuração se ele existir; não determina se `vim` pode ser resolvido."}
::option[`command -v vim`]{#editors-command-v-vim .correct explanation="O comando interno do shell verifica a resolução e mostra a forma resolvida quando ela está disponível."}
:::

## Compreensão do Modelo do Vim

O Vim é um editor modal. A mesma tecla pode ter significados diferentes conforme o modo atual:

- O modo Normal interpreta as teclas como comandos de navegação e edição.
- O modo de Inserção insere o texto digitado.
- O modo de Linha de Comando aceita comandos como gravar ou sair.

Esse modelo torna a edição repetitiva pelo teclado eficiente depois de alguma prática, mas novos usuários precisam acompanhar o modo ativo. As próximas lições apresentam uma operação do Vim por vez.

:::single-choice{#editors-vim-modal-meaning} O que significa dizer que o Vim é modal?

::option[Cada arquivo é aberto em uma janela gráfica separada.]{#editors-vim-windows explanation="Janelas e buffers são conceitos separados. Modal se refere à mudança do comportamento das teclas conforme o estado do editor."}
::option[O Vim só pode editar um tipo de arquivo de texto por vez.]{#editors-vim-file-type explanation="O Vim aceita muitos tipos de arquivo. A palavra modal descreve seu modelo de interação, não uma restrição de arquivos."}
::option[As teclas realizam ações diferentes conforme o modo ativo.]{#editors-vim-modes .correct explanation="Por exemplo, uma tecla pode emitir um comando no modo Normal e inserir texto no modo de Inserção."}
:::

## Compreensão do Modelo do Emacs

O Emacs normalmente usa combinações de teclas e comandos nomeados dentro de um ambiente extensível. Os arquivos são visitados em buffers, e modos principais e secundários personalizam o comportamento para diferentes conteúdos e tarefas. O Emacs pode ser executado em um terminal ou em um frame gráfico.

Tanto Vim quanto Emacs permitem muito mais que a edição básica por meio de configurações e extensões. Comece abrindo, alterando, salvando e fechando um arquivo de texto simples antes de acrescentar personalizações.

:::single-choice{#editors-emacs-buffer} Na terminologia do Emacs, onde o texto editável de um arquivo visitado normalmente é mantido?

::option[Em um buffer.]{#editors-emacs-buffer-answer .correct explanation="O Emacs visita um arquivo em um buffer, que mantém o texto visualizado ou editado."}
::option[Na tabela de aliases do shell.]{#editors-emacs-alias-table explanation="Aliases pertencem à resolução de comandos do shell e não armazenam o texto do editor."}
::option[Apenas no histórico de rolagem do terminal.]{#editors-emacs-scrollback explanation="O histórico de rolagem registra a saída exibida, enquanto o Emacs gerencia o texto editável em buffers."}
:::

## Definição de um Editor Preferido

Muitos programas de linha de comando consultam `VISUAL` ou `EDITOR` quando precisam iniciar um editor. Por exemplo, escolha o Vim para comandos iniciados pela sessão atual do Bash e seus filhos:

```bash
$ export VISUAL=vim
$ export EDITOR="$VISUAL"
```

Essas variáveis expressam uma preferência; elas não instalam o programa. Use um comando que realmente exista e coloque as exportações no arquivo de inicialização adequado somente depois de testá-las.

:::single-choice{#editors-editor-variable} O que `export EDITOR=vim` faz?

::option[Informa aos futuros processos filhos que `vim` é o valor do editor preferido.]{#editors-export-preference .correct explanation="A exportação coloca a preferência no ambiente herdado pelos comandos iniciados pelo shell atual."}
::option[Instala o Vim para todos os usuários do sistema.]{#editors-install-vim explanation="A atribuição de uma variável de ambiente não instala pacotes nem altera os sistemas de outros usuários."}
::option[Faz todos os programas obedecerem às teclas do Vim.]{#editors-global-bindings explanation="Os programas podem consultar a variável para iniciar um editor, mas ela não substitui seus próprios modelos de interação."}
:::

## Prática sem Arriscar Arquivos Importantes

Aprenda usando um arquivo descartável em um diretório de sua propriedade:

```bash
$ printf 'first line\nsecond line\n' > editor-practice.txt
$ vim editor-practice.txt
```

Evite começar com configurações do sistema ou dados de outro usuário. Faça um backup antes de alterar um arquivo importante, entenda como salvar e sair e examine o resultado com um comando somente para leitura, como `cat` ou `diff`.

:::single-choice{#editors-first-practice-file} Qual é o arquivo inicial mais seguro para praticar com um editor desconhecido?

::option[Um arquivo crítico de configuração da inicialização aberto como root.]{#editors-boot-file explanation="Uma alteração acidental pode impedir a inicialização normal, e o acesso elevado aumenta o impacto dos erros."}
::option[Um arquivo de texto descartável em um diretório de sua propriedade.]{#editors-disposable-file .correct explanation="Um arquivo de prática limita as consequências de edições acidentais enquanto você aprende a navegar, salvar e sair."}
::option[Um arquivo compartilhado de produção sem backup.]{#editors-production-file explanation="Praticar sem revisão em dados compartilhados pode prejudicar outras pessoas e não oferece uma recuperação simples."}
:::

Para praticar a abertura, a edição e o salvamento de arquivos de texto no terminal, experimente este laboratório:

1. **[Edição de Arquivos de Texto no Linux com Vim e Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Pratique a criação, edição e gravação de arquivos e a navegação tanto com vi/vim quanto com nano.

## Resumo

Agora você sabe escolher um editor de terminal e preparar um fluxo seguro de prática.

1. Verifique se o comando de um editor está disponível.
2. Reconheça o modelo modal de interação do Vim.
3. Reconheça os buffers e modos extensíveis do Emacs.
4. Defina uma preferência de editor sem confundi-la com instalação.
5. Pratique em texto descartável antes de editar arquivos importantes.
