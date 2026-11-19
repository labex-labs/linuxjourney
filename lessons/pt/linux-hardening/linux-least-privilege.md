---
lesson_id: "linux-least-privilege"
course_id: "linux-hardening"
lang: "pt"
order_index: 3
title: "Privilégio mínimo"
description: "Aprenda a escolher permissões de arquivo e de administração para uma tarefa específica de um serviço."
meta_title: "Privilégio mínimo - Hardening do Linux"
meta_description: "Aprenda a escolher permissões de arquivo e de administração para uma tarefa específica de um serviço."
meta_keywords: "privilégio mínimo, permissões, hardening do Linux, cibersegurança, Linux Journey"
---

O **privilégio mínimo** consiste em dar a uma conta apenas o acesso necessário ao seu trabalho. Comece pelas ações. A conta pode precisar ler um arquivo, gravar em outro e realizar nenhuma tarefa administrativa.

## Associando as permissões às tarefas

Um processo do serviço web precisa ler `index.html`. A conta de implantação atualiza esse arquivo. Cada tarefa pode usar permissões diferentes. O processo pode ler a página, e a conta de implantação pode alterá-la.

:::single-choice{#linux-least-privilege-read-only-page} De qual permissão sobre a página o processo web precisa neste exemplo?

::option[Permissão de leitura.]{#linux-least-privilege-read-only-page-a .correct explanation="Servir o arquivo requer ler seu conteúdo."}
::option[Permissão de escrita.]{#linux-least-privilege-read-only-page-b explanation="A conta de implantação é responsável por alterar a página."}
::option[Permissão para administrar serviços sem relação com a tarefa.]{#linux-least-privilege-read-only-page-c explanation="Essa atividade está fora da função do processo web."}
:::

## Verificando todo o caminho

As permissões do arquivo são apenas parte da verificação. No Linux, é preciso ter permissão para atravessar os diretórios que levam até ele. Em um diretório, a permissão de execução permite atravessá-lo quando o programa conhece o nome da entrada que procura. Mesmo que possa ler o arquivo, o processo fica sem acesso se não puder atravessar um diretório no caminho.

:::single-choice{#linux-least-privilege-path-boundary} As permissões de index.html permitem que o processo web leia o arquivo, mas ele não pode entrar no diretório pai. O que você deve revisar?

::option[Se a página tem um tamanho maior.]{#linux-least-privilege-path-boundary-a explanation="O tamanho não dá acesso ao diretório."}
::option[Se todos devem ter permissão para editar a página.]{#linux-least-privilege-path-boundary-c explanation="A permissão de escrita não resolve a falta de acesso pelo caminho."}
::option[Se o processo tem permissão para atravessar o diretório.]{#linux-least-privilege-path-boundary-b .correct explanation="O processo precisa ter acesso ao arquivo e aos diretórios do caminho."}
:::

## Limitando ações especiais

Ferramentas de administração como `sudo` podem permitir que um usuário autorizado execute tarefas específicas de manutenção. Defina a ação, quem tem autorização para executá-la e como verificar o novo acesso. Confirme que a manutenção autorizada continua funcionando e que uma ação administrativa sem relação com ela continua bloqueada pela mesma política.

:::single-choice{#linux-least-privilege-policy-test} Uma função de manutenção deve consultar o estado dos serviços. Qual plano verifica melhor as permissões necessárias?

::option[Verificar se todos os comandos administrativos passaram a funcionar.]{#linux-least-privilege-policy-test-a explanation="Essas permissões extras ultrapassariam o necessário para a tarefa registrada."}
::option[Verificar se a função pode consultar o estado e se alterações privilegiadas sem relação com a tarefa continuam restritas.]{#linux-least-privilege-policy-test-c .correct explanation="Isso testa o acesso necessário e os limites previstos."}
::option[Verificar apenas se o nome de usuário existe.]{#linux-least-privilege-policy-test-b explanation="A existência da conta não mostra quais são suas permissões."}
:::

## Resumo

Agora você consegue avaliar o acesso mínimo necessário para uma tarefa.

1. Distinga leitura, escrita e ações administrativas.
2. Verifique o acesso pelos diretórios do caminho.
3. Confirme as ações permitidas e restritas de cada função.
