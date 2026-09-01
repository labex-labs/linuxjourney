---
lesson_id: "setgid-set-group-id"
course_id: "permissions"
lang: "pt"
order_index: 6
title: "Setgid"
description: "Aprenda como o set-group-ID afeta as credenciais de executáveis e a herança de grupos em diretórios compartilhados."
meta_title: "Setgid - Permissões"
meta_description: "Aprenda sobre as permissões SGID (Set Group ID) do Linux, como elas funcionam e como modificá-las. Entenda este importante conceito de segurança do Linux."
meta_keywords: "SGID Linux, Set Group ID, permissões Linux, chmod g+s, segurança Linux, Linux para iniciantes, tutorial Linux"
---

O bit set-group-ID, normalmente chamado de setgid ou SGID, tem duas utilidades importantes. Em um arquivo comum executável, ele pode alterar o ID de grupo efetivo do novo processo. Em um diretório, ele faz com que as entradas recém-criadas herdem o grupo do diretório, algo especialmente útil em árvores colaborativas.

## Setgid em Arquivos Executáveis

Uma listagem longa pode mostrar o setgid na posição de execução do grupo:

```bash
$ ls -l /path/to/program
-rwxr-sr-x 1 root operators 24576 Jan 10 09:30 /path/to/program
```

O `s` minúsculo significa que tanto o setgid quanto a execução do grupo estão definidos. O `S` maiúsculo significa que o setgid está definido, mas a execução do grupo está ausente.

Quando o kernel respeita esse bit durante a execução, o processo recebe um ID de grupo efetivo baseado no grupo proprietário do executável. O comportamento pode ser suprimido por controles como uma montagem `nosuid` e não deve ser tratado como uma garantia universal para todos os tipos de arquivo ou ambientes.

:::single-choice{#setgid-executable-effect} Quando o setgid de um executável é respeitado, qual credencial vem do grupo proprietário do executável?

::option[O ID de grupo efetivo do processo.]{#setgid-effective-group .correct explanation="A execução set-group-ID estabelece o grupo proprietário do executável como a identidade de grupo efetiva do processo."}
::option[O ID de usuário real do processo.]{#setgid-real-user explanation="O bit diz respeito à credencial de grupo, não à identidade de usuário real do solicitante."}
::option[O proprietário de todos os arquivos que o processo abrir.]{#setgid-opened-owner explanation="As credenciais de execução não reescrevem os metadados de propriedade dos arquivos abertos."}
:::

## Setgid em Diretórios

O setgid em um diretório tem uma finalidade diferente. Novos arquivos e subdiretórios normalmente herdam o grupo do diretório, em vez do grupo padrão de quem os criou. No Linux, novos subdiretórios também herdam o bit setgid, ajudando uma árvore de projeto compartilhada a manter um grupo consistente.

O setgid não concede por si só acesso de escrita ao grupo. O modo do diretório, o umask do processo, o modo de criação solicitado, as ACLs padrão e outros controles ainda determinam o acesso.

```bash
$ sudo chgrp developers /srv/project
$ sudo chmod g+s /srv/project
$ ls -ld /srv/project
drwxr-sr-x 2 root developers 4096 Jan 10 09:30 /srv/project
```

:::single-choice{#setgid-directory-inheritance} O que o setgid em `/srv/project` normalmente faz um arquivo recém-criado herdar?

::option[O usuário proprietário do diretório.]{#setgid-inherit-user explanation="O setgid de diretório afeta a herança do grupo, não o usuário proprietário da nova entrada."}
::option[O modo completo de permissões do diretório.]{#setgid-inherit-mode explanation="As permissões de criação ainda são calculadas a partir do modo solicitado, do umask e de eventuais ACLs."}
::option[O grupo proprietário do diretório.]{#setgid-inherit-group .correct explanation="Uma nova entrada normalmente recebe o grupo do diretório setgid, favorecendo uma propriedade compartilhada consistente."}
:::

## Definição e Remoção do Setgid

Defina o bit simbolicamente com:

```bash
$ sudo chmod g+s myfile
```

Defina-o junto com os bits de modo comuns usando um `2` octal inicial:

```bash
$ sudo chmod 2755 myfile
```

Remova somente o bit especial com `chmod g-s myfile`.

:::single-choice{#setgid-octal-value} Qual valor o setgid acrescenta ao dígito octal inicial de bits especiais?

::option[`4`]{#setgid-value-four explanation="O valor `4` representa o setuid no dígito de bits especiais."}
::option[`1`]{#setgid-value-one explanation="O valor `1` representa o sticky bit."}
::option[`2`]{#setgid-value-two .correct explanation="O setgid contribui com `2`, como no modo `2755`."}
:::

## Uso Seguro de Diretórios Compartilhados

Em um diretório colaborativo, combine o grupo proprietário pretendido, o setgid e bits de acesso escolhidos com cuidado. Teste a criação como usuários representativos e inspecione os resultados com `ls -ld`. Evite tornar uma árvore gravável por todos apenas para resolver problemas de compartilhamento por grupo; um grupo dedicado, um umask ou uma ACL padrão apropriados e um diretório setgid normalmente oferecem um controle mais claro.

:::single-choice{#setgid-directory-write-access} Definir apenas o setgid concede aos membros do grupo permissão para criar arquivos em um diretório?

::option[Sim; o setgid sempre adiciona leitura, escrita e execução para o grupo.]{#setgid-adds-rwx explanation="O bit especial não altera automaticamente os três bits de permissão comuns do grupo."}
::option[Sim; o setgid desabilita todas as verificações para os membros do grupo.]{#setgid-disables-checks explanation="As verificações de segurança comuns e adicionais continuam sendo aplicadas."}
::option[Não; as permissões aplicáveis de escrita e busca também devem permitir a criação.]{#setgid-no-automatic-write .correct explanation="O setgid controla a herança de grupo, enquanto as permissões comuns e outros controles de acesso determinam a escrita no diretório."}
:::

## Resumo

Agora você sabe diferenciar os significados do setgid em executáveis e diretórios.

1. Reconheça o setgid na posição de execução do grupo.
2. Relacione o setgid de executáveis ao ID de grupo efetivo.
3. Use o setgid de diretório para preservar a propriedade de grupo em árvores compartilhadas.
4. Defina ou remova o bit sem confundi-lo com o acesso comum de escrita.
