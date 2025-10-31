---
index: 2
lang: "pt"
title: "Tabela de Roteamento"
meta_title: "Tabela de Roteamento - Roteamento"
meta_description: "Um guia para entender a tabela de roteamento do Linux. Aprenda a interpretar a saída do comando route, incluindo destino, gateway, genmask e a interface eth0. Domine o básico da sua tabela de rotas Linux."
meta_keywords: "tabela de roteamento linux, tabela de rotas linux, genmask, eth0, comando route, roteamento de rede, roteamento IP, destino, gateway, máscara de sub-rede, redes linux"
---

## Lesson Content

A **tabela de roteamento do Linux** armazena as regras que determinam para onde os pacotes de rede são enviados. Toda vez que seu sistema precisa enviar um pacote para um endereço IP, ele consulta esta tabela para encontrar o caminho apropriado. Para visualizar a **tabela de roteamento do Linux** da sua máquina, você pode usar o comando `route`.

```plaintext
pete@icebox:~$ sudo route -n
Tabela de roteamento IP do Kernel
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Entendendo as Colunas

A saída do comando `route` é organizada em várias colunas, cada uma fornecendo informações específicas sobre uma rota de rede.

### Destination (Destino)

A coluna Destination especifica uma rede ou um host. A entrada `192.168.224.0` direciona todos os pacotes destinados a essa rede específica. Se o destino de um pacote estiver dentro desta rede (por exemplo, de 192.168.224.5 para 192.168.224.7), ele é enviado diretamente através da interface especificada, como `eth0`.

A destinação `0.0.0.0` é a rota padrão. Se a tabela de roteamento não tiver uma entrada mais específica para o destino de um pacote, ela usará esta rota.

### Gateway

A coluna Gateway mostra o roteador para o qual os pacotes são enviados. Se um pacote não estiver na mesma rede local, ele é encaminhado para este endereço de gateway. Para a rota padrão, este é o endereço IP do roteador que conecta sua rede local a outras redes, como a internet.

### Genmask

A `genmask`, ou máscara de geração, é a máscara de sub-rede para a rede de destino. Ela é usada com o IP de destino para determinar se um pacote pertence a essa rede. Por exemplo, uma `genmask` de `255.255.255.0` significa que os primeiros três octetos do endereço IP devem corresponder aos primeiros três octetos do destino.

### Flags (Sinalizadores)

Estes sinalizadores fornecem informações adicionais sobre a rota:

- **U**: Indica que a rota está ativa e em funcionamento.
- **G**: Significa que a rota é para um gateway (roteador).
- **UG**: Significa que a rota está ativa e aponta para um gateway.

### Iface (Interface)

Esta coluna indica a interface de rede, como `eth0`, através da qual os pacotes para esta rota serão enviados. `eth0` geralmente representa o primeiro adaptador Ethernet no seu sistema.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de roteamento de rede e endereçamento IP:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços IP e interfaces de rede, que são componentes chave de uma tabela de roteamento.
2. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Aprenda a gerenciar endereçamento IP, configurar IPs estáticos, definir gateways padrão e verificar configurações de rede, relacionando-se diretamente com as entradas encontradas em uma tabela de roteamento.
3. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore o endereçamento IP e a acessibilidade de rede usando `ping` e `ip a`, ajudando você a entender como diferentes tipos de IP interagem e como a acessibilidade da rede é determinada, o que é refletido nas decisões de roteamento.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança com a configuração e solução de problemas de rede.

## Quiz Question

Se um destino não for encontrado na tabela de roteamento, para onde os pacotes são enviados? Por favor, responda com uma única palavra em inglês, prestando atenção à capitalização.

## Quiz Answer

Gateway
