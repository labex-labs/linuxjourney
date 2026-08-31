---
lesson_id: "find-command"
course_id: "command-line"
lang: "pt"
order_index: 14
title: "find"
description: "Aprenda a pesquisar árvores de diretórios por nome, tipo, tamanho e data e a agir sobre correspondências verificadas."
meta_title: "find - Linha de Comando"
meta_description: "Aprenda o comando find do Linux com exemplos para pesquisar por nome, tipo, tamanho e data de modificação e executar ações nos arquivos encontrados."
meta_keywords: "comando find Linux, comando find, encontrar arquivos Linux, pesquisar por nome, pesquisar por tipo, pesquisar por tamanho, find mtime, find exec"
---

O comando `find` percorre uma árvore de diretórios e testa cada entrada segundo critérios como nome, tipo, tamanho ou data de modificação.

## Escolha de Onde Pesquisar

A sintaxe básica é:

```bash
find [PATH] [EXPRESSION]
```

O caminho escolhe o ponto inicial, e a expressão seleciona ou atua nas entradas abaixo dele.

Este comando pesquisa `/home` e seus descendentes em busca de entradas chamadas `puppies.jpg`:

```bash
$ find /home -name puppies.jpg
```

A recursão é o comportamento padrão. Use `.` como caminho inicial para pesquisar a árvore do diretório atual.

