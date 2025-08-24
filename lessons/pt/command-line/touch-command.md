---
index: 5
lang: "pt"
title: "touch"
meta_title: "touch - Linha de Comando"
meta_description: "Aprenda a usar o comando Linux touch para criar novos arquivos e atualizar carimbos de data/hora. Este guia para iniciantes ajuda você a entender o gerenciamento de arquivos."
meta_keywords: "comando touch, criar arquivos, tutorial Linux, carimbos de data/hora de arquivos, Linux para iniciantes, guia Linux, comandos básicos"
---

## Lesson Content

Vamos aprender como criar alguns arquivos. Uma maneira muito simples é usar o comando `touch`. O `touch` permite criar novos arquivos vazios.

```bash
touch mysuperduperfile
```

E pronto, novo arquivo!

O `touch` também é usado para alterar os carimbos de data/hora em arquivos e diretórios existentes. Experimente: faça um `ls -l` em um arquivo e anote o carimbo de data/hora, então use `touch` nesse arquivo, e ele atualizará o carimbo de data/hora.

Existem muitas outras maneiras de criar arquivos que envolvem outras coisas como redirecionamento e editores de texto, mas abordaremos isso no curso de Manipulação de Texto.

## Exercise

1. Crie um novo arquivo.
2. Anote o carimbo de data/hora.
3. Use `touch` no arquivo e verifique o carimbo de data/hora novamente.

Para prática adicional com gerenciamento de arquivos, explore estes laboratórios interativos:

- [Linux Directory Navigation](https://labex.io/pt/labs/linux-directory-navigation-387844)
- [Setting Up a New Project Structure](https://labex.io/pt/labs/linux-setting-up-a-new-project-structure-387859)

## Quiz Question

Como você cria um arquivo chamado `myfile`?

## Quiz Answer

touch myfile
