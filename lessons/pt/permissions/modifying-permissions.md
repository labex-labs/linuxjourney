---
index: 2
lang: "pt"
title: "Modificando Permissões"
meta_title: "Modificando Permissões - Permissões"
meta_description: "Aprenda a usar o comando chmod para modificar permissões de arquivos no Linux. Entenda os modos simbólico e numérico para um gerenciamento seguro de arquivos. Comece a aprender agora!"
meta_keywords: "comando chmod, permissões Linux, permissões de arquivo, tutorial chmod, segurança Linux, Linux para iniciantes, guia Linux, chmod numérico"
---

## Lesson Content

Mudar permissões pode ser feito facilmente com o comando `chmod`.

Primeiro, escolha qual conjunto de permissões você deseja alterar: usuário, grupo ou outros. Você pode adicionar ou remover permissões com um `+` ou `-`. Vamos ver alguns exemplos.

### Adicionando bit de permissão em um arquivo

```bash
chmod u+x myfile
```

O comando acima lê-se assim: altera a permissão em `myfile` adicionando o bit de permissão executável ao conjunto do usuário. Então agora o usuário tem permissão de execução neste arquivo!

### Removendo bit de permissão em um arquivo

```bash
chmod u-x myfile
```

### Adicionando múltiplos bits de permissão em um arquivo

```bash
chmod ug+w
```

Existe outra maneira de mudar permissões usando o formato numérico. Este método permite que você mude as permissões de uma vez só. Em vez de usar r, w ou x para representar permissões, você usará uma representação numérica para um único conjunto de permissões. Assim, não há necessidade de especificar o grupo com `g` ou o usuário com `u`.

As representações numéricas são vistas abaixo:

- 4: permissão de leitura
- 2: permissão de escrita
- 1: permissão de execução

Vamos ver um exemplo:

```bash
chmod 755 myfile
```

Você consegue adivinhar quais permissões estamos dando a este arquivo? Vamos detalhar isso: `755` cobre as permissões para todos os conjuntos. O primeiro número (7) representa as permissões do usuário, o segundo número (5) representa as permissões do grupo, e o último 5 representa as outras permissões.

Espere um minuto, 7 e 5 não estavam listados acima. De onde estamos tirando esses números? Lembre-se, estamos combinando todas as permissões em um único número agora, então você terá que fazer alguns cálculos.

7 = 4 + 2 + 1, então 7 são as permissões do usuário, e ele tem permissões de leitura, escrita e execução.

5 = 4 + 1, o grupo tem permissões de leitura e execução.

5 = 4 + 1, e todos os outros usuários têm permissões de leitura e execução.

Uma coisa a notar: não é uma boa ideia mudar permissões de forma aleatória. Você poderia potencialmente expor um arquivo sensível para que todos o modificassem. No entanto, muitas vezes você legitimamente deseja mudar permissões; apenas tome precaução ao usar o comando `chmod`.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão das permissões de arquivos Linux:

1. **[Grupo de Usuários Linux e Permissões de Arquivos](https://labex.io/pt/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprenda conceitos essenciais de gerenciamento de usuários e grupos Linux, incluindo a compreensão das permissões de arquivos e a manipulação da propriedade de arquivos. Este laboratório oferece experiência prática na segurança de um ambiente Linux multiusuário.
2. **[Adicionar Novo Usuário e Grupo](https://labex.io/pt/labs/linux-add-new-user-and-group-17987)** - Neste desafio, você simulará a adição de novos membros da equipe a um ambiente de servidor, criando novas contas de usuário, configurando grupos personalizados e gerenciando associações de grupo, o que muitas vezes envolve a definição de permissões apropriadas.

Esses laboratórios o ajudarão a aplicar os conceitos de permissões de usuário, grupo e outros em cenários reais e a construir confiança no gerenciamento de acesso no Linux.

## Quiz Question

Qual número representa a permissão de leitura ao usar o formato numérico?

## Quiz Answer

4
