---
index: 4
lang: "pt"
title: "netstat"
meta_title: "netstat - Solução de Problemas"
meta_description: "Aprenda o comando netstat para análise de rede Linux. Entenda conexões de rede, portas e sockets com este guia amigável para iniciantes."
meta_keywords: "netstat, comando netstat, rede Linux, conexões de rede, tutorial Linux, iniciante, guia"
---

## Lesson Content

### Portas Conhecidas

Discutimos a transmissão de dados através de portas em nossa máquina; vamos ver algumas portas conhecidas.

Você pode obter uma lista de portas conhecidas consultando o arquivo **/etc/services**:

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

A primeira coluna é o nome do serviço, depois o número da porta e o protocolo da camada de transporte que ele usa.

### netstat

Uma ferramenta extremamente útil para obter informações detalhadas sobre sua rede é o **netstat**. O Netstat exibe várias informações relacionadas à rede, como conexões de rede, tabelas de roteamento, informações sobre interfaces de rede e muito mais; é o canivete suíço das ferramentas de rede. Focaremos principalmente em um recurso que o netstat possui, que é o status das conexões de rede. Antes de vermos um exemplo, vamos falar primeiro sobre sockets e portas. Um socket é uma interface que permite que programas enviem e recebam dados, enquanto uma porta é usada para identificar qual aplicativo deve enviar ou receber dados. O endereço do socket é a combinação do endereço IP e da porta. Cada conexão entre um host e um destino requer um socket exclusivo. Por exemplo, HTTP é um serviço que roda na porta 80; no entanto, podemos ter muitas conexões HTTP, e para manter cada conexão, um socket é criado por conexão.

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

O comando `netstat -a` mostra os sockets de escuta e não escuta para conexões de rede; a flag `-t` mostra apenas conexões TCP.

As colunas são as seguintes, da esquerda para a direita:

- **Proto**: Protocolo usado, TCP ou UDP.
- **Recv-Q**: Dados que estão na fila para serem recebidos.
- **Send-Q**: Dados que estão na fila para serem enviados.
- **Local Address**: Host conectado localmente.
- **Foreign Address**: Host conectado remotamente.
- **State**: O estado do socket.

Consulte a manpage para obter uma lista de estados de socket, mas aqui estão alguns:

- **LISTENING**: O socket está aguardando conexões de entrada. Lembre-se, quando fazemos uma conexão TCP, nosso destino precisa estar aguardando por nós antes que possamos nos conectar.
- **SYN_SENT**: O socket está tentando ativamente estabelecer uma conexão.
- **ESTABLISHED**: O socket tem uma conexão estabelecida.
- **CLOSE_WAIT**: O host remoto foi desligado e estamos esperando o socket fechar.
- **TIME_WAIT**: O socket está esperando após o fechamento para lidar com pacotes ainda na rede.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão das configurações da interface de rede:

1. **[Examine as configurações da interface de rede com ethtool no Linux](https://labex.io/pt/labs/linux-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Aprenda a usar o comando `ethtool` para examinar e gerenciar as configurações da interface de rede, incluindo a visualização e configuração da velocidade e duplex da interface, e a análise dos modos de link para solucionar problemas de rede na camada física.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento de interfaces de rede.

## Quiz Question

Qual porta é usada para HTTPS?

## Quiz Answer

443
