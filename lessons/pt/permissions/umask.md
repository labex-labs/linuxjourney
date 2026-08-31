---
lesson_id: "umask"
course_id: "permissions"
lang: "pt"
order_index: 4
title: "Umask"
description: "Aprenda como o umask de um processo limita os bits de permissão solicitados para novos arquivos e diretórios."
meta_title: "Umask - Permissões"
meta_description: "Aprenda a usar o comando `umask` para controlar as permissões padrão de arquivos no Linux. Entenda as permissões numéricas e gerencie facilmente o acesso a novos arquivos."
meta_keywords: "umask, permissões Linux, permissões de arquivos, comandos Linux, Linux para iniciantes, tutorial Linux, permissões padrão"
---

A máscara de criação de arquivos de um processo, ou umask, impede que determinados bits de permissão sejam definidos quando esse processo cria um objeto do sistema de arquivos. Ela é uma máscara, não um modo padrão completo: primeiro a aplicação solicita um modo, e então o kernel remove os bits proibidos pelo umask.

Conceitualmente:

```text
resulting mode = requested mode AND NOT umask
```

As listas de controle de acesso e o comportamento das aplicações podem acrescentar outros detalhes, portanto inspecione o resultado quando as permissões exatas forem importantes.

## Visualização e Definição do Umask

Execute `umask` sem um operando para exibir a máscara do shell atual, normalmente em formato octal:

```bash
$ umask
0022
```

Defina-a para o shell atual e para os processos iniciados posteriormente por esse shell:

```bash
$ umask 027
```

Cada posição octal corresponde ao proprietário, ao grupo e aos outros. Um bit da máscara remove a permissão solicitada correspondente: `2` mascara a escrita, `4` mascara a leitura e `1` mascara a execução.

:::single-choice{#umask-command-purpose}
O que `umask 027` altera no shell atual?

::option[As permissões de todos os arquivos que já existem.]{#umask-existing-files explanation="Um umask afeta as solicitações de criação; ele não executa `chmod` retroativamente nos objetos existentes."}
::option[A máscara herdada pelos comandos iniciados posteriormente a partir desse shell.]{#umask-current-shell-mask .correct explanation="O shell define o umask de seu processo, e os processos filhos normalmente herdam esse valor."}
::option[Os nomes do proprietário e do grupo armazenados nos novos arquivos.]{#umask-owner-group explanation="A máscara filtra bits de permissão e não seleciona identidades de propriedade."}
:::

## Cálculo dos Modos de Novos Arquivos e Diretórios

Muitos programas comuns solicitam `0666` para novos arquivos regulares, pois criar arquivos executáveis por padrão não seria seguro. Eles normalmente solicitam `0777` para novos diretórios, nos quais a permissão de execução é necessária para a travessia.

Com o umask `0022`:

```text
regular file: 0666 masked by 0022 -> 0644 (rw-r--r--)
directory:    0777 masked by 0022 -> 0755 (rwxr-xr-x)
```

O umask apenas remove bits solicitados. Ele não pode adicionar a permissão de execução quando uma aplicação não a solicitou. Uma aplicação também pode solicitar um modo inicial mais restritivo, produzindo um resultado mais restritivo.

:::single-choice{#umask-file-mode-022}
Se um programa solicitar o modo `0666` para um arquivo comum e o umask for `0022`, qual será o modo resultante?

::option[`0666`]{#umask-file-0666 explanation="Os bits de escrita solicitados por `0666` para o grupo e os outros são removidos pela máscara `0022`."}
::option[`0755`]{#umask-file-0755 explanation="Os bits de execução não foram solicitados para o arquivo comum, portanto o umask não pode adicioná-los."}
::option[`0644`]{#umask-file-0644 .correct explanation="Remover a escrita do grupo e dos outros de `0666` mantém leitura/escrita para o proprietário e somente leitura para o grupo e os outros."}
:::

:::single-choice{#umask-directory-mode-027}
Se um programa solicitar `0777` para um diretório e o umask for `0027`, qual será o modo resultante?

::option[`0777`]{#umask-directory-0777 explanation="A escrita solicitada para o grupo e as permissões dos outros são filtradas pela máscara diferente de zero."}
::option[`0640`]{#umask-directory-0640 explanation="Esse resultado também removeria bits de execução que a máscara `0027` não remove do proprietário nem do grupo."}
::option[`0750`]{#umask-directory-0750 .correct explanation="A máscara remove a escrita do grupo e todas as permissões dos outros, deixando `rwxr-x---`."}
:::

## Escopo e Persistência

Alterar o umask em um shell não modifica seu processo pai nem sessões não relacionadas. O valor se aplica às criações futuras desse shell e de seus descendentes; os arquivos existentes mantêm seus modos.

Para tornar persistente um valor de sua preferência, configure-o no login, shell, PAM, gerenciador de serviços ou aplicação apropriado para seu ambiente. O local correto varia, e os serviços podem definir seu próprio umask. Não presuma que editar um único arquivo de shell interativo controlará todos os processos do sistema.

:::single-choice{#umask-existing-file-effect}
O que acontece com um arquivo existente quando você define um novo umask?

::option[Seu modo atual permanece inalterado.]{#umask-existing-unchanged .correct explanation="Um novo umask filtra solicitações de criação posteriores e não modifica os modos já armazenados nos objetos do sistema de arquivos."}
::option[Seu modo é recalculado a partir de `0666`.]{#umask-existing-recalculated explanation="Os objetos existentes não são recriados nem passam automaticamente pela nova máscara."}
::option[Seu proprietário perde imediatamente as permissões mascaradas.]{#umask-existing-owner-loss explanation="Alterar o umask de um processo não é uma operação sobre os metadados de arquivos existentes."}
:::

Para praticar, crie arquivos e diretórios sob diferentes máscaras em um ambiente isolado e compare seus modos com `ls -ld`. O laboratório [Usuários, Grupos e Permissões de Arquivos no Linux](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) oferece um ambiente apropriado para permissões.

## Resumo

Agora você sabe prever como um umask limita as permissões recém-solicitadas.

1. Visualize ou defina a máscara do shell atual com `umask`.
2. Remova os bits mascarados do modo solicitado por uma aplicação.
3. Diferencie as solicitações comuns de `0666` para arquivos e `0777` para diretórios.
4. Trate o escopo e a persistência do umask como específicos do processo e do ambiente.
