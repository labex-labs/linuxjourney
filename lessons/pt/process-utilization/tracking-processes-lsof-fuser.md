---
index: 2
lang: "pt"
title: "lsof e fuser"
meta_title: "lsof e fuser - Utilização de Processos"
meta_description: "Aprenda a usar os comandos lsof e fuser no Linux para identificar processos que usam arquivos. Entenda os erros 'Dispositivo ou Recurso Ocupado' e gerencie arquivos abertos de forma eficaz."
meta_keywords: "lsof, fuser, comandos Linux, arquivos abertos, gerenciamento de processos, tutorial Linux, guia para iniciantes, dispositivo ocupado"
---

## Lesson Content

Digamos que você conectou um pendrive USB e começou a trabalhar em alguns arquivos. Depois de terminar, você tentou desmontar o dispositivo USB e recebeu um erro: "Dispositivo ou Recurso Ocupado". Como você descobriria quais arquivos no pendrive USB ainda estão em uso? Existem duas ferramentas que você pode usar para isso:

### lsof

Lembre-se, arquivos não são apenas arquivos de texto, imagens, etc.; eles são tudo no sistema: discos, pipes, sockets de rede, dispositivos, etc. Para ver o que está em uso por um processo, você pode usar o comando `lsof` (abreviação de "list open files"). Isso mostrará uma lista de todos os arquivos abertos e seus processos associados.

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
indicator 1809 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
lsof      5915 pete  cwd    DIR    8,6     4096  131 .
```

Agora posso ver quais processos estão atualmente mantendo o dispositivo/arquivo aberto. Em nosso exemplo de USB, você também pode encerrar esses processos para poder desmontar este drive problemático.

### fuser

Outra maneira de rastrear um processo é com o comando `fuser` (abreviação de "file user"). Isso mostrará informações sobre o processo que está usando o arquivo ou o usuário do arquivo.

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  1809 ..c.. indicator-power
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

Podemos ver quais processos estão atualmente usando nosso diretório `/home/pete`. As ferramentas `lsof` e `fuser` são muito semelhantes. Familiarize-se com essas ferramentas e tente usá-las na próxima vez que precisar rastrear um arquivo ou processo.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre o gerenciamento de processos e a solução de conflitos de recursos:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro e segundo plano, inspecionando-os com `ps`, monitorando recursos com `top` e encerrando-os com `kill`. Este laboratório o ajudará a identificar e gerenciar processos que podem estar retendo recursos, como arquivos em um pendrive USB.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a construir confiança na identificação e gerenciamento de processos do sistema.

## Quiz Question

Qual comando é usado para listar arquivos abertos e suas informações de processo?

## Quiz Answer

lsof
