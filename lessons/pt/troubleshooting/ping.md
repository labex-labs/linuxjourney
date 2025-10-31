---
index: 2
lang: "pt"
title: "ping"
meta_title: "ping - Solução de Problemas"
meta_description: "Aprenda a usar o comando ping do Linux para testar a conectividade de rede. Este guia explica a saída do ping, incluindo o significado de icmp_seq, TTL e tempo de ida e volta. Entenda como interpretar a sequência (seq) do ping para diagnosticar problemas de rede."
meta_keywords: "ping Linux, conectividade de rede, ICMP, TTL, comando ping, icmp_seq, sequência ping, seq icmp, significado icmp_seq, ping icmp_seq, rede Linux"
---

## Lesson Content

O comando **ping** é uma das utilidades de rede mais fundamentais, usada para testar se um host remoto é alcançável através de uma rede IP. Ele opera enviando pacotes ICMP (Internet Control Message Protocol) de "echo request" (solicitação de eco) para o host de destino e aguardando uma resposta ICMP de "echo reply" (resposta de eco). Um ping bem-sucedido ocorre quando o pacote de solicitação é enviado e uma resposta é recebida.

Vamos examinar um comando `ping` típico em ação:

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

Neste exemplo, usamos o `ping` para verificar a conectividade com `www.google.com`. A opção `-c 3` diz ao `ping` para enviar exatamente três pacotes de solicitação de eco e depois parar. Por padrão, o `ping` envia um pacote por segundo.

### Entendendo a Saída do Ping

A saída do comando `ping icmp_seq` fornece informações diagnósticas valiosas. Vamos detalhar os componentes principais.

### Sequência ICMP (icmp_seq)

O campo `icmp_seq` exibe o número de sequência de cada pacote ICMP. Em nosso exemplo, enviamos três pacotes, e a saída mostra que todos os três (`icmp_seq=1`, `icmp_seq=2`, `icmp_seq=3`) foram retornados com sucesso. O `ping seq` é crucial para diagnosticar a perda de pacotes. Se você notar números de sequência ausentes, isso indica um problema de conectividade onde alguns pacotes não estão chegando ao destino ou retornando. Se os números `icmp seq` aparecerem fora de ordem, isso pode sugerir congestionamento ou latência da rede, pois os pacotes estão demorando mais do que o intervalo padrão de um segundo para completar a ida e volta. Entender o `icmp_seq meaning` (significado do icmp_seq) é fundamental para a solução de problemas.

### Time To Live (TTL)

O campo Time To Live (TTL) atua como um contador de saltos (hops) para o pacote. Cada vez que o pacote passa por um roteador (um "salto"), o valor do TTL é decrementado em um. Se o contador chegar a zero antes que o pacote chegue ao seu destino, o pacote é descartado. Este mecanismo evita que os pacotes circulem indefinidamente na rede.

### Tempo (Time)

O campo `time` mede o tempo de ida e volta (roundtrip time)—a duração que o pacote levou para viajar da sua máquina até o host de destino e para a resposta de eco retornar. Esse valor é tipicamente medido em milissegundos (ms) e é um indicador primário da latência da rede.

## Exercise

A prática é essencial para dominar o diagnóstico de rede. Estes laboratórios práticos ajudarão a reforçar sua compreensão do comando `ping`:

1. **[Explore a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` e `arp` para explorar interações das camadas de rede e de enlace de dados e observar como o gateway padrão lida com tráfego remoto.
2. **[Explore Tipos de Endereço IP e Alcance no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Utilize `ping` e `ip a` para testar a pilha TCP/IP local, verificar a conectividade com a internet pública e explorar o alcance da rede.
3. **[Simule a Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aprenda a atribuir endereços IP estáticos com `ip addr` e testar a conectividade com `ping` na mesma sub-rede e em sub-redes diferentes.

Estes laboratórios ajudarão você a aplicar os conceitos de alcance de rede e o comando `ping` em cenários do mundo real, aumentando sua confiança com o diagnóstico de rede no Linux.

## Quiz Question

Qual é a unidade de medida do tempo de ida e volta? Por favor, responda em inglês, prestando atenção à sensibilidade a maiúsculas e minúsculas.

## Quiz Answer

ms
