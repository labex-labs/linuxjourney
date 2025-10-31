---
index: 3
lang: "pt"
title: "traceroute"
meta_title: "traceroute - Solução de Problemas"
meta_description: "Domine o comando traceroute do Linux para rastrear rotas de rede e solucionar problemas de conectividade. Este tutorial explica como o traceroute usa o TTL para mapear o caminho que os pacotes percorrem até o destino."
meta_keywords: "traceroute, traceroute linux, rede Linux, solução de problemas de rede, TTL, roteamento de pacotes, comandos Linux, iniciante, tutorial"
---

## Lesson Content

O comando `traceroute` é uma ferramenta fundamental de diagnóstico de rede usada para rastrear o caminho que os pacotes percorrem do seu computador até um host de destino. Ao revelar cada "salto" (hop) ou roteador ao longo do caminho, ele ajuda você a identificar gargalos de rede e solucionar problemas de conectividade. A utilidade `traceroute linux` é essencial para qualquer administrador de sistema ou engenheiro de rede.

### Como o Traceroute Funciona

O mecanismo por trás do `traceroute` reside em sua manipulação inteligente do campo Time To Live (TTL) no cabeçalho de um pacote IP. O processo funciona da seguinte forma:

1. `traceroute` envia um pacote de sonda com um valor TTL de 1.
2. O primeiro roteador no caminho recebe o pacote, decrementa o TTL para 0 e o descarta. O roteador então envia uma mensagem ICMP "Time Exceeded" (Tempo Excedido) de volta ao seu computador.
3. `traceroute` registra o endereço IP do roteador e o tempo de ida e volta.
4. Em seguida, ele envia outro pacote, desta vez com um TTL de 2. Este pacote passa com sucesso pelo primeiro roteador, mas é descartado pelo segundo roteador, que novamente envia uma mensagem "Time Exceeded".
5. Este processo se repete, com o TTL incrementando em um para cada conjunto subsequente de pacotes. Ao construir uma lista dos roteadores que retornam mensagens "Time Exceeded", o `traceroute` mapeia a rota inteira.
6. O processo é concluído quando os pacotes finalmente chegam ao destino, que responde com uma mensagem ICMP "Echo Reply" (Resposta de Eco).

### Entendendo a Saída do Traceroute

Vamos examinar uma saída de exemplo ao executar `traceroute` em um terminal Linux:

```bash
$ traceroute google.com
traceroute para google.com (216.58.216.174), 30 saltos máx, pacotes de 60 bytes
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Cada linha numerada representa um salto ao longo do caminho da rede. Veja como interpretar as informações:

- **Número do Salto:** A primeira coluna (ex: `1`, `2`, `3`) indica a sequência do roteador no caminho.
- **Nome do Roteador e Endereço IP:** A próxima parte mostra o nome do host (se puder ser resolvido) e o endereço IP do roteador naquele salto.
- **Tempos de Ida e Volta (RTT):** As últimas três colunas mostram o tempo de ida e volta para cada um dos três pacotes de sonda enviados para aquele salto específico. Esses tempos, medidos em milissegundos (ms), ajudam a avaliar a latência em cada etapa da jornada.

Usar o comando `traceroute linux` de forma eficaz fornece uma visão inestimável do desempenho e da estrutura da sua rede.

## Exercise

A prática é fundamental para dominar o diagnóstico de rede. Os seguintes laboratórios práticos ajudarão a reforçar sua compreensão da descoberta de caminhos de rede e solução de problemas com ferramentas como `traceroute`:

1. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Pratique o uso do comando `ip` para configurar configurações de rede e, em seguida, verifique a conectividade e os caminhos de roteamento com `traceroute`.
2. **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como `ping` e `arp` trabalham juntos para entender as interações da camada de rede, que são conceitos fundamentais para o funcionamento do `traceroute`.

Esses laboratórios ajudarão você a aplicar os conceitos de diagnóstico de rede em cenários do mundo real e a ganhar confiança com as ferramentas essenciais de rede Linux.

## Quiz Question

What gets decremented by one when making hops across the network? (Please answer in English, paying attention to capitalization.)

## Quiz Answer

TTL
