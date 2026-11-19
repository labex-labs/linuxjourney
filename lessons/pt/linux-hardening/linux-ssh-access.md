---
lesson_id: "linux-ssh-access"
course_id: "linux-hardening"
lang: "pt"
order_index: 6
title: "Acesso SSH"
description: "Aprenda a distinguir a identidade do servidor SSH, a autenticação do usuário e a política de acesso."
meta_title: "Acesso SSH - Hardening do Linux"
meta_description: "Aprenda a distinguir a identidade do servidor SSH, a autenticação do usuário e a política de acesso."
meta_keywords: "acesso SSH, chaves SSH, hardening do Linux, cibersegurança, Linux Journey"
---

Quando você usa SSH para manutenção, cada lado da conexão precisa responder a uma pergunta. O cliente precisa saber a qual servidor chegou. O servidor precisa saber se a conta tem permissão para entrar.

## Verificando a identidade do servidor

Um servidor SSH apresenta uma **chave de host**. O cliente pode compará-la com a identidade conhecida daquele host. Se a chave mudar sem aviso, confirme o novo valor por uma fonte independente e autorizada, como o inventário de hosts da equipe ou uma pessoa responsável pela manutenção em um canal confiável.

:::single-choice{#linux-ssh-access-unexpected-key} O cliente informa que a chave de host do servidor mudou. Qual verificação deve vir primeiro?

::option[Confirmar a nova chave de host esperada por uma fonte confiável.]{#linux-ssh-access-unexpected-key-b .correct explanation="Isso verifica a identidade antes que você confie na conexão."}
::option[Experimentar vários nomes de usuário até um funcionar.]{#linux-ssh-access-unexpected-key-a explanation="Um nome de usuário não verifica a identidade do servidor."}
::option[Apagar todas as chaves de host salvas e prosseguir.]{#linux-ssh-access-unexpected-key-c explanation="Isso descartaria informações de identidade conhecidas antes de entender a mudança."}
:::

## Verificando o acesso do usuário

Uma chave de usuário pode comprovar que um cliente está autorizado a agir como uma conta. A chave de host confirma a identidade do servidor. A política do servidor pode limitar as contas e os métodos de autenticação aceitos. O resumo deste exercício indica que `ops` entra por autenticação baseada em chave.

:::single-choice{#linux-ssh-access-distinguish-keys} Qual identidade está em verificação quando o servidor avalia a chave de usuário de ops?

::option[O nome da página web pública.]{#linux-ssh-access-distinguish-keys-b explanation="O conteúdo web é independente da autenticação SSH."}
::option[O servidor, que comprova a própria identidade.]{#linux-ssh-access-distinguish-keys-c explanation="Para essa verificação, o cliente usa a chave de host."}
::option[O cliente que tenta entrar como ops.]{#linux-ssh-access-distinguish-keys-a .correct explanation="A autenticação de usuário diz respeito à conta que o cliente tenta usar."}
:::

## Preservando o acesso de manutenção

Antes de fazer alterações autorizadas na política de SSH, acerte quais contas e qual método de acesso serão usados. Abra uma conexão de teste separada e mantenha o caminho de recuperação disponível até que o login previsto funcione. Uma sessão que já estava aberta pode sobreviver à mudança mesmo que novos logins falhem.

:::single-choice{#linux-ssh-access-test-new-login} Uma sessão que já existia continua aberta após uma mudança de política. O que confirma que a equipe de manutenção ainda consegue entrar?

::option[Apenas uma resposta a ping.]{#linux-ssh-access-test-new-login-a explanation="Uma resposta de rede não comprova que a autenticação SSH funcionou."}
::option[Uma nova sessão SSH autorizada com a conta e o método previstos.]{#linux-ssh-access-test-new-login-c .correct explanation="Ela testa diretamente a política que será aplicada a um login futuro."}
::option[A sessão antiga permanece ociosa.]{#linux-ssh-access-test-new-login-b explanation="Ela foi autenticada sob as condições anteriores."}
:::

## Resumo

Agora você consegue verificar as identidades e as regras envolvidas no acesso SSH para manutenção.

1. Confirme a identidade do servidor pela chave de host.
2. Distinga essa verificação da autenticação do usuário.
3. Após uma mudança, verifique se uma nova conexão autorizada funciona.
