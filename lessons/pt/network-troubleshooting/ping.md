---
index: 2
lang: "pt"
title: "ping"
meta_title: "ping - Solução de Problemas"
meta_description: "Aprenda a usar o comando ping do Linux para testar a conectividade de rede e solucionar problemas. Entenda ICMP, TTL e tempo de ida e volta para diagnósticos de rede eficazes."
meta_keywords: "Linux ping, conectividade de rede, ICMP, TTL, rede Linux, Linux para iniciantes, tutorial Linux, comando ping"
---

## Lesson Content

Uma das ferramentas de rede mais simples, o **ping**, é usada para testar se um pacote consegue ou não alcançar um host. Ele funciona enviando pacotes ICMP echo request (Tipo 8) para o host de destino e aguarda por uma ICMP echo reply (Tipo 0). O ping é bem-sucedido quando um host envia o pacote de requisição e recebe uma resposta do alvo. Vejamos um exemplo:

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

Neste exemplo, estamos usando o ping para verificar se conseguimos acessar `www.google.com`. A flag `-c` (count) é usada para parar de enviar pacotes de requisição de eco depois que a contagem for atingida.

A primeira parte diz que estamos enviando pacotes de 64 bytes para 74.125.239.112 (google.com), e o restante nos mostra os detalhes da viagem. Por padrão, ele envia um pacote por segundo.

### icmp_seq

O campo `icmp_seq` é usado para mostrar o número de sequência dos pacotes enviados. Neste caso, enviei 3 pacotes, e podemos ver que 3 pacotes retornaram. Se você fizer um ping e alguns números de sequência estiverem faltando, isso significa que algum problema de conectividade está ocorrendo, e nem todos os seus pacotes estão passando. Se o número de sequência estiver fora de ordem, sua conexão provavelmente está muito lenta, pois seus pacotes estão excedendo o padrão de um segundo.

### ttl

O campo Time To Live (TTL) é usado como um contador de saltos. À medida que você faz saltos, ele decrementa o contador em um, e uma vez que o contador de saltos atinge 0, nosso pacote morre. Isso serve para dar uma vida útil ao pacote; não queremos que nossos pacotes viajem para sempre.

### time

O tempo de ida e volta que levou desde o envio do pacote de requisição de eco até o recebimento de uma resposta de eco.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da conectividade de rede e do comando `ping`:

1. **[Explore a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` e `arp` para explorar as interações da camada de rede e de enlace de dados e observe como o gateway padrão lida com o tráfego remoto.
2. **[Explore Tipos de Endereços IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Utilize `ping` e `ip a` para testar a pilha TCP/IP local, verificar a conectividade com a internet pública e explorar a acessibilidade da rede.
3. **[Simule a Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aprenda a atribuir endereços IP estáticos com `ip addr` e teste a conectividade com `ping` na mesma sub-rede e em sub-redes diferentes.

Esses laboratórios o ajudarão a aplicar os conceitos de acessibilidade de rede e o comando `ping` em cenários reais e a construir confiança com o diagnóstico de rede no Linux.

## Quiz Question

Qual é a unidade de medida do tempo de ida e volta?

## Quiz Answer

ms
