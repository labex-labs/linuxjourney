---
lang: "pt"
title: "env (Ambiente)"
meta_description: "Aprenda sobre as variáveis de ambiente Linux com o comando 'env'. Entenda as variáveis PATH, HOME e USER. Obtenha um guia para iniciantes sobre como gerenciar seu ambiente Linux."
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

Isso retorna uma lista de caminhos separados por dois pontos que seu sistema pesquisa ao executar um comando. Digamos que você baixe e instale manualmente um pacote da internet e o coloque em um diretório não padrão, e você queira executar esse comando. Você digita `$ coolcommand`, e o prompt diz "command not found". Bem, isso é bobagem; você está olhando para o binário em uma pasta e sabe que ele existe. O que está acontecendo é que a variável `$PATH` não verifica esse diretório para este binário, então está lançando um erro.

Digamos que você tivesse muitos binários que queria executar a partir desse diretório; você pode simplesmente modificar a variável PATH para incluir esse diretório na sua variável de ambiente PATH.

## Exercise

O que o seguinte comando exibe? Por quê?

```bash
echo $HOME
```

## Quiz Question

Como você vê suas variáveis de ambiente?

## Quiz Answer

env
