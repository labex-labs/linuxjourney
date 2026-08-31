---
lesson_id: "vim-saving-and-exiting"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 8
title: "Salvamento e Saída no Vim"
description: "Aprenda a gravar, sair, salvar com outro nome ou descartar conscientemente as alterações de um buffer do Vim."
meta_title: "Salvamento e Saída no Vim - Text-Fu Avançado"
meta_description: "Aprenda a salvar no Vim com :w, salvar e sair com :wq ou ZZ e descartar alterações conscientemente com :q!."
meta_keywords: "como salvar Vim, wq Linux, vi gravar e sair, salvar e sair Vim, salvar arquivo Vim, sair Vim, comandos Vim"
---

Gravar e sair são operações separadas no Vim. Antes de inserir um comando Ex, pressione `Esc` para retornar ao modo Normal, digite `:`, insira o comando e pressione Enter. Leia a mensagem de status ou erro do Vim antes de presumir que uma gravação teve sucesso.

## Gravação do Buffer Atual

Use `:w` para gravar o buffer atual em seu arquivo associado sem fechar a janela:

```vim
:w
```

Uma gravação pode falhar porque o buffer não possui nome, o diretório não permite gravação, o sistema de arquivos está cheio ou outra condição impede a operação. Verifique a mensagem informada pelo Vim.

Use `:w copy.txt` para gravar o buffer atual em outro caminho, mantendo o nome atual do buffer. Use `:saveas copy.txt` quando o buffer deva adotar o novo caminho.

:::single-choice{#vim-save-without-quit}
Qual comando do Vim grava o buffer atual no arquivo associado sem sair?

::option[`:q`]{#vim-save-q explanation="`:q` solicita a saída e não grava um buffer modificado."}
::option[`:w`]{#vim-save-w .correct explanation="O comando `:write` salva o buffer atual e mantém a janela de edição aberta."}
::option[`:q!`]{#vim-save-q-force explanation="`:q!` abandona as alterações não salvas e sai; ele não as grava."}
:::

## Saída de um Buffer sem Alterações

Use `:q` para fechar a janela atual quando isso não abandonar alterações não salvas do buffer:

```vim
:q
```

Se o buffer atual estiver modificado e suas alterações forem perdidas, o Vim normalmente se recusará e mostrará um aviso. Essa salvaguarda oferece a oportunidade de gravar ou reconsiderar.

:::single-choice{#vim-quit-clean-buffer}
Qual comando fecha a janela atual do Vim quando nenhuma alteração não salva seria perdida?

::option[`:w`]{#vim-quit-w explanation="Esse comando grava o buffer, mas mantém a janela atual aberta."}
::option[`:q`]{#vim-quit-q .correct explanation="O comando comum de saída fecha a janela quando as salvaguardas de buffer modificado do Vim permitem."}
::option[`u`]{#vim-quit-u explanation="`u` do modo Normal desfaz uma alteração e não fecha a janela do editor."}
:::

## Descarte de Alterações Não Salvas

Use `:q!` apenas quando quiser intencionalmente fechar a janela atual e abandonar as alterações que impediriam a saída:

```vim
:q!
```

O ponto de exclamação ignora o aviso de alterações não salvas. Essas mudanças do buffer não serão gravadas; portanto, confirme que são realmente descartáveis antes de pressionar Enter.

:::single-choice{#vim-quit-discard-changes}
O buffer atual possui alterações que você conscientemente não quer salvar. Qual comando fecha a janela e as abandona?

::option[`:q`]{#vim-discard-plain-q explanation="`:q` simples normalmente se recusa a sair quando isso perderia alterações de um buffer modificado."}
::option[`:wq`]{#vim-discard-wq explanation="`:wq` grava as alterações antes de sair, o oposto de descartá-las."}
::option[`:q!`]{#vim-discard-q-force .correct explanation="O ponto de exclamação ignora o aviso de modificação e fecha sem gravar as alterações."}
:::

## Gravação e Saída em Conjunto

Use `:wq` quando o buffer deva ser gravado e a janela atual fechada depois de uma gravação bem-sucedida:

```vim
:wq
```

Se a gravação falhar, o Vim não concluirá a saída solicitada. Resolva o erro em vez de presumir que os dados chegaram ao disco.

:::single-choice{#vim-write-and-quit}
Qual comando grava o buffer atual e fecha a janela se a gravação tiver sucesso?

::option[`:wq`]{#vim-save-wq .correct explanation="Esse comando combina uma gravação com uma saída, e a saída depende do sucesso da gravação."}
::option[`:q!`]{#vim-save-force-quit explanation="Esse comando sai descartando as alterações, não as gravando."}
::option[`:w copy.txt`]{#vim-save-copy explanation="Esse comando grava outro caminho, mas mantém a janela de edição aberta."}
:::

## Uso de :x e ZZ

`:x` grava o buffer somente se ele estiver modificado e depois sai. No modo Normal, `ZZ` maiúsculo realiza o mesmo comportamento:

```vim
:x
```

```text
ZZ
```

Isso é ligeiramente diferente de `:wq`, que solicita uma gravação mesmo quando o buffer não foi alterado. `ZQ` maiúsculo é a contraparte do modo Normal para sair sem gravar, semelhante a `:q!`.

:::single-choice{#vim-write-if-modified-quit}
Qual comando do modo Normal grava apenas quando o buffer está modificado e depois sai?

::option[`ZZ`]{#vim-save-zz .correct explanation="`ZZ` maiúsculo realiza o comportamento de gravar se modificado e sair associado a `:x`."}
::option[`zz`]{#vim-center-screen explanation="`zz` minúsculo centraliza a linha atual na janela; ele não salva nem sai."}
::option[`ZQ`]{#vim-quit-zq explanation="`ZQ` maiúsculo sai sem gravar; portanto, descarta alterações não salvas em vez de salvá-las."}
:::

Quando várias janelas ou buffers estão envolvidos, um comando pode fechar apenas a janela atual. Comandos como `:qa`, `:wqa` e `:qa!` atuam em todas as janelas, mas examine todos os buffers modificados antes de usar um comando forçado global.

Para praticar a gravação e a saída em um arquivo descartável, experimente este laboratório:

1. **[Edição de Arquivos de Texto no Linux com Vim e Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Pratique a criação de arquivos, a edição de texto, o salvamento de arquivos e a navegação tanto com Vim quanto com Nano. Este laboratório consolidará sua compreensão das operações básicas do Vim, inclusive como salvar e sair.

## Resumo

Agora você sabe escolher um comando de saída do Vim de acordo com sua intenção para os dados não salvos.

1. Grave sem sair com `:w`.
2. Saia com segurança usando `:q` quando nenhuma alteração for perdida.
3. Descarte alterações conscientemente com `:q!`.
4. Grave e saia com `:wq`.
5. Use `:x` ou `ZZ` para gravar somente se houver modificações.
