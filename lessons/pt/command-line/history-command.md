---
index: 9
lang: "pt"
title: "history"
meta_title: "history - Linha de Comando"
meta_description: "Aprenda a usar o comando history do Linux, o atalho !! e Ctrl-R para recuperação eficiente de comandos. Melhore sua produtividade no terminal com estas dicas essenciais!"
meta_keywords: "histórico Linux, histórico bash, Ctrl-R, comando clear, tutorial Linux, linha de comando, guia para iniciantes"
---

## Lesson Content

No seu shell, há um histórico dos comandos que você inseriu anteriormente. Você pode realmente consultar esses comandos. Isso é bastante útil quando você deseja encontrar e executar um comando que usou anteriormente sem digitá-lo novamente.

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

Enquanto estamos falando de coisas úteis, uma das características mais úteis em qualquer ambiente de linha de comando é o preenchimento automático por tabulação. Se você começar a digitar o início de um comando, arquivo, diretório, etc., e pressionar a tecla Tab, ele fará o preenchimento automático com base no que encontrar no diretório que você está pesquisando, desde que você não tenha outros arquivos que comecem com essas letras. Por exemplo, se você estivesse tentando executar o comando `chrome`, você pode digitar `chr` e pressionar Tab, e ele fará o preenchimento automático para `chrome`.

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Caminho de Aprendizagem Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual é o comando para limpar o terminal?

## Quiz Answer

clear
