---
lesson_id: "linux-service-accounts"
course_id: "linux-hardening"
lang: "pt"
order_index: 2
title: "Contas de serviço"
description: "Aprenda a identificar a conta com a qual um processo Linux é executado e a avaliar seu acesso."
meta_title: "Contas de serviço - Hardening do Linux"
meta_description: "Aprenda a identificar a conta com a qual um processo Linux é executado e a avaliar seu acesso."
meta_keywords: "contas de serviço, identidade de processos, hardening do Linux, cibersegurança, Linux Journey"
---

Um servidor web inicia como um processo. O Linux associa cada processo a uma identidade que ajuda a determinar o que o programa pode ler ou alterar. Uma **conta de serviço** é uma identidade reservada para um programa.

## Lendo a identidade do processo

Em um terminal comum, `$$` fornece o ID do processo do shell. Use-o para ver a identidade do seu próprio shell. A opção `-p` seleciona o processo e `-o` escolhe as colunas a exibir. Os sinais de igual fazem o comando omitir os cabeçalhos.

```bash
$ ps -p "$$" -o user=,comm=
```

Em um terminal da LabEx, a conta pode ser `labex`. A coluna de comando mostra o nome do programa do shell. Os campos correspondentes de um processo de serviço indicam qual conta ele usa, independentemente de quem o iniciou.

:::single-choice{#linux-service-accounts-process-user} Qual campo indica a conta associada ao processo selecionado?

::option[O ID do processo informado com -p.]{#linux-service-accounts-process-user-a explanation="O ID do processo seleciona um processo em execução."}
::option[O nome do comando na última coluna.]{#linux-service-accounts-process-user-c explanation="Esse campo indica o programa em execução."}
::option[O campo de usuário exibido pelo ps.]{#linux-service-accounts-process-user-b .correct explanation="O campo de usuário mostra a identidade do processo."}
:::

![Saída do ps mostrando o processo do shell da LabEx e sua conta labex](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-service-accounts/shell-identity.png)

## Escolhendo uma identidade dedicada

Imagine um serviço web cujas únicas tarefas sejam ler páginas e gravar seu próprio log. Uma conta dedicada, `site-web`, pode receber essas permissões. Executar o serviço com o acesso mais amplo de um administrador daria ao programa mais formas de alterar o host do que ele precisa.

:::single-choice{#linux-service-accounts-isolate-service} Qual política de acesso é adequada para esse serviço?

::option[Permitir que site-web edite os arquivos de todos os usuários.]{#linux-service-accounts-isolate-service-b explanation="Nenhuma tarefa do serviço requer acesso tão amplo."}
::option[Permitir que site-web leia páginas e grave seu próprio log.]{#linux-service-accounts-isolate-service-a .correct explanation="Essas permissões correspondem às duas tarefas descritas."}
::option[Permitir que site-web atue como administrador em cada requisição.]{#linux-service-accounts-isolate-service-c explanation="A maioria das requisições precisa apenas do acesso restrito do serviço."}
:::

## Verificando vários processos

Alguns serviços têm processos separados para responsabilidades diferentes. Verifique o processo que atende à requisição antes de explicar quais permissões se aplicam a ele. Se você alterar a identidade de execução, confirme que o serviço ainda consegue ler o que precisa e gravar somente o necessário.

:::single-choice{#linux-service-accounts-verify-identity} Uma ferramenta de manutenção informa que o processo supervisor usa root. Como descobrir qual conta atende às requisições web?

::option[Pela identidade do processo de trabalho que atende às requisições.]{#linux-service-accounts-verify-identity-c .correct explanation="Inspecionar o processo relevante associa a conta ao trabalho que ele realmente executa."}
::option[Apenas pelo nome do arquivo de configuração do serviço.]{#linux-service-accounts-verify-identity-a explanation="O nome do arquivo não identifica a conta usada pelo processo em execução."}
::option[Pelo nome de quem abriu o terminal.]{#linux-service-accounts-verify-identity-b explanation="A conta do terminal pode ser diferente da conta do serviço em execução."}
:::

## Resumo

Agora você consegue associar um processo Linux à sua identidade em execução.

1. Encontre o usuário de um processo na saída do ps.
2. Escolha permissões adequadas à tarefa do serviço.
3. Examine o processo relevante quando o serviço tiver vários.
