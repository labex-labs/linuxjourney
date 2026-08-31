---
lesson_id: "dns-tools"
course_id: "dns"
lang: "pt"
order_index: 6
title: "Ferramentas de DNS"
description: "Aprenda a comparar a resolução do sistema e consultas DNS diretas com getent, resolvectl e dig."
meta_title: "Ferramentas de DNS - DNS"
meta_description: "Explore ferramentas essenciais de DNS no Linux, como nslookup e o poderoso comando dig. Este tutorial de Linux para iniciantes aborda consultas DNS e técnicas de solução de problemas de DNS."
meta_keywords: "nslookup, comando dig, ferramentas de DNS, DNS Linux, solução de problemas de DNS, consulta a servidor de nomes, tutorial Linux, Linux para iniciantes"
---

A solução de problemas de DNS começa pela identificação da camada que está sendo testada. Ferramentas do resolvedor do sistema incluem arquivos locais e políticas, enquanto `dig` e `nslookup` enviam consultas DNS e podem apontar diretamente para um servidor específico.

## Testando o resolvedor do sistema

Use o caminho normal de serviços de nomes do host com:

```bash
$ getent ahosts www.example.com
```

Em um host com systemd-resolved, inspecione servidores por enlace, domínios de pesquisa e estado dos protocolos com:

```bash
$ resolvectl status
$ resolvectl query www.example.com
```

Uma aplicação ainda pode usar uma biblioteca resolvedora ou um proxy próprio; portanto, reproduza o teste pela aplicação quando os resultados forem diferentes.

:::single-choice{#dns-tools-system-resolver}
Qual comando exercita o caminho configurado dos serviços de nomes do sistema?

::option[Apenas `dig @SERVER NAME`.]{#dns-tools-dig-direct explanation="Dig envia uma consulta DNS e normalmente não lê os mapeamentos do arquivo hosts."}
::option[`ip link set down`]{#dns-tools-link-down explanation="Isso interrompe a interface em vez de testar a resolução."}
::option[`getent ahosts NAME`]{#dns-tools-getent .correct explanation="Ele pode refletir `/etc/hosts`, DNS e outras fontes do Name Service Switch."}
:::

## Consultando com dig

Especifique um nome e um tipo de registro:

```bash
$ dig www.example.com A
$ dig www.example.com AAAA
$ dig example.com MX
```

A saída identifica o servidor que respondeu, o estado, os sinalizadores, a pergunta, a resposta, a autoridade, os dados adicionais, o tempo da consulta e os metadados do transporte. `+short` é conveniente para scripts, mas oculta evidências necessárias ao diagnóstico.

:::single-choice{#dns-tools-record-type}
Qual consulta solicita registros de endereço IPv6?

::option[`dig NAME AAAA`]{#dns-tools-aaaa .correct explanation="Registros AAAA contêm endereços IPv6."}
::option[`dig NAME MX`]{#dns-tools-mx explanation="MX solicita registros de servidores de mensagens."}
::option[`dig NAME PTR` no nome direto.]{#dns-tools-ptr-forward explanation="PTR normalmente é consultado por meio de um nome de pesquisa reversa."}
:::

## Selecionando um servidor

Aponte explicitamente para um resolvedor ou servidor autoritativo:

```bash
$ dig @192.0.2.53 www.example.com A
```

Compare o resolvedor recursivo configurado, um segundo resolvedor aprovado e cada servidor autoritativo ao diferenciar cache de autoridade. Um estado `NOERROR` pode não conter a resposta solicitada; `NXDOMAIN` significa que o nome consultado não existe, enquanto `SERVFAIL` significa que o servidor não conseguiu concluir a consulta.

:::single-choice{#dns-tools-noerror-empty}
`NOERROR` pode ter uma seção de resposta vazia?

::option[Sim, quando o nome existe, mas não possui os dados de registro solicitados.]{#dns-tools-noerror-nodata .correct explanation="O estado e a quantidade de respostas devem ser interpretados em conjunto."}
::option[Não, ele garante pelo menos um registro de endereço.]{#dns-tools-noerror-always-answer explanation="O nome pode existir sem dados do tipo solicitado."}
::option[Não, respostas vazias sempre são falhas do Ethernet.]{#dns-tools-empty-ethernet explanation="A semântica do DNS, não o enquadramento do enlace, explica uma resposta válida sem dados."}
:::

## Verificando recursão e autoridade

`rd` na consulta solicita recursão; `ra` em uma resposta indica que o servidor a oferece. `aa` significa que a resposta é autoritativa. Consulte um servidor autoritativo com `+norecurse` para não confundir o cache recursivo com os dados servidos pela zona.

`dig +trace NAME` realiza seu próprio percurso iterativo a partir das referências da raiz. Ele pode diferir de um resolvedor de produção porque ignora o cache, o encaminhamento, a política, a validação DNSSEC e a localização de rede desse resolvedor.

:::single-choice{#dns-tools-aa-flag}
O que o sinalizador de resposta `aa` significa?

::option[A consulta usou dois endereços IPv4 idênticos.]{#dns-tools-two-addresses explanation="O sinalizador não tem relação com a quantidade de respostas nem com a família de endereços."}
::option[A resposta foi criptografada com credenciais da aplicação.]{#dns-tools-aa-encrypted explanation="Os sinalizadores DNS não estabelecem um transporte criptografado."}
::option[A resposta é autoritativa.]{#dns-tools-authoritative-answer .correct explanation="O servidor que responde declara possuir autoridade sobre os dados da resposta."}
:::

## Testando consultas reversas e por TCP

Use `-x` para construir uma consulta PTR reversa:

```bash
$ dig -x 192.0.2.25
```

Teste DNS sobre TCP ao investigar truncamento, transferências de zona ou diferenças no firewall:

```bash
$ dig +tcp @192.0.2.53 example.com SOA
```

O DNS moderno pode usar a porta 53 por UDP ou TCP; ambos devem ser permitidos onde forem necessários. Uma resposta UDP com o sinalizador de truncamento leva clientes compatíveis a repetir a consulta por um transporte apropriado.

:::single-choice{#dns-tools-tcp-test}
O que `dig +tcp` altera?

::option[Ele envia a consulta DNS usando TCP em vez da tentativa UDP padrão.]{#dns-tools-use-tcp .correct explanation="Isso ajuda a isolar a filtragem do transporte e respostas que exigem um fluxo confiável maior."}
::option[Ele solicita apenas registros de nomes de serviços TCP.]{#dns-tools-tcp-records explanation="O tipo DNS solicitado continua sendo especificado separadamente."}
::option[Ele altera permanentemente a configuração do resolvedor do servidor.]{#dns-tools-tcp-persistent explanation="Uma consulta não edita as configurações do servidor."}
:::

## Resumo

Agora você pode escolher uma ferramenta de DNS adequada à camada do resolvedor sob investigação.

1. Use `getent` para o caminho configurado do resolvedor do sistema.
2. Use `dig` com tipos de registro e servidores explícitos.
3. Interprete em conjunto estado, sinalizadores, seções e servidor que respondeu.
4. Separe o cache recursivo dos dados autoritativos.
5. Teste consultas reversas e os dois transportes DNS necessários.
