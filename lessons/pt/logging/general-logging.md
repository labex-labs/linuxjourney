---
lesson_id: "general-logging"
course_id: "logging"
lang: "pt"
order_index: 3
title: "Registro Geral"
description: "Aprenda a descobrir, filtrar, acompanhar e correlacionar logs gerais de sistemas Linux."
meta_title: "Registro Geral - Logging"
meta_description: "Um guia para iniciantes sobre logs gerais do Linux. Aprenda sobre /var/log/messages e syslog para monitoramento eficaz do sistema, análise de logs e solução de problemas no Linux."
meta_keywords: "logs Linux, syslog, var/log/messages, solução de problemas Linux, logs do sistema, análise de logs, monitoramento do sistema, guia Linux, iniciante Linux, /var/log"
---

Logs gerais combinam avisos rotineiros, alertas e erros de várias fontes. São bons pontos de partida, mas nomes e conteúdo dos arquivos são escolhas da política de roteamento, não garantias universais do Linux.

## Localização da fonte relevante

Conforme distribuição e configuração, mensagens gerais podem aparecer em `/var/log/syslog`, `/var/log/messages`, no journal ou em vários destinos. Primeiro identifique o host e o intervalo do incidente, depois examine as fontes:

```bash
$ ls -lh /var/log
$ journalctl --since '2026-08-31 09:00' --until '2026-08-31 09:15'
```

Logs de aplicativos podem ficar em subdiretórios próprios ou serviços externos. Registros de autenticação, auditoria, pacotes, banco de dados e servidor web podem ser separados do fluxo geral.

:::single-choice{#general-logs-universal-file}
Por que não se deve presumir que `/var/log/messages` exista em todo host Linux?

::option[Os destinos dependem dos coletores e da política local.]{#general-logs-local-routing .correct explanation="Um sistema apenas com journal ou outra configuração syslog pode usar destinos diferentes."}
::option[O Linux permite apenas um arquivo de log por disco.]{#general-logs-one-file explanation="Sistemas mantêm rotineiramente vários arquivos e armazenamentos de journal."}
::option[O caminho é reservado exclusivamente a documentos pessoais.]{#general-logs-user-documents explanation="A hierarquia `/var/log` é convencionalmente usada para logs."}
:::

## Inspeção de logs de texto

Use `less` para navegação controlada e `tail` para os registros mais novos:

```bash
$ sudo less /var/log/syslog
$ sudo tail -n 100 /var/log/messages
```

Acompanhe linhas novas durante uma reprodução limitada com `tail -F FILE`. `-F` tenta novamente quando o arquivo é substituído na rotação. Pare com `Ctrl-C` e não deixe sessões privilegiadas amplas abertas.

:::single-choice{#general-logs-tail-f-capability}
Para que `tail -F` é útil durante uma reprodução controlada?

::option[Acompanhar um arquivo pelo nome quando ele é substituído na rotação.]{#general-logs-tail-follow .correct explanation="A repetição por nome permite continuar quando o arquivo ativo é renomeado e recriado."}
::option[Mudar a gravidade de todo log para debug.]{#general-logs-tail-debug explanation="Tail lê conteúdo e não reconfigura as fontes."}
::option[Descriptografar arquivos comprimidos sem outra ferramenta.]{#general-logs-tail-decrypt explanation="Ele não oferece descompactação ou descriptografia geral."}
:::

## Filtragem sem perder o contexto

Pesquise um arquivo ou intervalo limitado, em vez de canalizar imediatamente um fluxo ilimitado:

```bash
$ grep -n -C 3 'connection refused' /var/log/example.log
$ journalctl -u example.service --since '10 minutes ago' --grep='connection refused'
```

Maiúsculas, redação, limites de frequência e localização podem tornar a busca literal incompleta. Registre eventos bem-sucedidos e falhos e mantenha as linhas próximas, pois a causa pode preceder o erro visível.

:::single-choice{#general-logs-context-lines}
Por que incluir linhas ao redor de um erro encontrado?

::option[Um evento anterior pode explicar a falha posterior.]{#general-logs-preceding-context .correct explanation="O contexto temporal ajuda a reconstruir a sequência, em vez de tratar uma string como todo o incidente."}
::option[O contexto garante que o primeiro resultado seja a causa.]{#general-logs-guaranteed-cause explanation="Ainda é preciso correlacionar evidências; contexto não prova causalidade."}
::option[Ele altera automaticamente a configuração do serviço.]{#general-logs-context-config explanation="A saída da busca é somente leitura."}
:::

## Inclusão de logs rotacionados

Um incidente pode atravessar o limite de uma rotação. Arquivos ativos, arquivos numerados e arquivos comprimidos podem conter partes diferentes da mesma sequência. Ferramentas como `zgrep` e `zless` leem arquivos comprimidos com gzip:

```bash
$ sudo zgrep -n 'connection refused' /var/log/example.log*.gz
```

Ordene pelos horários reais, não apenas pelos sufixos. Antes de copiar evidências, preserve metadados e restrinja acesso, pois logs podem conter dados pessoais ou credenciais.

:::single-choice{#general-logs-rotation-boundary}
O que verificar quando um incidente atravessa uma rotação?

::option[Apenas o novo arquivo ativo vazio.]{#general-logs-active-only explanation="Registros anteriores podem ter sido movidos para arquivos rotacionados."}
::option[Logs ativos e arquivados ordenados pelo horário dos eventos.]{#general-logs-all-intervals .correct explanation="A sequência relevante pode estar dividida entre arquivos atuais e antigos."}
::option[Apenas nomes de arquivo, independentemente dos horários.]{#general-logs-filenames-only explanation="A ordem dos sufixos nem sempre equivale ao tempo dos eventos."}
:::

## Resumo

Agora você consegue investigar logs gerais em arquivos, journals e limites de rotação.

1. Descobrir destinos em vez de presumir um nome universal.
2. Ler um intervalo limitado e acompanhar apenas durante a reprodução.
3. Manter o contexto temporal ao redor dos registros.
4. Incluir arquivos rotacionados e proteger evidências sensíveis.
