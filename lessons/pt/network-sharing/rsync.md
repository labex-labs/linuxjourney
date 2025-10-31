---
index: 2
lang: "pt"
title: "rsync"
meta_title: "rsync - Compartilhamento de Rede"
meta_description: "Descubra como usar o poderoso comando rsync no Linux para sincronização eficiente de arquivos, transferência remota de dados e backups confiáveis. Este guia abrange os principais comandos e opções do rsync."
meta_keywords: "rsync, rsync linux, sincronização de arquivos, backup de dados, sincronização remota, comando rsync, transferência de arquivos linux, tutorial rsync"
---

## Lesson Content

### O que é rsync?

Outra ferramenta essencial para copiar dados entre diferentes hosts é o `rsync`, que significa sincronização remota (remote synchronization). Embora semelhante ao `scp`, o `rsync` possui uma diferença fundamental que o torna incrivelmente eficiente. Ele usa um algoritmo de transferência delta que verifica inteligentemente o destino em busca de dados existentes e transfere apenas as partes dos arquivos que foram alteradas.

Por exemplo, se a transferência de um arquivo grande for interrompida, o `rsync` pode retomar a cópia, transferindo apenas as partes restantes do arquivo em vez de recomeçar do zero. Isso o torna uma escolha robusta para conexões de rede instáveis.

### Principais Recursos do rsync

A eficiência do `rsync` vem de suas otimizações inteligentes. Ele verifica a integridade do arquivo usando somas de verificação (checksums) para garantir que os dados copiados não sejam corrompidos durante a transferência. Esses recursos oferecem flexibilidade significativa, tornando o `rsync` uma ferramenta ideal para:

- Sincronização de diretórios (tanto remota quanto local)
- Criação de backups incrementais de dados
- Manuseio eficiente de grandes transferências de dados

### Opções Comuns do rsync

Você pode modificar o comportamento do comando `rsync` com várias opções. Algumas das mais usadas incluem:

- `-v`: Saída detalhada (verbose), mostrando quais arquivos estão sendo transferidos.
- `-r`: Recursivo, necessário para copiar diretórios inteiros.
- `-h`: Saída legível por humanos (human-readable), exibindo números em um formato mais compreensível (ex: KB, MB).
- `-z`: Comprime os dados do arquivo durante a transferência, o que é ótimo para conexões lentas.
- `-a`: Modo de arquivo (archive), um atalho conveniente que combina várias opções (`-rlptgoD`) para preservar permissões, propriedade e carimbos de data/hora.

### Exemplos de Uso do rsync

#### Sincronizar Arquivos no Mesmo Host

Você pode usar o `rsync` para sincronizar dois diretórios em sua máquina local. Isso é útil para criar backups locais.

```bash
rsync -avh /meu/diretorio/local/um/ /meu/diretorio/local/dois/
```

#### Sincronizar Arquivos de um Host Remoto para um Host Local

Para puxar arquivos de um servidor remoto para sua máquina local, especifique a origem remota primeiro.

```bash
rsync -avh usuario@hostremoto.com:/diretorio/remoto/ /diretorio/local/
```

#### Sincronizar Arquivos de um Host Local para um Host Remoto

Para enviar arquivos de sua máquina local para um servidor remoto, especifique a origem local primeiro.

```bash
rsync -avh /diretorio/local/ usuario@hostremoto.com:/diretorio/remoto/
```

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Trilha de Aprendizagem do Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual comando, conhecido por seu algoritmo de transferência delta, é particularmente útil para criar backups de dados eficientes? Por favor, responda em inglês, prestando atenção à sensibilidade de maiúsculas e minúsculas.

## Quiz Answer

rsync
