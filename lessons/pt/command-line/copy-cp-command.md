---
index: 10
lang: "pt"
title: "cp (Copiar)"
meta_title: "cp (Copiar) - Linha de Comando"
meta_description: "Aprenda a usar o comando Linux cp para copiar arquivos e diretórios. Entenda opções como -r e curingas. Comece sua jornada Linux hoje!"
meta_keywords: "comando cp, copiar arquivos Linux, tutorial Linux, Linux para iniciantes, cp -r, curingas Linux, guia Linux"
---

## Lesson Content

Vamos começar a fazer algumas cópias desses arquivos. Assim como copiar e colar arquivos em outros sistemas operacionais, o shell nos oferece uma maneira ainda mais simples de fazer isso.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile` é o arquivo que você deseja copiar, e `/home/pete/Documents/cooldocs` é para onde você está copiando o arquivo.

Você pode copiar vários arquivos e diretórios, bem como usar curingas. Um curinga é um caractere que pode ser substituído por uma seleção baseada em padrão, dando-lhe mais flexibilidade nas buscas. Você pode usar curingas em todos os comandos para maior flexibilidade.

- `*` o curinga dos curingas, é usado para representar todos os caracteres únicos ou qualquer string.
- `?` usado para representar um caractere
- `[]` usado para representar qualquer caractere dentro dos colchetes

```bash
cp *.jpg /home/pete/Pictures
```

Isso copiará todos os arquivos com a extensão `.jpg` no seu diretório atual para o diretório `Pictures`.

Um comando útil é usar a flag `-r`; isso copiará recursivamente os arquivos e diretórios dentro de um diretório.

Tente fazer um `cp` em um diretório que contém alguns arquivos para o seu diretório `Documents`. Não funcionou, certo? Bem, isso porque você precisará copiar os arquivos e diretórios internos também com o comando `-r`.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

Uma coisa a notar, se você copiar um arquivo para um diretório que tem o mesmo nome de arquivo, o arquivo será sobrescrito com o que você está copiando. Isso não é bom se você tiver um arquivo que não deseja que seja sobrescrito acidentalmente. Você pode usar a flag `-i` (interativa) para ser solicitado antes de sobrescrever um arquivo.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

Copie alguns arquivos; tenha cuidado para não sobrescrever nada importante.

Para prática interativa com o comando `cp`, experimente este laboratório interativo:

- [Linux cp Command: File Copying](https://labex.io/pt/labs/linux-linux-cp-command-file-copying-209744)

## Quiz Question

Qual flag você precisa especificar para copiar um diretório?

## Quiz Answer

-r
