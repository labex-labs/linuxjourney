---
index: 8
lang: "pt"
title: "swap"
meta_title: "swap - O Sistema de Arquivos"
meta_description: "Aprenda sobre o espaço de swap do Linux, como funciona e como criar e gerenciar partições de swap. Otimize o uso da memória do seu sistema com este guia!"
meta_keywords: "Linux swap, mkswap, swapon, swapoff, /etc/fstab, memória virtual, Linux para iniciantes, tutorial de Linux"
---

## Lesson Content

No nosso exemplo anterior, mostrei como ver a sua tabela de partições. Vamos revisitar esse exemplo, mais especificamente esta linha:

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

O que é esta partição swap? Bem, swap é o que usamos para alocar memória virtual ao nosso sistema. Se você tem pouca memória, o sistema usa esta partição para "trocar" (swap) pedaços de memória de processos ociosos para o disco, para que você não fique sobrecarregado por falta de memória.

### Usando uma partição para espaço de swap

Digamos que queremos definir a nossa partição `/dev/sdb2` para ser usada como espaço de swap.

1. Primeiro, certifique-se de que não temos nada na partição.
2. Execute: `mkswap /dev/sdb2` para inicializar as áreas de swap.
3. Execute: `swapon /dev/sdb2`. Isso habilitará o dispositivo de swap.
4. Se você quiser que a partição de swap persista na inicialização, você precisa adicionar uma entrada ao arquivo `/etc/fstab`. `sw` é o tipo de sistema de arquivos que você usará.
5. Para remover o swap: `swapoff /dev/sdb2`.

Geralmente, você deve alocar cerca de duas vezes mais espaço de swap do que a memória que você tem. No entanto, os sistemas modernos de hoje são geralmente poderosos o suficiente e têm RAM suficiente como está.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do espaço de swap do Linux e do gerenciamento de memória virtual:

1. **[Criar e Ativar um Arquivo Swap no Linux](https://labex.io/pt/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Pratique a criação e ativação de um arquivo swap, uma habilidade crucial para gerenciar a memória virtual do seu sistema.

Este laboratório o ajudará a aplicar os conceitos de partições swap em cenários reais e a construir confiança no gerenciamento de recursos do sistema.

## Quiz Question

Qual é o comando para habilitar o espaço de swap em um dispositivo?

## Quiz Answer

swapon
