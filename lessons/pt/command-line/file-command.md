---
lesson_id: "file-command"
course_id: "command-line"
lang: "pt"
order_index: 6
title: "file"
description: "Aprenda a identificar o provável tipo de conteúdo de um arquivo sem depender do nome ou da extensão."
meta_title: "file - Linha de Comando"
meta_description: "Aprenda o comando file do Linux com exemplos para identificar arquivos de texto, imagens, scripts, arquivos compactados, binários e tipos MIME."
meta_keywords: "comando file Linux, comando file, identificar tipo de arquivo Linux, tipo MIME Linux, arquivo de texto, arquivo binário, arquivo compactado"
---

Na lição anterior, você usou `touch` para criar um arquivo sem acrescentar uma extensão. No Linux, os nomes dos arquivos não precisam descrever seu conteúdo: um arquivo chamado `funny.gif` não é necessariamente uma imagem GIF.

Use o comando `file` para inspecionar um arquivo e informar seu provável tipo:

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

## Por que as Extensões Não São Suficientes

As ferramentas do Linux normalmente não exigem uma extensão para determinar o tipo de um arquivo. Um script de shell pode se chamar `backup`, um arquivo de texto pode se chamar `README` e uma imagem pode ter uma extensão enganosa. O comando `file` examina propriedades como metadados do sistema de arquivos e padrões reconhecíveis no conteúdo.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

O resultado é uma classificação, não uma garantia. Um arquivo incomum, incompleto ou danificado pode receber uma descrição abrangente, como `data`, em vez de um tipo preciso.

:::single-choice{#identify-misleading-extension} Um arquivo chamado `report.jpg` pode não conter uma imagem. Qual comando verifica seu provável tipo de conteúdo?

::option[`ls report.jpg`]{#list-report explanation="`ls` confirma a existência do nome e pode mostrar metadados, mas não classifica o conteúdo do arquivo."}
::option[`file report.jpg`]{#inspect-report .correct explanation="O comando `file` examina o arquivo e informa um provável tipo. Ele não depende apenas do sufixo `.jpg`."}
::option[`touch report.jpg`]{#touch-report explanation="`touch` atualiza horários ou cria um arquivo ausente. Ele não identifica o tipo de conteúdo."}
:::

## Verificação de Vários Arquivos

Você pode verificar vários arquivos de uma só vez:

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

Também é possível fornecer um curinga do shell. O shell expande `*` para os nomes correspondentes antes que `file` os examine:

```bash
$ file *
```

:::single-choice{#inspect-multiple-files} Qual comando solicita que `file` inspecione todos os nomes não ocultos correspondentes a `*` no diretório atual?

::option[`file *`]{#file-wildcard .correct explanation="O shell expande `*` para os nomes não ocultos correspondentes, e `file` inspeciona cada operando resultante."}
::option[`file .`]{#file-current-directory explanation="Um único ponto representa o próprio diretório atual. Esse comando classifica o diretório, não cada entrada dentro dele."}
::option[`file -b`]{#file-brief-no-operand explanation="A opção `-b` muda a formatação da saída, mas esse comando não fornece os arquivos que devem ser inspecionados."}
:::

## Exibição de Informações MIME

A opção `-i` mostra informações no estilo MIME, incluindo um tipo de mídia e, quando disponível, um conjunto de caracteres. Essa forma é útil quando outro programa espera valores como `text/html`.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

:::single-choice{#show-mime-information} Qual comando informa dados no estilo MIME para `index.html`?

::option[`file -b index.html`]{#brief-index explanation="A opção `-b` omite o nome do arquivo na descrição comum. Ela não solicita especificamente a saída no estilo MIME."}
::option[`file -i index.html`]{#mime-index .correct explanation="A opção `-i` solicita a saída no estilo MIME, como `text/html` junto com informações do conjunto de caracteres."}
::option[`file -L index.html`]{#follow-index explanation="A opção `-L` controla o tratamento de links simbólicos. Ela não seleciona o formato de saída MIME."}
:::

## Opções Úteis de file

- `-i`: mostra informações no estilo MIME.
- `-b`: usa o modo breve e omite o nome do arquivo na saída.
- `-L`: segue links simbólicos e classifica seus destinos.
- `-z`: tenta examinar o conteúdo de arquivos compactados.

Por exemplo:

```bash
$ file -b notes.txt
ASCII text
```

:::single-choice{#omit-filename-from-output} Qual comando classifica `notes.txt`, mas omite seu nome na saída?

::option[`file -i notes.txt`]{#mime-notes explanation="A opção `-i` solicita informações no estilo MIME. Normalmente, a saída ainda inclui o nome do arquivo."}
::option[`file -z notes.txt`]{#compressed-notes explanation="A opção `-z` pede que `file` examine dados compactados quando possível. Ela não ativa a saída breve."}
::option[`file -b notes.txt`]{#brief-notes .correct explanation="O modo breve, selecionado com `-b`, mostra a classificação sem o prefixo com o nome do arquivo."}
:::

## Resumo

Agora você sabe usar `file` para investigar o que um arquivo provavelmente contém.

1. Classifique um arquivo sem confiar em sua extensão.
2. Inspecione vários caminhos em um único comando.
3. Solicite informações no estilo MIME.
4. Ajuste o tratamento de links, dados compactados e rótulos de saída.
