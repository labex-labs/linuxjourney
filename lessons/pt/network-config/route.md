---
index: 2
lang: "pt"
title: "Rota"
meta_title: "Rota - Configuração de Rede"
meta_description: "Aprenda a gerenciar sua tabela de roteamento Linux. Este guia aborda como adicionar e excluir rotas de rede usando o comando moderno 'ip route' e o comando legado 'route'."
meta_keywords: "comando ip route no linux, comando ip route linux, adicionar rota, excluir rota, tabela de roteamento, roteamento de rede, rede linux, ip route"
---

## Lesson Content

No Linux, a tabela de roteamento direciona o tráfego de rede para seu destino correto. Embora tenhamos discutido anteriormente como visualizar esta tabela, você também pode adicionar ou remover rotas manualmente para controlar como os pacotes de dados são encaminhados. Isso é essencial para configurar configurações de rede complexas ou solucionar problemas de conectividade.

### Usando o Comando Legacy route

O comando `route` é uma ferramenta tradicional para gerenciar a tabela de roteamento. Embora ainda funcional, é considerado legado, e o comando `ip` é agora o preferido.

Para adicionar uma nova rota de rede, você especifica o endereço da rede, a máscara de sub-rede e o gateway (`gw`):

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

Para excluir uma rota, use o sinalizador `del` com o endereço da rede:

```bash
sudo route del -net 192.168.2.1/23
```

### Gerenciamento Moderno de Rotas com ip route

O comando `ip route` é a ferramenta moderna e mais poderosa para configuração de rede no Linux. Ele oferece um conjunto mais consistente e extenso de opções para gerenciar interfaces de rede e rotas. Usar o **comando ip route do linux** é a prática recomendada para sistemas atuais.

Para adicionar uma rota com o **comando ip route no linux**, você usa a ação `add`, especificando a rede de destino e o próximo salto (next hop) através do gateway:

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

Para excluir uma rota, você pode usar a ação `delete`. Você pode especificar a rota completa ou apenas a rede de destino, se ela for única:

```bash
# Excluir especificando a rota completa
ip route delete 192.168.2.1/23 via 10.11.12.3

# Ou, excluir especificando apenas o destino
ip route delete 192.168.2.1/23
```

Dominar o comando `ip route` é uma habilidade fundamental para qualquer administrador Linux responsável pelo gerenciamento de rede.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de roteamento de rede e endereçamento IP:

1.  **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Pratique a configuração de um IP estático, a definição de um gateway padrão e a verificação da configuração de rede usando o comando `ip`.
2.  **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como o gateway padrão lida com o tráfego remoto e observe as interações da camada de rede.

Esses laboratórios ajudarão você a aplicar os conceitos de endereçamento IP e roteamento em cenários reais e a construir confiança com a rede Linux.

## Quiz Question

Ao usar o comando legado `route`, qual é o sinalizador usado para excluir uma rota? Por favor, responda em inglês, prestando atenção às maiúsculas e minúsculas.

## Quiz Answer

del
