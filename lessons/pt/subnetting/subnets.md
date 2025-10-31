---
index: 2
lang: "pt"
title: "Sub-redes"
meta_title: "Sub-redes - Sub-redes (Subnetting)"
meta_description: "Domine os fundamentos de sub-rede e máscara de sub-rede no Linux. Este guia explica sub-redes, prefixos de rede e como gerenciar a segmentação de rede em um ambiente Linux com sub-redes."
meta_keywords: "subnet linux, sub-rede linux, máscara de sub-rede linux, sub-redes, sub-redes, máscara de sub-rede, prefixo de rede, rede Linux, endereço IP"
---

## Lesson Content

Como você pode saber se dois computadores estão na mesma rede? A resposta reside na compreensão da sub-rede, abreviação de subnetwork. Uma sub-rede é uma divisão lógica de uma rede IP, agrupando hosts com endereços IP semelhantes. Esses hosts geralmente estão em proximidade física, permitindo transferência de dados eficiente entre eles. Pense nisso como enviar correspondência dentro do mesmo código postal; é muito mais rápido e simples do que enviá-la para um estado diferente.

Para que um host faça parte de uma **sub-rede linux**, seu endereço IP é dividido em duas partes: um prefixo de rede e um identificador de host. Por exemplo, se um host tem um IP de 192.168.1.8 e outro tem 192.168.1.9, eles provavelmente compartilham o mesmo prefixo de rede. A parte comum identifica a rede, enquanto os números exclusivos (8 e 9) identificam os hosts individuais.

### Entendendo a Máscara de Sub-rede Linux

A **máscara de sub-rede linux** é o que determina qual parte de um endereço IP é a porção de rede e qual parte é a porção de host. Uma máscara de sub-rede típica se parece com isto:

```plaintext
255.255.255.0
```

Para entender isso, precisamos pensar em binário. Cada número em um endereço IP ou máscara de sub-rede é um octeto, representando 8 bits. Em binário, um `1` significa "ligado" e um `0` significa "desligado". Se você converter o número binário `11111111` para decimal, você obtém 255. Isso significa que um octeto pode variar de 0 (`00000000`) a 255 (`11111111`).

Os `255`s na máscara "mascaram" a porção de rede do endereço IP. Portanto, com uma máscara de `255.255.255.0` e um IP de `192.168.1.8`, a parte `192.168.1` é a rede, e `8` é o host. Frequentemente, denotamos uma configuração de **sub-rede linux** pelo seu prefixo de rede seguido pela máscara de sub-rede, como `192.168.1.0/255.255.255.0`.

### O Propósito de Subnetting de Sub-redes

Por que criamos sub-redes? A prática de **subnetting de sub-redes** (divisão de sub-redes) é crucial para organizar e gerenciar redes de forma eficaz. Envolve dividir uma rede maior em segmentos menores e mais gerenciáveis. Isso oferece vários benefícios principais:

- **Melhor Desempenho:** Ao segmentar uma rede, você reduz o volume de tráfego de broadcast dentro de cada sub-rede, levando a menos congestionamento e melhor desempenho geral.
- **Segurança Aprimorada:** As sub-redes permitem isolar diferentes partes da sua rede. Um host em uma sub-rede não pode interagir diretamente com um host em outra sem um roteador, criando um limite de segurança. Você pode implementar regras de acesso no roteador para controlar o fluxo de tráfego entre sub-redes.
- **Administração Simplificada:** Dividir uma rede grande em unidades lógicas menores facilita o gerenciamento, a solução de problemas e a aplicação de políticas de rede.

### Conectando Sub-redes

E se você precisar se conectar a hosts em uma rede diferente, como yahoo.com? Para conectar sub-redes diferentes, você precisa de um dispositivo que esteja conectado a mais de uma sub-rede: um roteador.

Por exemplo, um host em `192.168.1.129` em uma rede com máscara `255.255.255.0` pode alcançar qualquer outro host na rede `192.168.1.0`. Para alcançar a internet, ele deve enviar tráfego através de seu gateway, que é o roteador. Em muitas redes domésticas, o endereço do roteador é frequentemente `.1` da sub-rede (por exemplo, `192.168.1.1`). Este roteador tem outra conexão com uma sub-rede diferente (como a rede do seu provedor de serviços de internet), permitindo a comunicação com a internet em geral.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de endereçamento IP e subnetting:

1.  **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços IPv4, o que é fundamental para entender sub-redes.
2.  **[Explorar Tipos de Endereços IP e Alcançabilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Aprenda a explorar diferentes tipos de endereços IP e testar a alcançabilidade da rede, ajudando você a verificar se os hosts estão na mesma rede.
3.  **[Realizar Subnetting IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine o subnetting IP e a conversão binária, aplicando diretamente os conceitos de prefixo de rede e identificação de host discutidos na lição.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança com o endereçamento de rede e subnetting.

## Quiz Question

Uma sub-rede é definida por um prefixo de rede e uma máscara de sub-rede. Verdadeiro ou Falso? (Por favor, responda com 'True' ou 'False'. A resposta diferencia maiúsculas de minúsculas e deve estar em inglês.)

## Quiz Answer

True
