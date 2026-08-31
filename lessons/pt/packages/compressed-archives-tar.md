---
lesson_id: "compressed-archives-tar"
course_id: "packages"
lang: "pt"
order_index: 3
title: "tar e gzip"
description: "Aprenda a arquivar arquivos com `tar`, compactar fluxos com `gzip` e inspecionar arquivos antes de extraí-los com segurança."
meta_title: "tar e gzip - Pacotes"
meta_description: "Um guia completo para usar tar e gzip no Linux. Aprenda a criar, compactar e extrair arquivos, entenda a diferença entre gzip e tar e gerencie arquivos tar.gz com segurança."
meta_keywords: "tar e gzip, compactação tar, gzip tar, compactar tar gz, arquivamento Linux, compactação de arquivos, comando tar, comando gzip, tutorial Linux"
---

Arquivamento e compactação resolvem problemas diferentes. Um arquivo de arquivamento combina uma árvore de diretórios e seus metadados em um único fluxo. A compactação codifica um fluxo para reduzir seu tamanho. Por convenção, um arquivo `.tar.gz` é um arquivo tar cujo fluxo foi compactado com gzip.

## Compactação de um Fluxo com `gzip`

Por padrão, `gzip` compacta um arquivo e substitui o nome original por um arquivo com a extensão `.gz`:

```bash
$ gzip report.txt
```

Normalmente, isso remove `report.txt` após criar `report.txt.gz` com sucesso. Descompacte-o com:

```bash
$ gunzip report.txt.gz
```

Use `gzip -k report.txt`, quando houver suporte, para manter o arquivo de entrada, ou use os fluxos padrão quando precisar de controle explícito. Uma extensão de nome de arquivo é apenas uma convenção, não uma prova do formato real; ferramentas como `file` podem inspecionar o conteúdo.

