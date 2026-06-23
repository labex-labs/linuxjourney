---
index: 19
lang: "pt"
title: "exit"
meta_title: "exit - Linha de Comando"
meta_description: "Aprenda o comando exit no Linux, como encerrar uma sessão shell, a diferença entre logout e exit, e como funcionam os valores de status de saída."
meta_keywords: "comando exit, linux exit, comando logout, sessão shell, saída do terminal, status de saída, bash exit"
---

## Lesson Content

Parabéns por completar as lições fundamentais da sua jornada Linux! Você aprendeu os conceitos básicos essenciais do Linux, e agora é hora de aprender como encerrar sua sessão corretamente. Sair do shell Linux é um passo final simples, mas importante.

### O Comando Exit

A maneira mais comum de encerrar uma sessão shell é com o comando `exit`. Quando você digita `exit` e pressiona Enter, o processo shell atual termina. Esse comando funciona em praticamente qualquer ambiente shell.

```bash
$ exit
```

Se você abriu uma janela de terminal, `exit` geralmente fecha o shell que está rodando dentro dela. Se você se conectou via SSH, `exit` encerra a sessão shell remota e retorna ao seu prompt local.

### Valores de Status de Saída

O comando `exit` também pode retornar um código de status. Um status `0` geralmente significa sucesso, e um status diferente de zero geralmente indica um erro ou condição especial.

```bash
$ exit 0
```

Você verá os status de saída com mais frequência ao escrever scripts shell. Para uso interativo, simplesmente digitar `exit` é suficiente.

### O Comando Logout

Outro comando que você pode usar para sair do terminal é `logout`. Esse comando é especificamente projetado para terminar um shell de login. Embora em muitos sistemas modernos ele se comporte de forma semelhante ao `exit`, é uma boa prática conhecer ambos os comandos.

```bash
$ logout
```

### Fechando a Janela do Terminal

Se você estiver trabalhando em uma interface gráfica, também tem a opção de simplesmente fechar a janela do terminal. Essa ação normalmente envia um sinal que termina a sessão shell que está rodando dentro dela.

### Maneiras Comuns de Sair de um Shell

- Digite `exit` para encerrar o shell atual.
- Pressione `Ctrl-D` em um prompt vazio para enviar um fim de arquivo, que frequentemente encerra o shell.
- Digite `logout` quando estiver em um shell de login.
- Feche a janela do terminal quando estiver usando um terminal gráfico.

### Perguntas Comuns

**O exit é o mesmo que fechar a janela do terminal?** Frequentemente o resultado é semelhante, mas `exit` informa ao shell para terminar de forma limpa.

**O que é Ctrl-D?** Ele envia um sinal de fim de arquivo para o shell. Em um prompt vazio, isso geralmente encerra o shell.

**O que significa exit 1?** Sai com o código de status `1`, comumente usado para indicar falha em scripts.

Você aprendeu com sucesso como navegar, trabalhar com arquivos, obter ajuda e sair do shell.

## Exercise

Embora não existam laboratórios específicos para este tópico, recomendamos explorar o abrangente [Caminho de Aprendizagem Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual é o comando mais comum para sair do shell Linux? Por favor, responda usando apenas uma palavra em inglês minúscula.

## Quiz Answer

exit
