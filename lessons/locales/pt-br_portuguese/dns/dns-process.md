# Processo DNS

## Conteúdo da lição

Vejamos um exemplo de como seu host encontra um domínio (catzontheinterwebz.com) com o DNS. Essencialmente, nos canalizamos até chegarmos ao servidor DNS que conhece esse domínio.

<b> Servidor DNS local </ b>

Primeiro, o nosso anfitrião pergunta: "Onde está o catzontheinterwebz.com?", O nosso servidor DNS local não sabe e começa da parte superior do funil para perguntar aos Servidores-Raiz. Tenha em mente que nosso host não está fazendo essas solicitações para localizar catzontheinterwebz.com diretamente, a maioria dos usuários fala com um servidor DNS recursivo fornecido por seus ISPs e esse servidor é então encarregado de encontrar o local de catzontheinterwebz.com.

<b> Servidores Raiz </ b>

Existem 13 Servidores Raiz para a Internet, eles são espelhados e distribuídos ao redor do mundo para lidar com solicitações de DNS para a Internet, então existem realmente centenas de servidores que estão funcionando, eles são controlados por diferentes organizações e contêm informações sobre o nível superior. Domínios Domínios de nível superior são o que você conhece como endereços .org, .com, .net, etc. Portanto, o Servidor Raiz não sabe onde está o catzontheinterwebz.com, portanto, ele nos pede para perguntar ao Servidor DNS de Domínio de Nível Superior .com em um endereço IP que ele nos fornece.

<b> Domínio de nível superior </ b>

Então agora nós enviamos outro pedido para o servidor de nomes que conhece os endereços ".com" e pergunta se ele sabe onde está o catzontheinterwebz.com? O TLD não tem o catzontheinterwebz.com em seus arquivos de zona, mas ele vê um registro para o servidor de nomes para catzontheinterwebz.com. Então, ele nos dá o endereço IP desse servidor de nomes e nos diz para procurar lá.

<b> Servidor DNS autoritativo </ b>

Agora enviamos uma solicitação final para o servidor DNS que realmente tem o registro que queremos. O servidor de nomes vê que tem um arquivo de zona para catzontheinterwebz.com e há um registro de recurso para 'www' para este host. Em seguida, ele nos dá o endereço IP desse host e podemos finalmente ver alguns gatos na Internet.

## Exercício

Nenhum exercício para esta lição.

## Questionário

Qual é a abreviação para os servidores de nomes em que os endereços .com, .net, .org, etc são encontrados?

## Resposta do questionário

TLD