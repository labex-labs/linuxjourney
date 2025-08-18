---
lang: "pt"
title: "traceroute"
meta_description: "Aprenda a usar o comando Linux traceroute para rastrear rotas de rede e solucionar problemas de conectividade. Entenda TTL e roteamento de pacotes para iniciantes."
meta_keywords: "traceroute, rede Linux, solução de problemas de rede, TTL, comandos Linux, iniciante, tutorial"
---

## Lesson Content

O comando `traceroute` é usado para ver como os pacotes são roteados. Ele funciona enviando pacotes com valores crescentes de TTL (Time To Live), começando com 1. Assim, o primeiro roteador recebe o pacote e decrementa o valor TTL em um, descartando o pacote. O roteador nos envia de volta uma mensagem ICMP Time Exceeded. Em seguida, o próximo pacote recebe um TTL de 2, então ele passa pelo primeiro roteador, mas quando chega ao segundo roteador, o TTL é 0, e ele retorna outra mensagem ICMP Time Exceeded. O Traceroute funciona dessa forma porque, ao enviar e descartar pacotes, ele constrói uma lista de roteadores que os pacotes atravessam até finalmente chegar ao seu destino e receber uma mensagem ICMP Echo Reply.

Aqui está um pequeno trecho de um traceroute:

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Cada linha representa um roteador ou máquina que está entre você e seu destino. Ela mostra o nome do destino e seu endereço IP, e as últimas três colunas correspondem ao tempo de ida e volta de um pacote para alcançar aquele roteador. Por padrão, três pacotes são enviados ao longo da rota.

## Exercise

Execute o comando `traceroute` em sua máquina e observe a saída.

## Quiz Question

O que é decrementado em um ao fazer saltos pela rede?

## Quiz Answer

TTL
