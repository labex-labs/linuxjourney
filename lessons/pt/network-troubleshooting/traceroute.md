---
index: 3
lang: "pt"
title: "traceroute"
meta_title: "traceroute - Solução de Problemas"
meta_description: "Aprenda a usar o comando Linux traceroute para rastrear rotas de rede e solucionar problemas de conectividade. Entenda TTL e roteamento de pacotes para iniciantes."
meta_keywords: "traceroute, rede Linux, solução de problemas de rede, TTL, comandos Linux, iniciante, tutorial"
---

## Lesson Content

O comando `traceroute` é usado para ver como os pacotes são roteados. Ele funciona enviando pacotes com valores TTL (Time To Live) crescentes, começando com 1. Assim, o primeiro roteador recebe o pacote e decrementa o valor TTL em um, descartando o pacote. O roteador nos envia de volta uma mensagem ICMP Time Exceeded. Em seguida, o próximo pacote recebe um TTL de 2, então ele passa pelo primeiro roteador, mas quando chega ao segundo roteador, o TTL é 0, e ele retorna outra mensagem ICMP Time Exceeded. O Traceroute funciona dessa forma porque, ao enviar e descartar pacotes, ele constrói uma lista de roteadores que os pacotes atravessam até que finalmente chegue ao seu destino e receba uma mensagem ICMP Echo Reply.

Aqui está um pequeno trecho de um traceroute:

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Cada linha representa um roteador ou máquina que está entre você e seu destino. Ela mostra o nome do destino e seu endereço IP, e as últimas três colunas correspondem ao tempo de ida e volta de um pacote para alcançar esse roteador. Por padrão, três pacotes são enviados ao longo da rota.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da descoberta de caminhos de rede e solução de problemas:

1. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Pratique o uso do comando `ip` para configurar as configurações de rede e verificar a conectividade com `traceroute`.
2. **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como `ping` e `arp` funcionam para entender as interações da camada de rede, que são fundamentais para o funcionamento do `traceroute`.

Esses laboratórios o ajudarão a aplicar os conceitos de diagnóstico de rede em cenários reais e a construir confiança com as ferramentas de rede do Linux.

## Quiz Question

O que é decrementado em um ao fazer saltos pela rede?

## Quiz Answer

TTL
