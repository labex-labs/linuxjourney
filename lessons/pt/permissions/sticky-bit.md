---
lesson_id: "sticky-bit"
course_id: "permissions"
lang: "pt"
order_index: 8
title: "O Sticky Bit"
description: "Aprenda como o sticky bit protege entradas em diretórios compartilhados com permissão de escrita, como `/tmp`."
meta_title: "O Sticky Bit - Permissões"
meta_description: "Conheça a finalidade do sticky bit nas permissões de arquivos Linux e Unix. Aprenda como ele protege arquivos em diretórios compartilhados, como /tmp, e como defini-lo com chmod."
meta_keywords: "sticky bit, sticky bit Linux, sticky bit permissões de arquivos Unix, chmod +t, diretório /tmp, permissões de arquivos, segurança Linux"
---

Um diretório com permissão de escrita normalmente permite que um usuário autorizado remova ou renomeie as entradas contidas nele, mesmo quando esse usuário não é proprietário dos próprios arquivos. O sticky bit acrescenta uma restrição de propriedade que torna diretórios compartilhados com permissão de escrita mais seguros.

## Como o Sticky Bit Restringe a Remoção

Quando um diretório possui o sticky bit, o Linux geralmente permite que uma entrada seja removida ou renomeada apenas por um processo com privilégios adequados, pelo proprietário do diretório ou pelo proprietário da entrada. As permissões comuns de escrita e busca no diretório ainda são necessárias.

A restrição diz respeito às entradas do diretório. Ela não impede que o proprietário de um arquivo edite seu conteúdo quando as permissões do arquivo permitem essa operação, nem torna o diretório privado.

:::single-choice{#sticky-bit-removal-rule}
Em um diretório compartilhado com sticky bit, qual usuário comum normalmente pode remover uma determinada entrada?

::option[Qualquer usuário que consiga listar o diretório.]{#sticky-bit-any-reader explanation="A permissão de leitura do diretório pode revelar nomes, mas não ignora a restrição de propriedade do sticky bit."}
::option[O proprietário da entrada, com o acesso necessário ao diretório.]{#sticky-bit-entry-owner .correct explanation="O proprietário da entrada é uma das identidades normalmente permitidas pela regra do diretório com sticky bit."}
::option[Somente um membro do grupo da entrada.]{#sticky-bit-entry-group explanation="A associação ao grupo, por si só, não é a exceção de propriedade definida pelo sticky bit."}
:::

## Reconhecimento do Bit em `/tmp`

O diretório temporário do sistema é um exemplo comum:

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

O `t` minúsculo final ocupa a posição de execução dos outros. Ele significa que tanto o sticky bit quanto a permissão de execução dos outros estão presentes. Um `T` maiúsculo significa que o sticky bit está definido, mas a permissão de execução dos outros está ausente.

Como `/tmp` normalmente permite escrita e busca para todos, vários usuários podem criar entradas nele. O sticky bit impede que um usuário comum remova as entradas de outro usuário apenas porque o diretório permite escrita para todos. As aplicações ainda devem criar objetos temporários com segurança, pois nomes previsíveis, links inseguros e modos de arquivos fracos geram riscos separados.

:::single-choice{#sticky-bit-lowercase-t}
O que um `t` minúsculo no final do modo de um diretório indica?

::option[O sticky bit e a execução dos outros estão definidos.]{#sticky-bit-t-with-execute .correct explanation="O `t` minúsculo combina o bit especial sticky com o bit comum de execução dos outros."}
::option[O sticky bit está definido, mas a execução dos outros está ausente.]{#sticky-bit-t-without-execute explanation="Essa combinação é mostrada como `T` maiúsculo."}
::option[O setgid e a execução do grupo estão definidos.]{#sticky-bit-setgid-position explanation="O setgid aparece na posição de execução do grupo, não na posição final dos outros."}
:::

## Definição e Remoção do Sticky Bit

Defina o bit simbolicamente:

```bash
$ chmod +t shared-directory
```

Em um dígito octal inicial de bits especiais, o sticky contribui com `1`:

```bash
$ chmod 1777 shared-directory
```

O `1` inicial define o sticky, enquanto `777` fornece o modo comum. Esse modo é apropriado somente quando o diretório é compartilhado intencionalmente por todos os usuários locais. Para um diretório de equipe, permissões de grupo mais restritas podem ser preferíveis. Remova somente o sticky bit com `chmod -t shared-directory`.

:::single-choice{#sticky-bit-octal-value}
Qual valor octal inicial representa o sticky bit?

::option[`2`]{#sticky-bit-value-two explanation="Um `2` inicial representa o setgid."}
::option[`1`]{#sticky-bit-value-one .correct explanation="O sticky bit contribui com `1` para o dígito inicial de bits especiais."}
::option[`4`]{#sticky-bit-value-four explanation="Um `4` inicial representa o setuid."}
:::

## Verificação da Política Completa do Diretório

O sticky não concede acesso de escrita nem de busca; ele apenas restringe a remoção e a renomeação depois que as permissões comuns permitem modificar o diretório. Verifique em conjunto o proprietário, o grupo, o modo comum, as ACLs e o contexto de montagem do diretório. Teste com contas sem privilégios em um ambiente isolado, em vez de alterar `/tmp` em um sistema em uso.

:::single-choice{#sticky-bit-access-scope}
Adicionar o sticky bit torna um diretório sem permissão de escrita gravável por outros usuários?

::option[Sim; o sticky adiciona automaticamente a escrita para todas as classes.]{#sticky-bit-adds-write explanation="O bit especial não reescreve os bits de escrita do proprietário, do grupo nem dos outros."}
::option[Sim; o sticky desabilita o trio de permissões dos outros no diretório.]{#sticky-bit-disables-other explanation="O trio dos outros continua participando das verificações normais de acesso."}
::option[Não; as permissões comuns de escrita e busca ainda controlam o acesso.]{#sticky-bit-no-write-grant .correct explanation="O sticky restringe determinadas operações de remoção e renomeação, mas não adiciona permissões comuns ausentes."}
:::

Para praticar, crie um diretório compartilhado descartável, defina um modo comum apropriado e o sticky bit e teste a remoção de entradas com dois usuários sem privilégios. O laboratório [Exclusão e Movimentação de Arquivos](https://labex.io/labs/linux-delete-and-move-files-7777) pode reforçar as operações básicas de renomeação e exclusão.

## Resumo

Agora você sabe explicar e verificar o sticky bit em diretórios compartilhados.

1. Relacione o sticky às restrições de propriedade sobre remoções e renomeações.
2. Reconheça `t` minúsculo e `T` maiúsculo em uma listagem longa.
3. Defina o bit simbolicamente ou com o valor octal inicial `1`.
4. Avalie o sticky junto com as permissões comuns do diretório.
