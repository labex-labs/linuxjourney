---
lesson_id: "less-command"
course_id: "command-line"
lang: "pt"
order_index: 8
title: "less"
description: "Aprenda a navegar, pesquisar e acompanhar arquivos de texto longos de forma interativa com less."
meta_title: "less - Linha de Comando"
meta_description: "Aprenda o comando less do Linux com exemplos para visualizar arquivos grandes, rolar, pesquisar, saltar entre linhas, acompanhar logs e sair do programa."
meta_keywords: "comando less, less Linux, visualizar arquivo grande Linux, pesquisar no less, sair do less, less -N, less +F, visualizador de texto Linux"
---

Quando um arquivo de texto é longo demais para uma única tela, `less` permite lê-lo sem enviar o arquivo inteiro pela rolagem do terminal. Seu nome inspirou a antiga piada do Unix “less is more”, pois `more` é outro paginador.

## Abertura de um Arquivo

Inicie o paginador fornecendo um nome de arquivo:

```bash
$ less /home/pete/Documents/text1
```

Enquanto `less` estiver ativo, as teclas controlarão o paginador em vez de iniciar comandos comuns do shell. Você retornará ao shell quando sair do paginador.

:::single-choice{#open-long-file} Qual comando abre `/var/log/syslog` em um paginador interativo?

::option[`less /var/log/syslog`]{#page-log .correct explanation="`less` abre o arquivo em um paginador para que você possa percorrê-lo, pesquisá-lo e voltar ao shell."}
::option[`cat /var/log/syslog`]{#print-log explanation="`cat` envia o arquivo inteiro à saída padrão de uma vez. Ele não oferece controles interativos de paginação."}
::option[`file /var/log/syslog`]{#classify-log explanation="`file` informa um provável tipo de conteúdo. Ele não abre o log para leitura interativa."}
:::

## Navegação no less

Use estas teclas enquanto o paginador estiver aberto:

- Use `Seta para cima`, `Seta para baixo`, `Page Up` e `Page Down` para avançar por linhas ou telas.
- Pressione `g` para ir ao início.
- Pressione `G` para ir ao final.
- Pressione `u` para subir meia tela ou `d` para descer meia tela.
- Pressione `h` para abrir a ajuda integrada.

:::single-choice{#jump-to-file-end} Qual tecla leva diretamente ao final de um arquivo no `less`?

::option[`g`]{#lowercase-g explanation="`g` minúsculo leva ao início do arquivo. A forma maiúscula segue na direção oposta."}
::option[`G`]{#uppercase-g .correct explanation="`G` maiúsculo leva ao final da entrada. O comando diferencia maiúsculas de minúsculas."}
::option[`h`]{#help-key explanation="A tecla `h` abre a ajuda do paginador. Ela não leva ao final do arquivo."}
:::

## Pesquisa no less

Digite `/`, seguido de um padrão, e pressione Enter para pesquisar para a frente. Comece com `?` para pesquisar para trás.

- `/search_term`: pesquisa `search_term` para a frente.
- `?search_term`: pesquisa `search_term` para trás.
- `n`: repete a pesquisa na mesma direção.
- `N`: repete a pesquisa na direção oposta.

:::single-choice{#repeat-search-direction} Depois de uma pesquisa para a frente por `error`, qual tecla repete a pesquisa na mesma direção?

::option[`n`]{#same-search .correct explanation="`n` minúsculo repete a pesquisa mais recente em sua direção original. Neste caso, a direção é para a frente."}
::option[`N`]{#opposite-search explanation="`N` maiúsculo repete a pesquisa mais recente na direção oposta. Depois de uma pesquisa para a frente, ele percorre os resultados para trás."}
::option[`g`]{#search-to-start explanation="A tecla `g` leva ao início da entrada. Ela não repete uma pesquisa."}
:::

## Saída do less

Pressione `q` para sair de `less` e retornar ao prompt do shell.

:::single-choice{#quit-less} Qual tecla encerra `less` e retorna ao shell?

::option[`q`]{#less-quit .correct explanation="O comando `q` encerra o paginador e restaura o prompt do shell."}
::option[`h`]{#less-help explanation="A tecla `h` abre a ajuda dentro de `less`. Ela não retorna diretamente ao shell."}
::option[`G`]{#less-end explanation="`G` maiúsculo leva ao final da entrada. O paginador continua aberto."}
:::

## Inicialização do less com Opções

Opções e comandos iniciais podem mudar a forma como o paginador começa:

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`: mostra números de linha.
- `+G`: abre no final do arquivo.
- `+F`: acompanha o novo conteúdo conforme ele é acrescentado, de modo semelhante a `tail -f`.

Ao acompanhar um arquivo com `+F`, pressione `Ctrl+C` para interromper o acompanhamento e voltar à navegação normal; depois, pressione `q` para sair. Use `-i` para pesquisas que ignorem maiúsculas e minúsculas, a menos que o padrão contenha uma letra maiúscula, ou `-I` para ignorá-las independentemente do padrão.

Os comandos também podem enviar sua saída por um pipe para `less`:

```bash
$ dmesg | less
```

:::single-choice{#follow-growing-log} Qual comando abre `/var/log/syslog` e acompanha o novo conteúdo conforme ele chega?

::option[`less +F /var/log/syslog`]{#follow-log .correct explanation="O comando inicial `+F` entra no modo de acompanhamento, fazendo `less` exibir o novo conteúdo acrescentado ao log."}
::option[`less +G /var/log/syslog`]{#open-at-log-end explanation="O comando inicial `+G` abre no final, mas não continua acompanhando o conteúdo que chegar depois."}
::option[`less -N /var/log/syslog`]{#number-log-lines explanation="A opção `-N` exibe os números das linhas. Ela não ativa o acompanhamento contínuo."}
:::

Para praticar paginação, pesquisa e leitura de textos do sistema, experimente estes laboratórios:

1. **[Comando less do Linux: Paginação de Arquivos](https://labex.io/labs/linux-linux-less-command-file-paging-214301)** — Aprenda a usar `less` para visualizar e percorrer arquivos de texto com eficiência, incluindo pesquisa, números de linha e correspondência de padrões.
2. **[Visualização de Arquivos de Log e Configuração no Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** — Aprenda habilidades essenciais para visualizar e percorrer arquivos de texto, inclusive logs e configurações do sistema, usando comandos como `cat`, `more` e `less`.

## Resumo

Agora você sabe usar `less` para inspecionar arquivos longos sem inundar o terminal.

1. Abra um arquivo ou a saída de um comando encaminhada ao paginador.
2. Navegue até partes específicas da entrada.
3. Pesquise para a frente ou para trás e repita uma pesquisa.
4. Mostre números de linha ou acompanhe conteúdo crescente.
5. Saia com segurança e retorne ao shell.
