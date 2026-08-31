---
lesson_id: "dns-process"
course_id: "dns"
lang: "pt"
order_index: 3
title: "Processo do DNS"
description: "Aprenda como resolvedores stub e recursivos usam cache, encaminhamentos, glue e autoridade para responder a uma consulta DNS."
meta_title: "Processo do DNS - DNS"
meta_description: "Explore o processo de resolução DNS passo a passo, dos servidores raiz ao servidor DNS autoritativo. Entenda como um servidor Linux encontra um domínio, um conceito crucial para ambientes de produção e hospedagem de domínios."
meta_keywords: "processo DNS, consulta DNS, resolução de domínio, dns linux, servidor de produção, hospedagem de domínio, servidor dns, TLD, servidores raiz, dns autoritativo"
---

Uma aplicação comum consulta o resolvedor stub do sistema operacional, que examina a política local de serviços de nomes e envia uma consulta recursiva a um resolvedor configurado. O resolvedor recursivo só percorre a hierarquia quando o cache válido ainda não responde à pergunta.

## Começando pela política local e pelo cache

O resolvedor do sistema pode consultar `/etc/hosts`, DNS e outras fontes na ordem configurada. Sufixos de pesquisa podem transformar um nome curto em vários nomes candidatos. Um resolvedor recursivo então verifica entradas positivas e negativas do cache antes de enviar tráfego aos servidores superiores.

:::single-choice{#dns-process-cache-first}
Por que um resolvedor recursivo pode não contatar nenhum servidor autoritativo para uma consulta?

::option[O DNS exige que toda consulta falhe localmente primeiro.]{#dns-process-requires-failure explanation="Um resolvedor pode responder imediatamente a partir do cache."}
::option[Ele possui uma resposta em cache que ainda é válida.]{#dns-process-valid-cache .correct explanation="O cache evita repetir o percurso pela hierarquia até que a duração do registro expire."}
::option[Servidores autoritativos aceitam apenas quadros Ethernet de clientes.]{#dns-process-authoritative-ethernet explanation="O DNS opera sobre transportes IP através de redes roteadas."}
:::

## Consultando um servidor raiz

Quando não há uma resposta no cache, um resolvedor recursivo pode consultar um servidor raiz. A raiz do DNS possui 13 identidades de servidores nomeadas de A a M, atendidas por muitas instâncias físicas que usam anycast e outras técnicas resilientes de implantação. Normalmente, a resposta encaminha o resolvedor aos servidores autoritativos do domínio de primeiro nível relevante, em vez de retornar o endereço final do host.

:::single-choice{#dns-process-root-response}
O que um servidor raiz normalmente retorna para uma consulta sem cache de `www.example.com`?

::option[Um encaminhamento para os servidores do domínio de primeiro nível `com`.]{#dns-process-root-referral .correct explanation="A hierarquia delega a responsabilidade, em vez de armazenar cada registro final de host na raiz."}
::option[A página Web hospedada em `www.example.com`.]{#dns-process-root-webpage explanation="O DNS retorna dados de registros de recursos, não conteúdo da aplicação."}
::option[O endereço MAC Ethernet do destino.]{#dns-process-root-mac explanation="Endereços MAC são resolvidos em enlaces locais, não pela hierarquia DNS."}
:::

## Seguindo encaminhamentos de TLD e servidores autoritativos

O resolvedor consulta um servidor autoritativo de `com`, que retorna os servidores de nomes autoritativos delegados de `example.com`. O encaminhamento pode incluir registros de endereço glue quando eles são necessários para alcançar um servidor cujo nome está dentro da zona filha delegada. Em seguida, o resolvedor consulta um servidor autoritativo sobre o registro solicitado.

:::single-choice{#dns-process-glue-purpose}
Que problema os registros glue do DNS ajudam a resolver?

::option[Criptografar cargas úteis HTTP depois da resolução DNS.]{#dns-process-glue-http explanation="O TLS ou outra segurança da aplicação cuida da criptografia da carga útil."}
::option[Escolher a porta mais rápida de um switch Ethernet.]{#dns-process-glue-switch explanation="Glue são dados de endereço da delegação, não uma política de encaminhamento do enlace."}
::option[Alcançar um servidor pertencente à zona delegada sem uma resolução circular.]{#dns-process-glue-reachability .correct explanation="A zona pai fornece os dados de endereço necessários para contatar um servidor nomeado dentro da zona filha."}
:::

## Seguindo aliases e tipos de registro

Uma resposta pode conter um alias CNAME que exige outra consulta de nome, ou registros específicos de aplicações que levam a outras consultas. Solicitar `A` retorna apenas registros de endereço IPv4 e os dados relacionados da cadeia; uma consulta `AAAA` separada recupera endereços IPv6. A resposta final contém um estado como `NOERROR`, `NXDOMAIN` ou `SERVFAIL`, cada um com um significado diferente.

:::single-choice{#dns-process-nxdomain-meaning}
O que `NXDOMAIN` informa?

::option[O nome de domínio consultado não existe segundo um resultado autoritativo.]{#dns-process-name-does-not-exist .correct explanation="Isso difere de um nome existente que apenas não possui o tipo de registro solicitado."}
::option[O nome existe e sempre possui um registro A vazio.]{#dns-process-empty-a explanation="Um nome existente sem os dados solicitados normalmente produz uma resposta sem dados, não NXDOMAIN."}
::option[O resolvedor alcançou o tamanho máximo do quadro Ethernet.]{#dns-process-frame-size explanation="O estado trata da existência do nome."}
:::

## Validação, cache e uso pela aplicação

Um resolvedor recursivo com validação pode usar assinaturas DNSSEC e a cadeia de confiança para verificar uma negação autenticada ou a integridade dos registros. O DNSSEC não criptografa as consultas nem comprova que a aplicação no endereço retornado é confiável.

O resolvedor armazena os resultados em cache segundo as regras de TTL e os retorna ao stub. A aplicação então escolhe um endereço e tenta seus próprios protocolos de rede e segurança.

:::single-choice{#dns-process-dnssec-limit}
O que a validação DNSSEC não fornece?

::option[Integridade e autenticação da origem para dados DNS assinados.]{#dns-process-dnssec-does-integrity explanation="Esses são objetivos centrais do DNSSEC."}
::option[Negação autenticada para dados inexistentes assinados.]{#dns-process-authenticated-denial explanation="Mecanismos de negação assinada podem fornecer essa validação."}
::option[Confidencialidade para a consulta e a resposta DNS.]{#dns-process-no-confidentiality .correct explanation="A criptografia exige um transporte DNS protegido separado, como DoT ou DoH."}
:::

## Resumo

Agora você pode acompanhar uma consulta DNS recursiva desde a política local até uma resposta final em cache.

1. Verifique primeiro as fontes locais e o cache do resolvedor.
2. Siga os encaminhamentos da raiz e do domínio de primeiro nível.
3. Use registros glue para alcançar os servidores delegados apropriados.
4. Diferencie aliases, respostas sem dados e nomes inexistentes.
5. Separe a integridade do DNSSEC da confidencialidade do transporte.
