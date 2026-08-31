---
lesson_id: "bgp-border-gateway-protocol"
course_id: "routing"
lang: "pt"
order_index: 7
title: "Protocolo de Gateway de Borda"
description: "Aprenda como o BGP troca informações de acessibilidade IP controladas por políticas entre sistemas autônomos e dentro deles."
meta_title: "Protocolo de Gateway de Borda - Roteamento"
meta_description: "Explore os fundamentos do Protocolo de Gateway de Borda (BGP), o protocolo central que possibilita o roteamento da Internet. Aprenda como o BGP facilita a comunicação entre sistemas autônomos e os princípios do roteamento por protocolo de gateway de borda."
meta_keywords: "BGP, Protocolo de Gateway de Borda, roteamento por protocolo de gateway de borda, roteamento da internet, sistemas autônomos, redes Linux, tutorial BGP, protocolos de rede"
---

O Protocolo de Gateway de Borda é o protocolo de roteamento por vetor de caminhos da Internet. Ele troca informações de acessibilidade de prefixos IP e atributos de caminho para que as redes possam aplicar políticas administrativas, em vez de escolher rotas apenas pela distância física.

## Sistemas autônomos e sessões

Um sistema autônomo é um conjunto de redes sob uma administração comum de roteamento, identificado no BGP por um número de sistema autônomo. O BGP externo troca rotas entre sistemas autônomos; o BGP interno distribui a acessibilidade BGP dentro de um AS.

Os pares BGP estabelecem uma sessão pela porta TCP 179. Uma sessão TCP funcional é apenas a base de transporte; os recursos, as políticas e a troca de rotas do BGP também precisam funcionar.

:::single-choice{#bgp-external-session}
O que o BGP externo troca?

::option[Somas de verificação de quadros Ethernet dentro de um switch.]{#bgp-ethernet-fcs explanation="O BGP opera acima do TCP e troca informações de acessibilidade da camada de rede."}
::option[Senhas de usuários entre navegadores Web.]{#bgp-browser-passwords explanation="Credenciais de aplicações não são atributos de roteamento."}
::option[Informações de acessibilidade e caminho entre sistemas autônomos.]{#bgp-between-as .correct explanation="O eBGP conecta administrações de roteamento separadas e aplica políticas entre domínios."}
:::

## Informações de vetor de caminhos

Um anúncio inclui um prefixo e atributos. `AS_PATH` lista os sistemas autônomos atravessados e ajuda a detectar loops. Outros atributos comuns incluem `LOCAL_PREF`, `MED`, origem, próximo salto e comunidades. Seus efeitos dependem da direção, da implementação e da política.

:::single-choice{#bgp-as-path-loop}
Como `AS_PATH` ajuda a evitar loops entre ASs?

::option[Um AS pode rejeitar um caminho que já contenha seu próprio número.]{#bgp-own-as-reject .correct explanation="O vetor de caminhos expõe a sequência de ASs usada para alcançar o prefixo anunciado."}
::option[Ele criptografa cada pacote que atravessa esses sistemas.]{#bgp-aspath-encryption explanation="O atributo descreve o caminho de roteamento e não fornece criptografia da carga útil."}
::option[Ele atribui um endereço MAC a cada AS.]{#bgp-aspath-mac explanation="Números de sistemas autônomos e endereços de enlace são espaços de nomes separados."}
:::

## Seleção baseada em políticas

O “melhor” caminho do BGP é o que vence um processo de decisão configurado. Os operadores podem preferir rotas de clientes, alterar a preferência local, filtrar prefixos, usar comunidades e aplicar políticas de engenharia de tráfego. Um `AS_PATH` mais curto pode importar em uma etapa, mas não substitui universalmente atributos de prioridade mais alta.

Depois que o BGP seleciona candidatos, o encaminhamento IP comum ainda aplica a correspondência de prefixo mais longo. Um `/24` selecionado é usado para seus destinos em vez de um `/16` selecionado que o abrange.

:::single-choice{#bgp-best-path-meaning}
O que representa o melhor caminho do BGP?

::option[A rota que vence o processo local de decisão por atributos e políticas.]{#bgp-policy-winner .correct explanation="A intenção administrativa é central para a seleção de caminhos entre domínios."}
::option[A rota fisicamente mais curta por cabos em todos os casos.]{#bgp-shortest-cable explanation="O BGP não possui um mapa completo das distâncias físicas."}
::option[Uma garantia da menor latência atual para a aplicação.]{#bgp-lowest-latency explanation="Por padrão, a seleção do BGP não otimiza continuamente a latência do usuário final."}
:::

## Anúncio e acessibilidade

Anunciar um prefixo declara acessibilidade conforme uma política; não cria a rota subjacente nem garante o caminho de retorno. Antes de originar um prefixo, assegure o encaminhamento válido, o comportamento da agregação, os filtros, o failover e a autorização de propriedade.

:::single-choice{#bgp-advertisement-limit}
O que o anúncio de um prefixo não consegue garantir?

::option[Que os pares possam receber uma rota do plano de controle.]{#bgp-peers-control explanation="O anúncio e a aceitação bem-sucedidos podem comprovar esse fato limitado do plano de controle."}
::option[Que o prefixo contém bits de endereço.]{#bgp-prefix-bits explanation="Um prefixo IP é definido por bits de endereço e um comprimento."}
::option[Que ele consegue entregar pacotes para todo o prefixo.]{#bgp-data-plane-not-guaranteed .correct explanation="Rotas subjacentes, próximos saltos, filtragem e integridade dos serviços ainda precisam ser verificados."}
:::

## Segurança de roteamento e controle de mudanças

Vazamentos e sequestros de rotas podem afetar o tráfego muito além de um roteador. Os operadores usam filtros rigorosos de importação e exportação, limites máximos de prefixos, políticas de pares, monitoramento e validação de origem pela Infraestrutura de Chaves Públicas de Recursos, quando apropriado. A validação de origem RPKI verifica se um AS está autorizado a originar um prefixo; ela não valida todo o caminho de ASs.

Alterações no BGP exigem implantação gradual, revisão das diferenças de rotas, acesso fora de banda, reversão e verificação dos planos de controle e dados.

:::single-choice{#bgp-rpki-limit}
O que a validação de origem RPKI verifica?

::option[Se toda carga útil dos pacotes está livre de malware.]{#bgp-payload-malware explanation="A RPKI não inspeciona o conteúdo das aplicações."}
::option[Se todo o caminho de ASs possui a menor latência.]{#bgp-path-latency explanation="A validação de origem não é uma seleção por desempenho nem uma validação completa do caminho."}
::option[Se o AS de origem está autorizado.]{#bgp-origin-authorized .correct explanation="Ela valida a autorização da origem, não todas as relações de trânsito no caminho de ASs."}
:::

## Resumo

Agora você pode descrever o BGP como roteamento por vetor de caminhos controlado por políticas.

1. Diferencie sessões BGP externas de internas.
2. Use `AS_PATH` como informação de caminho e de loops.
3. Interprete o melhor caminho por meio de atributos e políticas locais.
4. Verifique o encaminhamento por trás de cada prefixo anunciado.
5. Aplique filtragem, validação de origem, monitoramento e reversão.
