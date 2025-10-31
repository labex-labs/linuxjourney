---
index: 7
lang: "pt"
title: "IPv6"
meta_title: "IPv6 - Sub-redes"
meta_description: "Um guia para iniciantes no protocolo IPv6. Aprenda por que o IPv6 foi criado, como ele difere do IPv4 e entenda os conceitos básicos do seu esquema de endereçamento para redes Linux modernas."
meta_keywords: "IPv6, IPv4, endereço IP, rede Linux, protocolos de rede, protocolo de internet, esgotamento de endereços, iniciante, tutorial, guia"
---

## Lesson Content

Todo dispositivo que se conecta à internet, do seu servidor ao seu smartphone, requer um endereço IP exclusivo para se comunicar. A versão mais utilizada, IPv4, fornece um número finito de endereços, um limite que estamos a atingir rapidamente no nosso mundo cada vez mais conectado. Este problema é conhecido como esgotamento de endereços IPv4.

### O que é IPv6?

Para resolver este problema, a Internet Engineering Task Force (IETF) desenvolveu uma nova versão do Protocolo de Internet: IPv6. O objetivo principal do IPv6 é expandir drasticamente o conjunto disponível de endereços IP, garantindo que a internet possa continuar a crescer e acomodar milhares de milhões de novos dispositivos. Também inclui outras melhorias no protocolo de rede.

### IPv4 vs IPv6

Embora o IPv6 tenha sido criado para resolver as limitações do IPv4, a sua adoção tem sido gradual. Não se destina a substituir imediatamente o IPv4. Em vez disso, os dois protocolos de rede são concebidos para coexistir e complementar-se. Muitas redes hoje operam em modo "dual-stack", suportando IPv4 e IPv6 simultaneamente. Se estiver familiarizado com IPv4, os conceitos centrais do IPv6 serão fáceis de apreender.

### Compreender os Endereços IPv6

A diferença mais significativa que notará é o formato do endereço. Um endereço IPv4 é um número de 32 bits tipicamente escrito como quatro números decimais separados por pontos (ex: `192.168.1.1`). Em contraste, um endereço IPv6 é um número de 128 bits escrito em hexadecimal e separado por dois pontos.

Aqui está a aparência de um endereço IPv6 típico:

```plaintext
2dde:1235:1256:3:200:f8ed:fe23:59cf
```

Este formato mais longo permite um número vastamente maior de endereços IP exclusivos, garantindo o futuro da conectividade da internet.

## Exercise

Para dominar os conceitos de IPv6, a prática é essencial. Aqui estão alguns laboratórios práticos para reforçar a sua compreensão do endereçamento IPv6 e da sua interação com o IPv4 num ambiente Linux:

1. **[Configurar e Verificar Endereços IPv6 no Linux](https://labex.io/pt/labs/comptia-configure-and-verify-ipv6-addresses-in-linux-592858)** - Pratique a atribuição de endereços IPv6 estáticos e teste a conectividade usando os comandos `ip` e `ping6`.
2. **[Realizar Consultas DNS IPv6 no Linux](https://labex.io/pt/labs/comptia-perform-ipv6-dns-lookups-in-linux-592862)** - Aprenda a consultar registos AAAA e a verificar a resolução DNS IPv6 usando `dig`, `nslookup` e `ping6`.
3. **[Configurar um Túnel 6to4 de IPv4 para IPv6 no Linux](https://labex.io/pt/labs/comptia-configure-an-ipv4-to-ipv6-6to4-tunnel-in-linux-592867)** - Ganhe experiência prática na configuração de um túnel 6to4 para permitir conectividade IPv6 sobre uma rede IPv4 existente.

Estes laboratórios ajudarão a aplicar os conceitos de IPv6 em cenários reais e a construir confiança na configuração e resolução de problemas de rede.

## Quiz Question

What is the name of the IP protocol designed to increase the number of available addresses for hosts on the Internet? Please answer in English using the protocol's common name, paying attention to capitalization.

## Quiz Answer

IPv6
