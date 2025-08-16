---
title: "ping"
description: "Aprenda a usar o comando ping do Linux para testar a conectividade de rede e solucionar problemas. Entenda ICMP, TTL e tempo de ida e volta para um diagnóstico de rede eficaz."
keywords: "Linux ping, conectividade de rede, ICMP, TTL, rede Linux, Linux para iniciantes, tutorial Linux, comando ping"
---

## Lesson Content

Uma das ferramentas de rede mais simples, o **ping**, é usada para testar se um pacote consegue ou não alcançar um host. Ele funciona enviando pacotes ICMP echo request (Tipo 8) para o host de destino e aguarda por uma resposta ICMP echo reply (Tipo 0). O ping é bem-sucedido quando um host envia o pacote de requisição e recebe uma resposta do alvo. Vejamos um exemplo:

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

Neste exemplo, estamos usando o ping para verificar se conseguimos acessar <www.google.com>. A flag `-c` (count) é usada para parar de enviar pacotes de echo request depois que a contagem for atingida.

A primeira parte diz que estamos enviando pacotes de 64 bytes para 74.125.239.112 (google.com), e o restante nos mostra os detalhes da viagem. Por padrão, ele envia um pacote por segundo.

### icmp_seq

O campo `icmp_seq` é usado para mostrar o número de sequência dos pacotes enviados. Neste caso, enviei 3 pacotes, e podemos ver que 3 pacotes retornaram. Se você fizer um ping e alguns números de sequência estiverem faltando, isso significa que algum problema de conectividade está ocorrendo, e nem todos os seus pacotes estão chegando. Se o número de sequência estiver fora de ordem, sua conexão provavelmente está muito lenta, pois seus pacotes estão excedendo o padrão de um segundo.

### ttl

O campo Time To Live (TTL) é usado como um contador de saltos. À medida que você faz saltos, ele decrementa o contador em um, e uma vez que o contador de saltos atinge 0, nosso pacote morre. Isso serve para dar uma vida útil ao pacote; não queremos que nossos pacotes viajem para sempre.

### time

O tempo de ida e volta que levou desde o envio do pacote de echo request até o recebimento de uma resposta de echo reply.

## Exercise

Faça um ping em um site e observe a saída que você recebe.

## Quiz Question

Qual é a unidade de medida do tempo de ida e volta?

## Quiz Answer

ms
