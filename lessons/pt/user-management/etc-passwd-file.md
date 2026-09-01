---
lesson_id: "etc-passwd-file"
course_id: "user-management"
lang: "pt"
order_index: 3
title: "/etc/passwd"
description: "Aprenda a ler registros passwd locais e diferenciá-los da visão completa de contas fornecida pelo NSS."
meta_title: "/etc/passwd - Gerenciamento de Usuários"
meta_description: "Um guia completo do arquivo /etc/passwd no Linux. Aprenda a interpretar os campos de dados dos usuários, entender UIDs e analisar exemplos como root:x:0:0:root:/root:/bin/bash."
meta_keywords: "/etc/passwd, /etc/passwd no Linux, root:x:0:0:root:/root:/bin/bash, ID de usuário, UID, gerenciamento de usuários, tutorial Linux"
---

`/etc/passwd` armazena registros de contas locais em um formato de texto separado por dois-pontos. Ele mapeia nomes de login para UIDs numéricos e registra um GID primário, um campo descritivo, o caminho do diretório pessoal e o programa de login.

## Registros Locais e Contas Resolvidas

Exiba o arquivo local com um comando somente para leitura:

```bash
$ cat /etc/passwd
```

Isso não representa necessariamente todas as contas conhecidas pelo sistema. O Name Service Switch (NSS) pode resolver contas a partir de arquivos, serviços de diretório, bancos de dados do sistema ou outras fontes configuradas. Use `getent` para consultar o banco de dados passwd resolvido:

```bash
$ getent passwd
$ getent passwd root
```

O primeiro comando pode revelar nomes de contas e metadados, portanto revise a saída antes de compartilhá-la publicamente.

