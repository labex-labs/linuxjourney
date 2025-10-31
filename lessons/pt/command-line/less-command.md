---
index: 8
lang: "pt"
title: "less"
meta_title: "less - Linha de Comando"
meta_description: "Domine o comando less do Linux para visualização eficiente de arquivos de texto. Este guia aborda como usar o comando less, navegar, realizar uma pesquisa unix less e como sair do less."
meta_keywords: "comando less, less comando, sair less, pesquisa unix less, linux less, visualizar arquivos de texto, navegar arquivos, linha de comando linux"
---

## Lesson Content

Ao visualizar arquivos de texto que são grandes demais para caber em uma única tela, o `comando less` é uma ferramenta inestimável. Como diz o antigo ditado Unix, "less is more" (menos é mais). (Isso é um trocadilho com o fato de que também existe um comando `more` com funcionalidade semelhante). O utilitário `less` exibe o texto em um formato paginado, permitindo que você navegue por um arquivo página por página sem carregar o arquivo inteiro na memória.

### Primeiros Passos com o Comando Less

Para começar a visualizar um arquivo, simplesmente use o `comando less` seguido pelo nome do arquivo. Isso abrirá o arquivo na interface `less`.

```bash
less /home/pete/Documents/text1
```

Uma vez dentro do visualizador `less`, seus comandos de shell padrão não funcionarão. Em vez disso, você usa um conjunto específico de teclas para navegar e interagir com o texto.

### Navegação e Controles

Você pode usar várias teclas para se mover pelo documento:

- **Setas e Teclas de Página**: Use `Page Up`, `Page Down`, `Seta para Cima` e `Seta para Baixo` para navegar linha por linha ou página por página.
- **Ir para o Início**: Pressione `g` para mover diretamente para o início do arquivo de texto.
- **Ir para o Fim**: Pressione `G` (Shift + g) para saltar para o final do arquivo de texto.
- **Menu de Ajuda**: Se você esquecer os comandos dentro do `less`, basta pressionar `h` para exibir um resumo útil.

### Pesquisa Unix Less

Um recurso poderoso do `less` é sua capacidade de procurar texto. Para realizar uma `pesquisa unix less`, digite `/` seguido pelo texto que deseja encontrar e, em seguida, pressione Enter. Isso destacará todas as ocorrências do seu termo de pesquisa.

- `/termo_de_pesquisa`: Pesquisa para frente por "termo_de_pesquisa".
- `?termo_de_pesquisa`: Pesquisa para trás por "termo_de_pesquisa".
- `n`: Salta para a próxima ocorrência do termo de pesquisa.
- `N`: Salta para a ocorrência anterior.

### Como Sair do Less

Quando terminar de visualizar o arquivo, você precisa saber como `sair do less` e retornar ao seu prompt de comando.

- **Sair**: Simplesmente pressione `q` para fechar o visualizador `less` e voltar para o seu shell.

Dominar o `comando less` é uma habilidade fundamental para qualquer pessoa que trabalhe na linha de comando do Linux, tornando a inspeção de arquivos muito mais eficiente.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre visualização e navegação de arquivos de texto no Linux:

1. **[Comando Linux less: Paginação de Arquivos](https://labex.io/pt/labs/linux-linux-less-command-file-paging-214301)** - Aprenda o comando 'less' do Linux para visualização e navegação eficientes de arquivos de texto, incluindo pesquisa, números de linha e correspondência de padrões.
2. **[Comando Linux more: Rolagem de Arquivos](https://labex.io/pt/labs/linux-linux-more-command-file-scrolling-214299)** - Aprenda o comando 'more' do Linux para visualização eficiente de arquivos de texto, cobrindo uso básico, início a partir de linhas específicas e personalização da exibição.
3. **[Visualizando Arquivos de Log e Configuração no Linux](https://labex.io/pt/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Aprenda habilidades essenciais de linha de comando do Linux para visualizar e navegar eficientemente em arquivos de texto, incluindo logs do sistema e arquivos de configuração, usando comandos como `cat`, `more` e `less`.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança na manipulação e navegação de arquivos de texto.

## Quiz Question

Como você sai do comando `less`? Por favor, forneça a tecla de caractere único como sua resposta. Nota: a resposta é uma letra inglesa que diferencia maiúsculas de minúsculas.

## Quiz Answer

q
