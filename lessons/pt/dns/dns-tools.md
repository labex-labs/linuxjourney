---
index: 6
lang: "pt"
title: "Ferramentas DNS"
meta_title: "Ferramentas DNS - DNS"
meta_description: "Aprenda os comandos nslookup e dig para consultas DNS e solução de problemas no Linux. Entenda como usar essas ferramentas DNS essenciais com nosso guia para iniciantes."
meta_keywords: "nslookup, comando dig, ferramentas DNS, DNS Linux, solução de problemas DNS, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

### nslookup

A ferramenta "name server lookup" é usada para consultar servidores de nomes para encontrar informações sobre registros de recursos. Vamos descobrir onde está o servidor de nomes para google.com:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) é uma ferramenta poderosa para obter informações sobre servidores de nomes DNS. É mais flexível que o nslookup e excelente para solucionar problemas de DNS.

```bash
pete@icebox:~$ dig www.google.com

; <<>> DiG 9.9.5-3-Ubuntu <<>> www.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42376
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
;; QUESTION SECTION:
;www.google.com.                        IN      A

;; ANSWER SECTION:
www.google.com.         5       IN      A       74.125.239.147
www.google.com.         5       IN      A       74.125.239.144
www.google.com.         5       IN      A       74.125.239.146
www.google.com.         5       IN      A       74.125.239.145
www.google.com.         5       IN      A       74.125.239.148

;; Query time: 27 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Feb 07 10:14:00 PST 2016
;; MSG SIZE  rcvd: 123
```

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão das configurações da interface de rede:

1. **[Examinar Configurações da Interface de Rede com ethtool no Linux](https://labex.io/pt/labs/linux-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Aprenda a usar o comando `ethtool` para examinar e gerenciar as configurações da interface de rede, incluindo visualização e configuração de velocidade e duplex da interface, e análise de modos de link para solucionar problemas de rede na camada física.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento de interfaces de rede.

## Quiz Question

Qual ferramenta é usada para obter informações detalhadas sobre servidores de nomes DNS?

## Quiz Answer

dig
