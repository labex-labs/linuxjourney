---
lesson_id: "cron-jobs"
course_id: "process-utilization"
lang: "pt"
order_index: 8
title: "Tarefas Cron"
description: "Aprenda a criar, inspecionar, testar e operar com segurança tarefas recorrentes com cron."
meta_title: "Tarefas Cron - Utilização de Processos"
meta_description: "Aprenda a agendar tarefas e automatizar scripts no Linux usando cron. Este guia aborda a sintaxe do crontab, comandos essenciais como crontab -e e exemplos práticos."
meta_keywords: "tarefas cron, crontab, agendar tarefas, automação Linux, comandos Linux, Linux para iniciantes, tutorial Linux, crontab -e, cron"
---

O cron executa comandos em agendas recorrentes sem um shell interativo. A automação repete tanto os comportamentos corretos quanto os erros, portanto teste o comando, use caminhos explícitos, restrinja os privilégios e planeje o registro e a notificação de falhas antes de agendá-lo.

## Leitura de uma Entrada do Crontab

Uma entrada do crontab de um usuário contém cinco campos de tempo seguidos por um comando:

```cron
30 8 * * * /home/pete/scripts/change_wallpaper
```

Da esquerda para a direita, os campos são minuto, hora, dia do mês, mês e dia da semana. Esse exemplo é executado às 08:30 conforme o fuso horário aplicável ao daemon cron. Um asterisco significa todos os valores permitidos naquele campo.

Quando os campos de dia do mês e dia da semana estão restritos, muitas implementações do cron executam quando qualquer um deles corresponde. Confirme a semântica local antes de criar uma agenda que use os dois.

:::single-choice{#cron-daily-eight-thirty} Quando `30 8 * * * command` é executado?

::option[A cada 30 minutos durante oito horas.]{#cron-every-thirty explanation="Os campos são posições em uma agenda, não uma expressão de duração."}
::option[Às 08:30 todos os dias.]{#cron-eight-thirty .correct explanation="O minuto 30 e a hora 8 são fixos, enquanto os três campos de data permitem todos os valores."}
::option[Às 30:08 no oitavo dia de cada mês.]{#cron-invalid-time explanation="As horas variam de 0 a 23, e o exemplo não restringe o dia do mês."}
:::

## Gerenciamento do Crontab de um Usuário

Edite o crontab do usuário atual com:

```bash
$ crontab -e
```

Liste as entradas instaladas antes e depois de uma alteração:

```bash
$ crontab -l
```

`crontab -r` remove todo o crontab do usuário e pode fazer isso sem abrir um editor. Não o use para remover uma única linha; edite o crontab e verifique as entradas restantes.

:::single-choice{#cron-list-current-user} Qual comando lista as entradas cron instaladas do usuário atual?

::option[`crontab -l`]{#cron-list .correct explanation="A opção de listagem imprime as entradas instaladas para inspeção."}
::option[`crontab -r`]{#cron-remove-all explanation="Essa opção remove o crontab, em vez de exibi-lo."}
::option[`crontab -e`]{#cron-edit explanation="Essa opção abre o crontab para edição, em vez de apenas listá-lo."}
:::

## Consideração do Ambiente do Cron

O cron normalmente fornece um ambiente limitado e um shell não interativo. Use caminhos absolutos de comandos e arquivos, defina explicitamente as variáveis necessárias e não dependa de aliases, do diretório atual de um terminal ou de arquivos de inicialização do shell.

Redirecione a saída e o erro padrão para um log controlado ou use um mecanismo de notificação adequado ao sistema. Proteja as credenciais com permissões restritivas e evite incorporar segredos diretamente a um comando do crontab.

:::single-choice{#cron-absolute-paths} Por que um comando cron deve usar caminhos e configurações de ambiente explícitos?

::option[O cron sempre é executado dentro do terminal atual do usuário.]{#cron-current-terminal explanation="As tarefas agendadas são executadas independentemente de uma sessão interativa."}
::option[Caminhos absolutos fazem todos os comandos serem executados como root.]{#cron-path-root explanation="Os caminhos selecionam arquivos, mas não concedem privilégios."}
::option[O ambiente do cron pode ser diferente do shell interativo.]{#cron-limited-environment .correct explanation="Dependências explícitas evitam falhas causadas por suposições sobre PATH, diretório ou arquivos de inicialização."}
:::

## Testes e Prevenção de Sobreposição

Execute o script manualmente como o mesmo usuário, com um ambiente igualmente mínimo. Faça-o retornar status de saída úteis e registrar resultados com timestamps. Após a instalação, aguarde uma agenda de teste inofensiva ou uma execução controlada e verifique o efeito real e os logs.

Se uma execução puder durar mais que seu intervalo, projete-a para concorrência ou use um mecanismo de bloqueio, como `flock`, quando disponível:

```cron
*/5 * * * * /usr/bin/flock -n /run/user/1000/report.lock /home/pete/bin/report
```

Escolha um caminho de bloqueio que o usuário da tarefa possa criar com segurança e decida se execuções ignoradas são aceitáveis. O cron não garante automaticamente que apenas uma instância seja executada.

:::single-choice{#cron-overlapping-runs} Qual risco existe quando uma tarefa demora mais que o intervalo de sua agenda?

::option[Várias instâncias podem se sobrepor e disputar recursos.]{#cron-overlap .correct explanation="O cron pode iniciar uma nova ocorrência enquanto o processo anterior ainda está em execução."}
::option[Os cinco campos da agenda recebem automaticamente um sexto campo de bloqueio.]{#cron-auto-lock explanation="A sintaxe do crontab não acrescenta exclusão mútua automática."}
::option[O script é convertido permanentemente em uma thread do kernel.]{#cron-kernel-thread explanation="Agendar um comando não altera seu modelo de processos dessa forma."}
:::

## Escolha do Agendador Adequado

O cron é apropriado para comandos recorrentes simples. Os timers do systemd podem oferecer integração de dependências, execução posterior persistente, atraso aleatório e registro no journal em hosts com systemd. Agendadores de aplicações ou clusters podem ser mais seguros quando uma tarefa precisa ser executada exatamente uma vez em várias máquinas.

:::single-choice{#cron-cluster-exactly-once} Por que o cron comum por host pode ser inadequado para uma tarefa de cluster executada exatamente uma vez?

::option[Toda entrada cron é limitada a um caractere.]{#cron-one-character explanation="Os comandos do crontab podem conter linhas de comando comuns."}
::option[Cada host pode iniciar independentemente sua própria cópia.]{#cron-each-host .correct explanation="É necessário um mecanismo de coordenação distribuído para garantir uma única execução entre os hosts."}
::option[O cron não pode executar scripts armazenados no disco.]{#cron-no-scripts explanation="A execução de scripts é um caso de uso comum do cron."}
:::

## Resumo

Agora você sabe operar uma tarefa cron recorrente com suposições explícitas de agenda e execução.

1. Leia os cinco campos de tempo em sua ordem definida.
2. Inspecione e edite crontabs de usuários sem excluir tarefas não relacionadas.
3. Defina caminhos, ambiente, registro e tratamento de credenciais.
4. Teste como o usuário da tarefa e proteja contra sobreposições indesejadas.
5. Escolha um agendador adequado aos requisitos do host e de coordenação.
