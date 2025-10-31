---
index: 10
lang: "pt"
title: "cp (Copiar)"
meta_title: "cp (Copiar) - Linha de Comando"
meta_description: "Domine o comando cp do Linux para copiar arquivos e diretórios. Este guia abrange opções essenciais como cópia recursiva (-r), preservação de atributos com a flag cp -p e sobrescrita forçada com a flag cp -f. Aprenda como cp -p no Linux ajuda a manter metadados de arquivos."
meta_keywords: "comando cp, copiar arquivos linux, linux cp -p, flag cp -p, cp -p no linux, flag cp -f, cópia recursiva, cp -r, curingas linux, linha de comando linux"
---

## Lesson Content

O comando `cp` é a ferramenta padrão para copiar arquivos e diretórios no Linux. Sua sintaxe básica é `cp [ORIGEM] [DESTINO]`.

### Cópia Básica de Arquivos

Para copiar um arquivo, você especifica o arquivo de origem e o diretório ou caminho de destino.

```bash
cp meuarquivolegal /home/pete/Documents/documentoslegais
```

Neste exemplo, `meuarquivolegal` é o arquivo de origem, e `/home/pete/Documents/documentoslegais` é o diretório de destino. Você também pode copiar um arquivo e dar-lhe um novo nome no destino.

```bash
cp meuarquivolegal /home/pete/Documents/meuarquivolegal_backup
```

### Usando Curingas para Cópia em Massa

Curingas (wildcards) são caracteres especiais que ajudam você a selecionar vários arquivos com base em padrões, oferecendo grande flexibilidade.

- `*`: Corresponde a qualquer sequência de caracteres.
- `?`: Corresponde a qualquer caractere único.
- `[]`: Corresponde a qualquer um dos caracteres contidos nos colchetes.

Por exemplo, para copiar todas as imagens JPEG da sua localização atual para o diretório `Imagens`:

```bash
cp *.jpg /home/pete/Pictures
```

### Copiando Diretórios Recursivamente

Se você tentar copiar um diretório usando `cp` sem nenhuma opção, receberá um erro. Para copiar um diretório e todo o seu conteúdo, incluindo subdiretórios, você deve usar a flag `-r` (recursivo).

```bash
cp -r Abobora/ /home/pete/Documents
```

Este comando copia o diretório `Abobora` e tudo o que está dentro dele para o seu diretório `Documents`.

### Lidando com Sobrescrita de Arquivos

Por padrão, `cp` sobrescreverá um arquivo no destino se ele tiver o mesmo nome. Para evitar perda acidental de dados, use a flag `-i` (interativa), que solicita confirmação antes de sobrescrever.

```bash
cp -i meuarquivolegal /home/pete/Pictures
```

Inversamente, se você quiser forçar uma sobrescrita sem qualquer solicitação, pode usar a flag `cp -f`. Isso é útil em scripts onde a interação do usuário não é possível.

```bash
cp -f meuarquivolegal /home/pete/Pictures
```

### Preservando Atributos de Arquivo com cp -p

Quando você copia um arquivo, seus metadados, como tempo de modificação e propriedade, são tipicamente atualizados. Para preservar esses atributos originais, a flag `cp -p` é essencial. Usar `cp -p no linux` garante que a cópia seja uma réplica exata, não apenas no conteúdo, mas também em seus metadados.

A flag `cp -p` é particularmente útil para backups ou ao migrar arquivos onde preservar carimbos de data/hora é fundamental.

```bash
cp -p meuarquivolegal /home/pete/backups/
```

Este comando demonstra como usar `linux cp -p` para copiar `meuarquivolegal` preservando seu modo, propriedade e carimbos de data/hora.

## Exercise

Praticar leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre a cópia de arquivos e diretórios no Linux:

1. **[Comando cp do Linux: Cópia de Arquivos](https://labex.io/pt/labs/linux-linux-cp-command-file-copying-209744)** - Pratique o uso básico, opções avançadas como cópia recursiva, preservação de atributos e o uso de curingas para copiar arquivos e diretórios de forma eficiente.
2. **[Organizando Arquivos e Diretórios](https://labex.io/pt/labs/linux-organizing-files-and-directories-387877)** - Pratique habilidades essenciais de gerenciamento de arquivos do Linux usando os comandos `cp`, `mv` e `rm` para organizar uma estrutura de projeto, mover arquivos e limpar diretórios desnecessários.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança na cópia e gerenciamento de arquivos no Linux.

## Quiz Question

Qual flag você precisa especificar para copiar um diretório inteiro?

## Quiz Answer

-r