:::single-choice{#passwd-query-resolved-database} Qual comando consulta o banco de dados passwd resolvido pelo NSS, em vez de ler apenas o arquivo local?

::option[`cat /etc/passwd`]{#passwd-cat-local explanation="Esse comando exibe apenas o arquivo local e não inclui contas fornecidas exclusivamente por outras fontes do NSS."}
::option[`cat /etc/shadow`]{#passwd-cat-shadow explanation="O arquivo shadow contém dados protegidos de senhas e expiração de contas locais e não deve ser exibido para essa finalidade."}
::option[`getent passwd`]{#passwd-getent-all .correct explanation="`getent` consulta as fontes configuradas do banco de dados passwd por meio do NSS."}
:::

## Leitura dos Sete Campos

Um registro local geralmente se parece com isto:

```text
root:x:0:0:root:/root:/bin/bash
```

Os sete campos separados por dois-pontos são:

1. **Nome de login**: O nome legível da conta, como `root`.
2. **Campo de senha**: Normalmente `x` em um sistema com senhas shadow, indicando que os dados protegidos da senha são armazenados separadamente.
3. **UID**: A identidade numérica do usuário. O UID 0 recebe o tratamento tradicional de superusuário.
4. **GID primário**: O ID numérico do grupo primário da conta.
5. **GECOS/comentário**: Informações descritivas da conta, frequentemente separadas internamente por vírgulas.
6. **Diretório pessoal**: O caminho usado como configuração do diretório pessoal da conta; ele pode não existir no disco.
7. **Shell/programa de login**: O programa solicitado para as sessões de login aplicáveis, como `/bin/bash` ou um programa que não permite login.

O kernel não exige que os valores de UID sejam exclusivos em registros malformados ou deliberadamente duplicados, mas contas que compartilham um UID tornam-se indistinguíveis em muitas decisões de propriedade e permissões. Em geral, os administradores devem manter os UIDs das contas exclusivos.

:::single-choice{#passwd-uid-field} Em `root:x:0:0:root:/root:/bin/bash`, qual campo contém o UID?

::option[O segundo campo, `x`]{#passwd-second-password explanation="O segundo campo é o marcador da senha, não a identidade numérica do usuário."}
::option[O quarto campo, o segundo `0`]{#passwd-fourth-gid explanation="O campo 4 é o GID primário, não o UID."}
::option[O terceiro campo, o primeiro `0`]{#passwd-third-uid .correct explanation="O campo 3 é o UID, portanto o primeiro zero identifica esse registro como UID 0."}
:::

:::single-choice{#passwd-primary-gid-field} Qual campo de um registro passwd armazena o GID primário da conta?

::option[Campo 5]{#passwd-gecos-five explanation="O quinto campo é o campo GECOS ou de comentário."}
::option[Campo 4]{#passwd-gid-four .correct explanation="O quarto campo separado por dois-pontos identifica numericamente o grupo primário."}
::option[Campo 7]{#passwd-shell-seven explanation="O sétimo campo especifica o shell ou programa de login."}
:::

## Interpretação do Marcador de Senha

Em sistemas comuns com senhas shadow, `x` no campo 2 direciona as ferramentas de senha para os dados protegidos em `/etc/shadow`. Valores como `*` ou `!` não são hashes de senha válidos e geralmente impedem a autenticação com uma senha Unix por meio desse registro.

Isso não prova que a conta não possa se autenticar por qualquer método. Chaves SSH, certificados, tokens ou mecanismos específicos de serviços podem ser independentes. Da mesma forma, um campo de senha vazio possui um comportamento sensível à segurança que depende da pilha de autenticação; não o crie nem tente “corrigi-lo” manualmente.

:::single-choice{#passwd-x-placeholder} O que `x` geralmente significa no campo 2 de um registro local de `/etc/passwd`?

::option[A conta certamente não possui nenhum método de autenticação.]{#passwd-no-auth-guarantee explanation="O marcador não descreve todos os métodos de autenticação possíveis nem significa, por si só, que a conta não possa ser usada."}
::option[O diretório pessoal da conta foi excluído.]{#passwd-home-deleted explanation="As informações do diretório pessoal ficam no campo 6 e não têm relação com o marcador `x`."}
::option[Os dados protegidos da senha são mantidos no banco de dados shadow.]{#passwd-shadow-placeholder .correct explanation="O registro passwd público contém um marcador, enquanto o hash da senha e os campos de expiração ficam nos dados protegidos do shadow."}
:::

## Reconhecimento de Contas de Serviço

Muitos registros representam serviços, não pessoas. Identidades de serviço separadas ajudam a limitar arquivos e processos à autoridade necessária para um daemon. Seus caminhos de diretórios pessoais podem ser incomuns ou inexistentes, e seu programa de login pode ser `/usr/sbin/nologin`, `/bin/false` ou outro programa restrito.

Não deduza a finalidade de uma conta apenas pelo intervalo de UID sem verificar a política da distribuição. Os intervalos de alocação variam, e contas gerenciadas centralmente podem seguir convenções diferentes.

:::single-choice{#passwd-nologin-shell} Qual é uma finalidade comum de um programa de login como `/usr/sbin/nologin` no campo 7?

::option[Excluir os arquivos da conta sempre que um serviço for interrompido.]{#passwd-nologin-delete explanation="O programa de login não remove automaticamente os dados pertencentes à conta nem gerencia arquivos de encerramento de serviços."}
::option[Impedir um shell interativo comum pelos caminhos de login que respeitam esse campo.]{#passwd-nologin-purpose .correct explanation="Um programa que não permite login é usado com frequência para contas de serviço que não devem receber um shell interativo pelo login normal."}
::option[Conceder à conta os mesmos privilégios do UID 0.]{#passwd-nologin-root explanation="Restringir o login interativo não eleva os privilégios da conta nem altera seu UID numérico."}
:::

## Modificação Segura dos Registros de Contas

Prefira ferramentas de gerenciamento de contas, como `useradd`, `usermod` e `userdel`, pois elas coordenam os registros relacionados e aplicam os padrões do sistema. O comportamento exato dessas ferramentas pode ser configurado pela distribuição, portanto revise as opções antes de alterar uma conta.

Se um banco de dados passwd local realmente precisar de reparo manual, use `vipw` em vez de um editor comum. Ele aplica um bloqueio destinado a evitar edições simultâneas. Valide os bancos de dados com ferramentas como `pwck` e mantenha uma sessão de recuperação antes de alterar arquivos de autenticação remotamente.

Para praticar com registros de usuários e grupos em um ambiente controlado, experimente estes laboratórios práticos:

1. **[Gerenciamento de Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** — Pratique todo o ciclo de administração de usuários, desde a criação e proteção de novas contas até sua modificação e exclusão.
2. **[Gerenciamento de Grupos Linux com groupadd, usermod e groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** — Adquira experiência prática com os principais utilitários de linha de comando para administração de grupos, incluindo a criação de novos grupos e a alteração das associações dos usuários.

## Resumo

Agora você sabe interpretar registros passwd locais sem confundi-los com o banco de dados completo de identidades.

1. Consulte as contas resolvidas pelo NSS com `getent passwd`.
2. Leia os sete campos do passwd separados por dois-pontos.
3. Localize os campos de UID e GID primário.
4. Interprete os marcadores de senha sem tirar conclusões indevidas sobre o estado do login.
5. Use ferramentas de contas ou `vipw` em vez de um editor comum.
