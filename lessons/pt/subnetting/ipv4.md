---
lesson_id: "ipv4"
course_id: "subnetting"
lang: "pt"
order_index: 1
title: "IPv4"
description: "Aprenda como endereços IPv4, prefixos, escopos e a saída de interfaces no Linux se relacionam."
meta_title: "IPv4 - Sub-redes"
meta_description: "Comece sua jornada com nosso tutorial completo de Linux sobre endereços IPv4. Este guia para iniciantes é uma excelente maneira de aprender redes Linux, abordando a estrutura IP e ferramentas essenciais de linha de comando como ip addr."
meta_keywords: "IPv4, endereço IP, linux para iniciantes, melhor maneira de aprender linux, tutorial completo de linux, melhor curso de linux online grátis, cursos gratuitos de certificação linux, redes linux, ifconfig, ip addr"
---

O IPv4 fornece endereços de origem e destino de 32 bits para pacotes roteados. Um endereço possui significado junto com seu prefixo, interface, escopo, política de roteamento e duração — não como um identificador permanente de um dispositivo inteiro.

## Notação decimal pontuada

O IPv4 é exibido como quatro octetos de oito bits separados por pontos:

```text
192.0.2.165
```

Cada octeto varia de 0 a 255, portanto o endereço completo contém quatro bytes. O comprimento do prefixo identifica quantos bits iniciais pertencem ao prefixo de rede, como em `192.0.2.165/24`.

:::single-choice{#ipv4-address-size} Qual é o tamanho de um endereço IPv4?

::option[32 bits em quatro octetos.]{#ipv4-thirty-two-bits .correct explanation="Quatro grupos de oito bits produzem a representação decimal pontuada."}
::option[24 bits em todas as redes.]{#ipv4-always-twenty-four explanation="Um `/24` é um comprimento de prefixo, não o tamanho de todo endereço IPv4."}
::option[128 bytes separados por dois-pontos.]{#ipv4-128-bytes explanation="O IPv6 possui 128 bits e usa notação hexadecimal separada por dois-pontos."}
:::

## Escopo e finalidade dos endereços

Nem todo endereço IPv4 é roteável globalmente. Alguns exemplos são loopback `127.0.0.0/8`, link-local `169.254.0.0/16`, intervalos privados como `10.0.0.0/8` e intervalos de documentação como `192.0.2.0/24`. Endereços multicast e de broadcast limitado possuem outras semânticas.

Endereços privados podem ser reutilizados em redes separadas. O NAT pode traduzi-los para comunicação externa, mas não é necessário para a comunicação dentro do domínio privado roteado.

:::single-choice{#ipv4-private-reuse} Por que `10.0.0.1` pode aparecer em muitas organizações?

::option[Toda ocorrência identifica o mesmo roteador físico.]{#ipv4-same-router explanation="O endereço possui significado dentro de cada rede e não é globalmente exclusivo."}
::option[Os roteadores IPv4 ignoram o primeiro octeto.]{#ipv4-ignore-octet explanation="Todos os bits do endereço participam da correspondência de rotas."}
::option[Ele pertence a um intervalo de endereços destinado à reutilização em redes privadas.]{#ipv4-private-range .correct explanation="Redes privadas separadas podem usar os mesmos endereços sem anunciá-los globalmente."}
:::

## Inspecionando endereços IPv4 no Linux

Exiba as atribuições de IPv4 com:

```bash
$ ip -4 address show
```

Uma linha como esta informa mais do que o endereço:

```text
inet 192.0.2.165/24 brd 192.0.2.255 scope global dynamic eth0
```

Ela mostra prefixo, broadcast, escopo, marcador de origem dinâmica e interface. Linhas adicionais podem mostrar as durações válida e preferencial. Uma interface pode conter vários endereços IPv4.

:::single-choice{#ipv4-ip-output-prefix} O que `/24` significa em `192.0.2.165/24`?

::option[O endereço expira depois de 24 segundos.]{#ipv4-prefix-seconds explanation="A duração é informada separadamente."}
::option[Os primeiros 24 bits do endereço formam o prefixo de rede.]{#ipv4-prefix-bits .correct explanation="Os oito bits restantes identificam posições dentro desse prefixo."}
::option[A interface é a porta TCP 24.]{#ipv4-prefix-port explanation="A notação de prefixo CIDR é independente das portas de transporte."}
:::

## Determinando a origem selecionada

A presença de um endereço não comprova que o Linux o usará para um destino. Rotas, regras de política, métricas e a vinculação da aplicação influenciam a seleção da origem. Consulte a decisão atual de roteamento:

```bash
$ ip route get 198.51.100.20
```

Leia o próximo salto, a interface e a origem selecionados e depois teste o caminho real da aplicação. Não altere endereços em um host remoto sem acesso ao console e um plano de reversão.

:::single-choice{#ipv4-route-get-purpose} O que `ip route get DESTINATION` pode mostrar?

::option[A configuração de todos os roteadores no caminho completo pela Internet.]{#ipv4-all-router-config explanation="Uma consulta local não examina as configurações dos dispositivos seguintes."}
::option[A decisão de rota local, inclusive a interface e a origem preferida.]{#ipv4-route-decision .correct explanation="Ele avalia a política de roteamento atual do host para o destino fornecido."}
::option[A senha do usuário no destino.]{#ipv4-password explanation="Comandos de roteamento não expõem credenciais de aplicações."}
:::

## Resumo

Agora você pode ler um endereço IPv4 como parte do estado da interface e do roteamento.

1. Reconheça o IPv4 como quatro octetos, totalizando 32 bits.
2. Interprete um endereço junto com seu prefixo.
3. Diferencie escopos privados, de loopback, link-local e outros.
4. Inspecione as atribuições e a origem selecionada para um destino.
