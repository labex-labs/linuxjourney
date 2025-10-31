---
index: 3
lang: "pt"
title: "Permissões de Propriedade"
meta_title: "Permissões de Propriedade - Permissões"
meta_description: "Domine a propriedade de arquivos no Linux aprendendo a usar os comandos chown e chgrp do Linux. Este tutorial Linux explica como alterar a propriedade de usuário e grupo de arquivos, uma habilidade essencial para gerenciar permissões no Linux."
meta_keywords: "chown, chgrp, propriedade de arquivo linux, alterar proprietário de arquivo, alterar grupo de arquivo, permissões linux, comandos linux, tutorial linux, guia linux, propriedade de usuário, propriedade de grupo"
---

## Lesson Content

Em um sistema Linux, cada arquivo e diretório é atribuído a um proprietário e um grupo. Gerenciar a **propriedade de arquivos Linux** é uma tarefa fundamental para controlar o acesso e as permissões. Você pode modificar tanto a propriedade do usuário quanto a do grupo de um arquivo usando **comandos Linux** específicos.

### Alterando a Propriedade do Usuário

Para transferir a propriedade de um arquivo para um usuário diferente, você usa o comando `chown` (change owner - alterar proprietário). Isso é útil quando as responsabilidades de um usuário mudam ou quando você precisa atribuir o controle do arquivo a outra pessoa. Geralmente, você precisa de privilégios de superusuário (`sudo`) para alterar o proprietário de um arquivo que não lhe pertence.

```bash
sudo chown patty myfile
```

Este comando altera o proprietário do usuário de `myfile` para o usuário `patty`.

### Alterando a Propriedade do Grupo

Da mesma forma, você pode alterar o grupo associado a um arquivo usando o comando `chgrp` (change group - alterar grupo). Isso permite que todos os membros do novo grupo tenham acesso com base nas **permissões Linux** do grupo.

```bash
sudo chgrp whales myfile
```

Este comando define a propriedade do grupo de `myfile` para o grupo `whales`.

### Alterando Usuário e Grupo

Para maior eficiência, o comando `chown` permite alterar tanto a propriedade do usuário quanto a do grupo em uma única etapa. Ao separar o nome do usuário e do grupo com dois pontos (:), você pode atualizar ambos os atributos simultaneamente.

```bash
sudo chown patty:whales myfile
```

Este único comando atribui a propriedade do usuário a `patty` e a propriedade do grupo a `whales` para o arquivo `myfile`. Este é o método mais comum para gerenciar a **propriedade de arquivos Linux**.

## Exercise

Para solidificar sua compreensão sobre a **propriedade de arquivos Linux**, recomendamos praticar com estes laboratórios práticos. Eles fornecem cenários do mundo real para aplicar os comandos `chown` e `chgrp`.

1. **[Grupo de Usuários e Permissões de Arquivo Linux](https://labex.io/pt/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprenda conceitos essenciais de gerenciamento de usuários e grupos no Linux, incluindo a compreensão de permissões de arquivos e a manipulação da propriedade de arquivos. Este laboratório oferece experiência prática na proteção de um ambiente Linux multiusuário.
2. **[Adicionar Novo Usuário e Grupo](https://labex.io/pt/labs/linux-add-new-user-and-group-17987)** - Neste desafio, você simulará a adição de novos membros da equipe a um ambiente de servidor criando novas contas de usuário, configurando grupos personalizados e gerenciando associações de grupo. Isso testará suas habilidades em administração de usuários e grupos no Linux.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança no gerenciamento da propriedade de arquivos e permissões no Linux.

## Quiz Question

Qual comando é usado para alterar a propriedade do usuário de um arquivo? Por favor, forneça apenas o nome do comando em letras minúsculas em inglês.

## Quiz Answer

chown
