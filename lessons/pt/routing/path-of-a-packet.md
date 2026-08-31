---
lesson_id: "path-of-a-packet"
course_id: "routing"
lang: "pt"
order_index: 3
title: "Caminho de um pacote"
description: "Aprenda como rotas, descoberta de vizinhos, quadros e roteadores transportam um pacote IP por um caminho."
meta_title: "Caminho de um pacote - Roteamento"
meta_description: "Explore o caminho completo de um pacote de dados dentro de uma rede local e através da Internet. Aprenda como endereços IP, endereços MAC, ARP e tabelas de roteamento trabalham juntos para permitir a comunicação de rede no Linux."
meta_keywords: "caminho do pacote, comunicação de rede, ARP, endereço IP, endereço MAC, tabela de roteamento, gateway padrão, redes Linux, percurso do pacote"
---

O caminho de um pacote é uma sequência de decisões locais. O host de origem, cada roteador e o destino aplicam seus próprios estados de roteamento, vizinhança, filtragem e protocolo; normalmente, nenhum ponto de extremidade conhece antecipadamente todas as decisões internas.

## Enviando para um destino no enlace

Para um destino abrangido por uma rota conectada, a origem seleciona uma interface e um IP de origem. Em seguida, resolve o endereço de enlace do destino — ARP para IPv4 sobre Ethernet ou Descoberta de Vizinhos para IPv6 — e envia um quadro que transporta o pacote IP. Um switch pode encaminhar o quadro sem se tornar um salto IP.

:::single-choice{#packet-path-switch-hop}
Um switch Ethernet comum conta como um salto de roteamento IP?

::option[Não; ele encaminha quadros locais sem reduzir o campo de saltos do IP.]{#packet-path-switch-not-hop .correct explanation="Um salto roteado ocorre quando um roteador processa e encaminha o pacote IP."}
::option[Sim; todo switch substitui o destino IP.]{#packet-path-switch-replaces-ip explanation="O encaminhamento de Camada 2 normalmente não reescreve os destinos IP."}
::option[Sim; todo conector de cabo também é um salto IP.]{#packet-path-cable-hop explanation="Componentes físicos não realizam roteamento IP."}
:::

## Enviando por um gateway

Para um destino fora do enlace, a rota selecionada identifica um roteador de próximo salto. O destino IP continua sendo o ponto de extremidade remoto, enquanto o destino do quadro local é o endereço de enlace do gateway. O host resolve o gateway, não o servidor remoto, em seu enlace local.

:::single-choice{#packet-path-gateway-mac}
O endereço MAC de quem é usado no primeiro quadro Ethernet para um servidor fora do enlace?

::option[O endereço do servidor remoto através de todas as redes intermediárias.]{#packet-path-remote-mac explanation="O endereço de enlace remoto não possui significado na LAN de origem."}
::option[Um valor calculado a partir do nome DNS do servidor.]{#packet-path-dns-mac explanation="Nomes DNS não codificam o MAC do próximo salto local."}
::option[O endereço do gateway local selecionado.]{#packet-path-local-gateway .correct explanation="O quadro é entregue ao próximo salto, enquanto o cabeçalho IP aponta para o ponto de extremidade final."}
:::

## Processamento em cada roteador

Um roteador remove o enquadramento de enlace recebido, valida e processa o cabeçalho IP, reduz o TTL ou o Limite de Saltos, consulta o destino, aplica a política e cria um novo enquadramento para o enlace de saída. No IPv4, o processamento da soma de verificação do cabeçalho reflete a alteração do TTL. Se o campo de saltos chegar a zero, o roteador descarta o pacote e pode retornar uma mensagem ICMP de tempo excedido.

:::single-choice{#packet-path-router-change}
Qual campo IP é alterado por todo salto roteado normal?

::option[O nome de usuário da aplicação.]{#packet-path-username explanation="Roteadores não precisam de dados de contas da aplicação para o encaminhamento básico."}
::option[O TTL do IPv4 ou o Limite de Saltos do IPv6.]{#packet-path-hop-field .correct explanation="Cada roteador reduz o campo para limitar os loops de roteamento."}
::option[A porta de transporte de destino em todos os casos.]{#packet-path-port explanation="O roteamento comum preserva os pontos de extremidade do transporte; o NAT pode ser uma transformação separada."}
:::

## Considerando dispositivos intermediários e MTU

O roteamento comum preserva os endereços IP de origem e destino, mas o NAT pode reescrevê-los, e túneis podem encapsular o pacote original. Firewalls podem descartar o tráfego silenciosamente ou rejeitá-lo. As MTUs dos enlaces também diferem; roteadores IPv4 às vezes podem fragmentar pacotes, enquanto roteadores IPv6 não fragmentam pacotes encaminhados e dependem da Descoberta da MTU do Caminho.

:::single-choice{#packet-path-address-change-exception}
Quando os endereços IP de ponta a ponta podem mudar ao longo de um caminho?

::option[Sempre que um switch Ethernet aprende um MAC de origem.]{#packet-path-switch-learning-ip explanation="O aprendizado do switch afeta uma tabela de encaminhamento de enlace, não os endereços dos pontos de extremidade IP."}
::option[Quando uma política de NAT traduz os cabeçalhos dos pacotes.]{#packet-path-nat-change .correct explanation="A tradução é uma função de dispositivo intermediário além do encaminhamento de rotas comum."}
::option[Sempre que uma entrada do cache DNS expira.]{#packet-path-dns-expiry explanation="Os pacotes existentes já contêm endereços numéricos."}
:::

## Acompanhando o caminho de retorno

O destino realiza sua própria consulta de rota para a resposta. O caminho de retorno pode usar roteadores diferentes devido a políticas de roteamento, balanceamento de carga ou falhas. Firewalls com estado e NAT precisam considerar o fluxo observado; por isso, a assimetria pode importar operacionalmente mesmo quando é permitida pelo IP.

:::single-choice{#packet-path-return-symmetry}
Uma resposta precisa atravessar os mesmos roteadores na ordem inversa?

::option[Sim, porque o IP registra a rota completa de saída em cada pacote.]{#packet-path-records-route explanation="Pacotes IP comuns não transportam uma rota inversa completa obrigatória."}
::option[Sim, a menos que a origem e o destino compartilhem um nome de host.]{#packet-path-hostname-symmetry explanation="Os nomes não impõem simetria de caminho."}
::option[Não; cada direção é roteada de forma independente.]{#packet-path-independent-return .correct explanation="As políticas e a topologia podem produzir um caminho assimétrico, mas válido."}
:::

## Resumo

Agora você pode acompanhar a mudança do estado de enlace ao redor de um pacote IP roteado.

1. Resolva o host final somente quando ele estiver no enlace.
2. Enquadre o tráfego fora do enlace para o gateway local selecionado.
3. Acompanhe a consulta de rota e o processamento do limite de saltos em cada roteador.
4. Considere NAT, filtragem, túneis e limitações de MTU.
5. Trate a direção de retorno como uma rota independente.
