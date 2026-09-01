---
lesson_id: "symlinks"
course_id: "filesystem"
lang: "pt"
order_index: 12
title: "Links Simbólicos"
description: "Aprenda como links simbólicos e físicos diferem na resolução de caminhos, na identidade dos inodes e no escopo do sistema de arquivos."
meta_title: "Links Simbólicos - O Sistema de Arquivos"
meta_description: "Conheça os links simbólicos e físicos do Linux. Aprenda a criá-los com o comando ln, verificar a contagem de links com ls e entender as diferenças entre suas saídas."
meta_keywords: "links simbólicos Linux, links físicos, comando ln, symlinks, ls symlink, contagem de links Linux, ls links, sistema de arquivos Linux, tutorial Linux"
---

Uma entrada de diretório atribui um nome a um inode. Um link físico cria outra entrada de diretório para o mesmo inode, enquanto um link simbólico cria um inode diferente cujo conteúdo é um caminho a ser resolvido. Essa diferença controla a identidade, a duração e o comportamento entre sistemas de arquivos.

## Criação e Inspeção de um Link Simbólico

Crie um link simbólico com `ln -s TARGET LINK_NAME`:

```bash
$ printf '%s\n' 'example' > myfile
$ ln -s -- myfile myfilelink
$ ls -li myfile myfilelink
151   -rw-r--r-- 1 user user 8 ... myfile
93403 lrwxrwxrwx 1 user user 6 ... myfilelink -> myfile
```

O link simbólico possui seu próprio inode e armazena o texto `myfile`. Quando um programa segue `myfilelink`, a resolução do caminho continua até o destino. Exiba o texto armazenado sem segui-lo com:

```bash
$ readlink myfilelink
```

