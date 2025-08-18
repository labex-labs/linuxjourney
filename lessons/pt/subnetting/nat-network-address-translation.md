---
lang: "pt"
title: "NAT"
meta_description: "Aprenda sobre NAT (Network Address Translation) no Linux, como funciona e seu papel na segurança da rede. Entenda IPs privados vs. públicos. Guia de rede Linux."
meta_keywords: "NAT, Network Address Translation, rede Linux, IP privado, IP público, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Já mencionamos NAT (Network Address Translation) antes, mas não abordamos o assunto. Quando estamos trabalhando em nossa rede, isso significa que a internet pode ver nosso endereço IP? Não exatamente.

NAT faz com que um dispositivo como nosso roteador atue como um intermediário entre a internet e uma rede privada. Assim, apenas um único e exclusivo endereço IP é necessário para representar um grupo inteiro de computadores.

Pense no NAT como uma recepcionista em um grande escritório. Se alguém quiser contatá-lo, eles só conhecem o número de todo o escritório. A recepcionista teria então que procurar seu número de ramal e encaminhar a chamada para você.

### How does it work?

Um caso simples seria assim:

1. Patty quer se conectar a <www.google.com>, então sua máquina envia esta solicitação através do roteador.
2. O roteador pega essa solicitação e abre sua própria conexão para google.com, então ele envia a solicitação de Patty assim que faz uma conexão.
3. O roteador é o intermediário entre Patty e <www.google.com>. O Google não sabe sobre Patty; em vez disso, tudo o que pode ver é o roteador.

NAT e o roteamento de pacotes em geral podem ficar bem complicados, mas não vamos nos aprofundar nos detalhes.

## Exercise

No exercises for this lesson.

## Quiz Question

O que é usado para representar um único endereço privado para a internet?

## Quiz Answer

NAT
