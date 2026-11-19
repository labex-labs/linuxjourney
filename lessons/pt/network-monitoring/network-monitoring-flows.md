---
lesson_id: "network-monitoring-flows"
course_id: "network-monitoring"
lang: "pt"
order_index: 2
title: "Fluxos de rede"
description: "Aprenda a interpretar endereços, portas, horários e contagens de bytes em um resumo de fluxo."
meta_title: "Fluxos de rede - Monitoramento de redes"
meta_description: "Aprenda a interpretar endereços, portas, horários e contagens de bytes em um resumo de fluxo."
meta_keywords: "fluxos de rede, contagem de bytes, monitoramento de redes, cibersegurança, Linux Journey"
---

Um **fluxo** agrupa tráfego com propriedades em comum, como endereços de rede, portas e protocolo. Os sistemas de monitoramento podem contar os bytes ou pacotes de um fluxo sem guardar todo o conteúdo.

## Lendo os dois endpoints

Neste resumo simulado, o coletor registra o sentido da comunicação da origem ao destino. Protocolos de transporte como o TCP incluem números de porta, que podem identificar um socket em escuta no lado que recebe.

```text
start=09:21:00Z protocol=TCP src=192.0.2.10:51600 dst=192.0.2.20:443 bytes=1800
start=09:21:00Z protocol=TCP src=192.0.2.20:443 dst=192.0.2.10:51600 bytes=8200
```

A primeira linha segue em direção à porta 443. A segunda mostra o sentido inverso. Alguns coletores agrupam os dois sentidos, por isso confira o formato que você está lendo.

:::single-choice{#network-monitoring-flows-endpoint-direction} Na primeira linha, qual endereço e porta recebem o tráfego registrado?

::option[192.0.2.10:51600.]{#network-monitoring-flows-endpoint-direction-a explanation="Esse é o endpoint de origem no primeiro sentido."}
::option[Os dois endpoints listados são destinos.]{#network-monitoring-flows-endpoint-direction-c explanation="Cada linha da amostra registra um único sentido."}
::option[192.0.2.20:443.]{#network-monitoring-flows-endpoint-direction-b .correct explanation="O campo de destino indica para onde o tráfego foi enviado."}
:::

## Comparando as contagens

A amostra mostra mais bytes no sentido que sai da porta 443. Uma resposta maior pode ser normal para uma página web. A contagem, por si só, não informa o conteúdo da página, a conta nem o motivo desse volume.

:::single-choice{#network-monitoring-flows-byte-count} O que os 8.200 bytes da segunda linha descrevem?

::option[O texto exato da mensagem de resposta.]{#network-monitoring-flows-byte-count-b explanation="O resumo de fluxo informa o volume sem incluir a mensagem."}
::option[O volume registrado naquele sentido.]{#network-monitoring-flows-byte-count-a .correct explanation="A contagem de bytes resume o tráfego. A origem e o destino identificam seu sentido."}
::option[A garantia de que a página abriu com sucesso.]{#network-monitoring-flows-byte-count-c explanation="O volume não informa o resultado HTTP."}
:::

## Acrescentando contexto

Use o que você sabe sobre o serviço e o horário para decidir quais fluxos são relevantes. Se precisar saber o que o servidor web retornou, consulte os logs de acesso do mesmo horário e da mesma conexão, quando disponíveis.

:::single-choice{#network-monitoring-flows-next-source} Você quer saber o status HTTP da requisição web. Qual fonte adicional ajudaria?

::option[Um registro de acesso web correspondente.]{#network-monitoring-flows-next-source-c .correct explanation="O registro de acesso do servidor pode informar o resultado HTTP."}
::option[A contagem de bytes do fluxo arredondada para a centena mais próxima.]{#network-monitoring-flows-next-source-a explanation="O arredondamento muda a precisão sem informar o status da resposta."}
::option[Um segundo resumo de fluxo para os mesmos endpoints.]{#network-monitoring-flows-next-source-b explanation="Outro resumo de fluxo pode confirmar mais observações de tráfego. Normalmente ele não informa o status da resposta HTTP."}
:::

## Resumo

Agora você consegue interpretar os principais campos de um resumo de fluxo.

1. Encontre os endereços e as portas dos endpoints.
2. Interprete a contagem de bytes no sentido informado.
3. Use outra fonte quando precisar do resultado no aplicativo.
