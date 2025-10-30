---
index: 5
lang: "pt"
title: "Análise de Pacotes"
meta_title: "Análise de Pacotes - Solução de Problemas"
meta_description: "Aprenda os conceitos básicos de análise de pacotes usando tcpdump. Entenda o tráfego de rede, capture dados e interprete a saída com este guia Linux para iniciantes."
meta_keywords: "tcpdump, análise de pacotes, análise de rede, rede Linux, tutorial para iniciantes, Wireshark, comandos Linux, tráfego de rede"
---

## Lesson Content

O assunto da análise de pacotes poderia preencher um curso inteiro por si só, e há muitos livros escritos apenas sobre análise de pacotes. No entanto, hoje aprenderemos apenas o básico. Existem dois analisadores de pacotes extremamente populares: Wireshark e tcpdump. Essas ferramentas escaneiam suas interfaces de rede, capturam a atividade dos pacotes, analisam os pacotes e exibem as informações para que possamos vê-las. Elas nos permitem entrar nos detalhes da análise de rede e aprofundar nos aspectos de baixo nível. Usaremos o tcpdump, pois ele tem uma interface mais simples; no entanto, se você fosse adicionar a análise de pacotes ao seu conjunto de ferramentas, eu recomendaria pesquisar o Wireshark.

### Instalar tcpdump

```bash
sudo apt install tcpdump
```

### Capturar dados de pacotes em uma interface

```plaintext
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on wlan0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
11:28:24.960464 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 3, length 64
11:28:24.979299 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 3, length 64
11:28:25.961869 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 4, length 64
11:28:25.976176 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 4, length 64
11:28:26.963667 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 5, length 64
11:28:26.976137 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 5, length 64
11:28:30.674953 ARP, Request who-has 172.254.1.0 tell ThePickleParty.lan, length 28
11:28:31.190665 IP ThePickleParty.lan.51056 > 192.168.86.255.rfe: UDP, length 306
```

Você notará muitas coisas acontecendo quando executar uma captura de pacotes. Bem, isso é de se esperar; há muita atividade de rede acontecendo em segundo plano. No meu exemplo acima, eu peguei apenas um trecho da minha captura, especificamente o momento em que decidi fazer ping em `www.google.com`.

### Entendendo a saída

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- O primeiro campo é um carimbo de data/hora da atividade da rede.
- IP: Isso contém as informações do protocolo.
- Em seguida, você verá o endereço de origem e destino: `icebox.lan > nuq04s29-in-f4.1e100.net`.
- `seq`: Este é o número de sequência inicial e final do pacote TCP.
- `length`: Comprimento em bytes.

Como você pode ver na nossa saída do tcpdump, estamos enviando um pacote de solicitação de eco ICMP para `www.google.com` e recebendo um pacote de resposta de eco ICMP em troca! Além disso, observe que pacotes diferentes exibirão informações diferentes; consulte a manpage para ver quais são.

### Escrevendo a saída do tcpdump para um arquivo

```bash
sudo tcpdump -w /some/file
```

Algumas considerações finais: apenas arranhamos a superfície do assunto da análise de pacotes. Há muito o que você pode analisar, e nem sequer abordamos aprofundar ainda mais com a saída Hex e ASCII. Há muitos recursos online para ajudá-lo a aprender mais sobre analisadores de pacotes, e eu o encorajo a encontrá-los!

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da análise de pacotes:

1. **[Analisar Quadros Ethernet com tcpdump no Linux](https://labex.io/pt/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - Pratique a captura e inspeção de quadros Ethernet, gerando tráfego e analisando cabeçalhos de quadros e endereços MAC usando `tcpdump`.

Este laboratório o ajudará a aplicar os conceitos de análise de pacotes em um cenário real e a construir confiança com a solução de problemas de rede.

## Quiz Question

Qual é a flag para capturar uma interface específica com tcpdump?

## Quiz Answer

-i
