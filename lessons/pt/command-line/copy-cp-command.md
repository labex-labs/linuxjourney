---
index: 10
lang: "pt"
title: "cp (Copiar)"
meta_title: "cp (Copiar) - Linha de Comando"
meta_description: "Aprenda o comando cp do Linux com exemplos para copiar arquivos, diretórios, múltiplos arquivos, curingas, backups e opções como cp -r, cp -i e cp -p."
meta_keywords: "comando linux cp, comando cp, copiar arquivos linux, cp -r, cp -i, cp -p, cp -a, cp -u, cópia recursiva, curingas linux"
---

## Lesson Content

O comando `cp` é a ferramenta padrão para copiar arquivos e diretórios no Linux. Ele cria uma nova cópia enquanto mantém o arquivo original no lugar. Sua sintaxe básica é:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

Você pode copiar um arquivo para outro arquivo, um ou mais arquivos para um diretório, ou uma árvore inteira de diretórios com a opção correta.

### Cópia Básica de Arquivos

Para copiar um arquivo, você especifica o arquivo de origem e o diretório ou caminho de destino.

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

Neste exemplo, `mycoolfile` é o arquivo de origem, e `/home/pete/Documents/cooldocs` é o diretório de destino. Você também pode copiar um arquivo e dar um novo nome a ele no destino.

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

Se o destino for um diretório existente, o arquivo copiado mantém seu nome original. Se o destino for um nome de arquivo, o `cp` cria uma cópia com esse novo nome.

### Copiar Múltiplos Arquivos para um Diretório

Para copiar vários arquivos para o mesmo diretório, liste todas as fontes primeiro e coloque o diretório de destino por último.

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

O argumento final deve ser um diretório quando você fornece mais de uma fonte.

### Usando Curingas para Cópia em Massa

Curingas são caracteres especiais que ajudam você a selecionar múltiplos arquivos baseados em padrões, oferecendo grande flexibilidade.

- `*`: Corresponde a qualquer sequência de caracteres.
- `?`: Corresponde a qualquer caractere único.
- `[]`: Corresponde a qualquer um dos caracteres entre colchetes.

Por exemplo, para copiar todas as imagens JPEG da sua localização atual para o diretório `Pictures`:

```bash
$ cp *.jpg /home/pete/Pictures
```

Você pode visualizar os arquivos que correspondem antes de copiar:

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

### Copiando Diretórios Recursivamente

Se você tentar copiar um diretório usando `cp` sem opções, receberá um erro. Para copiar um diretório e todo o seu conteúdo, incluindo subdiretórios, você deve usar a flag `-r` (recursiva).

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

Este comando copia o diretório `Pumpkin` e tudo dentro dele para seu diretório `Documents`.

Você também pode ver `-R`, que tem o mesmo propósito recursivo em sistemas Linux típicos:

```bash
$ cp -R website /home/pete/backups/
```

### Lidando com Sobrescrita de Arquivos

Por padrão, o `cp` sobrescreve um arquivo no destino se ele tiver o mesmo nome. Para evitar perda acidental de dados, use a flag `-i` (interativa), que pede confirmação antes de sobrescrever.

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

Por outro lado, se você quiser forçar a sobrescrita sem prompts, use a opção `-f`. Isso é útil em scripts onde a interação do usuário não é possível.

```bash
$ cp -f mycoolfile /home/pete/Pictures
```

Outra opção útil de segurança é `-n`, que significa "não sobrescrever". Ela impede a sobrescrição de um arquivo de destino existente.

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

### Preservar Atributos do Arquivo com -p

Quando você copia um arquivo, seus metadados, como horário de modificação e propriedade, normalmente são atualizados. Para preservar esses atributos originais, use a opção `-p`.

A opção `cp -p` é particularmente útil para backups ou quando se migram arquivos onde preservar timestamps é importante.

```bash
$ cp -p mycoolfile /home/pete/backups/
```

Isso copia `mycoolfile` preservando seu modo, propriedade onde permitido, e timestamps.

### Cópias de Arquivo com Arquivamento -a

A opção `-a` significa arquivar. É comumente usada para cópias de diretórios no estilo backup porque preserva muitos atributos e copia recursivamente.

```bash
$ cp -a project/ project-backup/
```

Para muitos backups do dia a dia, `cp -a` é mais conveniente do que combinar várias opções manualmente.

### Copiar Apenas Arquivos Mais Novos com -u

A opção `-u` copia somente quando o arquivo de origem é mais novo que o arquivo de destino ou quando o arquivo de destino não existe.

```bash
$ cp -u *.txt /home/pete/Documents/
```

Isso é útil ao atualizar uma pasta sem reescrever arquivos que já estão atualizados.

### Opções Comuns do cp

Aqui estão as opções que você usará com mais frequência:

- `-r` ou `-R`: Copiar diretórios recursivamente.
- `-i`: Perguntar antes de sobrescrever um arquivo.
- `-f`: Forçar a sobrescrita removendo o destino primeiro, se necessário.
- `-n`: Não sobrescrever arquivos existentes.
- `-p`: Preservar modo, propriedade onde possível, e timestamps.
- `-a`: Modo arquivar, útil para preservar árvores de diretórios.
- `-u`: Copiar somente quando a origem for mais nova que o destino.
- `-v`: Mostrar cada arquivo conforme é copiado.

### Perguntas Comuns

**Por que o cp sobrescreveu meu arquivo?** Por padrão, o `cp` substitui um arquivo de destino com o mesmo nome. Use `cp -i` para perguntar antes ou `cp -n` para evitar sobrescrever.

**Por que o cp não pode copiar um diretório?** Um diretório requer cópia recursiva. Use `cp -r source-dir destination-dir`.

**Qual a diferença entre cp e mv?** `cp` cria uma cópia e mantém o original. `mv` move ou renomeia o original.

**Devo usar cp -r ou cp -a para backups?** Use `cp -r` para uma cópia recursiva simples. Use `cp -a` quando quiser uma cópia no estilo backup que preserve mais atributos de arquivo.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of copying files and directories in Linux:

1. **[Linux cp Command: File Copying](https://labex.io/pt/labs/linux-linux-cp-command-file-copying-209744)** - Practice basic usage, advanced options like recursive copying, preserving attributes, and using wildcards to efficiently copy files and directories.
2. **[Organizing Files and Directories](https://labex.io/pt/labs/linux-organizing-files-and-directories-387877)** - Practice essential Linux file management skills by using `cp`, `mv`, and `rm` commands to organize a project structure, move files, and clean up unnecessary directories.

These labs will help you apply the concepts in real scenarios and build confidence with file copying and management in Linux.

## Quiz Question

Qual flag você precisa especificar para copiar um diretório?

## Quiz Answer

-r
