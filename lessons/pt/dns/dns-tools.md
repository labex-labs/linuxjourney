---
index: 6
lang: "pt"
title: "Ferramentas DNS"
meta_title: "Ferramentas DNS - DNS"
meta_description: "Explore ferramentas DNS essenciais do Linux como nslookup e o poderoso comando dig. Este tutorial Linux para iniciantes abrange consultas DNS e técnicas de solução de problemas de DNS."
meta_keywords: "nslookup, comando dig, ferramentas DNS, DNS Linux, solução de problemas DNS, consulta de servidor de nomes, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

No Linux, várias utilidades de linha de comando estão disponíveis para diagnósticos de rede. Quando se trata de problemas de Sistema de Nomes de Domínio (DNS), duas **ferramentas DNS** principais se destacam: `nslookup` e `dig`. Entender como usá-las é crucial para qualquer **solução de problemas de DNS** em um servidor ou cliente **DNS Linux**.

### Usando nslookup para Consultas DNS Básicas

O `nslookup` (name server lookup) é uma utilidade clássica para consultar servidores DNS para obter informações de mapeamento de nome de domínio ou endereço IP. Embora às vezes seja considerado obsoleto em favor do `dig`, ele continua sendo uma ferramenta rápida e fácil para pesquisas simples.

Para encontrar o endereço IP de um domínio como `www.google.com`, você pode executar:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

Nesta saída, `Server` e `Address` mostram o servidor DNS que respondeu à consulta. A `Non-authoritative answer` (Resposta não autoritativa) significa que o servidor forneceu um resultado em cache em vez de consultar diretamente a fonte autoritativa. `Name` e `Address` mostram o endereço IP resolvido para o domínio.

### Solução Avançada de Problemas de DNS com dig

O comando `dig` (domain information groper) é uma ferramenta poderosa e flexível para interrogar servidores de nomes DNS. Ele fornece informações mais detalhadas do que o `nslookup`, tornando-o a escolha preferida para **solução de problemas de DNS** séria.

Aqui está um exemplo de uso do **comando dig**:

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

A saída do `dig` é organizada em seções:

- **QUESTION SECTION** (Seção de Pergunta): Mostra a consulta que foi enviada. Aqui, solicitamos um registro `A` (endereço) para `www.google.com`.
- **ANSWER SECTION** (Seção de Resposta): Exibe a resposta recebida do servidor DNS. Neste caso, o Google tem vários endereços IP associados ao seu domínio.
- **Statistics** (Estatísticas): A seção final fornece metadados sobre a consulta, como o tempo de consulta e o servidor que respondeu.

Devido à sua saída detalhada e flexibilidade, `dig` é uma utilidade indispensável para quem gerencia ou soluciona problemas de serviços de rede no Linux.

## Exercise

Para ganhar mais experiência com utilitários de rede Linux, considere experimentar o seguinte laboratório prático:

1. **[Examine Network Interface Settings with ethtool in Linux](https://labex.io/pt/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Aprenda a usar o comando `ethtool` para examinar e gerenciar configurações de interface de rede, incluindo a visualização e definição de velocidade e duplex da interface, e a análise de modos de link para solucionar problemas de rede na camada física.

Este laboratório ajudará você a aplicar os conceitos em cenários reais e a ganhar confiança no gerenciamento de interfaces de rede.

## Quiz Question

Qual ferramenta é usada para obter informações detalhadas sobre servidores de nomes DNS? Por favor, responda usando apenas caracteres minúsculos em inglês.

## Quiz Answer

dig
