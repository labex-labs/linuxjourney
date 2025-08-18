---
lang: "pt"
title: "CIDR"
meta_description: "Aprenda a notação CIDR para redes Linux. Entenda máscaras de sub-rede, endereçamento IP e cálculo de hosts com este guia amigável para iniciantes. Melhore suas habilidades de rede!"
meta_keywords: "CIDR, máscara de sub-rede, endereçamento IP, prefixo de rede, rede Linux, iniciante, tutorial, guia"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) é usado para representar uma máscara de sub-rede de uma forma mais compacta. Você pode ver sub-redes anotadas na notação CIDR, onde uma sub-rede como 10.42.3.0/255.255.255.0 é escrita como 10.42.3.0/24. Esta notação inclui tanto o prefixo da sub-rede quanto a máscara da sub-rede.

Lembre-se, um endereço IP consiste em 4 bytes ou 32 bits. O CIDR indica o número de bits usados como prefixo de rede. Assim, 123.12.24.0/23 significa que os primeiros 23 bits são usados. O que isso significa? Quantos hosts isso representa?

Um truque simples é subtrair o endereço CIDR (23) do número total de bits que um endereço IP pode ter (32). Isso deixa 9 bits. Portanto, 2^9 = 512. No entanto, devemos remover 2 endereços (o endereço da sub-rede e o endereço de broadcast), então temos 510 hosts utilizáveis.

## Exercise

No exercises for this lesson.

## Quiz Question

No questions, move along!

## Quiz Answer