:::single-choice{#search-current-tree}
Qual comando pesquisa o diretório atual e seus descendentes por entradas chamadas `notes.txt`?

::option[`find . -name notes.txt`]{#find-current-notes .correct explanation="O ponto seleciona o diretório atual como caminho inicial, e `-name` testa o nome-base de cada entrada."}
::option[`find / -name notes.txt`]{#find-root-notes explanation="Um caminho inicial `/` pesquisa a partir da raiz do sistema de arquivos, uma área muito mais ampla que a árvore do diretório atual."}
::option[`find notes.txt .`]{#find-operands-reversed explanation="`find` espera os caminhos iniciais antes da expressão. Essa ordem não representa a pesquisa solicitada."}
:::

## Correspondência de Nomes e Tipos

O teste `-name` aceita um nome-base exato ou um padrão no estilo do shell. Coloque padrões curingas entre aspas para que o shell atual os forneça inalterados a `find`:

```bash
$ find . -name "*.txt"
```

Sem as aspas, o shell pode expandir `*.txt` no diretório atual antes que `find` seja iniciado. Use `-iname` no lugar de `-name` quando a correspondência não deva diferenciar maiúsculas de minúsculas.

Acrescente `-type d` para selecionar diretórios ou `-type f` para selecionar arquivos comuns:

```bash
$ find /home -type d -name MyFolder
```

Os dois testes precisam ser verdadeiros: a entrada deve ser um diretório e seu nome-base deve ser `MyFolder`.

:::single-choice{#find-text-regular-files}
Qual comando encontra arquivos comuns cujos nomes terminam em `.txt` abaixo do diretório atual?

::option[`find . -type f -name "*.txt"`]{#text-files .correct explanation="`-type f` seleciona arquivos comuns, enquanto o padrão de `-name` entre aspas é avaliado por `find` para cada entrada."}
::option[`find . -type d -name "*.txt"`]{#text-directories explanation="O padrão está corretamente entre aspas, mas `-type d` seleciona diretórios, não arquivos comuns."}
::option[`find . -type f -name *.txt`]{#unquoted-text-files explanation="O curinga sem aspas pode ser expandido pelo shell atual antes da execução de `find`, alterando a expressão pretendida."}
:::

## Correspondência por Tamanho e Data de Modificação

Use `-size` com `+` para tamanhos maiores que a unidade indicada ou `-` para menores:

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

Aqui, `M` maiúsculo representa unidades de 1.048.576 bytes, enquanto `k` minúsculo representa unidades de 1.024 bytes. `find` arredonda os tamanhos para cima na unidade escolhida antes de aplicar a comparação numérica; portanto, o comportamento nos limites se baseia nessas unidades.

Use `-mtime` para testar a quantidade de períodos completos de 24 horas desde a modificação do arquivo:

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` corresponde a um valor menor que 7, enquanto `-mtime +30` corresponde a um valor maior que 30. Como são usados períodos completos de 24 horas, esses testes não se baseiam na virada do dia do calendário.

:::single-choice{#find-recent-regular-files}
Qual comando encontra arquivos comuns abaixo de `.` cuja idade de modificação é inferior a sete períodos completos de 24 horas?

::option[`find . -type f -mtime -7`]{#recent-files .correct explanation="`-type f` seleciona arquivos comuns, e `-mtime -7` seleciona idades de modificação inferiores a sete períodos completos de 24 horas."}
::option[`find . -type f -mtime +7`]{#older-than-seven explanation="O sinal de adição seleciona idades maiores que sete unidades. Ele procura arquivos mais antigos, não recentes."}
::option[`find . -type d -mtime -7`]{#recent-directories explanation="O teste de tempo seleciona itens recentes, mas `-type d` restringe os resultados a diretórios, não arquivos comuns."}
:::

## Exibição e Ações sobre as Correspondências

Se nenhuma ação for fornecida, o GNU `find` exibe os caminhos correspondentes. Você pode escrever `-print` explicitamente para deixar clara a ação da expressão:

Exiba as correspondências explicitamente:

```bash
$ find . -name "*.log" -print
```

Use `-exec` para executar outro comando nas correspondências:

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

Na forma com `\;`, `{}` é substituído por um caminho correspondente em cada invocação do comando. O ponto e vírgula encerra a ação `-exec` e recebe uma barra invertida para que o shell o forneça a `find`.

Antes de usar uma ação destrutiva como `-delete` ou um comando `-exec` que altere arquivos, execute os mesmos testes com `-print` e inspecione todos os resultados. Um caminho inicial mais restrito e `-maxdepth N` também podem limitar a pesquisa.

:::single-choice{#verify-before-delete}
Você está desenvolvendo um comando `find` que talvez exclua arquivos `.log` antigos mais tarde. O que deve fazer primeiro?

::option[Acrescentar `-delete` imediatamente e verificar quais arquivos desaparecem.]{#delete-first explanation="A exclusão não é uma visualização segura e não possui um recurso integrado para desfazer. Verifique todo o conjunto antes de acrescentá-la."}
::option[Executar os mesmos testes com `-print` e inspecionar cada correspondência.]{#print-first .correct explanation="Uma listagem somente para leitura verifica o caminho inicial e os testes antes da introdução de uma ação destrutiva."}
::option[Pesquisar a partir de `/` para que o comando não deixe de encontrar nenhum arquivo de log.]{#root-first explanation="Começar em `/` amplia o escopo e pode incluir caminhos não relacionados ou protegidos. Use o ponto inicial adequado mais restrito."}
:::

:::single-choice{#run-ls-for-each-match}
Em `find . -name "*.log" -exec ls -l {} \;`, o que `{}` representa?

::option[O caminho correspondente atual fornecido a `ls -l`.]{#match-placeholder .correct explanation="Nessa forma de `-exec`, `find` substitui `{}` pela correspondência atual antes de invocar `ls -l`."}
::option[O diretório em que o comando `find` foi iniciado.]{#starting-placeholder explanation="O diretório inicial é o ponto perto do começo do comando. As chaves têm outra função dentro de `-exec`."}
::option[O ponto e vírgula que encerra a expressão `-exec`.]{#terminator-placeholder explanation="O ponto e vírgula com escape encerra a ação `-exec`. As chaves são o marcador de posição do caminho."}
:::

Mensagens de permissão negada normalmente indicam que a conta atual não consegue pesquisar parte da árvore. Prefira um caminho inicial mais restrito e relevante; não acrescente privilégios elevados sem compreender e pretender o acesso ampliado.

Para praticar a criação de expressões de pesquisa, experimente estes laboratórios:

1. **[Comando find do Linux: Pesquisa de Arquivos](https://labex.io/labs/linux-linux-find-command-file-searching-219191)** — Este laboratório apresenta o comando `find`, uma ferramenta versátil para pesquisar e localizar arquivos e diretórios com base em vários critérios. Você praticará o uso de `find` para localizar arquivos específicos.
2. **[Descoberta de Recursos Críticos do Sistema](https://labex.io/labs/linux-discover-critical-system-resources-388032)** — Aprenda comandos essenciais para localizar arquivos e executáveis, inclusive `find`, e pratique a navegação eficiente pelo sistema de arquivos.

## Resumo

Agora você sabe criar expressões `find` específicas e verificar os resultados antes de agir.

1. Escolha o caminho inicial útil mais restrito.
2. Coloque padrões de nome entre aspas e combine-os com testes de tipo.
3. Filtre por tamanho ou períodos completos de 24 horas desde a modificação.
4. Limite a profundidade da recursão quando apropriado.
5. Exiba e inspecione as correspondências antes de ações destrutivas.
