---
index: 3
lang: "pt"
title: "stderr (Erro Padrão)"
meta_title: "stderr (Erro Padrão) - Text-Fu"
meta_description: "Aprenda sobre o redirecionamento de stderr (erro padrão) no Linux. Entenda 2>, 2>&1, &> e /dev/null para tratamento de erros no Bash. Melhore suas habilidades na linha de comando Linux!"
meta_keywords: "Linux stderr, erro padrão, redirecionamento 2>, 2>&1, redirecionamento &>, /dev/null, tratamento de erros Bash, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

Vamos tentar algo um pouco diferente agora. Vamos tentar listar o conteúdo de um diretório que não existe no seu sistema e redirecionar a saída para o arquivo `peanuts.txt` novamente.

```bash
ls /fake/directory > peanuts.txt
```

O que você deve ver é:

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

Agora você provavelmente está pensando, essa mensagem não deveria ter sido enviada para o arquivo? Na verdade, há outro fluxo de E/S em jogo aqui, chamado erro padrão (stderr). Por padrão, o stderr também envia sua saída para a tela; é um fluxo completamente diferente do stdout. Então você precisará redirecionar sua saída de uma maneira diferente.

Infelizmente, o redirecionador não é tão agradável quanto usar `<` ou `>`, mas é bem parecido. Teremos que usar descritores de arquivo. Um descritor de arquivo é um número não negativo usado para acessar um arquivo ou fluxo. Abordaremos isso em profundidade mais tarde, mas por enquanto saiba que o descritor de arquivo para stdin, stdout e stderr é 0, 1 e 2, respectivamente.

Então, agora, se quisermos redirecionar nosso stderr para o arquivo, podemos fazer isso:

```bash
ls /fake/directory 2> peanuts.txt
```

Você deve ver apenas as mensagens de stderr em `peanuts.txt`.

E se eu quisesse ver tanto stderr quanto stdout no arquivo `peanuts.txt`? É possível fazer isso com descritores de arquivo também:

```bash
ls /fake/directory > peanuts.txt 2>&1
```

Isso envia os resultados de `ls /fake/directory` para o arquivo `peanuts.txt` e então redireciona o stderr para o stdout via `2>&1`. A ordem das operações aqui importa; `2>&1` envia o stderr para onde quer que o stdout esteja apontando. Neste caso, o stdout está apontando para um arquivo, então `2>&1` também envia o stderr para um arquivo. Então, se você abrir o arquivo `peanuts.txt`, deverá ver tanto o stderr quanto o stdout. No nosso caso, o comando acima apenas gera stderr.

Existe uma maneira mais curta de redirecionar tanto stdout quanto stderr para um arquivo:

```bash
ls /fake/directory &> peanuts.txt
```

E se eu não quiser nada dessa bagunça e quiser me livrar das mensagens de stderr completamente? Bem, você também pode redirecionar a saída para um arquivo especial chamado `/dev/null` e ele descartará qualquer entrada.

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do redirecionamento de entrada/saída:

1. **[Redirecionando Entrada e Saída no Linux](https://labex.io/pt/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Neste laboratório, você aprenderá a redirecionar entrada e saída no shell Linux. Você praticará o controle do fluxo de dados de comandos manipulando a saída padrão (stdout), o erro padrão (stderr) e a entrada padrão (stdin) usando operadores como >, >>, 2> e o comando tee.

Este laboratório o ajudará a aplicar os conceitos de redirecionamento de E/S em cenários reais e a construir confiança no gerenciamento de fluxos de dados no Linux.

## Quiz Question

Qual é o redirecionador para stderr?

## Quiz Answer

2>
