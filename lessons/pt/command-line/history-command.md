---
index: 9
lang: "pt"
title: "histórico"
meta_title: "histórico - Linha de Comando"
meta_description: "Domine o comando history no Linux para relembrar e gerenciar eficientemente sua atividade na linha de comando. Aprenda a visualizar o histórico, usar atalhos como Ctrl-R e gerenciar seu histórico com opções como history -c e history -d."
meta_keywords: "history no linux, history -c linux, history -d linux, history -w linux, comando history unix, histórico bash, linha de comando, Ctrl-R, limpar comando"
---

## Lesson Content

Seu shell mantém um registro dos comandos que você inseriu anteriormente. Você pode acessar esta lista, que é incrivelmente útil quando você deseja encontrar e reutilizar um comando sem digitá-lo novamente. O comando `history` é uma ferramenta fundamental na maioria dos ambientes Unix e Linux.

### Visualizando Seu Histórico de Comandos

Para ver a lista de comandos que você usou, simplesmente digite o comando `history`. Este recurso fornece um log detalhado de sua atividade, facilitando o rastreamento do seu `history in linux`.

```bash
history
```

### Reexecutando Comandos Anteriores

O shell fornece vários atalhos para facilitar a reexecução de comandos.

- **Seta Para Cima**: Quer executar o mesmo comando que acabou de fazer? Basta pressionar a tecla de seta para cima para percorrer o histórico para trás.
- **O Atalho `!!`**: Para executar o comando mais recente novamente, você pode usar `!!`. Por exemplo, se você acabou de executar `cat file1`, digitar `!!` e pressionar Enter executará `cat file1` novamente.

### Pesquisando Seu Histórico

Um dos atalhos de histórico mais poderosos é `Ctrl-R`. Isso inicia uma pesquisa reversa. Depois de pressionar `Ctrl-R`, comece a digitar qualquer parte do comando que você está procurando, e o shell exibirá a correspondência mais recente. Você pode pressionar `Ctrl-R` repetidamente para percorrer correspondências mais antigas. Depois de encontrar o comando desejado, basta pressionar Enter para executá-lo.

### Gerenciando a Lista de Histórico

Além de apenas visualizar seu histórico, você também pode gerenciá-lo diretamente.

- **Limpar Histórico**: Se você deseja limpar o histórico de comandos para sua sessão atual, pode usar o comando `history -c linux`. Isso remove todas as entradas da lista de histórico na memória.
- **Gravar no Arquivo**: Para salvar o histórico da sessão atual em seu arquivo de histórico (geralmente `~/.bash_history`), você pode usar `history -w linux`. Isso é útil para preservar comandos antes de fechar uma sessão.
- **Excluir uma Entrada Específica**: Você pode remover um único comando do seu histórico usando `history -d <offset>`. O deslocamento é o número mostrado ao lado do comando na saída do `history`. Por exemplo, `history -d 101` excluiria a 101ª entrada. Esta é uma função chave do `history -d linux`.

### Outras Ferramentas de Terminal Úteis

À medida que sua janela do terminal fica cheia, você pode querer limpá-la. Use o comando `clear` para apagar sua tela e começar com uma tela limpa.

```bash
clear
```

Outro recurso indispensável é o preenchimento automático com tabulação. Se você começar a digitar o início de um comando, nome de arquivo ou diretório e pressionar a tecla Tab, o shell tentará autocompletá-lo. Se houver várias possibilidades, ele poderá mostrar as opções ou não fazer nada. Pressionar Tab uma segunda vez geralmente listará todas as possíveis conclusões.

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Caminho de Aprendizagem do Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual é o comando para limpar o terminal? (Por favor, responda apenas com letras minúsculas em inglês)

## Quiz Answer

clear
