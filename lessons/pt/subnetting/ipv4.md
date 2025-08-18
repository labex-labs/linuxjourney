---
lang: "pt"
title: "IPv4"
meta_description: "Aprenda sobre endereços IPv4, sua estrutura e como encontrar seu IP usando ifconfig. Entenda os conceitos básicos de rede para iniciantes em Linux."
meta_keywords: "IPv4, endereço IP, ifconfig, conceitos básicos de rede, rede Linux, iniciante, tutorial, guia"
---

## Lesson Content

Então, sabemos que os hosts de rede têm um endereço único onde podem ser encontrados. Esses endereços são conhecidos como endereços IP. Um endereço IPv4 se parece com isto:

```
204.23.124.23
```

Este endereço, na verdade, contém duas partes: a porção de rede que nos diz em qual rede ele está, e a porção de host que nos diz qual host nessa rede ele é. Para este curso, discutiremos principalmente os endereços IPv4, que são o que você comumente verá ao se referir a endereços IP.

Um endereço IP é separado em octetos por pontos. Assim, existem 4 octetos em um endereço IPv4. Se você sabe um pouco de ciência da computação, um octeto são 8 bits, e 8 bits, na verdade, equivalem a 1 byte, então também nos referimos a um endereço IPv4 como tendo 4 bytes. Usamos bits frequentemente ao lidar com sub-redes e endereços IP.

Você pode ver seu endereço IP com o comando `ifconfig -a`:

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

Como você pode ver, meu endereço IPv4 é: 192.168.1.129

## Exercise

Encontre seu endereço IP com `ifconfig`.

## Quiz Question

Quantos bytes tem um endereço IPv4?

## Quiz Answer

4
