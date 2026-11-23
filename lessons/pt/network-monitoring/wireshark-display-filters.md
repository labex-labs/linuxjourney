---
lesson_id: "wireshark-display-filters"
course_id: "network-monitoring"
lang: "pt"
order_index: 4
title: "Filtros de exibição do Wireshark"
description: "Aprenda a limitar a visualização de uma captura preparada com um filtro de exibição do Wireshark."
meta_title: "Filtros de exibição do Wireshark - Monitoramento de redes"
meta_description: "Aprenda a limitar a visualização de uma captura preparada com um filtro de exibição do Wireshark."
meta_keywords: "filtros de exibição do Wireshark, captura de pacotes, monitoramento de redes, cibersegurança, Linux Journey"
---

Uma captura de pacotes pode incluir vários protocolos. Um **filtro de exibição** informa ao Wireshark quais pacotes salvos deve exibir. Ele muda o que aparece na tela e mantém o arquivo de captura intacto.

## Selecionando um protocolo

Abra a página da [captura de exemplo](https://github.com/labex-labs/linuxjourney/blob/master/examples/network-monitoring/sample.pcap) no GitHub e salve o arquivo como `sample.pcap`. Abra o arquivo no Wireshark e digite `dns` no campo de filtro de exibição. Em um terminal Linux com o TShark instalado, o comando abaixo aplica o mesmo filtro ao arquivo salvo. O arquivo contém uma consulta inofensiva e outro tráfego de exemplo.

```bash
$ tshark -r sample.pcap -Y dns
```

A opção `-r` lê um arquivo e `-Y` aplica um filtro de exibição. Procure uma consulta e sua resposta.

:::single-choice{#wireshark-display-filters-display-effect} A lista filtrada exibe duas linhas a menos que a visualização original. O que aconteceu com os outros pacotes?

::option[Foram excluídos do arquivo de captura.]{#wireshark-display-filters-display-effect-a explanation="Um filtro de exibição muda os resultados visíveis."}
::option[Continuam salvos e ficaram fora da visualização porque não correspondem ao filtro.]{#wireshark-display-filters-display-effect-b .correct explanation="Limpe o filtro para voltar à visualização completa."}
::option[Foram enviados novamente pela rede.]{#wireshark-display-filters-display-effect-c explanation="Ler uma captura salva não transmite seus pacotes."}
:::

## Filtrando por endereço

Um filtro também pode usar um campo do pacote. `ip.addr` verifica se um endereço IPv4 corresponde à origem ou ao destino. Os dois sinais de igual comparam o campo com o valor do exemplo.

```bash
$ tshark -r sample.pcap -Y 'ip.addr == 192.0.2.10'
```

As aspas do shell mantêm a expressão inteira em um só argumento. Você pode identificar os endpoints nas linhas exibidas.

:::single-choice{#wireshark-display-filters-address-scope} Um pacote segue de outro endereço para 192.0.2.10. Ele corresponde ao filtro?

::option[Sim, porque basta o endereço aparecer como origem ou destino.]{#wireshark-display-filters-address-scope-a .correct explanation="O campo ip.addr pode corresponder à origem ou ao destino."}
::option[Não, porque a condição verifica apenas a origem.]{#wireshark-display-filters-address-scope-b explanation="Esse campo pode corresponder aos dois sentidos."}
::option[Somente se o pacote contiver DNS.]{#wireshark-display-filters-address-scope-c explanation="Essa expressão verifica apenas o endereço IPv4."}
:::

![Saída do TShark comparando a exibição apenas de DNS com a dos dois protocolos da captura de prática](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/network-monitoring/wireshark-display-filters/saved-dns-exchange.png)

## Interpretando uma exibição vazia

Um resultado vazio indica que o filtro não encontrou pacotes correspondentes no arquivo consultado. Confira a expressão, o horário e o ponto de captura antes de fazer uma afirmação mais ampla. Comece limpando o filtro para confirmar que há tráfego na captura.

:::single-choice{#wireshark-display-filters-empty-capture-view} Você aplica dns a uma captura salva e não vê nenhuma linha. O que pode relatar?

::option[Ninguém usou DNS em nenhum ponto da rede.]{#wireshark-display-filters-empty-capture-view-a explanation="Um arquivo cobre apenas um ponto de captura e um intervalo limitados."}
::option[O Wireshark apagou as evidências de DNS.]{#wireshark-display-filters-empty-capture-view-b explanation="O filtro de exibição não exclui pacotes salvos."}
::option[O filtro não exibiu pacotes DNS nessa captura.]{#wireshark-display-filters-empty-capture-view-c .correct explanation="A afirmação se limita às evidências examinadas."}
:::

Para examinar outra captura em um laboratório no navegador, experimente o exercício sobre filtros de exibição em [Wireshark para iniciantes](https://labex.io/courses/quick-start-with-wireshark).

## Resumo

Agora você consegue filtrar uma captura de pacotes salva e explicar o alcance do resultado.

1. Selecione um protocolo com um filtro de exibição.
2. Filtre os pacotes por endereço com ip.addr.
3. Interprete a exibição filtrada considerando os limites de visibilidade do arquivo.
