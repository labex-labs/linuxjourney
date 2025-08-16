---
title: "stderr (Erro Padrão)"
description: "Aprenda sobre o redirecionamento de stderr (erro padrão) no Linux. Entenda 2>, 2>&1, &> e /dev/null para tratamento de erros no Bash. Melhore suas habilidades na linha de comando Linux!"
keywords: "Linux stderr, erro padrão, redirecionamento 2>, 2>&1, redirecionamento &>, /dev/null, tratamento de erros Bash, tutorial Linux, Linux para iniciantes"
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

Infelizmente, o redirecionador não é tão agradável quanto usar `<` ou `>`, mas é bem parecido. Teremos que usar descritores de arquivo. Um descritor de arquivo é um número não negativo usado para acessar um arquivo ou fluxo. Entraremos em detalhes sobre isso mais tarde, mas por enquanto saiba que o descritor de arquivo para stdin, stdout e stderr é 0, 1 e 2, respectivamente.

Então, agora, se quisermos redirecionar nosso stderr para o arquivo, podemos fazer isso:

```bash
ls /fake/directory 2> peanuts.txt
```

Você deve ver apenas as mensagens de stderr em `peanuts.txt`.

E se eu quisesse ver tanto stderr quanto stdout no arquivo `peanuts.txt`? É possível fazer isso também com descritores de arquivo:

```bash
ls /fake/directory > peanuts.txt 2>&1
```

Isso envia os resultados de `ls /fake/directory` para o arquivo `peanuts.txt` e então redireciona stderr para stdout via `2>&1`. A ordem das operações aqui importa; `2>&1` envia stderr para onde quer que stdout esteja apontando. Neste caso, stdout está apontando para um arquivo, então `2>&1` também envia stderr para um arquivo. Então, se você abrir o arquivo `peanuts.txt`, deverá ver tanto stderr quanto stdout. No nosso caso, o comando acima apenas gera stderr.

Existe uma maneira mais curta de redirecionar stdout e stderr para um arquivo:

```bash
ls /fake/directory &> peanuts.txt
```

E se eu não quiser nada disso e quiser me livrar das mensagens de stderr completamente? Bem, você também pode redirecionar a saída para um arquivo especial chamado `/dev/null` e ele descartará qualquer entrada.

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

O que o seguinte comando está fazendo?

```bash
ls /fake/directory >> /dev/null 2>&1
```

## Quiz Question

Qual é o redirecionador para stderr?

## Quiz Answer

2>
