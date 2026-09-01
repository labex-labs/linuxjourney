---
lesson_id: "authentication-logging"
course_id: "logging"
lang: "pt"
order_index: 5
title: "Registro de Autenticação"
description: "Aprenda a localizar, interpretar e correlacionar com segurança registros de autenticação do Linux."
meta_title: "Registro de Autenticação - Logs"
meta_description: "Explore o registro de autenticação do Linux examinando o arquivo /var/log/auth.log. Este guia ajuda iniciantes a entender eventos de login de usuário, métodos de autenticação e como solucionar problemas de acesso para melhor segurança no Linux."
meta_keywords: "autenticação Linux, auth.log, logs Linux, login de usuário, segurança Linux, autorização de sistema, solucionar login, métodos de autenticação, iniciante, tutorial, guia, log seguro"
---

Logs de autenticação ajudam a explicar tentativas de login, mudanças de privilégio e atividade de sessões. São evidências sensíveis, mas uma única linha raramente demonstra a intenção de uma pessoa ou prova comprometimento da conta.

## Localização dos registros de autenticação

Configurações syslog da família Debian normalmente enviam eventos a `/var/log/auth.log`; as da família Red Hat costumam usar `/var/log/secure`. O journal pode guardar os mesmos eventos com metadados, e um coletor central pode ter a cópia oficial.

Descubra o destino local e consulte o serviço relevante:

```bash
$ sudo journalctl -u ssh.service --since '1 hour ago'
$ sudo less /var/log/auth.log
```

A unit pode se chamar `ssh.service` ou `sshd.service`. O acesso costuma ser restrito porque os registros expõem contas e detalhes de acesso.

:::single-choice{#auth-logs-file-location} Onde os eventos de autenticação Linux devem sempre ser armazenados?

::option[No destino escolhido pela política local de logging.]{#auth-logs-local-policy .correct explanation="Arquivos, journal e coletores centralizados variam por distribuição e configuração."}
::option[Em `/var/log/auth.log` em toda distribuição.]{#auth-logs-auth-only explanation="Esse caminho é comum na família Debian, mas não é universal."}
::option[No histórico do shell de cada usuário.]{#auth-logs-shell-history explanation="O histórico contém comandos do usuário, não o armazenamento de eventos de autenticação."}
:::

## Interpretação de um evento

Um registro tradicional pode conter:

```text
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

Ele identifica horário, host, programa, módulo e serviço PAM, usuário solicitado e UID de origem. Sozinho, não identifica a pessoa por trás do UID 1000 nem prova malícia. Resolva o UID conforme as contas válidas na data e correlacione terminal, endereço remoto, sessão e eventos próximos.

:::single-choice{#auth-logs-uid-inference} O que `uid=1000` estabelece nesse registro?

::option[Que a senha root foi digitada errada mil vezes.]{#auth-logs-thousand-passwords explanation="O valor é um identificador, não uma contagem de tentativas."}
::option[A identidade numérica da conta associada ao processo iniciador.]{#auth-logs-numeric-identity .correct explanation="Outras evidências de sessão e conta são necessárias para atribuir a ação a uma pessoa."}
::option[Que o evento veio da porta TCP 1000.]{#auth-logs-port explanation="UID não é um campo de porta de rede."}
:::

## Investigação de sucesso e falha

Pesquise tentativas aceitas e rejeitadas num intervalo limitado. Para SSH, examine fonte, método, conta-alvo, abertura e fechamento da sessão e reinícios do serviço. Falhas repetidas podem ser erro do usuário, automação com credenciais antigas, varredura ou ataque; a frequência sozinha não decide.

`last` e `lastb` podem resumir `wtmp` e `btmp`, quando mantidos, mas esses bancos binários têm limites de retenção e integridade. Compare-os com journal, syslog e fontes centralizadas.

:::single-choice{#auth-logs-failed-attempts} Com o que tentativas repetidas de login devem ser correlacionadas?

::option[Apenas com o espaço livre total do disco.]{#auth-logs-disk-space explanation="A capacidade não identifica fonte, alvo ou método."}
::option[Com fonte, conta-alvo, método, horário e sessões bem-sucedidas.]{#auth-logs-correlated-fields .correct explanation="Esses detalhes ajudam a distinguir erro, configuração, varredura e acesso indevido."}
::option[Com a conclusão de que a conta certamente foi comprometida.]{#auth-logs-certain-compromise explanation="Falhas podem ter causas benignas ou hostis."}
:::

## Preservação e resposta

Se houver suspeita de incidente, registre hora e fuso do host, preserve logs originais e metadados e proteja as cópias. Não edite evidências. Bloquear contas, mudar firewall e encerrar sessões pode interromper acesso legítimo ou alertar um invasor; siga o processo de resposta e mantenha recuperação.

:::single-choice{#auth-logs-preservation} Como tratar evidências de autenticação durante uma investigação?

::option[Editar linhas suspeitas no arquivo original para maior clareza.]{#auth-logs-edit-original explanation="Alterar a fonte compromete a integridade da evidência."}
::option[Publicar o log completo para que todos identifiquem os usuários.]{#auth-logs-publish explanation="Os registros podem expor identidades e detalhes da infraestrutura."}
::option[Preservar os originais e proteger as cópias exportadas.]{#auth-logs-preserve .correct explanation="Integridade e confidencialidade são essenciais para logs de segurança."}
:::

## Resumo

Agora você consegue examinar autenticações sem exagerar o que um registro prova.

1. Descobrir o destino local dos logs de autenticação.
2. Interpretar identidade, serviço, método e sessão no contexto.
3. Correlacionar falhas e sucessos entre fontes retidas.
4. Preservar evidências e coordenar respostas disruptivas.
