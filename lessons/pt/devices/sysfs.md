---
lesson_id: "sysfs"
course_id: "devices"
lang: "pt"
order_index: 4
title: "sysfs"
description: "Aprenda como o sysfs expõe o modelo ativo de dispositivos, drivers, barramentos e classes do kernel Linux em `/sys`."
meta_title: "sysfs - Dispositivos"
meta_description: "Conheça o sysfs e sua função no sistema Linux. Este guia explica o diretório virtual /sys para informações de dispositivos e o compara com /dev."
meta_keywords: "sysfs, o que é sysfs, /sys, Linux /sys, sistema sys Linux, sistema de arquivos virtual, dispositivos Linux, /dev"
---

`sysfs` é um sistema de arquivos virtual normalmente montado em `/sys`. Ele representa objetos do kernel e suas relações por meio de diretórios, links simbólicos e pequenos arquivos de atributos. Ferramentas de descoberta e gerenciadores de dispositivos o utilizam para compreender o modelo de dispositivos atual do kernel.

## Navegação pelo Modelo de Dispositivos

Algumas visualizações importantes no nível superior são:

- `/sys/devices/`: a hierarquia física e lógica dos dispositivos
- `/sys/class/`: dispositivos agrupados por classe funcional, como bloco ou rede
- `/sys/bus/`: barramentos, seus dispositivos e drivers
- `/sys/block/`: uma visualização conveniente dos dispositivos de bloco
- `/sys/dev/`: links indexados pelos números maiores e menores de dispositivos de caractere ou bloco

Muitas entradas fora de `/sys/devices` são links simbólicos para a hierarquia canônica. Resolva um link com `readlink -f` quando precisar do caminho pai real:

```bash
$ readlink -f /sys/class/block/sda
```

O nome do exemplo pode não existir em sistemas que usam outras interfaces de armazenamento.

:::single-choice{#sysfs-canonical-device-tree} Qual subárvore do sysfs contém a hierarquia principal de dispositivos do kernel?

::option[`/sys/passwords/`]{#sysfs-passwords-tree explanation="O sysfs não é um repositório de segredos de autenticação dos usuários."}
::option[`/sys/devices/`]{#sysfs-devices-tree .correct explanation="A subárvore devices representa a topologia pai-filho dos dispositivos; as visualizações de classes e barramentos apontam para ela."}
::option[`/sys/packages/`]{#sysfs-packages-tree explanation="O estado dos pacotes instalados é mantido pelas ferramentas de pacotes da distribuição, não por esse caminho do sysfs."}
:::

## Leitura de Atributos

Os arquivos de atributos expõem valores ou controles individuais. Para um dispositivo de bloco, alguns exemplos podem ser:

```bash
$ cat /sys/class/block/sda/dev
8:0
$ cat /sys/class/block/sda/ro
0
$ cat /sys/class/block/sda/size
1953525168
```

`dev` informa os números maior e menor do dispositivo. `ro` informa o indicador de somente leitura do dispositivo de bloco. Para dispositivos de bloco do Linux, `size` é convencionalmente expresso em setores de 512 bytes, independentemente do tamanho de setor físico do dispositivo. Consulte sempre a documentação da ABI do kernel para conhecer as unidades e o significado de um atributo específico.

:::single-choice{#sysfs-dev-attribute} O que o atributo `dev` de um dispositivo de bloco normalmente contém?

::option[Todos os arquivos atualmente armazenados no dispositivo.]{#sysfs-file-list explanation="Uma árvore de diretórios do sistema de arquivos não fica incorporada nesse pequeno atributo do dispositivo."}
::option[O nome do pacote que instalou o hardware.]{#sysfs-package-name explanation="O hardware não é instalado como um pacote identificado pelo atributo `dev`."}
::option[Seus números maior e menor de dispositivo.]{#sysfs-major-minor .correct explanation="O atributo conecta o objeto do sysfs à identidade correspondente do dispositivo de bloco."}
:::

## Relação entre `/sys` e `/dev`

`/dev` contém os nós que as aplicações abrem para a E/S dos dispositivos. `/sys` expõe relações entre objetos, propriedades, estados e controles selecionados. Um nó de bloco como `/dev/sda` pode ser associado a `/sys/dev/block/8:0`, que resolve para o objeto relevante do sysfs.

As duas interfaces se complementam. Nenhuma contém, sozinha, um inventário completo de todos os dados do hardware, e um dispositivo pode desaparecer enquanto é inspecionado.

:::single-choice{#sysfs-versus-dev} Qual afirmação diferencia corretamente `/sys` de `/dev`?

::option[`/sys` armazena documentos dos usuários; `/dev` armazena pacotes.]{#sysfs-dev-user-files explanation="Nenhum desses diretórios possui essas funções comuns de armazenamento de dados."}
::option[`/sys` expõe atributos de objetos do kernel; `/dev` fornece nós de dispositivos para E/S.]{#sysfs-dev-distinction .correct explanation="O sysfs modela objetos e controles, enquanto os nós de dispositivos encaminham operações para drivers de caractere ou de bloco."}
::option[Os dois são listas estáticas criadas uma única vez durante a instalação.]{#sysfs-dev-static explanation="O estado visível muda à medida que dispositivos e objetos do kernel aparecem ou desaparecem."}
:::

## Gravação Segura em Atributos

Alguns atributos do sysfs permitem escrita e podem alterar o estado de energia, a associação de drivers, o comportamento das filas, a autorização de dispositivos, LEDs ou outros controles ativos. Uma gravação de texto bem-sucedida pode causar efeitos imediatos no hardware ou nos serviços; ela não equivale a editar um arquivo de configuração persistente.

Leia a ABI documentada e o valor atual, identifique como tornar a configuração persistente e teste somente em um sistema autorizado. Nunca edite permissões recursivamente nem grave valores deduzidos em toda a árvore `/sys`.

:::single-choice{#sysfs-write-risk} Por que gravar em um atributo do sysfs pode ser operacionalmente significativo?

::option[Toda gravação cria uma cópia de backup comum no disco.]{#sysfs-backup-copy explanation="O sysfs é virtual e não oferece backups automáticos das alterações de controle."}
::option[O sysfs ignora todas as gravações, mesmo quando um atributo permite escrita.]{#sysfs-ignore-writes explanation="Os atributos graváveis existem justamente para aceitar valores de controle compatíveis."}
::option[A gravação pode acionar um controle ativo do kernel ou do driver.]{#sysfs-live-control .correct explanation="Os atributos graváveis são interfaces ativas e podem alterar imediatamente o comportamento do dispositivo."}
:::

Use o laboratório [Exploração de Dispositivos de Hardware no Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) para navegar pelo sysfs somente para leitura e relacioná-lo aos nós de dispositivos.

## Resumo

Agora você sabe usar o sysfs como uma visualização estruturada dos objetos ativos do kernel.

1. Navegue pelas visualizações de dispositivos, classes, barramentos, blocos e números de dispositivos.
2. Leia um atributo documentado por vez, usando as unidades corretas.
3. Relacione objetos do sysfs aos nós de `/dev`.
4. Trate atributos graváveis como interfaces de controle ativas.