:::single-choice{#tar-gzip-gzip-role}
Qual é a principal função de `gzip` nesta lição?

::option[Combinar uma árvore de diretórios e seus metadados em um arquivo.]{#tar-gzip-directory-archive explanation="O tar realiza essa função de arquivamento antes da aplicação da compactação com gzip."}
::option[Compactar um único fluxo de entrada.]{#tar-gzip-compress-stream .correct explanation="O gzip transforma um fluxo de bytes e não codifica por si só uma hierarquia de diretórios."}
::option[Instalar metadados de dependências em um banco de dados de pacotes.]{#tar-gzip-package-install explanation="A compactação é uma operação separada da instalação de pacotes nativos e do acompanhamento de dependências."}
:::

## Criação de um Arquivo Tar

Crie um arquivo não compactado com:

```bash
$ tar -cvf project.tar file1 file2 directory1
```

- `-c` cria um novo arquivo.
- `-v` lista os membros durante o processamento e é opcional.
- `-f project.tar` define o nome do arquivo; como `-f` consome um argumento, mantenha o nome ao lado dessa opção.

Os caminhos são armazenados como nomes de membros do arquivo. Crie arquivos a partir de um diretório de trabalho escolhido conscientemente e evite incluir sem querer segredos, caches, sockets ou caminhos absolutos muito abrangentes.

:::single-choice{#tar-gzip-create-option}
Qual opção de `tar` cria um novo arquivo?

::option[`-x`]{#tar-gzip-option-extract explanation="A operação `-x` extrai membros do arquivo."}
::option[`-c`]{#tar-gzip-option-create .correct explanation="A operação de criação grava um novo arquivo com base nas entradas indicadas."}
::option[`-t`]{#tar-gzip-option-list explanation="A operação `-t` lista os membros sem extraí-los."}
:::

## Criação de um Arquivo Tar Compactado com Gzip

O GNU tar e muitas outras implementações podem chamar o gzip por meio de `-z`:

```bash
$ tar -czvf project.tar.gz file1 file2 directory1
```

O resultado é um único fluxo tar compactado com gzip. A compactação não criptografa o arquivo nem oculta seu conteúdo de quem puder lê-lo e descompactá-lo. Se houver necessidade de confidencialidade, use um fluxo de trabalho adequado com criptografia autenticada e gerencie as chaves separadamente.

:::single-choice{#tar-gzip-z-option}
O que `-z` solicita no comando `tar` exibido?

::option[Criptografar o arquivo usando uma chave de conhecimento zero.]{#tar-gzip-z-encrypt explanation="Nem o tar nem o gzip fornece criptografia por meio dessa opção."}
::option[Descartar todos os membros com tamanho zero.]{#tar-gzip-z-zero explanation="A opção seleciona o gzip e não filtra membros do arquivo pelo tamanho."}
::option[Processar o fluxo do arquivo por meio do gzip.]{#tar-gzip-z-gzip .correct explanation="A opção `z` conecta a operação de arquivamento do tar à compactação ou descompactação com gzip."}
:::

## Listagem Antes da Extração

Trate um arquivo recebido de terceiros como uma entrada não confiável. Primeiro, liste os nomes de seus membros:

```bash
$ tar -tzf download.tar.gz
```

Procure caminhos absolutos inesperados, componentes de travessia `..`, links simbólicos ou físicos suspeitos, arquivos de dispositivo e nomes que sobrescreveriam arquivos importantes. Implementações modernas de tar aplicam proteções, mas os comportamentos e as opções variam, e a extração ainda cria nomes e conteúdos escolhidos pelo remetente.

Extraia o conteúdo em um diretório de preparação recém-criado e sem privilégios:

```bash
$ mkdir extraction-stage
$ tar -xzf download.tar.gz -C extraction-stage
```

Não extraia como root um arquivo que ainda não foi examinado. Verifique o que foi criado antes de mover os arquivos selecionados para seus locais definitivos.

:::single-choice{#tar-gzip-list-before-extract}
Qual operação lista os membros de um arquivo sem extraí-los?

::option[`tar -czf download.tar.gz .`]{#tar-gzip-create-download explanation="Esse comando cria ou substitui um arquivo usando o diretório atual."}
::option[`tar -xzf download.tar.gz`]{#tar-gzip-extract-download explanation="A operação `-x` grava os membros no diretório de destino."}
::option[`tar -tzf download.tar.gz`]{#tar-gzip-list-members .correct explanation="A operação `-t` lê e exibe a tabela de membros, enquanto `-z` processa o gzip."}
:::

## Outros Formatos de Compactação

As implementações de tar podem trabalhar com compactadores como bzip2 e xz, normalmente selecionados no GNU tar com `-j` e `-J`, respectivamente. O suporte a formatos e a detecção automática variam; portanto, consulte `tar --help` ou o manual local. ZIP é um formato de arquivamento separado, operado por ferramentas como `zip` e `unzip`.

:::single-choice{#tar-gzip-archive-confidentiality}
A compactação com gzip torna um arquivo tar confidencial?

::option[Não; normalmente, qualquer pessoa que consiga lê-lo também pode descompactá-lo.]{#tar-gzip-not-encryption .correct explanation="A compactação altera a representação e o tamanho, mas não fornece controle de acesso nem sigilo criptográfico."}
::option[Sim; o gzip deriva uma chave de criptografia do nome do arquivo.]{#tar-gzip-filename-key explanation="O gzip não implementa esse mecanismo de criptografia."}
::option[Sim; o tar criptografa cada membro antes de o gzip recebê-lo.]{#tar-gzip-tar-encrypt explanation="O tar arquiva os membros, mas não criptografa automaticamente seu conteúdo."}
:::

Pratique com arquivos descartáveis em [Empacotamento e Compactação de Arquivos](https://labex.io/labs/linux-file-packaging-and-compression-385413) e depois aplique a inspeção e a preparação em [Criar e Restaurar um Backup com tar](https://labex.io/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843).

## Resumo

Agora você sabe combinar o arquivamento com tar e a compactação com gzip de forma segura.

1. Diferencie um arquivo tar da compactação com gzip.
2. Crie arquivos com `-c` e fluxos gzip com `-z`.
3. Liste os membros com `-t` antes de extraí-los com `-x`.
4. Extraia conteúdo não confiável em um diretório de preparação sem privilégios.
5. Trate a compactação como algo separado da criptografia.
