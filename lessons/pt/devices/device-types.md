---
lesson_id: "device-types"
course_id: "devices"
lang: "pt"
order_index: 2
title: "Tipos de Dispositivos"
description: "Aprenda a diferenciar nós de dispositivos de caractere e bloco de pipes, sockets e objetos comuns do sistema de arquivos."
meta_title: "Tipos de Dispositivos - Dispositivos"
meta_description: "Conheça os diferentes tipos de dispositivos Linux, incluindo dispositivos de caractere e bloco, pipes e sockets. Aprenda a identificar um arquivo de dispositivo com `ls -l /dev` e entenda os números maiores e menores."
meta_keywords: "dispositivos Linux, tipos de dispositivos Linux, arquivo de dispositivo, dispositivo de caractere, dispositivo de bloco, números maiores menores, diretório /dev"
---

O primeiro caractere de um modo exibido por `ls -l` identifica o tipo do objeto no sistema de arquivos. Em `/dev`, os arquivos especiais de caractere e de bloco são nós de dispositivos. Nós de pipes e sockets de domínio Unix também podem aparecer ali, mas são objetos de comunicação entre processos, não nós de dispositivos de hardware.

```text
$ ls -l /dev/null /dev/sda /run/systemd/journal/dev-log /tmp/example-fifo
crw-rw-rw- 1 root root 1, 3 ... /dev/null
brw-rw---- 1 root disk 8, 0 ... /dev/sda
srw-rw-rw- 1 root root      ... /run/systemd/journal/dev-log
prw------- 1 user user      ... /tmp/example-fifo
```

As entradas e permissões variam conforme o sistema; o exemplo ilustra apenas os caracteres de tipo.

## Nós de Dispositivos de Caractere

Um `c` identifica um dispositivo de caractere. Ele normalmente expõe uma interface orientada a fluxo ou específica do dispositivo, em vez de blocos de armazenamento de tamanho fixo endereçáveis. Alguns exemplos são os terminais e pseudodispositivos como `/dev/null`.

“Caractere” não exige que cada chamada de sistema transfira exatamente um caractere. As aplicações podem ler ou gravar buffers, enquanto o driver define o bloqueio, o enquadramento e o comportamento de controle.

:::single-choice{#device-types-character-marker} Qual primeiro caractere de modo identifica um nó de dispositivo de caractere?

::option[`b`]{#device-types-marker-block explanation="O marcador `b` identifica um nó de dispositivo de bloco."}
::option[`p`]{#device-types-marker-pipe explanation="O marcador `p` identifica um FIFO, ou pipe nomeado."}
::option[`c`]{#device-types-marker-character .correct explanation="Os arquivos especiais de caractere aparecem com `c` no início do modo de uma listagem longa."}
:::

## Nós de Dispositivos de Bloco

Um `b` identifica um dispositivo de bloco. Os dispositivos de bloco fornecem armazenamento endereçável em blocos por meio da camada de blocos do kernel e podem oferecer suporte a operações como E/S com buffer, particionamento e sistemas de arquivos. Discos, partições e volumes lógicos normalmente possuem nós de bloco.

Um nó de bloco não é um sistema de arquivos montado. Ele representa um dispositivo de armazenamento ou uma região lógica; um sistema de arquivos pode ser criado nele e montado separadamente. Gravar dados brutos no nó de bloco errado pode destruir tabelas de partições, sistemas de arquivos ou dados dos usuários.

:::single-choice{#device-types-block-marker} O que o primeiro caractere de modo `b` indica?

::option[Uma tarefa do shell em segundo plano.]{#device-types-background-job explanation="O estado das tarefas do shell não é codificado como um caractere de tipo do sistema de arquivos."}
::option[Uma interface de dispositivo de bloco.]{#device-types-block-device .correct explanation="Arquivos especiais de bloco expõem armazenamento endereçável por meio do subsistema de blocos do kernel."}
::option[Um link simbólico quebrado.]{#device-types-broken-link explanation="Links simbólicos usam `l`, independentemente de seu destino existir no momento."}
:::

## FIFOs e Nós de Sockets

Um `p` identifica um FIFO, também chamado de pipe nomeado. Ele fornece um fluxo de bytes nomeado por meio do qual os processos podem se comunicar. Os dados não ficam armazenados de forma persistente no nó FIFO depois de serem consumidos.

Um `s` identifica um nó de socket de domínio Unix. Ele nomeia um endpoint de socket local e pode oferecer comunicação orientada a conexões ou por datagramas, passagem de descritores e recursos de credenciais dos pares. Sockets de rede que usam endereços da Internet não necessariamente possuem nós no sistema de arquivos.

Nem um FIFO nem um nó de socket Unix usa números maiores e menores de dispositivos para selecionar um driver de hardware.

:::single-choice{#device-types-pipe-socket-distinction} Qual afirmação diferencia corretamente esses tipos de objetos IPC?

::option[`p` indica uma partição de disco, enquanto `s` indica armazenamento de estado sólido.]{#device-types-storage-letters explanation="As partições normalmente são dispositivos de bloco, e as letras não codificam a tecnologia de armazenamento."}
::option[`p` indica um FIFO, enquanto `s` indica um nó de socket de domínio Unix.]{#device-types-p-and-s .correct explanation="Esses são tipos distintos de objetos do sistema de arquivos usados para comunicação local entre processos."}
::option[Os dois tipos identificam drivers de bloco do kernel por meio de números maiores.]{#device-types-ipc-major explanation="Os nós FIFO e de socket não são nós de dispositivos de caractere nem de bloco."}
:::

## Números Maiores e Menores de Dispositivos

Os nós de dispositivos de caractere e bloco armazenam um número de dispositivo dividido em componentes maior e menor. Em uma listagem longa, eles substituem a coluna comum de tamanho do arquivo:

```text
brw-rw---- 1 root disk 8, 0 ... /dev/sda
```

O par informa ao kernel qual interface e instância de dispositivo registradas o nó endereça. Um número maior está associado a um driver ou classe de dispositivos, enquanto o driver interpreta o número menor. Não codifique suposições como “o número menor zero sempre significa a primeira unidade”; os mapeamentos dependem do subsistema e das interfaces do kernel.

Exiba explicitamente o tipo e os números do dispositivo com:

```bash
$ stat -c 'type=%F major=%t minor=%T path=%n' /dev/null
```

Os valores `%t` e `%T` são mostrados em hexadecimal pelo `stat` do GNU.

:::single-choice{#device-types-major-minor-scope} Quais objetos usam números maiores e menores para identificar uma interface de dispositivo do kernel?

::option[Todos os arquivos comuns e diretórios.]{#device-types-all-files explanation="Arquivos comuns usam tamanho e metadados do sistema de arquivos, não um par maior/menor de nó de dispositivo."}
::option[Somente links simbólicos cujos destinos não existem.]{#device-types-broken-symlinks explanation="Links simbólicos armazenam o texto de um caminho e não se tornam nós de dispositivos quando o destino está ausente."}
::option[Nós de dispositivos de caractere e de bloco.]{#device-types-device-number-nodes .correct explanation="Os metadados especiais de seus inodes contêm o número do dispositivo encaminhado para uma interface de driver."}
:::

## Resumo

Agora você sabe interpretar tipos especiais do sistema de arquivos sem tratar todos eles como dispositivos de hardware.

1. Leia `c` como nó de dispositivo de caractere e `b` como nó de dispositivo de bloco.
2. Leia `p` como FIFO e `s` como nó de socket de domínio Unix.
3. Associe números maiores e menores somente a nós de dispositivos.
4. Trate o acesso bruto a dispositivos de bloco como potencialmente destrutivo.
