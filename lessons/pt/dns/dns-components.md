---
lesson_id: "dns-components"
course_id: "dns"
lang: "pt"
order_index: 2
title: "Componentes do DNS"
description: "Aprenda como resolvedores recursivos, servidores autoritativos, zonas e registros de recursos dividem as responsabilidades do DNS."
meta_title: "Componentes do DNS - DNS"
meta_description: "Aprenda sobre os componentes do DNS: servidores de nomes, arquivos de zona e registros de recursos. Entenda como o DNS funciona neste guia para iniciantes e comece sua jornada pelas redes Linux!"
meta_keywords: "componentes do DNS, servidor de nomes, arquivo de zona, registros de recursos, tutorial DNS, redes Linux, guia para iniciantes"
---

O DNS separa a função de recursão voltada para o cliente da publicação autoritativa. Entender esse limite evita confundir uma resposta em cache com o proprietário de uma zona.

## Resolvedores stub e recursivos

Um resolvedor stub em uma aplicação ou sistema operacional envia consultas a um resolvedor recursivo configurado. O resolvedor recursivo retorna uma resposta final, um erro ou o resultado de um encaminhamento depois de usar o cache e, quando necessário, realizar consultas iterativas. Sua resposta só pode conter o sinalizador de resposta autoritativa quando o servidor que responde possui autoridade sobre os dados; a recursão por si só não o torna autoritativo.

:::single-choice{#dns-components-recursive-role} O que um resolvedor recursivo faz para um cliente stub?

::option[Obtém um resultado DNS final usando o cache e outros servidores de nomes.]{#dns-components-recursive-result .correct explanation="O cliente delega ao serviço recursivo o trabalho da consulta em várias etapas."}
::option[Substitui todos os roteadores de rede no caminho dos pacotes.]{#dns-components-replaces-router explanation="A resolução de nomes e o encaminhamento IP são funções separadas."}
::option[Torna-se autoritativo para todo registro que armazena em cache.]{#dns-components-cache-authority explanation="Os dados em cache mantêm a autoridade de sua origem; o resolvedor não é o proprietário da zona."}
:::

## Servidores de nomes autoritativos

Um servidor autoritativo responde a partir dos dados de zona sobre os quais possui autoridade. Uma zona deve ter vários servidores autoritativos com dados sincronizados e considerações independentes de falha. Um servidor apenas autoritativo não precisa realizar recursão para clientes arbitrários.

:::single-choice{#dns-components-authoritative-role} O que torna um servidor autoritativo para uma zona?

::option[Ele consultou a zona uma vez por meio de um resolvedor público.]{#dns-components-once-queried explanation="Consultar ou armazenar em cache não confere autoridade."}
::option[Ele serve os dados da zona segundo a delegação e a configuração relevantes.]{#dns-components-serves-zone .correct explanation="A autoridade vem da delegação DNS e da zona carregada pelo servidor, não de possuir uma cópia em cache."}
::option[Ele responde mais rapidamente a um ping.]{#dns-components-fastest-ping explanation="O tempo do ICMP não define a autoridade DNS."}
:::

## Zonas e armazenamento de zonas

Uma zona é uma parte do espaço de nomes DNS servida administrativamente. Ela começa no ápice da zona e pode delegar zonas filhas. Os dados da zona podem ser armazenados em um arquivo de zona textual, gerados a partir de um banco de dados, carregados por uma API ou sintetizados por software; um “arquivo de zona” não é uma implementação física obrigatória.

O ápice da zona normalmente possui um registro SOA e um conjunto NS. Os dados de delegação no pai identificam os servidores autoritativos filhos, às vezes acompanhados por registros de endereço glue necessários para alcançar nomes de servidores pertencentes à própria zona delegada.

:::single-choice{#dns-components-zone-meaning} O que é uma zona DNS?

::option[Uma parte do espaço de nomes servida administrativamente.]{#dns-components-admin-portion .correct explanation="Ela pode conter registros e delegações, independentemente do mecanismo de armazenamento."}
::option[Um único arquivo de texto obrigatório em cada cliente.]{#dns-components-client-file explanation="Implementações autoritativas podem usar várias formas de armazenamento, e os clientes não mantêm todas as zonas."}
::option[Um domínio de broadcast Ethernet identificado por uma VLAN.]{#dns-components-vlan explanation="Zonas DNS e segmentos da camada de enlace são conceitos independentes."}
:::

## Campos dos registros de recursos

Um registro de recurso possui nome do proprietário, TTL, classe, tipo e RDATA específico do tipo. Por exemplo:

```text
www.example.com.  300  IN  A  192.0.2.25
```

O proprietário é `www.example.com.`, o TTL é 300 segundos, a classe é Internet, o tipo é endereço IPv4 e o RDATA é o endereço. As regras de omissão de campos e nomes relativos na sintaxe dos arquivos de zona exigem cuidado com a origem.

:::single-choice{#dns-components-mx-type} Qual tipo de registro publica a preferência e os nomes de host dos servidores de mensagens?

::option[`A`]{#dns-components-a explanation="Um registro A armazena um endereço IPv4."}
::option[`NS`]{#dns-components-ns explanation="Registros NS identificam servidores de nomes autoritativos."}
::option[`MX`]{#dns-components-mx .correct explanation="O RDATA de MX inclui uma preferência e o nome de um servidor de mensagens."}
:::

## TTL e cache negativo

Registros positivos usam TTLs para limitar a reutilização do cache. Respostas negativas, como um nome comprovadamente inexistente, também podem ser armazenadas em cache de acordo com regras derivadas do SOA. Reduzir um TTL pouco antes de uma mudança planejada afeta apenas registros obtidos depois que os caches observam o valor menor; valores maiores armazenados anteriormente permanecem até expirar.

:::single-choice{#dns-components-lower-ttl-timing} Por que reduzir o TTL do DNS bem antes de uma mudança planejada de endereço?

::option[O TTL modifica a MTU Ethernet do servidor.]{#dns-components-ttl-mtu explanation="A duração do cache e o tamanho dos pacotes no enlace não têm relação."}
::option[Um TTL menor garante que a nova aplicação esteja íntegra.]{#dns-components-ttl-health explanation="Ele afeta o comportamento do cache, não a correção do serviço."}
::option[Os caches existentes precisam de tempo para expirar registros aprendidos com o TTL antigo e maior.]{#dns-components-old-cache-expiry .correct explanation="Alterar os dados autoritativos não pode reduzir retroativamente a duração restante de um registro já armazenado em cache."}
:::

## Resumo

Agora você pode separar recursão DNS, autoridade, gerenciamento do espaço de nomes e registros em cache.

1. Identifique as funções dos resolvedores stub e recursivo.
2. Defina a autoridade por meio do serviço delegado da zona.
3. Trate uma zona como responsabilidade sobre o espaço de nomes, não como um arquivo obrigatório.
4. Leia os campos proprietário, TTL, classe, tipo e RDATA.
5. Planeje as durações do cache antes de mudanças no DNS.
