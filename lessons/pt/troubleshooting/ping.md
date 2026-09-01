---
lesson_id: "ping"
course_id: "troubleshooting"
lang: "pt"
order_index: 2
title: "ping"
description: "Aprenda a executar testes de ping limitados e interpretar respostas, perdas, RTT, TTL e limitações."
meta_title: "ping - Solução de Problemas"
meta_description: "Aprenda a usar o comando ping do Linux para testar a conectividade de rede. Este guia explica a saída do ping, incluindo o significado de icmp_seq, TTL e tempo de ida e volta. Entenda como interpretar a sequência (seq) do ping para diagnosticar problemas de rede."
meta_keywords: "ping Linux, conectividade de rede, ICMP, TTL, comando ping, icmp_seq, sequência ping, seq icmp, significado icmp_seq, ping icmp_seq, rede Linux"
---

`ping` envia ICMP Echo Requests e informa respostas observadas. Ele testa um caminho de mensagem de controle até um endereço; não prova que TCP, UDP, DNS, autenticação ou um aplicativo funcionem.

## Execução de um teste limitado

Envie três solicitações IPv4 com timeout de dois segundos em implementações iputils comuns:

```bash
$ ping -4 -c 3 -W 2 example.com
```

Use `-6` para IPv6. Registre o endereço resolvido, pois um nome pode retornar vários e execuções posteriores escolherem outro.

:::single-choice{#ping-count-option} O que `-c 3` solicita?

::option[Um payload de exatamente três megabytes.]{#ping-three-megabytes explanation="O tamanho usa outra opção."}
::option[Três rotas permanentes até o destino.]{#ping-three-routes explanation="Ping faz sondagens e não instala rotas."}
::option[Três Echo Requests antes de parar normalmente.]{#ping-three-requests .correct explanation="Uma contagem finita torna o diagnóstico limitado e repetível."}
:::

## Sequência e perda

`icmp_seq` identifica solicitações na execução. Respostas ausentes contribuem para a perda observada; respostas fora de ordem podem indicar atrasos diferentes. Amostras pequenas são ruidosas; compare intervalos limitados e a taxa de erros do aplicativo.

A perda pode ocorrer em qualquer direção, e rate limiting ICMP pode diferir da perda do aplicativo.

:::single-choice{#ping-sequence-gap} O que uma resposta `icmp_seq` ausente pode indicar?

::option[O destino mudou permanentemente seu MAC.]{#ping-sequence-mac explanation="Uma lacuna sozinha não sustenta essa conclusão."}
::option[Solicitação ou resposta perdida, filtrada, atrasada além da espera ou limitada.]{#ping-sequence-possibilities .correct explanation="A lacuna identifica uma resposta não observada, não a direção ou causa exata."}
::option[O disco de origem ficou sem inodes.]{#ping-sequence-inodes explanation="Inodes não têm relação com a sequência ICMP."}
:::

## Tempo de ida e volta

O campo `time` é o round-trip time em milissegundos, do envio à resposta. Combina atraso de ida, processamento remoto e retorno. Não revela latência de uma direção sem medições sincronizadas nas pontas.

:::single-choice{#ping-rtt-meaning} O que `time=23.7 ms` mede?

::option[Apenas a latência de ida.]{#ping-outbound-only explanation="Ping mede o intervalo completo de solicitação e resposta."}
::option[O tempo de atividade do alvo.]{#ping-target-uptime explanation="O valor é o tempo da sondagem, não do boot."}
::option[O tempo de ida e volta desse eco.]{#ping-round-trip .correct explanation="Ele inclui as duas direções e o tratamento no endpoint."}
:::

## TTL ou Hop Limit

O TTL IPv4 ou Hop Limit IPv6 exibido é o valor restante na resposta recebida. Sem conhecer o valor inicial e a rota de retorno, subtraí-lo não dá a contagem exata de saltos. Uma mudança pode refletir outro respondedor, valor inicial ou caminho.

:::single-choice{#ping-received-ttl} O que é o TTL impresso numa Echo Reply IPv4?

::option[O valor restante quando a resposta chegou ao host local.]{#ping-remaining-ttl .correct explanation="Cada roteador no retorno decrementou o valor inicial do remetente."}
::option[Uma contagem exata de roteadores nas duas direções.]{#ping-exact-hop-count explanation="O valor inicial e os caminhos direcionais não são conhecidos."}
::option[O tempo de cache do registro DNS.]{#ping-dns-ttl explanation="TTL do DNS e do pacote IP são campos diferentes."}
:::

## Teste da camada correta

Se ping funciona e o serviço falha, teste porta, TLS, protocolo e solicitação reais. Se ping falha, examine resolução, `ip route get`, vizinhos, firewall e capturas antes de declarar o host desligado.

:::single-choice{#ping-success-limit} O que um ping bem-sucedido não prova?

::option[Que algum caminho ICMP de solicitação e resposta funcionou.]{#ping-icmp-worked explanation="Essa é a evidência direta das respostas."}
::option[Que a resposta tinha número de sequência.]{#ping-sequence-present explanation="A saída normal informa a sequência."}
::option[Que o aplicativo pretendido aceita e conclui solicitações.]{#ping-app-not-proven .correct explanation="O comportamento do aplicativo exige teste apropriado à aplicação."}
:::

## Resumo

Agora você consegue usar ping como medição ICMP limitada e com limites explícitos.

1. Selecionar a família e registrar o endereço resolvido.
2. Limitar contagem e espera para testes repetíveis.
3. Interpretar perda sem presumir direção ou causa.
4. Tratar RTT como ida e volta e TTL como valor restante.
5. Testar separadamente o aplicativo real.
