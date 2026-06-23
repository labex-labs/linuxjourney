---
index: 17
lang: "pt"
title: "whatis"
meta_title: "whatis - Linha de Comando"
meta_description: "Aprenda o comando Linux whatis com exemplos para obter descrições de comandos em uma linha a partir das páginas man e entender múltiplas seções do manual."
meta_keywords: "comando whatis, linux whatis, descrição de comando linux, resumo página man, ajuda linha de comando, apropos"
---

## Lesson Content

Ao explorar a linha de comando do Linux, você encontrará uma grande quantidade de comandos. É natural esquecer o que um comando específico faz. Felizmente, existe uma utilidade simples para ajudar você.

### O que é o comando whatis

O comando `whatis` exibe uma descrição concisa, em uma linha, de um comando diretamente da sua página de manual. É uma forma rápida de lembrar a função principal de um comando sem precisar ler toda a página man.

### Como usar o comando whatis

Usar o `whatis` é simples. Digite `whatis` seguido do comando sobre o qual você quer saber.

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

### Entendendo a saída

A descrição fornecida pelo `whatis` vem da seção `NAME` da página de manual do comando. Se um nome tiver múltiplas páginas man em seções diferentes, o `whatis` pode exibir mais de uma linha.

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

O número entre parênteses é a seção da página man.

### Whatis vs Man vs Apropos

- `whatis ls`: Mostra uma descrição em uma linha para um nome exato de comando.
- `man ls`: Abre a página de manual completa.
- `apropos palavra-chave`: Pesquisa descrições das páginas man por uma palavra-chave.

Por exemplo:

```bash
$ apropos password
```

Use `whatis` quando você souber o nome do comando, mas esqueceu o que ele faz.

### Perguntas Comuns

**Por que o whatis diz "nothing appropriate"?** O comando pode não ter uma página man instalada, ou o banco de dados do man pode precisar ser atualizado.

**O whatis mostra opções do comando?** Não. Use `man COMANDO` ou `COMANDO --help` para opções.

**O whatis é igual ao which?** Não. `whatis` descreve um comando. `which` mostra o caminho do executável.

## Exercise

A prática leva à perfeição! Embora não exista um laboratório específico para o comando `whatis`, entender como encontrar informações sobre comandos e arquivos é crucial. Aqui estão alguns laboratórios práticos para reforçar seu entendimento sobre localização de comandos e arquivos no Linux:

1. **[Comando Linux which: Localizando Comandos](https://labex.io/pt/labs/linux-linux-which-command-command-locating-215210)** - Pratique o uso do comando `which` para localizar arquivos executáveis e entender a prioridade dos comandos no PATH do seu sistema.
2. **[Comando Linux whereis: Encontrando Arquivos e Comandos](https://labex.io/pt/labs/linux-linux-whereis-command-file-and-command-finding-215211)** - Aprenda a usar o `whereis` para encontrar o binário, código-fonte e páginas de manual dos comandos, aprofundando seu entendimento sobre a estrutura dos comandos.
3. **[Descubra Recursos Críticos do Sistema](https://labex.io/pt/labs/linux-discover-critical-system-resources-388032)** - Este desafio combina `which`, `whereis` e `find` para ajudar você a navegar eficientemente pelo sistema de arquivos e descobrir recursos importantes do sistema.

Esses laboratórios ajudarão você a aplicar os conceitos de descoberta de comandos e arquivos em cenários reais e a ganhar confiança com utilitários essenciais do Linux.

## Quiz Question

Qual comando você pode usar para ver uma pequena descrição de um comando? Por favor, responda em inglês, prestando atenção às letras minúsculas.

## Quiz Answer

whatis
