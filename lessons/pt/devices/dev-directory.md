---
lesson_id: "dev-directory"
course_id: "devices"
lang: "pt"
order_index: 1
title: "Diretório /dev"
description: "Aprenda como o Linux expõe interfaces de dispositivos e pseudodispositivos por meio de nós em `/dev`."
meta_title: "Diretório /dev - Dispositivos"
meta_description: "Conheça a finalidade do diretório /dev no Linux. Este guia explica o que é a pasta dev, como explorá-la com `ls /dev` e a função dos arquivos de dispositivos no hardware do sistema."
meta_keywords: "dev no Linux, diretório /dev no Linux, pasta dev Linux, ls /dev, comando dev no Linux, arquivos de dispositivos, nós de dispositivos, dispositivos Linux"
---

O Linux expõe muitas interfaces de dispositivos do kernel por meio de objetos especiais do sistema de arquivos chamados nós de dispositivos. Eles normalmente aparecem em `/dev`, junto com links simbólicos úteis e endpoints de comunicação. Abrir um nó de dispositivo conecta uma aplicação a um driver do kernel, em vez de acessar bytes armazenados em um arquivo comum.

## Exploração de `/dev`

Liste o diretório sem desreferenciar nem ler dispositivos:

```bash
$ ls -l /dev
```

As entradas podem representar armazenamento físico, terminais, interfaces de entrada, dispositivos lógicos ou pseudodispositivos fornecidos pelo kernel. Nem todo componente de hardware precisa de seu próprio nó visível ao usuário, e um dispositivo pode ser representado por vários links ou interfaces.

O primeiro caractere de uma listagem longa identifica o tipo de objeto do sistema de arquivos. Os nós de dispositivos de caractere e de bloco aparecem como `c` e `b`; lições posteriores examinam esses tipos e seus números maiores e menores.

:::single-choice{#dev-directory-device-node-purpose}
O que acontece quando um programa abre um nó de dispositivo em `/dev`?

::option[Ele sempre lê um arquivo comum do disco que contém uma cópia do hardware.]{#dev-directory-ordinary-copy explanation="Um nó de dispositivo é um objeto especial e não armazena uma cópia dos dados do dispositivo como um arquivo comum."}
::option[Ele acessa uma interface implementada por um driver do kernel.]{#dev-directory-kernel-interface .correct explanation="As operações no nó de dispositivo são encaminhadas, por sua identidade, ao comportamento de um driver do kernel."}
::option[Ele recompila o código-fonte do driver desse dispositivo.]{#dev-directory-recompile-driver explanation="Abrir uma interface não invoca um compilador nem recompila módulos do kernel."}
:::

## Pseudodispositivos

Alguns nós fornecem serviços do kernel sem corresponder a um hardware físico. `/dev/null` aceita e descarta os dados gravados:

```bash
$ command > /dev/null
```

Outros exemplos conhecidos incluem `/dev/zero`, que produz bytes zero, e `/dev/urandom`, que fornece bytes aleatórios por meio do subsistema de aleatoriedade do kernel. Cada um possui uma semântica específica; não deduza seu comportamento apenas pelo nome do arquivo.

:::single-choice{#dev-directory-null-behavior}
O que `/dev/null` faz com os dados gravados nele?

::option[Armazena os dados até a próxima reinicialização.]{#dev-directory-null-temporary-storage explanation="O dispositivo null é um destino de descarte e não atua como armazenamento temporário."}
::option[Envia os dados para todos os terminais com usuários conectados.]{#dev-directory-null-broadcast explanation="A transmissão para terminais não tem relação com o pseudodispositivo null."}
::option[Descarta os dados.]{#dev-directory-null-discards .correct explanation="O dispositivo null aceita gravações sem preservar seu conteúdo."}
:::

## Gerenciamento Dinâmico de Dispositivos

Em sistemas Linux modernos, o `devtmpfs`, apoiado pelo kernel, pode preencher os nós básicos de dispositivos à medida que eles aparecem. Um gerenciador de dispositivos no espaço do usuário, como o `udev`, processa eventos, aplica permissões e propriedades e cria links simbólicos úteis ou nomes definidos por políticas. As responsabilidades exatas variam conforme o sistema.

Links estáveis, como as entradas em `/dev/disk/by-id/` ou `/dev/disk/by-uuid/`, podem ser mais seguros em configurações do que nomes baseados na ordem de detecção, como `/dev/sda`, que podem mudar quando a topologia do hardware ou a ordem de descoberta é alterada.

:::single-choice{#dev-directory-persistent-link}
Por que um administrador pode preferir `/dev/disk/by-id/...` a `/dev/sda` em uma configuração?

::option[O link baseado em identificador depende menos da ordem de descoberta dos dispositivos.]{#dev-directory-stable-identifier .correct explanation="Os links persistentes são derivados das propriedades do dispositivo, não de uma letra atribuída pela ordem de enumeração."}
::option[O link faz automaticamente um backup de todos os blocos do dispositivo.]{#dev-directory-link-backup explanation="Um link simbólico nomeia o mesmo dispositivo e não cria dados de backup."}
::option[O link ignora todas as permissões do dispositivo de destino.]{#dev-directory-link-permissions explanation="Abrir por um link simbólico ainda alcança o dispositivo de destino e seus controles de acesso."}
:::

## Interação Segura

Ferramentas comuns podem abrir nós de dispositivos, mas isso não torna seguras leituras e gravações arbitrárias. A leitura pode expor entradas ou dados confidenciais; a gravação em um disco, terminal ou interface de firmware pode corromper dados ou atrapalhar usuários. É por isso que permissões de nós de dispositivos, grupos, ACLs, capacidades e a intermediação por serviços restringem o acesso.

Use primeiro ferramentas de descoberta somente para leitura, confirme o nó exato e a identidade do dispositivo e siga a documentação específica dele. Nunca faça experiências redirecionando dados para uma entrada desconhecida de `/dev` em um sistema importante.

:::single-choice{#dev-directory-direct-write-risk}
Por que você deve evitar gravar dados arbitrários em um nó de dispositivo desconhecido?

::option[Todo nó de dispositivo certamente é um arquivo de texto inofensivo.]{#dev-directory-harmless-text explanation="Os nós de dispositivos não são, justamente, arquivos de texto comuns."}
::option[A operação pode afetar diretamente o hardware, o armazenamento ou outra interface do kernel.]{#dev-directory-write-impact .correct explanation="As gravações em dispositivos invocam operações definidas pelo driver e podem ter efeitos destrutivos ou prejudiciais."}
::option[O Linux converte toda gravação em dispositivo em uma listagem somente para leitura.]{#dev-directory-write-listing explanation="O driver decide a semântica da gravação; o kernel não converte universalmente gravações em listagens."}
:::

Use o laboratório [Exploração de Dispositivos de Hardware no Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) para realizar uma inspeção somente para leitura em um ambiente controlado.

## Resumo

Agora você sabe descrever `/dev` como um conjunto de interfaces ativas voltadas ao kernel.

1. Diferencie nós de dispositivos de arquivos comuns.
2. Reconheça pseudodispositivos como `/dev/null`.
3. Relacione nós dinâmicos e links persistentes ao gerenciamento de dispositivos.
4. Trate o acesso direto a dispositivos como específico da interface e potencialmente destrutivo.
