---
index: 3
lang: "pt"
title: "Chamadas de Sistema"
meta_title: "Chamadas de Sistema - Kernel"
meta_description: "Aprenda sobre chamadas de sistema Linux (syscalls) e como elas interagem com o kernel. Entenda os modos de usuário e kernel, e use `strace` para depuração. Comece sua jornada no Linux!"
meta_keywords: "Chamadas de sistema Linux, syscalls, modo kernel, modo usuário, comando strace, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Lembra-se da Britney na lição anterior? Digamos que queremos vê-la e tomar uns drinques juntos. Como saímos de estar do lado de fora no meio da multidão para dentro do círculo mais íntimo dela? Usaríamos chamadas de sistema. As chamadas de sistema são como os passes VIP que te levam a uma porta lateral secreta que leva diretamente à Britney.

Chamadas de sistema (syscalls) fornecem aos processos do espaço do usuário uma maneira de solicitar ao kernel que faça algo por nós. O kernel disponibiliza certos serviços através da API de chamadas de sistema. Esses serviços nos permitem ler ou escrever em um arquivo, modificar o uso da memória, modificar nossa rede, etc. A quantidade de serviços é fixa, então você não pode adicionar chamadas de sistema de qualquer jeito. Seu sistema já possui uma tabela de quais chamadas de sistema existem, e cada chamada de sistema tem um ID único.

Não entrarei em detalhes específicos sobre chamadas de sistema, pois isso exigiria que você soubesse um pouco de C, mas o básico é que, quando você chama um programa como `ls`, o código dentro deste programa contém um wrapper de chamada de sistema (ainda não a chamada de sistema real). Dentro deste wrapper, ele invoca a chamada de sistema que executará uma armadilha. Esta armadilha é então capturada pelo manipulador de chamadas de sistema e então referencia a chamada de sistema na tabela de chamadas de sistema. Digamos que estamos tentando chamar a chamada de sistema `stat()`; ela é identificada por um ID de syscall, e o propósito da chamada de sistema `stat()` é consultar o status de um arquivo. Agora lembre-se, você estava executando o programa `ls` em modo não privilegiado. Então, agora ele vê que você está tentando fazer uma syscall, ele então o muda para o modo kernel. Lá ele faz muitas coisas, mas o mais importante, ele procura o seu número de syscall, o encontra em uma tabela baseada no ID da syscall, e então executa a função que você queria executar. Uma vez que termina, ele retornará ao modo de usuário, e seu processo receberá um status de retorno se foi bem-sucedido ou se teve um erro. O funcionamento interno das syscalls se torna realmente detalhado; eu recomendaria procurar informações online se você quiser aprender mais.

Você pode realmente visualizar as chamadas de sistema que um processo faz com o comando `strace`. O comando `strace` é útil para depurar como um programa foi executado.

```bash
strace ls
```

## Exercise

A prática leva à perfeição! Embora o funcionamento interno das chamadas de sistema seja complexo, entender como os programas do espaço do usuário interagem com o kernel é fundamental. A melhor maneira de compreender essa interação é praticando com comandos que executam essas operações subjacentes. Aqui estão alguns laboratórios práticos para reforçar sua compreensão das interações do sistema de arquivos, que dependem fortemente das chamadas de sistema:

1. **[Navegar no Sistema de Arquivos no Linux](https://labex.io/pt/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Pratique comandos essenciais como `ls`, `cd` e `pwd` para se mover e inspecionar seu sistema de arquivos Linux, interagindo diretamente com os serviços do sistema de arquivos do kernel.
2. **[Gerenciar Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-files-and-directories-in-linux-590835)** - Aprenda a criar, remover, copiar e mover arquivos e diretórios usando comandos como `mkdir`, `rm`, `cp` e `mv`, todos os quais envolvem chamadas de sistema para executar suas ações.
3. **[Encontrar Arquivos e Comandos no Linux](https://labex.io/pt/labs/comptia-find-files-and-commands-in-linux-590834)** - Domine técnicas para localizar arquivos e comandos usando `find`, `whereis` e `which`, ilustrando ainda mais como os comandos do usuário utilizam os serviços do kernel para interagir com o sistema de arquivos.

Esses laboratórios o ajudarão a aplicar os conceitos de interação do sistema de arquivos em cenários reais e a construir confiança com operações fundamentais do Linux que implicitamente dependem de chamadas de sistema.

## Quiz Question

O que é usado para alternar do modo de usuário para o modo kernel?

## Quiz Answer

System call
