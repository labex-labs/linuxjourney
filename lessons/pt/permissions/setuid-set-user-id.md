---
lesson_id: "setuid-set-user-id"
course_id: "permissions"
lang: "pt"
order_index: 5
title: "Setuid"
description: "Aprenda como o bit de modo set-user-ID afeta programas executáveis e por que ele exige uma revisão cuidadosa de segurança."
meta_title: "Setuid - Permissões"
meta_description: "Aprenda sobre as permissões Setuid (SUID) do Linux, como elas funcionam e como modificá-las. Entenda o SUID para o acesso seguro a arquivos no Linux."
meta_keywords: "Setuid Linux, SUID, permissões Linux, chmod, comando passwd, segurança Linux, Linux para iniciantes, tutorial Linux"
---

Alguns programas precisam de um acesso rigorosamente controlado que seus solicitantes normalmente não possuem. Em um arquivo comum executável, o bit set-user-ID pode fazer com que um novo processo receba o ID de usuário do proprietário do arquivo como seu ID de usuário efetivo. O programa pode então realizar operações autorizadas para essa identidade enquanto mantém informações sobre o solicitante.

Setuid não é uma instrução geral para “executar como root”. Seu efeito depende do proprietário do executável, do sistema operacional, do sistema de arquivos e das opções de montagem, além da forma como o programa gerencia suas credenciais.

## Reconhecimento do Setuid

Em sistemas que usam um executável `passwd` com setuid, uma listagem longa pode se parecer com esta:

```bash
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68248 Jan 10 09:30 /usr/bin/passwd
```

O `s` minúsculo na posição de execução do proprietário significa que tanto o setuid quanto a execução do proprietário estão definidos. Se o setuid estiver presente, mas a execução do proprietário estiver ausente, `ls -l` mostrará um `S` maiúsculo nessa posição.

Não presuma que todas as distribuições tenham o mesmo modo ou projeto de autenticação. Inspecione o sistema real em vez de depender do exemplo.

:::single-choice{#setuid-lowercase-s}
O que um `s` minúsculo na posição de execução do proprietário indica?

::option[O setuid está definido, mas a execução do proprietário está ausente.]{#setuid-s-without-execute explanation="Essa combinação é mostrada como `S` maiúsculo, não como `s` minúsculo."}
::option[O arquivo possui um sticky bit e execução para o grupo.]{#setuid-sticky-group explanation="O sticky bit aparece na posição de execução dos outros, enquanto o setuid aparece na posição do proprietário."}
::option[O setuid e a execução do proprietário estão definidos.]{#setuid-s-with-execute .correct explanation="O `s` minúsculo representa o bit setuid junto com o bit comum de execução do proprietário."}
:::

## Compreensão da Alteração de Credenciais

Quando o kernel respeita o setuid durante a execução, o novo processo normalmente recebe um ID de usuário efetivo baseado no proprietário do executável. Para um programa pertencente ao root, isso pode fornecer acesso autorizado como root, mas apenas enquanto o programa é executado e somente por meio das operações realizadas por seu código.

Esse mecanismo pode permitir que um programa cuidadosamente desenvolvido valide uma solicitação e faça uma alteração restrita em um estado protegido. Por exemplo, um utilitário local para alterar senhas pode precisar de acesso controlado a dados de autenticação que usuários comuns não podem editar diretamente. As implementações modernas também dependem do PAM, de bloqueio de arquivos, de políticas e de outras proteções; o setuid sozinho não explica todo o fluxo de trabalho.

:::single-choice{#setuid-effective-identity}
Quando um executável setuid é respeitado, qual identidade é obtida principalmente do proprietário do arquivo?

::option[O nome de login armazenado em `/etc/passwd`.]{#setuid-login-name explanation="Executar um arquivo não reescreve o registro de conta nem o nome de login do solicitante."}
::option[O ID de usuário efetivo do processo.]{#setuid-effective-user .correct explanation="O mecanismo de execução set-user-ID altera a identidade de usuário efetiva usada em muitas verificações de autorização."}
::option[O grupo proprietário de todos os arquivos abertos.]{#setuid-opened-file-group explanation="O setuid afeta as credenciais do processo, não os metadados de propriedade de arquivos não relacionados."}
:::

## Definição e Remoção do Bit

Defina o setuid simbolicamente com:

```bash
$ sudo chmod u+s myfile
```

Na notação octal, o setuid contribui com `4` em um dígito inicial de bits especiais:

```bash
$ sudo chmod 4755 myfile
```

Neste caso, o `4` inicial define o setuid e `755` define os bits comuns do proprietário, do grupo e dos outros. Remova o setuid sem alterar os demais modos com `chmod u-s myfile`.

:::single-choice{#setuid-octal-value}
Qual valor octal inicial representa o bit especial setuid?

::option[`4`]{#setuid-octal-four .correct explanation="O setuid contribui com o valor `4` no dígito inicial de bits especiais."}
::option[`1`]{#setuid-octal-one explanation="Um `1` inicial representa o sticky bit."}
::option[`2`]{#setuid-octal-two explanation="Um `2` inicial representa o bit setgid."}
:::

## Tratamento do Setuid como Recurso Sensível à Segurança

Uma falha em um programa setuid privilegiado pode se tornar um caminho de elevação de privilégios. Esses programas devem validar as entradas, controlar o ambiente e os caminhos de arquivos nos quais confiam, evitar comportamentos inseguros em subprocessos, minimizar o código privilegiado e descartar as credenciais elevadas assim que possível.

Normalmente, o Linux não respeita o setuid em scripts interpretados, pois sua implementação segura apresenta problemas de condições de corrida e relacionados ao interpretador. Sistemas de arquivos montados com `nosuid` também suprimem os efeitos de setuid e setgid. Prefira mecanismos mais restritos, como operações intermediadas por serviços, uma política `sudo` cuidadosamente delimitada ou capacidades, quando forem adequados ao requisito.

Nunca adicione setuid a um shell, interpretador ou programa copiado arbitrariamente como experimento em um sistema compartilhado. Audite os arquivos setuid existentes e pratique apenas em um ambiente isolado e descartável.

:::single-choice{#setuid-nosuid-mount}
Qual é a finalidade de montar um sistema de arquivos com `nosuid`?

::option[Remover todos os bits de execução armazenados nos arquivos desse sistema de arquivos.]{#setuid-nosuid-remove-execute explanation="A opção não reescreve os bits comuns de execução nos metadados dos arquivos."}
::option[Suprimir os efeitos de execução de setuid e setgid nesse sistema de arquivos.]{#setuid-nosuid-suppress .correct explanation="A opção de montagem `nosuid` impede que esses bits de modo especiais concedam seu comportamento normal de alteração de credenciais durante a execução."}
::option[Tornar o root proprietário de todos os arquivos do sistema de arquivos.]{#setuid-nosuid-root-owner explanation="A montagem com `nosuid` não altera os campos de propriedade de usuário nem de grupo."}
:::

## Resumo

Agora você sabe reconhecer o setuid e explicar suas implicações de credenciais e segurança.

1. Encontre `s` ou `S` na posição de execução do proprietário.
2. Relacione a execução setuid à identidade de usuário efetiva do proprietário do executável.
3. Defina ou remova o bit com os modos simbólico ou octal de `chmod`.
4. Trate todo executável privilegiado como código sensível à segurança.
