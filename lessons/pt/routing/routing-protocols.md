---
lang: "pt"
title: "Protocolos de Roteamento"
description: "Aprenda sobre protocolos de roteamento como vetor de distância e estado de link. Entenda a convergência de rede e como os roteadores se adaptam às mudanças. Comece sua jornada em redes Linux!"
keywords: "protocolos de roteamento, convergência de rede, vetor de distância, estado de link, redes Linux, guia para iniciantes, tutorial de rede"
---

## Lesson Content

Seria um incômodo ter que configurar manualmente as rotas em uma tabela de roteamento para cada dispositivo em sua rede. Em vez disso, usamos o que são conhecidos como protocolos de roteamento. Os protocolos de roteamento ajudam nosso sistema a se adaptar às mudanças na rede; eles aprendem diferentes rotas, as constroem na tabela de roteamento e, em seguida, roteiam nossos pacotes dessa forma. Existem dois tipos principais de protocolo de roteamento: protocolos de vetor de distância e protocolos de estado de link.

### Convergence

Antes de falarmos sobre os protocolos, devemos abordar um termo usado em roteamento conhecido como convergence. Ao usar protocolos de roteamento, os roteadores se comunicam com outros roteadores para coletar e trocar informações sobre a rede. Quando eles concordam sobre como uma rede deve ser, cada tabela de roteamento mapeia a topologia completa da rede, assim "converging". Quando algo ocorre na topologia da rede, a convergence será temporariamente quebrada até que todos os roteadores estejam cientes dessa mudança.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual é o termo usado quando todas as tabelas de roteamento conhecem a topologia da rede?

## Quiz Answer

Convergence
