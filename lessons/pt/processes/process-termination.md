---
index: 5
lang: "pt"
title: "Terminação de Processos"
meta_title: "Terminação de Processos - Processos"
meta_description: "Explore a terminação de processos no Linux, a chamada de sistema wait e as principais diferenças no debate sobre processos zumbis vs. órfãos. Aprenda a gerenciar e matar processos filhos no Linux para um sistema estável."
meta_keywords: "Terminação de processos Linux, processo zumbi, processo órfão, zumbi vs órfão, matar processo filho Linux, chamada de sistema wait, _exit, gerenciamento de processos"
---

## Lesson Content

### O Processo de Terminação

Uma vez que um processo é criado, como ele termina? A terminação de um processo é uma parte crítica do ciclo de vida do processo, garantindo que os recursos do sistema sejam gerenciados de forma eficaz.

Um processo tipicamente termina chamando a chamada de sistema `_exit`. Esta ação sinaliza ao kernel que o processo terminou e que seus recursos, como memória e descritores de arquivo, podem ser recuperados. Ao sair, o processo fornece um status de terminação ao kernel, que é um valor inteiro. Por convenção, um status de 0 indica execução bem-sucedida, enquanto um valor diferente de zero sinaliza um erro.

No entanto, chamar `_exit` não apaga imediatamente o processo. O processo pai deve reconhecer a terminação de seu filho usando a chamada de sistema `wait`. Esta chamada permite que o pai recupere o status de terminação do filho. Este mecanismo de duas etapas é essencial para a limpeza adequada do processo. Outra forma de `linux kill child process` (matar processo filho no linux) é usando sinais, um tópico que exploraremos em uma lição posterior.

### Processos Órfãos

O que acontece se um processo pai terminar antes de seu filho? O processo filho se torna um "órfão". Como seu pai original não pode mais chamar `wait`, o kernel intervém. O processo órfão é imediatamente adotado por um processo especial do sistema, tipicamente `init` (ID de processo 1), que é considerado o ancestral de todos os processos. O processo `init` então assume o papel de pai, chamando periodicamente `wait` para coletar o status de terminação de qualquer um de seus filhos adotados, permitindo que eles terminem de forma limpa.

### Processos Zumbis

Um cenário diferente ocorre quando um processo filho termina, mas seu pai ainda não chamou `wait`. Nesse estado, o filho se torna um processo "zumbi". O kernel libera a maioria dos recursos do zumbi, mas mantém uma entrada na tabela de processos. Essa entrada contém o ID do processo e o status de terminação, esperando que o pai o colete.

Processos zumbis já estão mortos, portanto, não consomem tempo de CPU. Você não pode matá-los com sinais porque eles não estão em execução. O processo de o pai chamar `wait` para limpar um zumbi é chamado de "reaping" (colheita). Se o processo pai nunca chamar `wait`, esses zumbis podem se acumular. Embora alguns sejam inofensivos, um grande número pode preencher a tabela de processos, impedindo a criação de novos processos. Nos casos em que o processo pai também termina, `init` adotará e colherá o zumbi.

### Processo Zumbi vs Órfão

Entender a diferença entre um `zombie vs orphan process` (processo zumbi vs órfão) é fundamental para diagnosticar problemas relacionados a processos.

- Um **processo órfão** é um processo ativo e em execução cujo pai morreu. Ele é adotado por `init` e continua a ser executado até terminar.
- Um **processo zumbi** é um processo morto que concluiu sua execução, mas ainda possui uma entrada na tabela de processos. Ele está esperando que seu processo pai leia seu status de saída.

Em resumo, um órfão está vivo, mas sem pai, enquanto um zumbi está morto, mas ainda não foi totalmente colhido por seu pai.

## Exercise

Para aplicar esses conceitos, tente o seguinte laboratório prático:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro plano e em segundo plano, inspecionando-os com `ps`, monitorando recursos com `top`, ajustando a prioridade com `renice` e terminando-os com `kill`. Este laboratório oferece experiência prática com o ciclo de vida do processo, incluindo como terminá-los e observar seus estados.

## Quiz Question

Qual é o status de terminação mais comum para um processo que obteve sucesso?

## Quiz Answer

0
