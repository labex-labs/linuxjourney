---
index: 5
lang: "pt"
title: "env (Ambiente)"
meta_title: "env (Ambiente) - Text-Fu"
meta_description: "Aprenda sobre variáveis de ambiente Linux com o comando 'env'. Entenda as variáveis PATH, HOME e USER. Obtenha um guia para iniciantes para gerenciar seu ambiente Linux."
meta_keywords: "comando env, variáveis de ambiente Linux, variável PATH, tutorial Linux, Linux para iniciantes, variáveis de shell, guia Linux"
---

## Lesson Content

Execute o seguinte comando:

```bash
echo $HOME
```

Você deverá ver o caminho para o seu diretório home; o meu se parece com /home/pete.

E este comando?

```bash
echo $USER
```

Você deverá ver seu nome de usuário!

De onde vem essa informação? Ela vem das suas variáveis de ambiente. Você pode visualizá-las digitando:

```bash
env
```

Isso exibe uma grande quantidade de informações sobre as variáveis de ambiente que você tem atualmente definidas. Essas variáveis contêm informações úteis que o shell e outros processos podem usar.

Aqui está um pequeno exemplo:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Uma variável particularmente importante é a variável PATH. Você pode acessar essas variáveis colocando um `$` na frente do nome da variável, assim:

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
```

Isso retorna uma lista de caminhos separados por dois pontos que seu sistema pesquisa ao executar um comando. Digamos que você baixe e instale manualmente um pacote da internet e o coloque em um diretório não padrão, e você queira executar esse comando. Você digita `$ coolcommand`, e o prompt diz "command not found". Bem, isso é bobo; você está olhando para o binário em uma pasta e sabe que ele existe. O que está acontecendo é que a variável `$PATH` não verifica esse diretório para este binário, então está lançando um erro.

Digamos que você tivesse muitos binários que queria executar a partir desse diretório; você pode simplesmente modificar a variável PATH para incluir esse diretório em sua variável de ambiente PATH.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão das variáveis de ambiente Linux:

1. **[Gerenciar Ambiente de Shell e Configuração no Linux](https://labex.io/pt/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Pratique a criação e o gerenciamento de variáveis locais e de ambiente, compreendendo a herança e tornando as configurações persistentes modificando o arquivo `.bashrc`.
2. **[Variáveis de Ambiente no Linux](https://labex.io/pt/labs/linux-environment-variables-in-linux-385274)** - Aprenda o conceito e o uso das variáveis de ambiente, como criá-las, modificá-las e gerenciá-las, e seu papel na configuração do sistema.
3. **[Configurar Variáveis de Ambiente Linux](https://labex.io/pt/labs/linux-configure-linux-environment-variables-437861)** - Obtenha experiência prática na criação, definição e gerenciamento de variáveis de ambiente em um sistema Linux.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento do seu ambiente de shell Linux.

## Quiz Question

Como você vê suas variáveis de ambiente?

## Quiz Answer

env
