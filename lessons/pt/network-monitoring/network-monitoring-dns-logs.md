---
lesson_id: "network-monitoring-dns-logs"
course_id: "network-monitoring"
lang: "pt"
order_index: 3
title: "Logs de DNS"
description: "Aprenda a distinguir uma consulta DNS, sua resposta e uma conexão posterior do aplicativo."
meta_title: "Logs de DNS - Monitoramento de redes"
meta_description: "Aprenda a distinguir uma consulta DNS, sua resposta e uma conexão posterior do aplicativo."
meta_keywords: "logs de DNS, resolução de nomes, monitoramento de redes, cibersegurança, Linux Journey"
---

Antes de se conectar a um serviço pelo nome, um cliente pode consultar o DNS para obter um endereço. Um resolvedor pode registrar a consulta e seu resultado. Um **resolvedor** consulta nomes em nome dos clientes.

## Identificando a consulta

Um registro DNS pode conter o horário, o endereço do cliente, o nome e o tipo de registro solicitado. Uma consulta do tipo `A` pede um endereço IPv4.

```text
09:21:00Z client=192.0.2.10 query=site.example type=A result=NOERROR answer=192.0.2.20
09:21:03Z client=192.0.2.10 query=preview.example type=A result=NXDOMAIN
```

O primeiro resultado contém um endereço para `site.example`. O segundo informa que o DNS não encontrou um nome correspondente a `preview.example` nessa consulta.

:::single-choice{#network-monitoring-dns-logs-lookup-name} Qual linha retornou um endereço IPv4 para o nome consultado?

::option[A consulta a site.example.]{#network-monitoring-dns-logs-lookup-name-a .correct explanation="Essa linha traz uma resposta com um endereço IPv4."}
::option[A consulta a preview.example.]{#network-monitoring-dns-logs-lookup-name-b explanation="NXDOMAIN informa que o resolvedor recebeu a indicação de que o nome não existe nessa consulta."}
::option[As duas linhas, porque têm o mesmo cliente.]{#network-monitoring-dns-logs-lookup-name-c explanation="O cliente é o mesmo, mas os resultados das consultas são diferentes."}
:::

## Interpretando o resultado

`NOERROR` indica que a troca de mensagens DNS não relatou erro de protocolo. Confira também o campo da resposta. Uma resposta pode indicar `NOERROR` e não conter um registro de endereço do tipo solicitado. Uma consulta malsucedida também pode aparecer como outro resultado, como tempo de espera esgotado no registro do cliente.

:::single-choice{#network-monitoring-dns-logs-no-answer} Uma linha do DNS mostra NOERROR, mas não traz um endereço na resposta. O que você deve informar?

::option[O cliente necessariamente recebeu um endereço IPv4.]{#network-monitoring-dns-logs-no-answer-a explanation="O campo de resposta informa os endereços retornados na amostra."}
::option[O site certamente recusou uma conexão do navegador.]{#network-monitoring-dns-logs-no-answer-c explanation="Essa linha registra o resultado de uma consulta DNS. A requisição do navegador seria outra operação."}
::option[A troca terminou sem erro de protocolo e essa linha não informa um endereço.]{#network-monitoring-dns-logs-no-answer-b .correct explanation="O campo de resultado e o de resposta dão informações diferentes."}
:::

## Rastreando a conexão posterior

Um cliente pode consultar um nome e depois decidir se fará uma conexão. Para verificar se isso aconteceu, procure um registro de fluxo ou de conexão correspondente. Compare o endpoint e o horário. Resultados DNS podem ficar no cache, por isso algumas conexões ocorrem sem uma nova consulta nos logs disponíveis.

:::single-choice{#network-monitoring-dns-logs-dns-vs-flow} O que indicaria melhor que um cliente depois se conectou ao endereço retornado?

::option[Uma segunda visualização da mesma resposta DNS.]{#network-monitoring-dns-logs-dns-vs-flow-a explanation="A resposta lista um endereço que o cliente pode usar."}
::option[Um registro correspondente de conexão ou de fluxo com o destino.]{#network-monitoring-dns-logs-dns-vs-flow-c .correct explanation="Esse registro acompanha o tráfego posterior à consulta."}
::option[Uma segunda consulta DNS do mesmo cliente.]{#network-monitoring-dns-logs-dns-vs-flow-b explanation="Outra consulta confirma que houve nova resolução de nome. A conexão posterior do aplicativo ainda precisa ser verificada."}
:::

## Resumo

Agora você consegue interpretar um log de DNS e distinguir a consulta da atividade de rede posterior.

1. Identifique o cliente, a consulta e o tipo de registro solicitado.
2. Interprete o resultado junto com a resposta.
3. Procure um registro separado da conexão posterior.
