---
lesson_id: "what-is-a-router"
course_id: "routing"
lang: "pt"
order_index: 1
title: "O que é um roteador?"
description: "Aprenda como os roteadores selecionam próximos saltos e encaminham pacotes IP entre redes."
meta_title: "O que é um roteador? - Roteamento"
meta_description: "Um guia de introdução para entender o que é um roteador em redes. Aprenda sobre roteamento, comutação de pacotes, saltos e como roteadores usam tabelas de roteamento para encaminhar dados entre redes. Este guia é essencial para aprender redes Linux."
meta_keywords: "roteador, redes, roteamento, saltos, comutação de pacotes, redes Linux, tutorial para iniciantes, guia de redes"
---

Um roteador conecta domínios da camada de rede e encaminha pacotes IP entre eles. Um host Linux pode atuar como roteador quando o encaminhamento está habilitado e suas interfaces, rotas, descoberta de vizinhos e política de filtragem estão configuradas adequadamente.

## Roteamento e encaminhamento

O roteamento cria ou seleciona informações sobre prefixos acessíveis. O encaminhamento aplica essas informações a cada pacote: examina o destino, escolhe uma rota elegível e o próximo salto, reduz o limite de saltos e transmite por uma interface de saída.

Essas são questões separadas do plano de controle e do plano de dados. Uma rota pode existir enquanto a política de firewall bloqueia o encaminhamento, ou uma interface de encaminhamento pode estar ativa enquanto não existe uma rota válida.

:::single-choice{#router-forwarding-role} O que o encaminhamento de pacotes faz?

::option[Aplica as informações de roteamento para enviar um pacote em direção ao próximo salto.]{#router-apply-route .correct explanation="O encaminhamento é a ação realizada em cada pacote com base na rota e na política selecionadas."}
::option[Cria um login permanente na aplicação para cada destino.]{#router-create-login explanation="O roteamento não gerencia contas de aplicações remotas."}
::option[Copia cada pacote para todas as interfaces quando não existe uma rota.]{#router-flood-no-route explanation="O encaminhamento IP comum descarta um pacote sem rota, em vez de recorrer à inundação no estilo Ethernet."}
:::

## Tabelas de roteamento e rotas padrão

Uma rota associa um prefixo de destino a uma interface de saída, próximo salto, métrica, preferência de origem ou outros atributos. A correspondência de prefixo mais longo favorece uma rota elegível mais específica. Uma rota padrão, IPv4 `/0` ou IPv6 `::/0`, é a correspondência menos específica e só é usada quando nenhuma rota mais específica vence.

Se nenhuma rota elegível existir, o roteador descarta o pacote e pode gerar uma mensagem ICMP de destino inacessível. Uma rota padrão é opcional e não precisa apontar diretamente para a Internet pública.

:::single-choice{#router-default-route} Quando uma rota padrão é selecionada?

::option[Antes da verificação de qualquer prefixo específico do destino.]{#router-default-first explanation="Prefixos elegíveis mais específicos têm precedência."}
::option[Apenas quando o pacote é um broadcast Ethernet.]{#router-default-broadcast explanation="A seleção da rota IP se baseia nos destinos da camada de rede."}
::option[Quando nenhuma rota elegível mais específica corresponde.]{#router-default-fallback .correct explanation="O prefixo de comprimento zero é a rota menos específica."}
:::

## Tráfego local e roteado

Dois hosts na mesma sub-rede no enlace normalmente trocam quadros sem enviar o pacote IP por um roteador. Um roteador participa quando a seleção de rota o escolhe como próximo salto ou quando a topologia e a política impõem deliberadamente a passagem roteada.

Um “roteador” residencial geralmente combina roteador IP, switch Ethernet, ponto de acesso Wi-Fi, serviço DHCP, NAT e firewall. Cada função deve ser diagnosticada separadamente.

:::single-choice{#router-same-subnet-path} O tráfego entre dois hosts no enlace precisa passar pelo roteador padrão?

::option[Sim, porque todo pacote precisa alcançar uma porta WAN.]{#router-always-wan explanation="A entrega local no enlace pode ocorrer diretamente por ele."}
::option[Sim, a menos que ambos os hosts tenham endereços públicos.]{#router-public-required explanation="O escopo público ou privado não determina o encaminhamento básico no enlace."}
::option[Não; o remetente pode endereçar o destino diretamente no enlace local.]{#router-direct-on-link .correct explanation="A tabela de roteamento identifica o prefixo conectado como pertencente ao enlace."}
:::

## Saltos e prevenção de loops

Um salto roteado é uma etapa de encaminhamento da camada de rede. O TTL do IPv4 e o Limite de Saltos do IPv6 são reduzidos em cada roteador, limitando os loops. A contagem de saltos não é uma métrica completa de distância nem de qualidade: os enlaces diferem em largura de banda, latência, perda, política e congestionamento.

:::single-choice{#router-hop-count-limit} O que uma contagem menor de saltos não consegue garantir?

::option[Que existe pelo menos uma etapa roteada.]{#router-hop-exists explanation="Uma contagem positiva de saltos indica diretamente uma passagem roteada."}
::option[Um caminho mais rápido ou melhor para a aplicação.]{#router-hop-not-quality .correct explanation="Menos roteadores ainda podem atravessar enlaces mais lentos, congestionados ou limitados por políticas."}
::option[Que os campos de limite de saltos são finitos.]{#router-hop-limit-finite explanation="Esses campos são finitos por definição do protocolo."}
:::

## Resumo

Agora você pode separar a seleção de rotas de um roteador de sua ação de encaminhamento.

1. Defina roteadores pelo encaminhamento entre redes IP.
2. Diferencie o roteamento do plano de controle do encaminhamento do plano de dados.
3. Trate a rota padrão como a alternativa menos específica.
4. Reconheça que a contagem de saltos, por si só, não mede a qualidade do caminho.
