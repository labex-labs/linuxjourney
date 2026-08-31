---
lesson_id: "what-is-dns"
course_id: "dns"
lang: "pt"
order_index: 1
title: "O que é DNS?"
description: "Aprenda como o DNS organiza e resolve nomes distribuídos e registros de recursos tipados."
meta_title: "O que é DNS? - DNS"
meta_description: "Para aprender redes Linux, é essencial entender o DNS. Este guia explica o que é o Sistema de Nomes de Domínio (DNS), como ele traduz nomes de domínio em endereços IP e por que é o catálogo de endereços essencial da Internet. Um ponto de partida ideal para aprender Linux."
meta_keywords: "DNS, Sistema de Nomes de Domínio, endereço IP, aprender linux, linux aprender, nome de host, redes Linux, iniciante, tutorial, guia, labex linux"
---

O Sistema de Nomes de Domínio é um banco de dados distribuído e hierárquico e um protocolo de consulta. Ele permite que os clientes recuperem informações tipadas associadas a nomes, incluindo endereços, roteamento de mensagens, servidores autoritativos, dados de serviços e registros de verificação.

## Nomes e registros de recursos

O DNS faz mais do que traduzir um nome de host em um endereço IP. Um registro `A` contém um endereço IPv4, `AAAA` um endereço IPv6, `MX` dados de roteamento de mensagens, `NS` nomes de servidores autoritativos, e muitos outros tipos transportam dados diferentes. Um nome pode ter vários registros ou nenhum registro de endereço.

:::single-choice{#dns-purpose-beyond-address}
Por que o DNS é mais do que uma lista de nomes de host e endereços?

::option[Ele atribui permanentemente endereços MAC a todos os quadros Ethernet.]{#dns-mac-frames explanation="A descoberta de vizinhos da camada de enlace não usa o DNS dessa maneira."}
::option[Ele armazena registros tipados para vários tipos de dados de serviços e delegação.]{#dns-typed-records .correct explanation="Registros de endereço, mensagens, autoridade, alias e políticas possuem semânticas distintas."}
::option[Ele garante que toda aplicação nomeada esteja íntegra.]{#dns-health-guarantee explanation="Os dados DNS podem ser resolvidos mesmo quando o serviço de destino está indisponível."}
:::

## Nomes hierárquicos

Um nome de domínio totalmente qualificado identifica um caminho na árvore DNS. Em `www.example.com.`, o ponto final representa a raiz, `com` está abaixo dela, `example` está abaixo de `com`, e `www` é um nome dentro desse domínio. O ponto final costuma ser omitido nas interfaces de usuário, mas é importante para diferenciar nomes absolutos de nomes localmente relativos na configuração.

:::single-choice{#dns-trailing-dot}
O que o ponto final em `www.example.com.` representa?

::option[A raiz do DNS e um nome absoluto.]{#dns-root-dot .correct explanation="O ponto encerra o caminho completo entre o nó nomeado e a raiz."}
::option[Um curinga para todos os domínios de primeiro nível.]{#dns-dot-wildcard explanation="Um curinga usa um rótulo como `*`, não o terminador da raiz."}
::option[Uma instrução para usar apenas IPv4.]{#dns-dot-ipv4 explanation="O tipo de registro controla a família de endereços solicitada."}
:::

## Autoridade distribuída

A autoridade do DNS é delegada ao longo da hierarquia. Servidores raiz direcionam os resolvedores para servidores de domínios de primeiro nível, que os direcionam aos servidores autoritativos das zonas delegadas. As organizações gerenciam seus próprios dados autoritativos sem armazenar todo o espaço global de nomes em um servidor central.

:::single-choice{#dns-authoritative-data}
Quem fornece os dados definitivos de uma zona DNS delegada?

::option[Qualquer navegador que já tenha visitado o site.]{#dns-browser-authority explanation="O cache de um navegador não é autoritativo para a zona."}
::option[Os servidores de nomes autoritativos configurados para a zona.]{#dns-authoritative-servers .correct explanation="A delegação identifica os servidores responsáveis por responder com autoridade."}
::option[Todo roteador que transporta um pacote até o endereço.]{#dns-router-authority explanation="O encaminhamento de pacotes e a autoridade DNS são funções separadas."}
:::

## Resolução e cache

O resolvedor stub de um host geralmente envia uma consulta a um resolvedor recursivo. Esse resolvedor pode responder a partir de um cache válido ou consultar a hierarquia em nome do cliente. Os TTLs dos registros limitam por quanto tempo as entradas de cache normalmente podem ser reutilizadas, melhorando a escalabilidade, mas adiando a visibilidade das alterações até que os caches sejam atualizados.

O sucesso do DNS não comprova a integridade da rota, do transporte, do TLS nem da aplicação. Uma falha de DNS também pode ocorrer antes de qualquer consulta externa, pois `/etc/hosts`, sufixos de pesquisa, caches locais ou políticas de serviços de nomes afetam o resolvedor do sistema.

:::single-choice{#dns-cache-ttl-role}
O que o TTL de um registro DNS controla principalmente?

::option[Quantos roteadores um pacote IP pode atravessar.]{#dns-ip-hop-limit explanation="O TTL ou o Limite de Saltos do IP é um campo de protocolo diferente."}
::option[Por quanto tempo a aplicação deve permanecer íntegra.]{#dns-app-health-time explanation="O cache DNS não fornece garantia de disponibilidade do serviço."}
::option[Por quanto tempo um resolvedor pode armazenar o registro em cache segundo as regras normais.]{#dns-cache-lifetime .correct explanation="Um cache mais curto ou mais longo afeta a carga de consultas e a propagação das alterações."}
:::

## Resumo

Agora você pode descrever o DNS como um sistema de dados tipados, em cache e hierárquico.

1. Diferencie os tipos de registros de recursos DNS por finalidade.
2. Leia um nome totalmente qualificado a partir da raiz.
3. Identifique a delegação e a responsabilidade autoritativa.
4. Separe a resolução de nomes da conectividade com a aplicação.
