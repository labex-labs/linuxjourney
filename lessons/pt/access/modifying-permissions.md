---
index: 2
lang: "pt"
title: "Modificando Permissões"
meta_title: "Modificando Permissões - Permissões"
meta_description: "Aprenda como usar o comando chmod para modificar permissões de arquivos no Linux. Entenda os modos simbólico e numérico para gerenciamento seguro de arquivos. Comece a aprender agora!"
meta_keywords: "comando chmod, permissões Linux, permissões de arquivo, tutorial chmod, segurança Linux, Linux para iniciantes, guia Linux, chmod numérico"
---

## Lesson Content

Alterar permissões pode ser facilmente feito com o comando `chmod`.

Primeiro, escolha qual conjunto de permissões você deseja alterar: usuário, grupo ou outros. Você pode adicionar ou remover permissões com um `+` ou `-`. Vamos ver alguns exemplos.

### Adicionando bit de permissão em um arquivo

```bash
chmod u+x myfile
```

O comando acima lê-se assim: altera a permissão em `myfile` adicionando o bit de permissão de execução ao conjunto do usuário. Então agora o usuário tem permissão de execução neste arquivo!

### Removendo bit de permissão em um arquivo

```bash
chmod u-x myfile
```

### Adicionando múltiplos bits de permissão em um arquivo

```bash
chmod ug+w
```

Existe outra maneira de alterar permissões usando o formato numérico. Este método permite que você altere as permissões de uma só vez. Em vez de usar r, w ou x para representar permissões, você usará uma representação numérica para um único conjunto de permissões. Assim, não há necessidade de especificar o grupo com `g` ou o usuário com `u`.

As representações numéricas são as seguintes:

- 4: permissão de leitura
- 2: permissão de escrita
- 1: permissão de execução

Vamos ver um exemplo:

```bash
chmod 755 myfile
```

Você consegue adivinhar quais permissões estamos dando a este arquivo? Vamos detalhar: `755` cobre as permissões para todos os conjuntos. O primeiro número (7) representa as permissões do usuário, o segundo número (5) representa as permissões do grupo e o último 5 representa as outras permissões.

Espere um minuto, 7 e 5 não foram listados acima. De onde estamos tirando esses números? Lembre-se, estamos combinando todas as permissões em um único número agora, então você terá que fazer alguns cálculos.

7 = 4 + 2 + 1, então 7 são as permissões do usuário, e ele tem permissões de leitura, escrita e execução.

5 = 4 + 1, o grupo tem permissões de leitura e execução.

5 = 4 + 1, e todos os outros usuários têm permissões de leitura e execução.

Uma coisa a notar: não é uma boa ideia ficar mudando permissões de forma aleatória. Você poderia potencialmente expor um arquivo sensível para que todos o modifiquem. No entanto, muitas vezes você legitimamente deseja alterar permissões; apenas tome precaução ao usar o comando `chmod`.

## Exercise

Altere algumas permissões básicas de arquivos de texto e veja os bits mudando ao fazer um `ls -l`.

## Quiz Question

Qual número representa a permissão de leitura ao usar o formato numérico?

## Quiz Answer

4
