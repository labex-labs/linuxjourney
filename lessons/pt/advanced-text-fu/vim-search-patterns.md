---
index: 4
lang: "pt"
title: "Padrões de Busca do Vim"
meta_title: "Padrões de Busca do Vim - Text-Fu Avançado"
meta_description: "Aprenda a realizar uma busca no Vim para frente e para trás usando padrões. Domine as técnicas de pesquisa do Vim para encontrar texto rapidamente e navegue pelos resultados com 'n' e 'N'."
meta_keywords: "Busca Vim, pesquisa Vim, comandos Vim, editor de texto Linux, tutorial Vim, guia Vim, padrões de busca"
---

## Lesson Content

A busca por texto é uma tarefa fundamental em qualquer editor. O Vim oferece maneiras poderosas e rápidas de realizar uma `busca no Vim` (vim search) diretamente do modo normal. Vamos explorar como usar esses padrões de busca para melhorar seu fluxo de trabalho.

### Busca para Frente

Para realizar uma `busca no Vim` (vim search) para frente padrão, basta pressionar a tecla `/` no modo normal, seguida pelo termo de busca. Ao pressionar Enter, o Vim saltará para a primeira ocorrência do termo após o cursor.

```plaintext
Meu arquivo bonito é muito bonito.

/bonito

Isso encontrará a primeira palavra "bonito" após o cursor.
```

### Busca para Trás

Da mesma forma, você pode buscar para trás a partir da posição do seu cursor. Use a tecla `?` seguida pelo termo de busca. O Vim encontrará a primeira ocorrência antes do seu cursor.

```plaintext
Meu arquivo bonito é muito bonito.

?bonito

Isso encontrará a última palavra "bonito" no arquivo primeiro.
```

### Navegando pelos Resultados da Busca

Uma vez iniciada uma busca, você pode navegar facilmente por todas as correspondências no arquivo.

- Pressione `n` para saltar para a **próxima** correspondência na direção da busca original.
- Pressione `N` para saltar para a correspondência **anterior**, movendo-se na direção oposta à busca original.

### Pesquisa Eficaz no Vim (Vim Lookup)

Os comandos `/` e `?` são o núcleo de qualquer operação de `pesquisa no Vim` (vim lookup). Se você precisa encontrar o nome de uma função específica, uma variável ou apenas uma palavra, este mecanismo de busca é sua principal ferramenta. Dominar este simples processo de `pesquisa no Vim` (vim lookup) é essencial para uma navegação e edição eficientes.

## Exercise

Para aplicar esses conceitos, tente o seguinte laboratório prático. Ele o ajudará a se tornar proficiente com ferramentas essenciais de edição de texto, incluindo funcionalidades de busca.

1. **[Edite Arquivos de Texto no Linux com Vim e Nano](https://labex.io/pt/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Pratique a criação, edição, salvamento e navegação de arquivos de texto com Vim e Nano.

## Quiz Question

Qual tecla é usada para iniciar uma busca para frente no Vim?

## Quiz Answer

/
