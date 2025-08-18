---
index: 9
lang: "pt"
title: "histórico"
meta_title: "histórico - Linha de Comando"
meta_description: "Aprenda a usar o comando history do Linux, o atalho !! e Ctrl-R para uma recuperação eficiente de comandos. Melhore sua produtividade no terminal com estas dicas essenciais!"
meta_keywords: "histórico Linux, histórico bash, Ctrl-R, comando clear, tutorial Linux, linha de comando, guia para iniciantes"
---

## Lesson Content

No seu shell, há um histórico dos comandos que você inseriu anteriormente. Você pode realmente consultar esses comandos. Isso é bastante útil quando você quer encontrar e executar um comando que usou anteriormente sem digitá-lo novamente.

```bash
history
```

Quer executar o mesmo comando que você executou antes? Basta pressionar a seta para cima.

Quer executar o comando anterior sem digitá-lo novamente? Use `!!`. Se você digitou `cat file1` e quer executá-lo novamente, você pode simplesmente digitar `!!` e ele executará o último comando que você executou.

Outro atalho de histórico é `Ctrl-R`. Este é o comando de busca reversa. Se você pressionar `Ctrl-R` e começar a digitar partes do comando que deseja, ele mostrará as correspondências. Você pode navegar por elas pressionando a tecla `Ctrl-R` novamente. Assim que encontrar o comando que deseja usar novamente, basta pressionar a tecla Enter.

Nosso terminal está um pouco bagunçado, não está? Vamos fazer uma pequena limpeza. Use o comando `clear` para limpar sua tela.

```bash
clear
```

Pronto, parece melhor, não parece?

Enquanto estamos falando de coisas úteis, uma das características mais úteis em qualquer ambiente de linha de comando é o preenchimento automático com Tab. Se você começar a digitar o início de um comando, arquivo, diretório, etc., e pressionar a tecla Tab, ele completará automaticamente com base no que encontrar no diretório em que você está pesquisando, desde que você não tenha outros arquivos que comecem com essas letras. Por exemplo, se você estivesse tentando executar o comando `chrome`, você pode digitar `chr` e pressionar Tab, e ele completará automaticamente para `chrome`.

## Exercise

Navegue pelo seu histórico de comandos anteriores com as teclas Para Cima e Para Baixo. Experimente a busca reversa `Ctrl-R`.

## Quiz Question

Qual é o comando para limpar o terminal?

## Quiz Answer

clear
