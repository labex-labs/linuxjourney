---
lesson_id: "emacs-text-editor"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 9
title: "Emacs"
description: "Aprenda a iniciar o Emacs, interpretar sua notação de teclas e diferenciar buffers, janelas e frames."
meta_title: "Emacs - Text-Fu Avançado"
meta_description: "Conheça o Emacs, um editor de texto potente e extensível para Linux. Entenda buffers, janelas, frames, notação de teclas e o uso básico."
meta_keywords: "Emacs, editor texto Linux, tutorial Emacs, buffers Emacs, comandos Linux, Emacs para iniciantes, guia"
---

O GNU Emacs é um editor de texto extensível cujo comportamento pode ser personalizado com Emacs Lisp. Ele oferece edição de texto simples, modos de programação, gerenciamento de arquivos e buffers e muitos pacotes opcionais. Você pode aprender seus comandos essenciais de edição sem adotar todas as extensões.

## Verificação e Inicialização do Emacs

Não presuma que o Emacs está instalado. Verifique como o shell o resolve:

```bash
$ command -v emacs
/usr/bin/emacs
```

Inicie o Emacs com sua seleção normal de exibição:

```bash
$ emacs
```

Em uma sessão gráfica, isso pode criar um frame gráfico. Use `-nw`, abreviação de no window system, quando o Emacs deva permanecer dentro do terminal atual:

```bash
$ emacs -nw
```

:::single-choice{#emacs-terminal-start} Qual comando inicia o Emacs dentro do terminal atual, em vez de usar um sistema gráfico de janelas?

::option[`emacs -w`]{#emacs-window-option explanation="Essa não é a forma sem sistema de janelas apresentada aqui."}
::option[`emacs -nw`]{#emacs-no-window .correct explanation="A opção `-nw` instrui o Emacs a não usar um sistema gráfico de janelas e a ser executado no terminal."}
::option[`command -v emacs`]{#emacs-check-only explanation="Esse comando verifica a resolução e não inicia o editor."}
:::

## Abertura de um Arquivo

Forneça um caminho para visitar um arquivo quando o Emacs for iniciado:

```bash
$ emacs notes.txt
```

Se o arquivo existir, o Emacs o lerá em um buffer. Se estiver ausente, criará um novo buffer associado ao caminho; o arquivo só será criado depois de um salvamento bem-sucedido. As permissões do sistema de arquivos continuam determinando se a gravação pode ter sucesso.

:::single-choice{#emacs-open-file-buffer} O que `emacs notes.txt` normalmente faz quando `notes.txt` ainda não existe?

::option[Abre um novo buffer associado a esse caminho.]{#emacs-new-file-buffer .correct explanation="O buffer pode manter o novo texto de `notes.txt`, enquanto a criação do arquivo real é adiada até o salvamento."}
::option[Cria o arquivo no disco antes de iniciar o editor.]{#emacs-immediate-file explanation="O Emacs pode associar um novo buffer ao caminho sem criar o arquivo no disco até que um salvamento tenha sucesso."}
::option[Recusa-se a iniciar porque todos os arquivos visitados precisam existir.]{#emacs-refuse-new-file explanation="O Emacs permite compor novos arquivos em buffers associados a caminhos ausentes."}
:::

## Compreensão de Buffers, Janelas e Frames

O Emacs usa objetos relacionados, mas distintos:

- Um **buffer** mantém texto ou outro estado do editor. O conteúdo de um arquivo visitado vive em um buffer.
- Uma **janela** é uma área dentro de um frame do Emacs que exibe um buffer.
- Um **frame** é uma exibição de nível superior do Emacs, como um frame gráfico ou de terminal.

Vários buffers podem existir sem estar visíveis, e duas janelas podem exibir o mesmo buffer. Fechar uma janela não necessariamente encerra seu buffer nem exclui um arquivo.

:::single-choice{#emacs-buffer-definition} O que é um buffer do Emacs?

::option[Um frame gráfico de nível superior do aplicativo.]{#emacs-buffer-frame explanation="Um frame é o objeto de exibição de nível superior; um buffer mantém conteúdo ou estado do editor."}
::option[Um objeto que mantém texto editável ou outro estado do editor.]{#emacs-buffer-content .correct explanation="O conteúdo de arquivos visitados e muitas visualizações sem arquivos vivem em buffers do Emacs."}
::option[Um arquivo de histórico do shell com comandos anteriores.]{#emacs-buffer-history explanation="O histórico do shell é separado do armazenamento dos buffers do Emacs."}
:::

## Leitura da Notação de Teclas do Emacs

A documentação do Emacs usa uma notação compacta:

- `C-x` significa manter Control pressionado e apertar `x`.
- `M-x` significa manter Meta pressionado e apertar `x`; Alt normalmente atua como Meta em terminais e áreas de trabalho modernos.
- `C-x C-f` é uma sequência: pressione Control+x e depois Control+f.

O terminal específico pode interceptar ou remapear algumas teclas. `Esc`, seguido de uma tecla, muitas vezes pode substituir uma combinação com Meta.

:::single-choice{#emacs-key-sequence-notation} Como inserir a sequência de teclas do Emacs escrita `C-x C-f`?

::option[Manter Control para `x` e depois manter Control para `f`.]{#emacs-control-x-f .correct explanation="Cada prefixo `C-` se aplica à tecla seguinte, e as duas combinações são inseridas em sequência."}
::option[Digitar os caracteres literais `C-x C-f` no buffer.]{#emacs-literal-key-text explanation="A notação descreve eventos com a tecla Control, não um texto a ser inserido."}
::option[Manter Control, `x` e `f` pressionados simultaneamente como uma única combinação.]{#emacs-simultaneous-x-f explanation="A notação contém duas combinações sucessivas, não uma combinação simultânea de três teclas."}
:::

## Inicialização do Tutorial Integrado

Dentro do Emacs, digite `C-h t` para abrir o tutorial interativo. Ele ensina movimentação, inserção, salvamento e saída em um buffer seguro de prática. `C-h` é o prefixo da ajuda; `C-h C-h` mostra ajuda sobre como usar a ajuda.

Se o Emacs exibir um menu ou buffer de boas-vindas, o tutorial ainda será um ponto de partida mais estruturado do que experimentar em um arquivo importante.

:::single-choice{#emacs-open-tutorial} Qual sequência de teclas do Emacs abre o tutorial integrado?

::option[`C-x C-s`]{#emacs-save-buffer explanation="Essa sequência salva o buffer atual; ela não abre o tutorial."}
::option[`C-x C-c`]{#emacs-exit-sequence explanation="Essa sequência inicia a saída do Emacs, não uma lição."}
::option[`C-h t`]{#emacs-help-tutorial .correct explanation="O prefixo da ajuda `C-h`, seguido de `t`, inicia o tutorial do Emacs."}
:::

## Resumo

Agora você sabe iniciar o Emacs e interpretar os conceitos fundamentais de sua interface.

1. Verifique se o comando `emacs` está disponível.
2. Escolha a operação gráfica ou no terminal com `-nw`.
3. Visite um caminho existente ou novo em um buffer.
4. Diferencie buffers, janelas e frames.
5. Leia a notação de teclas e abra o tutorial integrado.
