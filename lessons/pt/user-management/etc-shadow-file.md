---
lesson_id: "etc-shadow-file"
course_id: "user-management"
lang: "pt"
order_index: 4
title: "/etc/shadow"
description: "Aprenda como os registros shadow locais representam hashes de senha e políticas de expiração sem expor dados confidenciais."
meta_title: "/etc/shadow - Gerenciamento de Usuários"
meta_description: "Conheça o arquivo /etc/shadow no Linux, um componente essencial da autenticação de usuários. Aprenda a consultar seus dados com segurança e entenda a estrutura que armazena hashes de senha e informações de política."
meta_keywords: "etc shadow, arquivo etc/shadow no Linux, /etc/shadow, autenticação de usuários, segurança de senhas, expiração de senhas, administração de sistemas Linux"
---

`/etc/shadow` armazena campos protegidos de hashes de senhas locais e de expiração de senhas. Separar esses valores do banco de dados `/etc/passwd`, geralmente legível, reduz a exposição a ataques de tentativa de descoberta de senhas offline.

## Proteção dos Dados do Shadow

As senhas não são armazenadas de forma reversível, “criptografadas” para exibição posterior. Uma entrada de senha local normalmente contém um hash unidirecional da senha, codificado com um identificador de algoritmo, salt e parâmetros. Um invasor que obtém hashes pode testar senhas candidatas offline, portanto o banco de dados deve permanecer restrito.

Os detalhes exatos de propriedade e permissão variam, mas o acesso costuma ser limitado ao root e a componentes do sistema com autorização restrita. Não imprima, copie, registre nem compartilhe o conteúdo do shadow apenas para inspecionar o estado de uma conta.

