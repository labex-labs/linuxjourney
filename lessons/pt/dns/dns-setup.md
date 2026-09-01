---
lesson_id: "dns-setup"
course_id: "dns"
lang: "pt"
order_index: 5
title: "Configuração do DNS"
description: "Aprenda a escolher, proteger, validar e operar serviços DNS autoritativos ou recursivos."
meta_title: "Configuração do DNS - DNS"
meta_description: "Aprenda sobre servidores DNS populares para Linux, como BIND, dnsmasq e PowerDNS. Descubra qual servidor DNS é mais adequado à configuração de sua rede com este guia para iniciantes."
meta_keywords: "DNS Linux, BIND, dnsmasq, PowerDNS, configuração de servidor DNS, redes Linux, tutorial DNS, iniciante"
---

O software de DNS deve ser selecionado pela função e pelos requisitos operacionais, não por um “melhor servidor” universal. Um serviço autoritativo publica zonas; um serviço recursivo responde aos clientes resolvendo e armazenando em cache; um resolvedor encaminhador envia consultas a outro resolvedor. Combinar funções altera a superfície de ataque.

## Escolhendo uma função e uma implementação

- O BIND pode fornecer serviços autoritativos e recursivos com amplo suporte aos padrões.
- O Unbound é normalmente implantado como um resolvedor recursivo com validação.
- O dnsmasq fornece recursos leves de encaminhamento, cache e DHCP para redes controladas menores.
- O PowerDNS oferece produtos autoritativos e recursivos separados, com vários mecanismos de armazenamento.

Os recursos e o empacotamento mudam; portanto, consulte a documentação oficial da versão instalada. Implante apenas a função necessária e desabilite recursão ou serviço de zona não intencionais.

