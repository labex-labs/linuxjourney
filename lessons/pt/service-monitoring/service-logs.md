---
lesson_id: "service-logs"
course_id: "service-monitoring"
lang: "pt"
order_index: 2
title: "Logs de serviço"
description: "Aprenda a acompanhar uma requisição nos logs de diferentes serviços usando seu identificador e horário."
meta_title: "Logs de serviço - Monitoramento de serviços"
meta_description: "Aprenda a acompanhar uma requisição nos logs de diferentes serviços usando seu identificador e horário."
meta_keywords: "logs de serviço, ID de requisição, monitoramento de serviços, DevOps, Linux Journey"
---

Um usuário vê um erro. O log de um serviço pode indicar em que ponto a requisição falhou. Comece pelo horário e procure o **ID da requisição**, um identificador que acompanha os registros da mesma requisição.

## Lendo uma requisição

A amostra abaixo mostra dois serviços. Uma **dependência** é um serviço de que outro programa precisa para concluir seu trabalho. Aqui, o serviço web pede uma lista de itens ao serviço de catálogo.

```text
09:14:02 service=web     request=r17 path=/items status=502
09:14:02 service=catalog request=r17 action=read result=timeout
09:14:03 service=catalog request=r18 action=read result=ok
```

A linha do serviço web mostra uma falha na resposta de `r17`. A linha do catálogo com o mesmo ID registra que o tempo de espera se esgotou. A requisição ao catálogo que funcionou em um horário próximo corresponde à `r18`.

:::single-choice{#service-logs-matching-request} Qual resultado do catálogo corresponde à falha do serviço web para r17?

::option[O resultado bem-sucedido de r18.]{#service-logs-matching-request-a explanation="Essa linha pertence a outra requisição."}
::option[Os dois resultados do catálogo.]{#service-logs-matching-request-c explanation="Horários próximos podem corresponder a requisições diferentes."}
::option[O tempo de espera esgotado de r17.]{#service-logs-matching-request-b .correct explanation="O ID em comum liga os dois registros da mesma requisição."}
:::

## Filtrando a amostra

Salve as três linhas acima como `requests.log` em um diretório de prática. Use `grep -F` para buscar texto literal. Inclua o espaço depois do identificador para fazer a correspondência até o fim do campo nesta amostra.

```bash
$ grep -F 'request=r17 ' requests.log
```

Você deve ver as linhas do serviço web e do catálogo para `r17`. Logs reais podem usar formatos diferentes ou omitir o ID da requisição. Confirme que os campos que você pesquisa representam a mesma informação em todos os serviços.

:::single-choice{#service-logs-choose-filter} Por que incluir o campo inteiro da requisição na busca, em vez de procurar a palavra timeout?

::option[Isso garante que todo o tráfego apresentou o mesmo erro.]{#service-logs-choose-filter-b explanation="O filtro seleciona os registros de uma requisição."}
::option[A busca retorna os registros correspondentes do serviço web e do catálogo, embora só um contenha timeout.]{#service-logs-choose-filter-a .correct explanation="O ID em comum permite acompanhar a requisição nos dois serviços."}
::option[Isso altera o log para que buscas futuras encontrem o resultado correto.]{#service-logs-choose-filter-c explanation="O grep lê o arquivo e imprime as linhas correspondentes."}
:::

![Saída do grep relacionando o erro do serviço web ao tempo de espera esgotado no catálogo para a requisição r17](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-logs/request-id.png)

## Delimitando o relato

O tempo de espera esgotado mostra onde essa requisição encontrou uma falha. Ainda é preciso identificar qual componente interno do catálogo ficou lento. Em seguida, examine as métricas ou os registros recentes da dependência. Ao compartilhar um trecho do log com a equipe, preserve o ID da requisição e remova segredos ou dados pessoais desnecessários.

:::single-choice{#service-logs-evidence-limit} O que você deve informar no primeiro relato?

::option[O tempo de espera do catálogo se esgotou durante r17 e precisa ser investigado.]{#service-logs-evidence-limit-c .correct explanation="Isso resume os registros correspondentes sem presumir a causa da falha."}
::option[O tempo de espera se esgotou em todas as requisições ao catálogo.]{#service-logs-evidence-limit-a explanation="A amostra inclui outra requisição ao catálogo que funcionou."}
::option[Um disco específico do banco de dados falhou.]{#service-logs-evidence-limit-b explanation="Os registros não trazem observações sobre discos."}
:::

Para praticar a consulta aos registros de serviço em um host Linux, faça o exercício [Análise de logs para resposta a incidentes](https://labex.io/labs/linux-monitoring-and-incident-response-log-analysis-594586).

## Resumo

Agora você consegue acompanhar uma requisição nos logs de vários serviços.

1. Encontre o mesmo ID de requisição nos registros relevantes.
2. Use um filtro literal para reduzir a amostra.
3. Relate o que os registros sustentam e formule a próxima pergunta.
