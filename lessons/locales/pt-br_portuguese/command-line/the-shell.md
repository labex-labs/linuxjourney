# O shell

## Conteúdo da lição

O mundo é sua ostra, ou realmente a casca(shell em inglês) é sua ostra. O que é o shell? O shell é basicamente um programa que pega seus comandos do teclado e os envia para o sistema operacional para executar. Se você já usou uma GUI, provavelmente já viu programas como "Terminal" ou "Console", são apenas programas que iniciam um shell para você. Ao longo de todo este curso, estaremos aprendendo sobre as maravilhas do shell.

Neste curso, usaremos o programa shell bash (shell Bourne Again), quase todas as distribuições Linux serão padronizadas para o shell bash. Existem outras shells disponíveis, como ksh, zsh, tsch, mas não entraremos em nenhuma delas.

Vamos pular direto! Dependendo da distribuição, o prompt do seu shell pode mudar, mas na maioria das vezes ele deve seguir o seguinte formato:
<pre> nomedeusuario @ nomedocomputador: diretorio_atual
pete @ icebox: / home / pete $ </ pre>

Observou o $ no final do prompt? Shells diferentes terão prompts diferentes, no nosso caso o $ é para um usuário normal usando shell Bash, Bourne ou Korn, você não adiciona o símbolo de prompt ao digitar o comando, apenas saiba que ele estará lá.

Vamos começar com um comando simples, echo. O comando echo apenas exibe os argumentos de texto na tela.

<pre> $ echo Olá mundo </ pre>

## Exercício

Tente alguns outros comandos do Linux e veja o que eles geram:

<ol>
<li> $ date </ li>
<li> $ whoami </ li>
</ ol>

## Questionário

O que deve ser enviado para a tela quando você digita echo Olá mundo?

## Resposta do questionário

Olá Mundo