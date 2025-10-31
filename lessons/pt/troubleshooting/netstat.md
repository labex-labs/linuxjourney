---
index: 4
lang: "pt"
title: "netstat"
meta_title: "netstat - Solução de Problemas"
meta_description: "Domine o comando netstat do linux para analisar conexões de rede, portas e sockets. Este guia aborda estados comuns como SYN_SENT e netstat close_wait para solução de problemas eficaz."
meta_keywords: "netstat linux, netstat, comando netstat, syn_sent netstat, netstat close_wait, conexões de rede, rede linux, análise de rede, tutorial linux"
---

## Lesson Content

### Portas Bem Conhecidas

Discutimos como os dados são transmitidos através de portas em nossa máquina. Vamos analisar algumas portas comuns e bem conhecidas. Você pode encontrar uma lista dessas portas no arquivo **/etc/services**:

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

A primeira coluna mostra o nome do serviço, seguido pelo seu número de porta atribuído e o protocolo de camada de transporte que ele utiliza.

### Introdução ao netstat do Linux

Uma ferramenta extremamente útil para coletar informações detalhadas de rede é o **netstat**. O comando `linux netstat` exibe uma ampla gama de dados relacionados à rede, incluindo conexões de rede ativas, tabelas de roteamento e estatísticas de interface. É frequentemente chamado de canivete suíço das ferramentas de rede.

Esta lição se concentrará no uso do `netstat` para verificar o status das conexões de rede. Antes de mergulharmos em um exemplo, vamos esclarecer a diferença entre sockets e portas. Uma **porta** é um identificador numérico usado para direcionar dados para uma aplicação específica. Um **socket** é um ponto final para comunicação, permitindo que programas enviem e recebam dados. O endereço do socket é a combinação única de um endereço IP e um número de porta. Cada conexão entre um host e um destino requer um socket exclusivo. Por exemplo, embora o serviço HTTP seja executado na porta 80, várias conexões HTTP podem existir simultaneamente, e um socket exclusivo é criado para cada uma delas.

Vamos examinar a saída de `netstat -at`:

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
```

O comando `netstat -a` exibe todos os sockets em escuta e não em escuta, enquanto o sinalizador `-t` filtra a saída para mostrar apenas as conexões TCP.

A seguir estão as colunas:

- **Proto**: O protocolo usado (ex: TCP ou UDP).
- **Recv-Q**: A fila de dados esperando para ser recebida.
- **Send-Q**: A fila de dados esperando para ser enviada.
- **Local Address**: O endereço do host local.
- **Foreign Address**: O endereço do host remoto.
- **State**: O estado atual do socket.

### Entendendo os Estados da Conexão

A coluna **State** fornece informações cruciais sobre o status de uma conexão. Aqui estão alguns estados comuns que você encontrará:

- **LISTENING**: O socket está esperando por conexões de entrada. Para que uma conexão TCP seja estabelecida, o destino deve estar em escuta.
- **SYN_SENT**: Ao usar `netstat`, um estado `SYN_SENT` indica que o socket está tentando ativamente estabelecer uma conexão.
- **ESTABLISHED**: O socket possui uma conexão totalmente estabelecida.
- **CLOSE_WAIT**: O estado `netstat close_wait` significa que o host remoto foi encerrado, e o sistema local está esperando que a aplicação feche o socket.
- **TIME_WAIT**: O socket está esperando após o fechamento para lidar com quaisquer pacotes que ainda possam estar na rede.

You can see a full list of socket states in the `netstat` man page.

Você pode ver uma lista completa dos estados de socket na página de manual do `netstat`.

## Exercise

Prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão das configurações de interface de rede:

1. **[Examinar Configurações de Interface de Rede com ethtool no Linux](https://labex.io/pt/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Aprenda a usar o comando `ethtool` para examinar e gerenciar configurações de interface de rede, incluindo visualizar e definir a velocidade e o duplex da interface, e analisar modos de link para solucionar problemas de rede da camada física.

Este laboratório ajudará você a aplicar os conceitos em cenários reais e a ganhar confiança no gerenciamento de interfaces de rede.

## Quiz Question

Qual porta é usada para HTTPS?

## Quiz Answer

443