:::single-choice{#dns-setup-authoritative-role} Qual função publica registros definitivos para as zonas que serve?

::option[Servidor DNS autoritativo.]{#dns-setup-authoritative .correct explanation="Ele responde a partir da autoridade configurada da zona, em vez de resolver recursivamente nomes arbitrários."}
::option[Switch Ethernet.]{#dns-setup-switch explanation="Um switch encaminha quadros da camada de enlace e não publica zonas DNS."}
::option[Um resolvedor recursivo que responde a consultas arbitrárias de clientes.]{#dns-setup-stub explanation="Um stub envia consultas a um serviço recursivo e não hospeda zonas autoritativas."}
:::

## Projetando antes de instalar

Defina zonas, clientes, volume de consultas, mecanismo de atualização, necessidades de DNSSEC, registros, monitoramento, backups e recuperação. Zonas autoritativas precisam de servidores redundantes e delegações registradas corretamente. O serviço recursivo precisa de controle explícito de acesso dos clientes, política de cache, acessibilidade dos servidores superiores ou iterativos e proteção contra abuso.

Nunca exponha recursão irrestrita à Internet. Resolvedores abertos podem ser usados indevidamente em ataques de reflexão e consumir recursos locais.

:::single-choice{#dns-setup-open-recursion} Por que restringir consultas recursivas a clientes autorizados?

::option[O DNS recursivo não consegue armazenar nenhum registro em cache.]{#dns-setup-no-cache explanation="O cache é uma função central do resolvedor recursivo."}
::option[Delegações autoritativas exigem que todo usuário seja root.]{#dns-setup-all-root explanation="A delegação DNS não concede privilégios do sistema operacional."}
::option[A recursão aberta pode ser usada indevidamente para amplificação e consumo de recursos.]{#dns-setup-recursion-abuse .correct explanation="Os controles de acesso reduzem o uso do resolvedor como infraestrutura pública de ataque."}
:::

## Validando a configuração e os dados das zonas

Use as ferramentas da implementação para verificar a sintaxe e as zonas antes do reload. Para o BIND, alguns exemplos comuns são:

```bash
$ named-checkconf
$ named-checkzone example.com /etc/bind/zones/db.example.com
```

Execute com as permissões e os caminhos apropriados ao host. O sucesso do analisador não comprova a delegação, a propagação do serial, a cadeia DNSSEC, a acessibilidade pelo firewall nem a correção das respostas; portanto, prossiga com consultas controladas.

:::single-choice{#dns-setup-zone-validation-limit} O que uma verificação bem-sucedida da sintaxe da zona não consegue comprovar?

::option[Que a delegação e as respostas autoritativas de ponta a ponta funcionam.]{#dns-setup-not-end-to-end .correct explanation="Os dados da zona pai, a ativação do serviço, a política de rede e o carregamento em tempo de execução continuam separados."}
::option[Que o texto da zona pode ser analisado pela ferramenta de verificação.]{#dns-setup-parser-proves explanation="Essa é a evidência direta fornecida pela verificação."}
::option[Que o arquivo possui um campo de proprietário do registro.]{#dns-setup-record-owner explanation="A análise de registros válidos já verifica aspectos estruturais."}
:::

## Aplicando e testando com segurança

Preserve a configuração atual e o acesso de recuperação, valide e então faça reload em vez de restart, quando houver suporte. Consulte cada servidor autoritativo diretamente, com a recursão desabilitada, e compare o serial SOA, o conjunto NS, registros positivos, nomes inexistentes e o comportamento tanto por UDP quanto por TCP:

```bash
$ dig @192.0.2.53 example.com SOA +norecurse
$ dig @192.0.2.53 missing.example.com A +norecurse
$ dig @192.0.2.53 example.com SOA +norecurse +tcp
```

Para a recursão, teste redes de clientes permitidas e negadas, validação DNSSEC, comportamento do cache e falhas das dependências superiores.

:::single-choice{#dns-setup-norecurse-test} Por que consultar um servidor autoritativo com `+norecurse`?

::option[Para testar respostas autoritativas sem solicitar recursão.]{#dns-setup-authority-only .correct explanation="Isso separa o serviço de zona de qualquer comportamento recursivo."}
::option[Para remover todos os registros da zona.]{#dns-setup-remove-records explanation="Uma consulta não edita os dados autoritativos."}
::option[Para forçar todas as respostas a usar HTTP.]{#dns-setup-force-http explanation="A opção controla o sinalizador de recursão desejada do DNS."}
:::

## Operando o serviço

Monitore falhas de consultas, latência, comportamento do cache, uso de recursos, transferências de zonas, consistência do serial, expiração do DNSSEC e integridade da delegação. Faça backup seguro da configuração de origem e do material de assinatura, mas verifique se uma nova instância consegue carregar as zonas e servir respostas corretas. Aplique correções às versões com suporte e limite as interfaces de controle, as atualizações dinâmicas e o acesso a transferências.

:::single-choice{#dns-setup-redundancy-verification} O que os testes de redundância de DNS autoritativo devem incluir?

::option[Consultar cada servidor e testar a operação quando outro estiver indisponível.]{#dns-setup-test-each-server .correct explanation="Listar vários registros NS não comprova que cada serviço independente está acessível e atualizado."}
::option[Verificar apenas se todos os servidores possuem nomes de host semelhantes.]{#dns-setup-hostname-similarity explanation="Os nomes não comprovam a sincronização dos dados nem a disponibilidade."}
::option[Usar um processo e um disco compartilhados para todos os servidores anunciados.]{#dns-setup-shared-failure explanation="Um domínio de falha compartilhado enfraquece a redundância."}
:::

## Resumo

Agora você pode projetar uma implantação de DNS em torno de funções explícitas de autoridade ou recursão.

1. Escolha o software somente depois de definir a função necessária.
2. Restrinja a recursão e as interfaces administrativas.
3. Valide a configuração e as zonas antes do reload.
4. Teste diretamente autoridade, negação, transporte e políticas de clientes.
5. Monitore redundância, DNSSEC, consistência dos dados e recuperação.
