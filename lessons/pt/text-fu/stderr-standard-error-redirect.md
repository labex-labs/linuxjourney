---
index: 3
lang: "pt"
title: "stderr (Erro Padrão)"
meta_title: "stderr (Erro Padrão) - Text-Fu"
meta_description: "Aprenda a gerenciar o erro padrão no Linux. Este guia aborda o redirecionamento de stderr, o descritor de arquivo stderr (2) e como redirecionar stderr para um arquivo ou /dev/null usando 2>, 2>&1 e &>."
meta_keywords: "stderr, erro padrão linux, descritor de arquivo stderr, arquivo stderr, erro padrão linux, redirecionar stderr, 2>, 2>&1, &>, /dev/null, tratamento de erro bash"
---

## Lesson Content

Vamos explorar o que acontece quando um comando produz um erro. Tente listar o conteúdo de um diretório que não existe e redirecionar a saída para um arquivo chamado `peanuts.txt`.

```bash
ls /fake/directory > peanuts.txt
```

Em vez de um prompt limpo, você verá uma mensagem de erro na sua tela:

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

Você pode estar se perguntando por que essa mensagem não foi enviada para o arquivo. Isso ocorre porque outro fluxo de E/S está em jogo: **erro padrão**, ou **stderr**.

### O que é Erro Padrão no Linux?

No Linux, `stderr` é um fluxo de saída padrão usado por programas para enviar mensagens de erro e diagnósticos. Ele é completamente separado do fluxo de saída padrão (`stdout`), que é usado para a saída normal do programa. Por padrão, tanto `stdout` quanto `stderr` enviam sua saída para a tela do seu terminal, razão pela qual você vê a mensagem de erro diretamente.

Para controlar `stderr`, você precisa de um método de redirecionamento diferente.

### Entendendo Descritores de Arquivo

Para gerenciar fluxos de E/S como `stdin`, `stdout` e `stderr`, o sistema usa descritores de arquivo. Um **descritor de arquivo** é um número não negativo que o kernel usa para identificar um arquivo ou fluxo aberto. Os descritores de arquivo padrão são:

- `0`: stdin (entrada padrão)
- `1`: stdout (saída padrão)
- `2`: stderr (erro padrão)

O número `2` é o **descritor de arquivo stderr** dedicado, e podemos usá-lo para controlar para onde as mensagens de erro vão.

### Redirecionando stderr para um Arquivo

Para redirecionar `stderr` para um arquivo, você usa o descritor de arquivo `2` seguido pelo operador `>`. Este comando enviará quaisquer mensagens de erro para o `arquivo stderr` especificado.

```bash
ls /fake/directory 2> peanuts.txt
```

Agora, seu terminal ficará silencioso, e a mensagem de erro estará dentro de `peanuts.txt`.

### Combinando stdout e stderr

E se você quiser capturar tanto a saída normal quanto as mensagens de erro no mesmo arquivo? Você pode conseguir isso redirecionando ambos os fluxos.

```bash
ls /fake/directory /etc/passwd > peanuts.txt 2>&1
```

Vamos analisar isso:

1. `> peanuts.txt` redireciona `stdout` (descritor de arquivo 1) para o arquivo `peanuts.txt`.
2. `2>&1` redireciona `stderr` (descritor de arquivo 2) para o mesmo local para o qual `stdout` (descritor de arquivo 1) está apontando atualmente.

A ordem é importante. `2>&1` envia `stderr` para o destino atual de `stdout`. Neste caso, `stdout` está apontando para um arquivo, então `stderr` também é enviado para esse arquivo.

Uma maneira mais moderna e curta de redirecionar tanto `stdout` quanto `stderr` é usando `&>`.

```bash
ls /fake/directory /etc/passwd &> peanuts.txt
```

### Descartando Mensagens de Erro

Às vezes, você pode querer executar um comando e ignorar completamente quaisquer mensagens de erro potenciais. Para fazer isso, você pode redirecionar `stderr` para um arquivo especial chamado `/dev/null`, que descarta quaisquer dados gravados nele.

```bash
ls /fake/directory 2> /dev/null
```

Este comando será executado, e qualquer saída de erro de `stderr` será enviada para `/dev/null` e descartada, deixando sua tela limpa.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do redirecionamento de entrada/saída:

1. **[Redirecionando Entrada e Saída no Linux](https://labex.io/pt/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Neste laboratório, você aprenderá a redirecionar entrada e saída no shell Linux. Você praticará o controle do fluxo de dados dos comandos, manipulando a saída padrão (stdout), o erro padrão (stderr) e a entrada padrão (stdin) usando operadores como >, >>, 2> e o comando tee.

Este laboratório o ajudará a aplicar os conceitos de redirecionamento de E/S em cenários reais e a ganhar confiança no gerenciamento de fluxos de dados no Linux.

## Quiz Question

Qual é o operador usado para redirecionar o fluxo `stderr`? Por favor, forneça o operador exato em sua resposta.

## Quiz Answer

2>
