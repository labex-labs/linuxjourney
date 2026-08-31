---
lesson_id: "history-command"
course_id: "command-line"
lang: "pt"
order_index: 9
title: "history"
description: "Aprenda a inspecionar, pesquisar, reutilizar e gerenciar o histórico de comandos no Bash."
meta_title: "history - Linha de Comando"
meta_description: "Aprenda o comando history do Linux com exemplos para visualizar e executar comandos anteriores, fazer pesquisa reversa, excluir entradas e limpar o terminal."
meta_keywords: "comando history Linux, histórico Bash, history -c, history -d, history -w, Ctrl-R, histórico de comandos, comando clear"
---

Shells interativos podem manter um registro dos comandos digitados. Esta lição se concentra no Bash, em que o comando interno `history` exibe e gerencia esse registro. Outros shells podem usar atalhos, arquivos ou configurações diferentes.

## Visualização do Histórico do Bash

Execute `history` para exibir a lista atual:

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

Cada linha possui um número de histórico seguido do comando.

:::single-choice{#show-command-history}
Qual comando do Bash exibe a lista atual numerada do histórico?

::option[`clear`]{#clear-display explanation="`clear` atualiza a área visível do terminal. Ele não exibe os comandos anteriores."}
::option[`history -w`]{#write-history explanation="`history -w` grava a lista atual no arquivo de histórico. Sua finalidade é salvar, não exibir a lista."}
::option[`history`]{#show-history .correct explanation="O comando interno `history` mostra os comandos da lista atual, normalmente acompanhados de seus números."}
:::

## Reutilização de Comandos Anteriores

O Bash oferece vários atalhos para recuperar ou executar comandos imediatamente:

- **Seta para cima**: recupera comandos anteriores para revisão ou edição.
- **`!!`**: expande e executa o comando mais recente.
- **Executar pelo número**: use `!102` para executar o comando número 102 do histórico.
- **Executar pelo prefixo**: use `!cat` para executar o comando mais recente que começou com `cat`.

As formas de expansão do histórico iniciadas por `!` podem executar um comando assim que você pressiona Enter. Inspecione a correspondência primeiro sempre que houver dúvida, especialmente antes de acrescentar privilégios elevados ou operar em arquivos importantes.

:::single-choice{#repeat-most-recent-command}
Qual expansão do histórico do Bash repete o comando executado mais recentemente?

::option[`!102`]{#event-number explanation="Essa expansão seleciona o comando com o número 102 no histórico. Essa entrada não é necessariamente a mais recente."}
::option[`!cat`]{#event-prefix explanation="Essa forma seleciona o comando mais recente cujo texto começa com `cat`. Ela não representa o comando mais recente de qualquer tipo."}
::option[`!!`]{#previous-event .correct explanation="No Bash, `!!` se expande para o comando anterior e o executa depois que você envia a linha."}
:::

## Pesquisa Interativa no Histórico

Pressione `Ctrl+R` para iniciar uma pesquisa incremental reversa e digite parte do comando desejado. Pressione `Ctrl+R` novamente para ir a uma correspondência mais antiga.

Pressione Enter para executar a correspondência exibida. Se quiser revisá-la ou editá-la primeiro, use uma tecla de seta para colocar o comando na linha de edição.

:::single-choice{#search-before-executing}
Você se lembra de parte de um comando anterior do Bash e quer encontrá-lo interativamente. O que deve pressionar primeiro?

::option[`Ctrl+D`]{#end-input explanation="`Ctrl+D` sinaliza o fim da entrada em muitos contextos do terminal e pode encerrar um shell ocioso. Ele não inicia uma pesquisa no histórico."}
::option[`Ctrl+C`]{#cancel-input explanation="`Ctrl+C` normalmente interrompe ou cancela a operação atual. Ele não pesquisa no histórico de comandos."}
::option[`Ctrl+R`]{#reverse-search .correct explanation="`Ctrl+R` inicia uma pesquisa incremental reversa no histórico. Digitar mais caracteres restringe a correspondência."}
:::

## Gerenciamento da Lista de Histórico

O comando interno `history` pode modificar ou salvar a lista atual:

- `history -c`: limpa a lista atual do histórico na memória.
- `history -w`: grava a lista atual no arquivo de histórico configurado, geralmente `~/.bash_history`.
- `history -d <offset>`: exclui a entrada na posição indicada.

Exemplos:

```bash
$ history -d 101
$ history -w
```

Limpar a lista na memória não garante, por si só, que os comandos antigos tenham desaparecido de todos os arquivos, backups ou outros shells ativos. O comportamento do histórico também depende das configurações do Bash e do momento em que as sessões leem ou gravam seus arquivos.

:::single-choice{#save-current-history-list}
Qual comando grava a lista atual do histórico do Bash em seu arquivo configurado?

::option[`history -c`]{#clear-current-list explanation="A opção `-c` limpa a lista na memória. Ela não solicita que a lista atual seja salva."}
::option[`history -d 101`]{#delete-one-entry explanation="A opção `-d` remove uma entrada selecionada do histórico. Ela não salva a lista completa."}
::option[`history -w`]{#write-current-list .correct explanation="A opção `-w` grava a lista atual do histórico no arquivo configurado."}
:::

## Limpeza da Tela e Conclusão de Nomes

Use `clear` quando quiser uma área visível limpa no terminal:

```bash
$ clear
```

Esse comando não apaga a lista do histórico do Bash. Dependendo do terminal, o conteúdo antigo da tela também pode continuar disponível no histórico de rolagem.

A conclusão com Tab é outra forma de evitar redigitação. Comece a digitar um comando, nome de arquivo ou diretório e pressione Tab. O Bash pode completar uma correspondência inequívoca ou mostrar as possibilidades quando houver mais de uma.

As linhas de comando podem ser armazenadas no histórico; portanto, não coloque senhas, tokens ou outros segredos diretamente nos comandos quando houver um método de entrada mais seguro.

:::single-choice{#distinguish-clear-from-history-clear}
Você quer atualizar a área visível do terminal sem excluir o histórico de comandos na memória. Qual comando deve executar?

::option[`clear`]{#clear-visible-area .correct explanation="`clear` atualiza a área visível do terminal e preserva a lista do histórico do Bash na memória."}
::option[`history -c`]{#clear-memory explanation="Esse comando remove as entradas da lista atual na memória. Ele altera o histórico, em vez de apenas atualizar a tela."}
::option[`history -d 1`]{#delete-first-entry explanation="Esse comando pede ao Bash para excluir uma entrada selecionada do histórico. Ele não limpa a área visível do terminal."}
:::

## Resumo

Agora você sabe localizar e reutilizar comandos do Bash, além de gerenciar o histórico conscientemente.

1. Exiba a lista atual numerada do histórico.
2. Recupere ou expanda um comando anterior com cuidado.
3. Pesquise interativamente no histórico com `Ctrl+R`.
4. Exclua, limpe ou grave entradas do histórico.
5. Diferencie o histórico de comandos da exibição do terminal.
