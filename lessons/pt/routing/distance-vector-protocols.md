---
lesson_id: "distance-vector-protocols"
course_id: "routing"
lang: "pt"
order_index: 5
title: "Protocolos de vetor de distância"
description: "Aprenda como protocolos de vetor de distância derivam rotas dos anúncios de vizinhos e limitam loops."
meta_title: "Protocolos de vetor de distância - Roteamento"
meta_description: "Um guia de introdução aos protocolos de vetor de distância no roteamento de redes. Este tutorial explica como protocolos como o RIP usam a contagem de saltos para determinar rotas e apresenta suas limitações nas redes Linux modernas."
meta_keywords: "protocolos de vetor de distância, roteamento de rede, RIP, protocolo de informações de roteamento, contagem de saltos, redes Linux, guia para iniciantes, tutorial"
---

O roteamento por vetor de distância informa aos vizinhos quais destinos estão acessíveis e uma métrica que descreve a distância. Um roteador combina o anúncio de um vizinho com o custo até esse vizinho para derivar seu próprio caminho candidato.

## Aprendendo por meio dos vizinhos

Se o Roteador A anuncia uma distância de três até um prefixo e o Roteador B alcança A com custo um, B pode derivar a distância quatro por A. A informação descreve uma direção e uma métrica, não um mapa completo da topologia; por isso, a abordagem às vezes é chamada de roteamento por rumores.

:::single-choice{#distance-vector-derived-distance}
Se um vizinho anuncia a métrica 3 e o custo do enlace é 1, qual métrica é derivada por ele?

::option[2]{#distance-vector-two explanation="O custo do enlace é somado, não subtraído."}
::option[31]{#distance-vector-thirty-one explanation="Os valores são métricas, não dígitos decimais a serem concatenados."}
::option[4]{#distance-vector-four .correct explanation="A distância do vizinho e o custo do enlace local se combinam para formar o caminho candidato."}
:::

## Loops e contagem até o infinito

Depois de uma falha, vizinhos podem anunciar equivocadamente uma rota de volta um para o outro, aumentando gradualmente sua métrica. Os protocolos atenuam isso com valores finitos de infinito, horizonte dividido, envenenamento de rotas, retorno envenenado, atualizações acionadas e temporizadores. Esses mecanismos reduzem o problema, mas não transformam toda mudança de topologia em uma convergência instantânea.

:::single-choice{#distance-vector-split-horizon}
O que o horizonte dividido pretende reduzir?

::option[A quantidade de bits em cada endereço IPv4.]{#distance-vector-ip-bits explanation="O tamanho dos endereços IPv4 é fixo e independe das atualizações de roteamento."}
::option[A sobrecarga de criptografia nas cargas úteis das aplicações.]{#distance-vector-encryption explanation="A técnica trata da direção do anúncio de rotas."}
::option[O anúncio de uma rota aprendida de volta ao vizinho de onde ela veio.]{#distance-vector-no-return .correct explanation="Suprimir essa direção ajuda a evitar loops simples de realimentação."}
:::

## Métricas e limites do RIP

O RIP usa contagem de saltos. Uma rota com métrica 16 é inacessível, portanto a maior métrica utilizável é 15. Isso limita a escalada dos loops, mas também restringe o diâmetro da rede. Menos saltos não significam necessariamente menor latência ou maior largura de banda.

O RIPv2 usa atualizações periódicas e acionadas e oferece suporte a informações CIDR. Normalmente, ele envia atualizações por multicast em vez de transmitir uma tabela inteira por broadcast em todas as circunstâncias. Autenticação e filtragem ainda exigem configuração deliberada.

:::single-choice{#distance-vector-rip-infinity}
O que a métrica 16 do RIP representa?

::option[O caminho mais rápido com dezesseis enlaces paralelos.]{#distance-vector-fastest-16 explanation="O RIP trata esse valor como inacessível."}
::option[Infinito, indicando que o destino está inacessível.]{#distance-vector-unreachable .correct explanation="O RIP limita os caminhos utilizáveis a 15 saltos."}
::option[Uma rota aprendida pelo BGP.]{#distance-vector-bgp-route explanation="O número possui um significado específico do RIP."}
:::

## Avaliando uma rota aprendida

Verifique o estado dos vizinhos, os prefixos recebidos e anunciados, a métrica, o próximo salto, a instalação da rota e a acessibilidade do plano de dados. Uma rota pode ser válida dentro do RIP, mas perder para outra origem de rota segundo a política local de preferência.

:::single-choice{#distance-vector-fewest-hop-limit}
Por que a rota de menor quantidade de saltos do RIP pode ter um desempenho ruim?

::option[A contagem de saltos não representa a largura de banda, a latência, a perda nem o congestionamento dos enlaces.]{#distance-vector-hop-limited .correct explanation="Um caminho com mais saltos pode ter enlaces melhores e um desempenho superior para a aplicação."}
::option[O RIP sempre escolhe a rota com mais saltos.]{#distance-vector-most-hops explanation="Sua métrica prefere contagens menores de saltos utilizáveis."}
::option[A contagem de saltos é medida em bytes de espaço em disco.]{#distance-vector-disk-bytes explanation="Ela conta transições roteadas, não armazenamento."}
:::

## Resumo

Agora você pode explicar tanto a simplicidade quanto as limitações do roteamento por vetor de distância.

1. Derive a distância candidata a partir do anúncio de um vizinho.
2. Reconheça o comportamento de loops e contagem até o infinito.
3. Explique o limite utilizável de 15 saltos do RIP e a métrica 16.
4. Verifique separadamente a instalação da rota e o resultado no plano de dados.
