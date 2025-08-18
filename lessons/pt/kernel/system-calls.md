---
index: 3
lang: "pt"
title: "Chamadas de Sistema"
meta_title: "Chamadas de Sistema - Kernel"
meta_description: "Aprenda sobre chamadas de sistema Linux (syscalls) e como elas interagem com o kernel. Entenda os modos de usuário e kernel, e use `strace` para depuração. Comece sua jornada no Linux!"
meta_keywords: "chamadas de sistema Linux, syscalls, modo kernel, modo de usuário, comando strace, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Lembra-se da Britney na lição anterior? Digamos que queremos vê-la e tomar uns drinques juntos. Como passamos de estar do lado de fora, no meio da multidão, para dentro do círculo mais íntimo dela? Usaríamos chamadas de sistema. As chamadas de sistema são como os passes VIP que o levam a uma porta lateral secreta que dá diretamente para a Britney.

As chamadas de sistema (syscalls) fornecem aos processos do espaço do usuário uma maneira de solicitar ao kernel que faça algo por nós. O kernel disponibiliza certos serviços através da API de chamadas de sistema. Esses serviços nos permitem ler ou escrever em um arquivo, modificar o uso da memória, modificar nossa rede, etc. A quantidade de serviços é fixa, então você não pode adicionar chamadas de sistema de forma aleatória. Seu sistema já possui uma tabela de quais chamadas de sistema existem, e cada chamada de sistema tem um ID único.

Não entrarei em detalhes específicos sobre chamadas de sistema, pois isso exigiria que você soubesse um pouco de C, mas o básico é que, quando você chama um programa como `ls`, o código dentro deste programa contém um wrapper de chamada de sistema (portanto, ainda não é a chamada de sistema real). Dentro deste wrapper, ele invoca a chamada de sistema que executará uma trap. Esta trap é então capturada pelo manipulador de chamadas de sistema e, em seguida, referencia a chamada de sistema na tabela de chamadas de sistema. Digamos que estamos tentando chamar a chamada de sistema `stat()`; ela é identificada por um ID de syscall, e o propósito da chamada de sistema `stat()` é consultar o status de um arquivo. Agora, lembre-se, você estava executando o programa `ls` em modo não privilegiado. Então, agora ele vê que você está tentando fazer uma syscall, ele então o muda para o modo kernel. Lá ele faz muitas coisas, mas o mais importante, ele procura o seu número de syscall, o encontra em uma tabela baseada no ID da syscall, e então executa a função que você queria executar. Uma vez que ele termina, ele retornará ao modo de usuário, e seu processo receberá um status de retorno se foi bem-sucedido ou se teve um erro. O funcionamento interno das syscalls se torna realmente detalhado; eu recomendaria procurar informações online se você quiser aprender mais.

Você pode realmente visualizar as chamadas de sistema que um processo faz com o comando `strace`. O comando `strace` é útil para depurar como um programa foi executado.

```bash
strace ls
```

## Exercise

No exercises for this lesson.

## Quiz Question

O que é usado para alternar do modo de usuário para o modo kernel?

## Quiz Answer

System call