:::single-choice{#symlinks-create-symbolic} Qual comando cria o link simbólico `myfilelink` com o texto de destino `myfile`?

::option[`ln -s -- myfile myfilelink`]{#symlinks-ln-s .correct explanation="A opção `-s` solicita um link simbólico, seguida pelo destino e pelo nome do novo link."}
::option[`ln -- myfile myfilelink`]{#symlinks-ln-hard explanation="Sem `-s`, `ln` solicita um link físico para o inode existente."}
::option[`readlink myfile myfilelink`]{#symlinks-readlink-create explanation="Readlink inspeciona um link simbólico e não cria um."}
:::

## Destinos Relativos e Absolutos de Links Simbólicos

Um destino absoluto começa em `/`. Um destino relativo é resolvido em relação ao diretório que contém o link simbólico — não em relação ao diretório atual do shell no momento em que alguém o abrir mais tarde.

```bash
$ mkdir -p tree/data tree/current
$ printf '%s\n' 'value' > tree/data/item
$ ln -s ../data/item tree/current/item
```

Mover toda a hierarquia `tree` preserva essa relação relativa. Mover apenas o link ou o destino pode quebrá-la. Um link simbólico pode conter um destino inexistente e, nesse caso, é chamado de pendente ou quebrado.

:::single-choice{#symlinks-relative-resolution} A partir de onde um destino relativo de link simbólico é resolvido?

::option[Do diretório pessoal do usuário que o criou.]{#symlinks-creator-home explanation="A identidade de quem criou o link não se torna uma base permanente de resolução."}
::option[Do diretório atual do primeiro shell que o listar.]{#symlinks-listing-shell explanation="O contexto da listagem não reescreve a relação armazenada do destino."}
::option[Do diretório que contém o link simbólico.]{#symlinks-containing-directory .correct explanation="A travessia do caminho substitui o texto relativo armazenado no local do link simbólico."}
:::

## Criação de um Link Físico

Crie outro nome para um arquivo comum existente sem `-s`:

```bash
$ ln -- myfile myhardlink
$ ls -li myfile myhardlink
151 -rw-r--r-- 2 user user 8 ... myfile
151 -rw-r--r-- 2 user user 8 ... myhardlink
```

Os dois nomes apontam para o mesmo sistema de arquivos e número de inode. A contagem de links passa a ser 2. Nenhum dos nomes é inerentemente o “original”; alterar o conteúdo por um deles modifica o objeto compartilhado, e remover um nome preserva o outro.

Links físicos não podem atravessar os limites dos sistemas de arquivos, pois um número de inode só possui significado dentro de seu sistema. O Linux também impede usuários comuns de criar links físicos para diretórios e pode restringir links para arquivos que eles não possuem, evitando ciclos e problemas de segurança.

:::single-choice{#symlinks-hard-link-inode} O que dois links físicos para um mesmo arquivo comum compartilham?

::option[Somente nomes parecidos, mas dados de arquivos separados.]{#symlinks-separate-data explanation="Isso descreveria cópias independentes, não links físicos."}
::option[Um caminho armazenado em um inode separado de link simbólico.]{#symlinks-stored-path explanation="O texto do caminho é o mecanismo que define um link simbólico."}
::option[O mesmo inode e o mesmo conteúdo de arquivo.]{#symlinks-same-inode .correct explanation="Cada entrada de diretório nomeia o mesmo objeto do sistema de arquivos."}
:::

## Duração e Exclusão

Remover um link simbólico exclui esse objeto de link, não seu destino:

```bash
$ rm -- myfilelink
```

Remover o nome de um link físico reduz a contagem de links do inode compartilhado. O sistema de arquivos só pode recuperar o objeto depois que a contagem chega a zero e nenhum descritor de arquivo aberto ou outra referência do sistema de arquivos o mantém existente.

Evite uma barra final ao remover um link simbólico para um diretório, pois a resolução de caminhos com barra final pode seguir a semântica de diretórios, dependendo do comando. Inspecione com `ls -ld -- LINK` e remova deliberadamente o nome do link.

:::single-choice{#symlinks-remove-symbolic} O que normalmente acontece quando você remove o próprio link simbólico?

::option[O inode e o nome do link simbólico são removidos, enquanto o destino permanece.]{#symlinks-remove-link-only .correct explanation="Desvincular o link simbólico não atua sobre o objeto indicado pelo texto de destino armazenado."}
::option[O destino e todos os links físicos para ele são apagados automaticamente.]{#symlinks-remove-target explanation="O link simbólico é um objeto separado do sistema de arquivos e não é proprietário de seu destino."}
::option[O destino é copiado para dentro do link simbólico antes da remoção.]{#symlinks-copy-target explanation="A remoção não preserva o conteúdo do destino dentro do link."}
:::

## Seguimento Seguro dos Links

Links simbólicos podem redirecionar um programa privilegiado para fora de um diretório esperado ou mudar entre a validação e o uso. Programas seguros devem evitar condições de corrida entre verificar e abrir caminhos e usar interfaces relativas a diretórios, sem seguimento ou com resolução restrita, conforme a linguagem e o sistema operacional.

Para a inspeção comum:

- `ls -ld LINK` mostra o próprio link.
- `readlink LINK` imprime o texto de destino armazenado.
- `stat LINK` normalmente informa os metadados do link, enquanto `stat -L LINK` o segue no GNU coreutils.
- `find -L` segue links e pode encontrar ciclos; use-o apenas intencionalmente.

As permissões mostradas como `lrwxrwxrwx` não são uma concessão geral de acesso. O acesso é decidido pela travessia dos diretórios, pela política de seguimento dos links e pelas permissões do destino; a propriedade dos links simbólicos também importa para algumas regras de diretórios protegidos.

:::single-choice{#symlinks-readlink-output} O que `readlink LINK` imprime por padrão?

::option[O texto do caminho armazenado no link simbólico.]{#symlinks-readlink-target-text .correct explanation="Ele inspeciona o objeto de link sem ler o conteúdo do arquivo de destino."}
::option[Todo o conteúdo em bytes do arquivo comum de destino.]{#symlinks-readlink-file-content explanation="Use um comando de leitura de arquivos após resolver o destino intencionalmente para obter seu conteúdo."}
::option[Todos os links físicos existentes no sistema de arquivos.]{#symlinks-readlink-all-hard explanation="A descoberta de links físicos exige buscas no sistema de arquivos que considerem inodes e não tem relação com o texto de destino do link simbólico."}
:::

Use o laboratório [Gerenciamento de Arquivos e Diretórios no Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835) para praticar links em arquivos descartáveis e comparar números de inodes.

## Resumo

Agora você sabe escolher e inspecionar o tipo correto de link do sistema de arquivos.

1. Use `ln -s TARGET LINK` para um link simbólico baseado em caminho.
2. Resolva destinos relativos a partir do diretório que contém o link.
3. Use `ln EXISTING LINK` para criar outro nome de inode no mesmo sistema de arquivos.
4. Diferencie a remoção de um link simbólico da remoção de um link físico.
5. Evite seguir links de forma insegura em operações privilegiadas ou recursivas.
