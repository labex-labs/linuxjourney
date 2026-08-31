---
lesson_id: "vim-text-editor"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 3
title: "Vim (Vi Improved)"
description: "Aprenda o que é o Vim, sua relação com vi e como abrir arquivos, a ajuda e a prática guiada."
meta_title: "Vim (Vi Improved) - Text-Fu Avançado"
meta_description: "Conheça o Vim, o editor de texto potente e leve cujo nome significa Vi Improved. Aprenda a abrir arquivos, consultar a ajuda e praticar com segurança."
meta_keywords: "Vim, vi improved, editor texto Linux, tutorial Vim, editor Vi, Vim melhorado, comandos Linux"
---

O Vim é um editor de texto configurável cujo nome significa **Vi Improved**. Ele preserva o modelo de edição modal associado ao editor `vi` original e acrescenta recursos como desfazer em vários níveis, suporte à sintaxe, scripts e um amplo sistema de ajuda.

## Relação entre Vim e vi

`vi` descreve tanto um editor histórico quanto uma interface de comandos comum. Em um sistema Linux, `vi` pode iniciar o Vim em um modo orientado à compatibilidade; em outro, pode iniciar uma implementação diferente de vi. Não presuma que todo comando `vi` ofereça todos os recursos do Vim.

Verifique o que o shell atual resolve:

```bash
$ command -v vim
/usr/bin/vim
$ command -v vi
/usr/bin/vi
```

O caminho resolvido não identifica por si só se `vi` e `vim` são a mesma implementação. `type -a vi vim` e a saída de versão do editor podem fornecer mais detalhes.

:::single-choice{#vim-name-origin}
O que significa o nome Vim?

::option[Visual Input Manager]{#vim-visual-input explanation="Essa expressão não é a origem do nome do editor."}
::option[Virtual Interface Mode]{#vim-virtual-interface explanation="O Vim realmente usa modos, mas essa expressão não é o significado do nome."}
::option[Vi Improved]{#vim-vi-improved .correct explanation="O Vim começou como um editor aprimorado e compatível com vi, algo refletido em seu nome."}
:::

:::single-choice{#vim-check-command}
Qual comando verifica se o Bash consegue resolver o nome `vim` no momento?

::option[`vim --create`]{#vim-create-option explanation="Essa não é uma verificação de resolução do shell nem uma forma de instalar ou descobrir o Vim."}
::option[`command -v vim`]{#vim-command-resolution .correct explanation="O comando interno do shell informa qual comando seria usado para esse nome, caso esteja disponível."}
::option[`file ~/.vimrc`]{#vim-file-vimrc explanation="Esse comando examina um possível arquivo de configuração e não determina se o executável do Vim está disponível."}
:::

## Abertura do Vim e de Arquivos

Inicie o Vim com um buffer sem nome:

```bash
$ vim
```

Forneça um caminho para editar esse arquivo:

```bash
$ vim filename.txt
```

Se `filename.txt` existir e puder ser lido, o Vim carregará seu conteúdo em um buffer. Se o caminho não existir, o Vim abrirá um novo buffer associado ao nome; nenhum arquivo será criado até que você grave o buffer com sucesso.

O Vim não ignora as permissões do sistema de arquivos. Abrir um arquivo não garante que sua conta consiga salvar alterações nesse caminho.

:::single-choice{#vim-open-missing-path}
O que normalmente acontece quando `vim draft.txt` indica um caminho que ainda não existe?

::option[O Vim abre um novo buffer e só cria o arquivo quando ele é gravado.]{#vim-new-buffer .correct explanation="O caminho é lembrado para o buffer, enquanto a criação no disco é adiada até uma gravação bem-sucedida."}
::option[O Vim cria um arquivo vazio no disco antes de abrir a interface.]{#vim-immediate-create explanation="O novo buffer é associado ao caminho, mas o arquivo não é criado até uma gravação bem-sucedida."}
::option[O Vim se recusa a iniciar porque todos os caminhos precisam existir.]{#vim-refuse-missing explanation="O Vim pode abrir um novo buffer para um caminho ausente, permitindo compor um novo arquivo."}
:::

## Uso dos Recursos Integrados de Aprendizado

Se a instalação do Vim incluir `vimtutor`, execute-o no shell para uma lição prática interativa:

```bash
$ vimtutor
```

Dentro do Vim, entre no modo Normal com `Esc`, digite `:help` e pressione Enter para abrir o sistema de ajuda. Um tópico específico pode vir depois do comando:

```vim
:help user-manual
:help :write
```

As tags da ajuda são precisas; por isso, a pontuação pode importar. Use `Ctrl+]` em um link da ajuda para segui-lo e `Ctrl+T` para retornar.

:::single-choice{#vim-guided-tutorial}
Qual comando do shell inicia o tutorial guiado do Vim quando ele está instalado?

::option[`vim --quiz`]{#vim-quiz-option explanation="O Vim não usa essa opção como interface padrão de tutorial guiado."}
::option[`vimtutor`]{#vim-tutor-command .correct explanation="`vimtutor` abre uma cópia do tutorial interativo projetado para uma prática segura."}
::option[`help vim`]{#vim-shell-help explanation="O `help` do Bash documenta comandos internos do shell; ele não inicia o tutorial interativo do Vim."}
:::

## Prática com um Arquivo Descartável

Comece com um arquivo em um diretório de sua propriedade:

```bash
$ printf 'alpha\nbeta\n' > vim-practice.txt
$ vim vim-practice.txt
```

As próximas lições apresentam pesquisa, navegação, inserção, edição e salvamento. Até saber sair com segurança, lembre-se de que `Esc` retorna ao modo Normal e `:q!`, seguido de Enter, abandona as alterações não salvas da janela atual. Use esse comando apenas quando realmente quiser descartá-las.

:::single-choice{#vim-abandon-practice-changes}
Em um arquivo descartável de prática, qual comando do Vim fecha a janela atual e descarta suas alterações não salvas?

::option[`:w`]{#vim-write-only explanation="`:w` grava o buffer, mas não fecha a janela atual."}
::option[`:wq`]{#vim-write-quit explanation="`:wq` salva as alterações antes de sair; portanto, não as descarta."}
::option[`:q!`]{#vim-quit-force .correct explanation="O `!` instrui o Vim a ignorar o aviso de buffer modificado e sair sem gravar as alterações."}
:::

Para praticar a abertura, a edição e o salvamento com Vim, experimente este laboratório:

1. **[Edição de Arquivos de Texto no Linux com Vim e Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Pratique a criação, edição, gravação e navegação de arquivos com Vim e Nano em um ambiente Linux real.

## Resumo

Agora você sabe identificar o Vim, abrir um buffer e encontrar recursos seguros de aprendizado.

1. Explique a relação entre Vim e vi sem presumir uma implementação.
2. Verifique se o comando `vim` está disponível.
3. Abra um arquivo existente ou um novo buffer nomeado.
4. Inicie `vimtutor` ou abra a ajuda integrada do Vim.
5. Descarte alterações não salvas de um arquivo de prática apenas quando essa for a intenção.
