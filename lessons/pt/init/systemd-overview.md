---
index: 5
lang: "pt"
title: "Visão Geral do Systemd"
meta_title: "Visão Geral do Systemd - Init"
meta_description: "Aprenda o básico do Systemd: entenda unidades, targets e o processo de boot. Descubra como o Systemd gerencia serviços e estados do sistema no Linux. Comece sua jornada!"
meta_keywords: "Systemd, unidades Systemd, targets Systemd, processo de boot Linux, serviços Linux, iniciante, tutorial, guia"
---

## Lesson Content

Systemd é o sistema init padrão na maioria das distribuições Linux modernas. Se você tem um diretório `/usr/lib/systemd`, é muito provável que esteja usando systemd.

Systemd usa metas (goals) para colocar seu sistema em funcionamento. Basicamente, você tem um target que deseja alcançar, e este target também tem dependências que precisam ser satisfeitas. Systemd é extremamente flexível e robusto; ele não segue uma sequência estrita para iniciar processos. Veja o que acontece durante um boot típico do systemd:

1. Primeiro, systemd carrega seus arquivos de configuração, geralmente localizados em `/etc/systemd/system` ou `/usr/lib/systemd/system`.
2. Em seguida, ele determina sua meta de boot, que geralmente é `default.target`.
3. Systemd descobre as dependências do target de boot e as ativa.

Semelhante aos runlevels do SysV, o systemd inicializa em diferentes targets:

- `poweroff.target` - desligar o sistema
- `rescue.target` - modo de usuário único
- `multi-user.target` - multiusuário com rede
- `graphical.target` - multiusuário com rede e GUI
- `reboot.target` - reiniciar

A meta de boot padrão de `default.target` geralmente aponta para o `graphical.target`.

Os principais objetos com os quais o systemd trabalha são conhecidos como unidades (units). Systemd não apenas para e inicia serviços; ele pode montar sistemas de arquivos, monitorar seus sockets de rede, etc. Por causa dessa robustez, ele tem diferentes tipos de unidades com as quais opera. As unidades mais comuns são:

- Service units - estes são os serviços que temos iniciado e parado; esses arquivos de unidade terminam em `.service`.
- Mount units - Estes montam sistemas de arquivos; esses arquivos de unidade terminam em `.mount`.
- Target units - Estes agrupam outras unidades; os arquivos terminam em `.target`.

Por exemplo, digamos que inicializamos no nosso `default.target`. Este target agrupa a unidade `networking.service`, a unidade `crond.service`, etc., então, assim que ativamos uma única unidade, tudo abaixo dessa unidade também é ativado.

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Caminho de Aprendizagem do Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual unidade é usada para agrupar outras unidades?

## Quiz Answer

target
