---
lesson_id: "touch-command"
course_id: "command-line"
lang: "pt"
order_index: 5
title: "touch"
description: "Aprenda a criar arquivos vazios e gerenciar os carimbos de data e hora com o comando touch."
meta_title: "touch - Linha de Comando"
meta_description: "Aprenda o comando touch do Linux com exemplos para criar arquivos vazios, atualizar datas, definir horários, usar arquivos de referência e evitar a criação de arquivos."
meta_keywords: "comando touch Linux, comando touch, criar arquivo Linux, atualizar data de arquivo Linux, touch -d, touch -r, touch -c"
---

O comando `touch` altera os carimbos de data e hora dos arquivos. Ele também é usado com frequência para criar um ou mais arquivos vazios.

A sintaxe básica é:

```bash
touch [OPTIONS] FILE...
```

## Criação de Arquivos Vazios

Se o arquivo indicado não existir, `touch` o criará como um arquivo vazio:

```bash
$ touch mysuperduperfile
```

Você pode criar vários arquivos em um único comando listando cada nome:

```bash
$ touch file1.txt file2.txt file3.log
```

Isso é útil para criar marcadores de posição, mas `touch` não adiciona texto a um arquivo. Use um editor de texto ou outro comando destinado à gravação de conteúdo quando precisar de um arquivo não vazio.

:::single-choice{#create-several-empty-files} Qual comando cria três arquivos vazios chamados `one`, `two` e `three`, caso ainda não existam?

::option[`touch "one two three"`]{#touch-one-spaced explanation="As aspas transformam o texto em um único nome de arquivo com espaços. Esse comando se refere a um arquivo, não a três."}
::option[`mkdir one two three`]{#mkdir-three explanation="`mkdir` cria diretórios, não arquivos comuns vazios. Use `touch` para os arquivos solicitados."}
::option[`touch one two three`]{#touch-three .correct explanation="`touch` aceita vários operandos de arquivo. Ele cria cada arquivo ausente sem adicionar conteúdo."}
:::

## Atualização dos Carimbos de Data e Hora

Os arquivos registram vários carimbos de data e hora. Por padrão, executar `touch` em um arquivo existente altera tanto a hora de acesso quanto a de modificação para o momento atual. O conteúdo do arquivo permanece inalterado.

Você pode comparar a hora de modificação exibida antes e depois da execução:

```bash
$ ls -l mysuperduperfile
$ touch mysuperduperfile
$ ls -l mysuperduperfile
```

A saída de `ls -l` normalmente mostra a hora de modificação, não a hora de acesso.

:::single-choice{#touch-existing-file} O que acontece ao executar `touch report.txt` quando `report.txt` já existe?

::option[Seus carimbos de data e hora são atualizados sem substituir o conteúdo.]{#timestamps-only .correct explanation="Por padrão, `touch` atualiza as horas de acesso e modificação de um arquivo existente. Ele não sobrescreve os dados."}
::option[Seu conteúdo é excluído e o arquivo se torna vazio.]{#contents-deleted explanation="A criação de um arquivo vazio é o comportamento para um arquivo ausente. Um arquivo existente preserva o conteúdo quando `touch` atualiza seus horários."}
::option[O comando falha porque o nome do arquivo já está em uso.]{#existing-error explanation="`touch` foi projetado para atuar tanto em arquivos existentes quanto ausentes. Um nome existente não é um erro por si só."}
:::

## Controle do Carimbo Alterado

Use `-a` para alterar apenas a hora de acesso ou `-m` para alterar apenas a hora de modificação:

```bash
$ touch -a notes.txt
$ touch -m notes.txt
```

:::single-choice{#change-modification-time-only} Qual comando atualiza apenas a hora de modificação de `notes.txt`?

::option[`touch -a notes.txt`]{#access-only explanation="A opção `-a` altera somente a hora de acesso. Ela não seleciona a hora de modificação solicitada."}
::option[`touch -m notes.txt`]{#modification-only .correct explanation="A opção `-m` restringe a alteração à hora de modificação. A hora de acesso permanece inalterada."}
::option[`touch -c notes.txt`]{#no-create explanation="A opção `-c` controla se um arquivo ausente será criado. Ela não limita a atualização a um único carimbo."}
:::

## Definição ou Cópia de um Horário

A opção `-d` aceita uma expressão de data em vez de usar o horário atual:

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

Para atribuir a um arquivo as mesmas horas de acesso e modificação de um arquivo de referência, use `-r`:

```bash
$ touch -r file1.txt file2.txt
```

Aqui, `file1.txt` fornece os horários e `file2.txt` é o arquivo alterado. A opção `-t` é outra maneira de fornecer um horário, usando um formato numérico compacto.

:::single-choice{#copy-reference-timestamps} Qual comando copia os carimbos de data e hora de `source.txt` para `target.txt`?

::option[`touch -r source.txt target.txt`]{#reference-source .correct explanation="Com `-r`, o operando seguinte é o arquivo de referência e o último é o arquivo cujos horários serão atualizados."}
::option[`touch -r target.txt source.txt`]{#reference-target explanation="Esse comando inverte as funções dos arquivos. Ele usaria `target.txt` como referência e atualizaria `source.txt`."}
::option[`touch -d source.txt target.txt`]{#date-source explanation="A opção `-d` espera uma expressão de data, não o nome de um arquivo de referência. Use `-r` para copiar horários de outro arquivo."}
:::

## Como Evitar a Criação de Arquivos

Normalmente, `touch` cria um arquivo quando o caminho indicado não existe. Acrescente `-c` quando quiser atualizar um arquivo somente se ele já existir:

```bash
$ touch -c existing-file.txt
```

Se `existing-file.txt` estiver ausente, esse comando não o criará. Esse comportamento pode ser útil em scripts que devem atualizar um horário sem introduzir um novo arquivo.

:::single-choice{#update-without-creating} Qual comando atualiza `status.log` se ele existir, mas não o cria se estiver ausente?

::option[`touch -a status.log`]{#touch-access explanation="A opção `-a` seleciona a hora de acesso, mas um arquivo ausente ainda pode ser criado. Ela não oferece o comportamento solicitado."}
::option[`touch -m status.log`]{#touch-modification explanation="A opção `-m` seleciona a hora de modificação, mas não impede a criação de um arquivo ausente. Use `-c` para essa condição."}
::option[`touch -c status.log`]{#touch-no-create .correct explanation="A opção `-c` impede a criação de um arquivo ausente. Um arquivo existente ainda pode ter seus horários atualizados."}
:::

## Resumo

Agora você sabe usar `touch` para criar arquivos vazios e controlar seus carimbos de data e hora.

1. Crie um ou mais arquivos vazios.
2. Atualize horários sem alterar o conteúdo dos arquivos.
3. Selecione a hora de acesso ou a hora de modificação.
4. Defina um horário específico ou copie os horários de um arquivo de referência.
5. Impeça a criação de um arquivo ausente.
