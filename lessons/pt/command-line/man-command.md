---
lesson_id: "man-command"
course_id: "command-line"
lang: "pt"
order_index: 16
title: "man"
description: "Aprenda a abrir, navegar, pesquisar e selecionar seções das páginas de manual instaladas."
meta_title: "man - Linha de Comando"
meta_description: "Aprenda o comando man do Linux com exemplos para ler e pesquisar páginas de manual, entender suas seções e encontrar opções de comandos."
meta_keywords: "comando man, páginas man Linux, manual de comandos, man ls, seções man, pesquisar página man, ajuda linha de comando"
---

Muitos comandos, interfaces, arquivos de configuração e ferramentas administrativas do Linux possuem uma documentação de referência instalada chamada página de manual, ou página man. O comando `man` localiza e exibe essas páginas.

## Abertura de uma Página de Manual

Forneça o nome de um tópico a `man`. Por exemplo, abra a página de `ls` com:

```bash
$ man ls
```

As páginas de manual normalmente incluem uma sinopse, descrição, opções, arquivos relacionados e referências cruzadas, embora as seções exatas variem.

:::single-choice{#open-ls-manual} Qual comando abre a página de manual instalada de `ls`?

::option[`help ls`]{#help-ls explanation="O `help` do Bash documenta comandos internos do shell e normalmente não abre a página de manual do programa externo `ls`."}
::option[`man ls`]{#manual-ls-page .correct explanation="`man` procura o tópico `ls` no banco de dados de manuais e exibe a página correspondente."}
::option[`ls --help`]{#ls-usage explanation="Esse comando solicita que `ls` mostre seu próprio resumo de uso. Ele não abre a página de manual instalada."}
:::

## Navegação e Pesquisa em uma Página

Em muitos sistemas, `man` exibe as páginas por meio de um paginador como `less`. Enquanto uma página estiver aberta, você poderá rolar com as teclas de seta ou de página e usar estes controles:

Dentro de uma página man:

- Digite `/pattern` e pressione Enter para pesquisar para a frente.
- Pressione `n` para repetir a pesquisa na mesma direção.
- Pressione `N` para repeti-la na direção oposta.
- Pressione `q` para sair.

O paginador pode variar conforme o sistema ou ambiente; por isso, suas teclas exatas não são garantidas em todos os lugares. Os controles acima se aplicam à configuração comum com `less`.

:::single-choice{#search-man-page} Com uma página man aberta em `less`, o que inicia uma pesquisa para a frente por `--recursive`?

::option[Digitar `?--recursive` e pressionar Enter.]{#backward-man-search explanation="Um ponto de interrogação inicia uma pesquisa para trás. Ele procura na direção oposta à solicitada."}
::option[Digitar `/--recursive` e pressionar Enter.]{#forward-man-search .correct explanation="Uma barra inicia uma pesquisa para a frente em `less`, e Enter envia o padrão."}
::option[Digitar `n--recursive` e pressionar Enter.]{#repeat-man-search explanation="A tecla `n` repete uma pesquisa existente. Ela não introduz um novo padrão dessa maneira."}
:::

:::single-choice{#leave-man-page} Com uma página man aberta no paginador usual, qual tecla retorna ao shell?

::option[`G`]{#man-page-end explanation="`G` maiúsculo leva ao final da página em `less`. Ele não fecha o paginador."}
::option[`n`]{#next-man-match explanation="A tecla `n` repete a pesquisa mais recente. Ela mantém a página de manual aberta."}
::option[`q`]{#quit-man .correct explanation="A tecla `q` encerra o paginador comum e devolve o controle ao shell."}
:::

## Seleção de uma Seção do Manual

O manual é organizado em seções numeradas. Algumas seções comuns são:

- `1`: comandos de usuário.
- `2`: chamadas de sistema.
- `3`: funções de biblioteca.
- `5`: formatos de arquivos.
- `8`: comandos de administração do sistema.

O mesmo tópico pode aparecer em mais de uma seção. Coloque a seção antes do tópico para selecionar uma explicitamente:

```bash
$ man 5 passwd
$ man 1 passwd
```

O primeiro comando abre a página do formato de arquivo `passwd` na seção 5. O segundo abre a página do comando de usuário na seção 1. Referências como `passwd(5)` usam a mesma notação `tópico(seção)`.

:::single-choice{#open-passwd-file-format} Qual comando abre a página da seção 5 que documenta o formato do arquivo `passwd`?

::option[`man passwd 5`]{#section-after-topic explanation="Nessa forma do comando, o seletor da seção deve vir antes do tópico. Essa ordem não solicita `passwd(5)`."}
::option[`man 5 passwd`]{#passwd-format-page .correct explanation="Colocar a seção `5` antes de `passwd` seleciona especificamente a página do formato de arquivo."}
::option[`man 1 passwd`]{#passwd-command-page explanation="A seção 1 contém comandos de usuário; portanto, essa forma seleciona a página do comando `passwd`, não a do formato de arquivo."}
:::

## Quando uma Página Está Ausente

Nem todo nome de comando possui uma página de manual instalada separadamente. Se `man` informar que não existe uma entrada:

- Execute `type NAME` para descobrir como o Bash resolve o nome.
- Use `help NAME` quando for um comando interno do Bash.
- Tente `NAME --help` quando um programa externo aceitar essa convenção.
- Verifique se a distribuição oferece um pacote separado de documentação.

:::single-choice{#missing-builtin-manual} `type cd` informa que `cd` é um comando interno do Bash e não há uma página man separada. Qual comando você deve tentar em seguida?

::option[`whatis cd`]{#whatis-missing-cd explanation="`whatis` resume entradas do banco de dados de manuais. Ele não pode fornecer uma página dedicada ausente para o comando interno."}
::option[`file cd`]{#file-cd-name explanation="`file` classifica objetos do sistema de arquivos, mas neste caso `cd` é resolvido como comando interno, não como caminho."}
::option[`help cd`]{#builtin-cd-help .correct explanation="O comando interno `help` do Bash fornece a documentação do próprio shell para `cd`."}
:::

## Resumo

Agora você sabe localizar e percorrer a documentação de manual instalada.

1. Abra uma página pelo nome do tópico.
2. Pesquise e navegue por uma página no paginador usual.
3. Feche o paginador e retorne ao shell.
4. Selecione uma seção numerada do manual.
5. Escolha outra fonte de ajuda quando uma página não estiver disponível.
