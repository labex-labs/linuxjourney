---
index: 5
lang: "pt"
title: "Visão Geral do Systemd"
meta_title: "Visão Geral do Systemd - Init"
meta_description: "Aprenda os fundamentos do sistema init systemd. Este guia aborda como o systemd (ou system d) usa unidades e alvos para gerenciar o processo de boot e os serviços do sistema Linux. Entenda os conceitos centrais do padrão moderno para inicialização Linux."
meta_keywords: "systemd, system d, sistema init, unidades systemd, alvos systemd, processo boot linux, serviços linux, gerenciamento sistema, iniciante, tutorial"
---

## Lesson Content

LESSON CONTENT:

### O que é Systemd?

Systemd é o sistema init e gerenciador de serviços padrão para a maioria das distribuições Linux modernas. Ele é responsável por inicializar o sistema na ordem correta após o kernel ser carregado. Uma maneira simples de verificar se o seu sistema o utiliza é verificar se o diretório `/usr/lib/systemd` existe. Se existir, você provavelmente está executando um sistema gerenciado por **systemd**.

### O Processo de Inicialização do Systemd

Em vez de scripts sequenciais rígidos, o **systemd** usa o conceito de "metas" (goals) para colocar seu sistema em um estado funcional. Ele identifica uma meta principal, ou `target`, e trabalha para satisfazer suas dependências. Essa abordagem permite maior flexibilidade e paralelização durante a inicialização. Um processo de boot típico gerenciado pelo **systemd** segue estas etapas:

1. O **systemd** primeiro carrega seus arquivos de configuração de diretórios como `/etc/systemd/system` e `/usr/lib/systemd/system`.
2. Em seguida, ele identifica a meta de boot padrão, que geralmente é um link simbólico chamado `default.target`.
3. Finalmente, o **systemd** resolve todas as dependências para este alvo e ativa as unidades necessárias para atingir o estado de sistema desejado.

### Entendendo os Alvos (Targets) do Systemd

Targets no **systemd** são análogos aos runlevels no sistema init SysV mais antigo. Eles representam diferentes estados em que o sistema pode estar. Targets comuns incluem:

- `poweroff.target`: Desliga o sistema.
- `rescue.target`: Inicializa em um shell de usuário único para manutenção.
- `multi-user.target`: Um ambiente multiusuário padrão com rede, mas sem interface gráfica.
- `graphical.target`: Um ambiente multiusuário completo com rede e uma interface gráfica do usuário (GUI).
- `reboot.target`: Reinicia o sistema.

A `default.target` é um link simbólico que aponta para o alvo no qual o sistema inicializará por padrão, frequentemente `graphical.target` em sistemas desktop.

### Conceito Central: Unidades do Systemd

Os objetos fundamentais que o **systemd** gerencia são chamados de "unidades". Uma unidade é um arquivo de configuração que descreve um recurso ou serviço. O poder da arquitetura do **system d** reside em sua capacidade de gerenciar vários tipos de recursos, não apenas serviços. Cada tipo de unidade é identificado por sua extensão de arquivo. Os tipos mais comuns são:

- **Unidades de Serviço (`.service`):** Gerenciam daemons ou serviços do sistema, como um servidor web ou um banco de dados.
- **Unidades de Montagem (`.mount`):** Controlam os pontos de montagem do sistema de arquivos.
- **Unidades de Alvo (`.target`):** São usadas para agrupar outras unidades, criando pontos de sincronização durante a inicialização.

Por exemplo, quando o sistema inicializa em `graphical.target`, essa unidade de alvo garante que todas as suas dependências, como `multi-user.target` e várias unidades de serviço como `network.service`, sejam iniciadas primeiro.

## Exercise

EXERCISE:
Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Trilha de Aprendizado de Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual unidade é usada para agrupar outras unidades? Por favor, responda em uma única palavra em inglês minúscula.

## Quiz Answer

target
