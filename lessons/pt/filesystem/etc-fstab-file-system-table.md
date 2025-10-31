---
index: 7
lang: "pt"
title: "/etc/fstab"
meta_title: "/etc/fstab - O Sistema de Arquivos"
meta_description: "Aprenda a usar o arquivo /etc/fstab no Linux para montar sistemas de arquivos automaticamente na inicialização. Este guia aborda a sintaxe do fstab, como editar o arquivo etc fstab com segurança e seu papel na inicialização do sistema."
meta_keywords: "fstab, fstab linux, etc fstab, /etc/fstab, arquivo fstab, montar sistemas de arquivos, inicialização Linux, tutorial fstab"
---

## Lesson Content

No Linux, quando você deseja montar automaticamente sistemas de arquivos na inicialização, você os configura em um arquivo de configuração especial localizado em `/etc/fstab`. O nome `fstab` é a abreviação de "filesystem table" (tabela de sistemas de arquivos), e este arquivo contém uma lista permanente de sistemas de arquivos que o sistema deve montar durante o processo de boot.

Compreender a configuração **fstab linux** é uma habilidade fundamental para qualquer administrador de sistema.

### O que é /etc/fstab

O arquivo `/etc/fstab` é um arquivo de configuração do sistema que define todas as partições de disco disponíveis e outros tipos de sistemas de arquivos e fontes de dados que não são necessariamente baseados em disco. O sistema consulta este arquivo durante a inicialização para determinar quais sistemas de arquivos montar automaticamente.

Aqui está um exemplo de um **arquivo fstab** típico:

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

### A Estrutura do Arquivo fstab

Cada linha no arquivo **etc fstab** representa um sistema de arquivos e contém seis campos separados por espaços ou tabulações. Vamos detalhar o que cada campo significa:

- **Identificador do Dispositivo**: Especifica o dispositivo a ser montado. Sistemas modernos usam um UUID (Universally Unique Identifier) para evitar problemas se o nome do dispositivo (ex: `/dev/sda1`) mudar.
- **Ponto de Montagem (Mount Point)**: O diretório no sistema de arquivos onde o dispositivo será montado (ex: `/` ou `/home`).
- **Tipo de Sistema de Arquivos**: O tipo de sistema de arquivos no dispositivo, como `ext4`, `xfs`, `btrfs` ou `swap`.
- **Opções**: Opções de montagem que controlam como o sistema de arquivos é montado. Opções comuns incluem `defaults`, `relatime` e `errors=remount-ro`. Para uma lista completa, consulte a página de manual (`man`) do comando `mount`.
- **Dump**: Este campo é usado pela utilidade `dump` para determinar se um sistema de arquivos precisa ser copiado de segurança (backup). Um valor de `0` significa que será ignorado, o que é um padrão seguro.
- **Pass (Ordem de Verificação)**: Este campo é usado pelo `fsck` para determinar a ordem de verificação dos sistemas de arquivos no boot. O sistema de arquivos raiz (`/`) deve ser `1`, outros sistemas de arquivos devem ser `2`, e um valor de `0` significa que o sistema de arquivos não será verificado.

### Como Editar /etc/fstab

Você pode adicionar uma entrada modificando diretamente o arquivo `/etc/fstab` usando um editor de texto com privilégios de root. Tenha extremo cuidado ao editar este arquivo; uma entrada incorreta no **fstab** pode impedir que seu sistema inicie corretamente. É sempre uma boa prática fazer uma cópia de segurança do arquivo antes de fazer alterações. Após salvar suas alterações, você pode testá-las sem reiniciar, executando o comando `sudo mount -a`, que monta todos os sistemas de arquivos listados em `/etc/fstab`.

## Exercise

Praticar é fundamental! A experiência prática é crucial para entender como gerenciar sistemas de arquivos e garantir que eles sejam montados corretamente na inicialização do sistema. Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de sistemas de arquivos Linux e do arquivo `/etc/fstab`:

1. **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Pratique a criação de partições, a formatação delas, a montagem e a configuração da montagem persistente usando `/etc/fstab`.
2. **[Criar e Ativar um Arquivo de Swap no Linux](https://labex.io/pt/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Aprenda a tarefa administrativa essencial de criar e ativar um arquivo de swap, o que frequentemente envolve entradas em `/etc/fstab`.

Esses laboratórios ajudarão você a aplicar os conceitos de montagem e configuração de sistemas de arquivos em cenários reais e a construir confiança no gerenciamento de recursos de disco no Linux.

## Quiz Question

Qual arquivo é usado para definir como os sistemas de arquivos devem ser montados? (Por favor, forneça o caminho completo. A resposta diferencia maiúsculas de minúsculas.)

## Quiz Answer

/etc/fstab