:::single-choice{#shadow-restricted-reason}
Por que os dados locais do shadow normalmente são protegidos contra o acesso geral de leitura?

::option[O arquivo contém a senha atual não criptografada de cada usuário.]{#shadow-plaintext-passwords explanation="Entradas shadow adequadas armazenam hashes unidirecionais de senhas ou marcadores especiais, não senhas em texto simples recuperável."}
::option[Hashes de senhas podem sofrer ataques offline caso sejam revelados.]{#shadow-offline-guessing .correct explanation="Um invasor pode testar tentativas de senha contra hashes roubados sem interagir com o serviço de login."}
::option[A leitura altera automaticamente todas as datas de expiração de senhas.]{#shadow-read-changes explanation="Uma leitura não atualiza por si só os campos de política; a preocupação é a revelação de material de autenticação confidencial."}
:::

## Leitura do Formato de Nove Campos

Um registro shadow local contém nove campos separados por dois-pontos. Um registro esquemático se parece com este, com o hash omitido deliberadamente:

```text
alice:<password-field>:20000:0:90:7:14:20500:
```

Os campos são:

1. **Nome de login**.
2. **Hash da senha ou marcador especial de senha**.
3. **Última alteração da senha**, em dias desde 1970-01-01; em ferramentas comuns, `0` solicita uma alteração no próximo login autenticado por senha.
4. **Idade mínima da senha**, em dias.
5. **Idade máxima da senha**, em dias.
6. **Período de aviso** antes da expiração da senha, em dias.
7. **Período de inatividade** após a expiração da senha, em dias.
8. **Data de expiração da conta**, em dias desde 1970-01-01.
9. **Campo reservado**.

Campos vazios e valores numéricos especiais têm significados definidos que podem variar conforme o campo e a ferramenta. Use comandos de gerenciamento de contas em vez de editar os valores visualmente.

:::single-choice{#shadow-account-expiration-field}
Qual campo do shadow armazena a data de expiração da conta em dias desde 1970-01-01?

::option[Campo 3]{#shadow-field-three explanation="O campo 3 registra a data da última alteração da senha, não a expiração da conta."}
::option[Campo 8]{#shadow-field-eight .correct explanation="O oitavo campo é a contagem absoluta de dias para a expiração da conta."}
::option[Campo 5]{#shadow-field-five explanation="O campo 5 registra a idade máxima da senha."}
:::

## Interpretação Cuidadosa do Campo de Senha

Um hash válido no campo 2 permite a verificação da senha Unix local. Um valor iniciado por `!` normalmente bloqueia esse hash de senha, enquanto `*` ou outro marcador de hash inválido impede a verificação bem-sucedida da senha por esse campo. Um valor vazio é sensível à segurança e pode permitir um comportamento sem senha, dependendo da política do PAM.

Esses marcadores descrevem o caminho da senha local, não todos os métodos de autenticação possíveis. Chaves públicas SSH, certificados, tokens e credenciais específicas de aplicações podem continuar disponíveis se não forem restringidos separadamente. A expiração da conta no campo 8 também é distinta do bloqueio da senha.

:::single-choice{#shadow-password-lock-scope}
O que você pode concluir com segurança de um campo de senha do shadow iniciado por `!`?

::option[O hash de senha Unix armazenado foi inutilizado para a verificação normal de senhas.]{#shadow-password-locked .correct explanation="Adicionar `!` antes do hash impede que ele corresponda a uma senha fornecida pelo caminho de senha do shadow."}
::option[Todos os métodos de login possíveis para a conta estão desabilitados.]{#shadow-all-login-disabled explanation="Outros métodos de autenticação podem ser independentes, portanto o marcador de senha sozinho não comprova o bloqueio completo da conta."}
::option[A conta foi excluída de todos os bancos de dados de identidades.]{#shadow-account-deleted explanation="Ainda existe um registro shadow, e a exclusão é uma operação separada de gerenciamento de contas."}
:::

## Distinção entre Datas de Senha e de Conta

Os campos 3 a 7 dizem respeito à expiração da senha: quando ela foi alterada pela última vez, quando outra alteração é permitida, quando expira, quando começam os avisos e por quanto tempo após a expiração o login por senha permanece disponível. O campo 8 expira a conta em um dia absoluto, independentemente da idade da senha.

Por exemplo, uma idade máxima de senha de 90 dias não é o mesmo que uma data de expiração da conta. A primeira se desloca em relação à última alteração da senha; a segunda é uma data fixa até que um administrador a modifique.

:::single-choice{#shadow-max-age-versus-expire}
Qual é a diferença entre os campos 5 e 8 do shadow?

::option[O campo 5 armazena o nome de usuário; o campo 8 armazena o shell de login.]{#shadow-username-shell explanation="O nome de usuário fica no campo 1, e o shell de login é registrado em `/etc/passwd`, não no registro shadow."}
::option[O campo 5 armazena um hash de senha; o campo 8 armazena seu salt.]{#shadow-hash-salt explanation="A codificação do hash de senha fica no campo 2, e os campos de expiração não armazenam seu salt separadamente."}
::option[O campo 5 é a idade máxima da senha; o campo 8 é uma data absoluta de expiração da conta.]{#shadow-password-vs-account-expiry .correct explanation="A idade da senha é relativa à última alteração, enquanto a expiração da conta é armazenada como uma contagem absoluta de dias."}
:::

## Inspeção e Alteração da Política por Ferramentas

Os administradores devem consultar apenas as informações necessárias para a tarefa:

```bash
$ sudo passwd -S alice
$ sudo chage -l alice
```

`passwd -S` resume o estado da senha local, enquanto `chage -l` lista as informações de expiração em um formato legível. Os formatos de saída e os requisitos de autorização podem variar conforme a distribuição.

Use `passwd`, `chage`, `usermod` e ferramentas de contas relacionadas para realizar alterações. Se o reparo manual do banco de dados shadow local for inevitável, `vipw -s` oferece bloqueio; valide os bancos de dados de contas com `pwck`. Mantenha uma sessão de recuperação antes de alterar a autenticação remotamente.

:::single-choice{#shadow-list-aging-policy}
Qual comando foi projetado para listar informações legíveis sobre a expiração da senha da conta local `alice`?

::option[`cat /etc/shadow`]{#shadow-cat-entire-file explanation="Esse comando expõe todos os registros shadow locais e mais informações confidenciais do que a tarefa exige."}
::option[`passwd -d alice`]{#shadow-passwd-delete explanation="A operação `-d` remove o hash da senha e altera um estado sensível à segurança, em vez de apenas listar informações."}
::option[`chage -l alice`]{#shadow-chage-list .correct explanation="A opção `-l` minúscula solicita que `chage` exiba os campos de expiração da senha da conta em formato legível."}
:::

O PAM e o NSS podem integrar fontes de autenticação e identidade além dos arquivos shadow locais. Por isso, uma conta do sistema pode não ter um registro shadow local ou pode se autenticar por serviços adicionais.

Para praticar o estado de contas e as políticas de expiração em um ambiente controlado, experimente estes laboratórios práticos:

1. **[Gerenciamento de Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** — Pratique todo o ciclo de administração de usuários, desde a criação e proteção de novas contas com `useradd` e `passwd` até sua modificação e exclusão.
2. **[Configuração de Contas de Usuário e Privilégios sudo no Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** — Aprenda técnicas essenciais de gerenciamento de contas de usuário e privilégios sudo, incluindo a aplicação de políticas de senha e a proteção das contas.

## Resumo

Agora você sabe interpretar a política do shadow sem expor todo o banco de dados de senhas.

1. Trate hashes de senhas como material de autenticação restrito.
2. Leia os nove campos do shadow de acordo com sua finalidade.
3. Diferencie o bloqueio da senha da desativação de todos os métodos de login.
4. Separe a expiração da senha da expiração absoluta da conta.
5. Inspecione e altere políticas por meio de ferramentas específicas de contas.
