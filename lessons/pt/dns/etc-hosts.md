---
lesson_id: "etc-hosts"
course_id: "dns"
lang: "pt"
order_index: 4
title: "/etc/hosts"
description: "Aprenda como os mapeamentos do arquivo hosts local participam da resolução de nomes no Linux e como testá-los com segurança."
meta_title: "/etc/hosts - DNS"
meta_description: "Explore a finalidade do arquivo /etc/hosts no Linux. Aprenda como ele mapeia nomes de host para endereços IP, sua função na resolução DNS local e como configurá-lo em sistemas como o Debian. Um guia para a configuração do etc hosts no Linux."
meta_keywords: "/etc/hosts, etc hosts linux, hosts debian, etc host linux, etc hosts, redes Linux, mapeamento de nome de host, resolução DNS"
---

`/etc/hosts` fornece entradas estáticas de endereço e nome para a pilha local de serviços de nomes do sistema. Ele é útil para nomes de loopback, dependências de inicialização e testes de escopo restrito, mas não publica registros para outros hosts nem atualiza o DNS.

## Lendo o arquivo

Uma linha começa com um endereço IPv4 ou IPv6, seguido por um ou mais nomes:

```text
127.0.0.1       localhost
192.0.2.25      app-test.example.net app-test
2001:db8::25    app-test-v6.example.net app-test-v6
```

Comentários começam com `#`. Por convenção, algumas ferramentas tratam o primeiro nome como canônico e os posteriores como aliases, mas o comportamento das aplicações e as APIs dos resolvedores variam. Evite entradas duplicadas ou conflitantes para o mesmo nome.

:::single-choice{#hosts-file-entry-order} O que aparece primeiro em uma linha normal de mapeamento de `/etc/hosts`?

::option[Um endereço IP.]{#hosts-file-address-first .correct explanation="Um ou mais nomes seguem o endereço na mesma linha."}
::option[Um TTL de registro DNS.]{#hosts-file-ttl-first explanation="Entradas do arquivo hosts não usam campos TTL do DNS."}
::option[Um número de porta de transporte.]{#hosts-file-port-first explanation="O arquivo mapeia nomes e endereços, não portas de aplicações."}
:::

## Ordem do resolvedor

A configuração do Name Service Switch, normalmente em `/etc/nsswitch.conf`, determina como as funções do resolvedor do sistema combinam `files`, DNS, sistemas multicast e outras fontes. Uma linha comum é:

```text
hosts: files dns
```

Não presuma que os arquivos sempre vêm primeiro sem inspecionar a política. As aplicações também podem usar suas próprias bibliotecas DNS, caches, proxies ou resolvedores criptografados e talvez não sigam o caminho do sistema.

:::single-choice{#hosts-file-nss-order} O que determina se `/etc/hosts` é consultado antes do DNS pelo resolvedor do sistema?

::option[A ordem alfabética dos nomes dos arquivos em `/etc`.]{#hosts-file-alphabetical explanation="A ordem da listagem do sistema de arquivos não define a política dos serviços de nomes."}
::option[A ordem das fontes na política do Name Service Switch.]{#hosts-file-nss-policy .correct explanation="A linha do banco de dados `hosts:` controla a ordem normal das fontes do resolvedor da libc."}
::option[O tamanho da janela TCP do destino.]{#hosts-file-tcp-window explanation="O controle de fluxo do transporte não tem relação com a consulta local de nomes."}
:::

## Testando pelo resolvedor do sistema

Use `getent` para exercitar o caminho configurado dos serviços de nomes do sistema:

```bash
$ getent ahosts app-test.example.net
```

`dig` consulta o DNS diretamente e normalmente não informa os mapeamentos de `/etc/hosts`. Essa diferença é útil: se `getent` funcionar e `dig` não, isso pode indicar uma fonte local ou uma diferença na política do resolvedor.

:::single-choice{#hosts-file-getent-versus-dig} Qual ferramenta é melhor para verificar se a resolução normal do sistema enxerga uma entrada do arquivo hosts?

::option[`dig`, porque ele sempre lê `/etc/hosts` primeiro.]{#hosts-file-dig-first explanation="Dig envia consultas DNS e ignora o caminho de consulta do arquivo hosts."}
::option[`getent ahosts`, porque ele usa as fontes configuradas dos serviços de nomes.]{#hosts-file-getent .correct explanation="Ele reflete o caminho do resolvedor usado por muitas aplicações nativas."}
::option[`ip route flush`, porque ele reconstrói todos os nomes.]{#hosts-file-flush-route explanation="Limpar as rotas é destrutivo e não tem relação com a consulta do arquivo hosts."}
:::

## Editando com segurança

Preserve as entradas necessárias de localhost e identidade do host, valide o endereço pretendido e faça uma alteração recuperável com ferramentas de edição privilegiadas. Evite substituir um domínio público real em um teste casual; isso pode redirecionar credenciais ou tráfego de aplicações inesperadamente. Use um nome dedicado de teste e remova a entrada depois do experimento.

Após a edição, teste a aplicação exata, pois ela pode manter um cache ou usar outro resolvedor. Documente substituições persistentes para que elas não permaneçam silenciosamente além de sua finalidade.

:::single-choice{#hosts-file-test-name} Por que usar um nome dedicado de teste em vez de substituir o nome de um serviço público?

::option[Nomes públicos não podem conter pontos.]{#hosts-file-public-no-dots explanation="Nomes de domínio normalmente contêm vários rótulos separados por pontos."}
::option[Nomes dedicados criam automaticamente zonas DNS autoritativas.]{#hosts-file-auto-zone explanation="Uma entrada do arquivo hosts permanece local e não publica uma zona."}
::option[Isso reduz o risco de redirecionar tráfego ou credenciais reais.]{#hosts-file-reduce-redirection .correct explanation="Uma substituição local pode afetar qualquer cliente do resolvedor do sistema que use esse nome público."}
:::

## Configuração do servidor resolvedor

`/etc/resolv.conf` tradicionalmente lista as configurações do resolvedor DNS, mas muitas vezes é gerado pelo NetworkManager, systemd-resolved, DHCP ou outro gerenciador. Inspecione os links simbólicos e os comentários do arquivo e, depois, altere a fonte de configuração responsável em vez de editar uma saída gerada que será sobrescrita.

:::single-choice{#hosts-file-resolv-owner} O que você deve fazer antes de editar `/etc/resolv.conf`?

::option[Excluir `/etc/hosts` e todas as rotas de rede.]{#hosts-file-delete-state explanation="Essas alterações destrutivas não têm relação com o objetivo e podem remover a conectividade."}
::option[Presumir que todas as distribuições armazenam as configurações permanentes diretamente nele.]{#hosts-file-assume-direct explanation="Muitos sistemas geram o arquivo dinamicamente ou o vinculam a um stub gerenciado."}
::option[Identificar se outro serviço o gera e controla.]{#hosts-file-identify-resolver-owner .correct explanation="Alterações persistentes nos servidores DNS pertencem à configuração do gerenciador ativo."}
:::

## Resumo

Agora você pode usar `/etc/hosts` como uma entrada local controlada do resolvedor.

1. Escreva mapeamentos começando pelo endereço, com nomes e aliases deliberados.
2. Inspecione a ordem do Name Service Switch em vez de presumi-la.
3. Teste a resolução do sistema com `getent` e o DNS separadamente com `dig`.
4. Use nomes temporários dedicados e verifique a aplicação real.
5. Altere os servidores resolvedores por meio do responsável pela configuração.
