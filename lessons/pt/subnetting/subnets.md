---
lesson_id: "subnets"
course_id: "subnetting"
lang: "pt"
order_index: 2
title: "Sub-redes"
description: "Aprenda como os prefixos definem sub-redes IPv4 e influenciam a entrega no enlace, o roteamento e as políticas."
meta_title: "Sub-redes - Sub-redes"
meta_description: "Domine os fundamentos das sub-redes e máscaras de sub-rede no Linux. Este guia explica a divisão em sub-redes, os prefixos de rede e como gerenciar a segmentação de redes em um ambiente Linux."
meta_keywords: "sub-rede linux, linux sub-rede, máscara de sub-rede linux, divisão em sub-redes, sub-redes, máscara de sub-rede, prefixo de rede, redes Linux, endereço IP"
---

Uma sub-rede é um intervalo de endereços IP definido por um prefixo de rede. Hosts em uma sub-rede costumam estar no mesmo enlace local, mas a proximidade física não é a definição: VLANs, túneis, sobreposições e enlaces roteados podem alterar a topologia.

## Prefixos e máscaras

O IPv4 pode expressar um prefixo de 24 bits como `/24` ou como a máscara `255.255.255.0`. Em binário, uma máscara de sub-rede convencional válida possui uns contíguos seguidos por zeros:

```text
11111111.11111111.11111111.00000000
```

Para o endereço `192.168.1.8/24`, o prefixo de rede é `192.168.1.0/24`. A escrita `192.168.1.0/255.255.255.0` é entendida em alguns contextos, mas a notação de prefixo CIDR é a forma compacta padrão.

:::single-choice{#subnets-mask-24} Qual máscara decimal pontuada corresponde a `/24`?

::option[`255.255.255.0`]{#subnets-mask-correct .correct explanation="Três octetos completos contêm 24 bits um iniciais."}
::option[`255.255.0.255`]{#subnets-noncontiguous explanation="Ela possui bits de rede não contíguos e não é a máscara `/24` convencional."}
::option[`0.0.0.24`]{#subnets-prefix-as-octet explanation="Um comprimento de prefixo não é colocado no último octeto da máscara."}
:::

## Decidindo se um destino está no enlace

O Linux instala rotas conectadas a partir dos endereços e prefixos das interfaces. Ele compara um destino com as rotas elegíveis, em vez de apenas comparar os três primeiros octetos decimais. Em limites que não coincidem com octetos, como `/20`, a divisão ocorre dentro de um octeto.

Inspecione as rotas conectadas e a decisão para um endereço:

```bash
$ ip route show
$ ip route get 192.168.1.50
```

:::single-choice{#subnets-on-link-decision} Como um host Linux determina se deve enviar diretamente ou por um roteador?

::option[Ele sempre presume que endereços terminados em `.1` são locais.]{#subnets-dot-one explanation="Convenções de números de host não substituem os prefixos e as rotas configurados."}
::option[Ele consulta os prefixos e a política de roteamento.]{#subnets-route-policy .correct explanation="A rota selecionada identifica se o destino está no enlace e qual interface ou próximo salto usar."}
::option[Ele solicita uma máscara de sub-rede à aplicação de destino depois de se conectar.]{#subnets-ask-application explanation="A seleção da rota precisa ocorrer antes dessa troca com a aplicação."}
:::

## Roteamento entre sub-redes

Um roteador com interfaces e rotas adequadas pode encaminhar tráfego entre sub-redes. Um gateway padrão é simplesmente um próximo salto selecionado por uma rota padrão; ele não precisa usar o primeiro endereço utilizável nem terminar em `.1`.

A separação em sub-redes cria um ponto para aplicar políticas de roteamento e filtragem, mas não constitui automaticamente um limite de segurança. Se o encaminhamento for permitido sem uma política restritiva, hosts em sub-redes diferentes ainda poderão se comunicar.

:::single-choice{#subnets-security-boundary} A criação de duas sub-redes bloqueia automaticamente o tráfego entre elas?

::option[Sim, porque roteadores não podem conectar prefixos diferentes.]{#subnets-never-route explanation="Conectar prefixos é a principal função do roteamento."}
::option[Não; as políticas de roteamento e filtragem determinam o tráfego permitido.]{#subnets-policy-required .correct explanation="A segmentação permite aplicar políticas, mas não as define por si só."}
::option[Sim, a menos que ambas usem o endereço de host `.1`.]{#subnets-dot-one-security explanation="Uma convenção de número de host não controla o encaminhamento."}
:::

## Motivos para criar sub-redes

A divisão em sub-redes pode organizar a alocação de endereços, limitar o escopo de broadcast da camada de enlace, separar domínios de falha e fornecer limites para políticas. Ela também pode acrescentar complexidade de roteamento, firewall, DHCP, monitoramento e documentação. Projete os prefixos de acordo com requisitos reais de escala, crescimento, redundância e segurança, em vez de presumir que menor sempre significa mais rápido.

:::single-choice{#subnets-design-tradeoff} Qual é uma compensação real da divisão em sub-redes?

::option[Domínios de broadcast menores não exigem roteamento nem documentação.]{#subnets-no-complexity explanation="Mais limites geralmente exigem mais gerenciamento de rotas, políticas, endereços e serviços."}
::option[A segmentação pode melhorar a organização enquanto aumenta a complexidade das políticas.]{#subnets-tradeoff .correct explanation="Os limites das sub-redes podem favorecer o controle, mas acrescentam estado operacional que precisa ser mantido."}
::option[Toda sub-rede garante a mesma latência até a Internet.]{#subnets-equal-latency explanation="As condições do caminho e da carga de trabalho determinam a latência."}
:::

## Resumo

Agora você pode relacionar um prefixo IPv4 à entrega local e às políticas roteadas.

1. Expresse máscaras contíguas com comprimentos de prefixo CIDR.
2. Calcule o prefixo de rede a partir dos bits do endereço e da máscara.
3. Use rotas para determinar a entrega no enlace ou pelo próximo salto.
4. Trate o isolamento de sub-redes como uma oportunidade para aplicar políticas, não como uma garantia.
