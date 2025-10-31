---
index: 6
lang: "pt"
title: "Objetivos do Systemd"
meta_title: "Objetivos do Systemd - Init"
meta_description: "Explore os objetivos do systemd e aprenda a gerenciar serviços Linux usando comandos essenciais do systemctl. Este guia abrange o básico dos arquivos de unidade systemd, como iniciar, parar e habilitar serviços, e visualizar seu status."
meta_keywords: "systemd, systemctl, serviços Linux, arquivos de unidade, objetivos systemd, gerenciamento de serviços, unidades systemd, iniciante, tutorial, guia, comandos Linux"
---

## Lesson Content

Esta lição fornece uma visão geral fundamental dos arquivos de unidade systemd e como gerenciá-los com `systemctl`, a principal ferramenta para controlar o sistema init. Abordaremos a estrutura básica de um arquivo de unidade e os comandos essenciais para gerenciar serviços Linux.

### Entendendo um Arquivo de Unidade Systemd

A unit file (arquivo de unidade) do systemd é um arquivo de texto simples que descreve um serviço, um ponto de montagem, um dispositivo ou outro recurso que o systemd pode gerenciar. Aqui está um exemplo básico de um arquivo de unidade de serviço chamado `foobar.service`:

```
[Unit]
Description=Meu Serviço Foobar
After=network.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

Este arquivo de serviço simples é dividido em seções:

- **[Unit]**: Esta seção contém metadados e informações de dependência. A diretiva `Description` fornece um nome legível para a unidade. Diretivas como `After` e `Before` controlam a ordem de inicialização, garantindo que esta unidade inicie após a rede estar disponível.
- **[Service]**: Esta seção define como gerenciar o serviço. A diretiva `ExecStart` é crucial, pois especifica o comando a ser executado para iniciar o serviço. Outras diretivas como `ExecStop` e `ExecReload` podem definir como parar ou recarregar o serviço.
- **[Install]**: Esta seção define o comportamento da unidade quando ela é habilitada ou desabilitada com `systemctl`. A diretiva `WantedBy` informa ao systemd para iniciar este serviço como parte de um alvo específico, como o `multi-user.target` para uma inicialização padrão não gráfica.

Este é apenas um vislumbre dos arquivos de unidade systemd. Para configurações mais avançadas, é altamente recomendada uma leitura adicional sobre o tópico.

### Comandos Essenciais do Systemctl

Agora, vamos explorar os comandos essenciais do `systemctl` que você usará para interagir com as unidades systemd e gerenciar serviços Linux.

### Listando Unidades Systemd

Para ver todas as unidades ativas que o systemd está gerenciando atualmente, use o comando `list-units`.

```bash
systemctl list-units
```

### Verificando o Status de uma Unidade

Para visualizar o status detalhado de uma unidade específica, incluindo se ela está ativa, habilitada e suas entradas de log mais recentes, use o comando `status`.

```bash
systemctl status networking.service
```

### Gerenciando Estados de Serviço

Você pode controlar o estado de execução de um serviço usando `start`, `stop` e `restart`.

Para iniciar um serviço imediatamente:

```bash
sudo systemctl start networking.service
```

Para parar um serviço em execução:

```bash
sudo systemctl stop networking.service
```

Para parar e depois iniciar o serviço novamente:

```bash
sudo systemctl restart networking.service
```

### Habilitando e Desabilitando Serviços

Habilitar um serviço cria um link simbólico que o conecta ao processo de inicialização, garantindo que ele inicie automaticamente. Desabilitá-lo remove esse link.

Para habilitar um serviço para iniciar na inicialização:

```bash
sudo systemctl enable networking.service
```

Para desabilitar um serviço de iniciar na inicialização:

```bash
sudo systemctl disable networking.service
```

Estes comandos são os blocos de construção para o gerenciamento de serviços em sistemas Linux modernos. Dominá-los é um passo fundamental em sua jornada Linux.

## Exercise

A prática é fundamental para dominar novas habilidades. Este laboratório prático ajudará a reforçar sua compreensão do gerenciamento de processos, que são frequentemente controlados por serviços systemd:

1.  **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro plano e em segundo plano, inspecionando-os com `ps`, monitorando recursos com `top`, ajustando a prioridade com `renice` e terminando-os com `kill`. Este laboratório lhe dará experiência prática com os efeitos em tempo de execução do gerenciamento de unidades systemd.

Este laboratório o ajudará a aplicar esses conceitos em um cenário do mundo real e a construir confiança no gerenciamento de processos no Linux.

## Quiz Question

What is the command to start a service named peanut.service? Please answer in English. The answer is case-sensitive.

## Quiz Answer

sudo systemctl start peanut.service
