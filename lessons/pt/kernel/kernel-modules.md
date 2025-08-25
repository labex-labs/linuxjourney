---
index: 6
lang: "pt"
title: "Módulos do Kernel"
meta_title: "Módulos do Kernel - Kernel"
meta_description: "Aprenda sobre os módulos do kernel Linux: como carregá-los, descarregá-los e gerenciá-los. Entenda os comandos `modprobe` e `lsmod` para estender a funcionalidade do kernel. Comece sua jornada no Linux!"
meta_keywords: "módulos do kernel Linux, modprobe, lsmod, gerenciamento do kernel, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Digamos que eu tenha um carro incrível; invisto muito tempo e dinheiro nele. Adiciono um spoiler, engate, suporte para bicicletas e outras coisas aleatórias. Esses componentes não alteram a funcionalidade principal do carro, e posso removê-los e adicioná-los muito facilmente. O kernel usa o mesmo conceito com os módulos do kernel.

O kernel em si é uma peça monolítica de software. Quando queremos adicionar suporte para um novo tipo de teclado, não escrevemos esse código diretamente no código do kernel. Assim como não fundiríamos um suporte de bicicleta ao nosso carro (bem, talvez algumas pessoas fizessem isso). Módulos do kernel são pedaços de código que podem ser carregados e descarregados no kernel sob demanda. Eles nos permitem estender a funcionalidade do kernel sem realmente adicionar ao código principal do kernel. Também podemos adicionar módulos e não precisar reiniciar o sistema (na maioria dos casos).

### Ver uma lista de módulos atualmente carregados

```bash
lsmod
```

### Carregar um módulo

```bash
sudo modprobe bluetooth
```

`modprobe` carrega o módulo de `/lib/modules/(kernel version)/kernel/drivers`. Os módulos do kernel também podem ter dependências; `modprobe` carrega as dependências do nosso módulo se elas ainda não estiverem carregadas.

### Remover um módulo

```bash
sudo modprobe -r bluetooth
```

### Carregar na inicialização

Você também pode carregar módulos durante a inicialização do sistema, em vez de carregá-los temporariamente com `modprobe` (que serão descarregados quando você reiniciar). Basta modificar o diretório `/etc/modprobe.d` e adicionar um arquivo de configuração nele, assim:

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

Um exemplo um tanto extravagante, mas se você tivesse um módulo chamado `peanut_butter` e quisesse adicionar um parâmetro de kernel para `type=almond`, você pode fazer com que ele carregue na inicialização usando este arquivo de configuração. Além disso, observe que os módulos do kernel têm seus próprios parâmetros de kernel, então você vai querer ler sobre o módulo especificamente para saber mais.

### Não carregar na inicialização

Você também pode garantir que um módulo não seja carregado na inicialização adicionando um arquivo de configuração assim:

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão dos módulos do kernel Linux:

1. **[Gerenciar Módulos do Kernel no Linux](https://labex.io/pt/labs/comptia-manage-kernel-modules-in-linux-590865)** - Pratique listar, inspecionar, carregar e descarregar módulos do kernel, e configurá-los para carregar automaticamente na inicialização. Este laboratório o ajudará a aplicar os conceitos em um cenário real e a construir confiança no gerenciamento de módulos do kernel.

## Quiz Question

Qual comando é usado para descarregar um módulo?

## Quiz Answer

modprobe -r
