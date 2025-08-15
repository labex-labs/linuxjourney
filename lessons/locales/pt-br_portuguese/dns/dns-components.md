# Componentes de DNS

## Conteúdo da lição

O banco de dados DNS da Internet depende de sites e organizações que fornecem parte desse banco de dados. Para isso, eles precisam:

<b> Servidor de nomes </ b>

Nós configuramos o DNS através de "servidores de nomes", os servidores de nome carregam nossas configurações de DNS e configurações e respondem a quaisquer perguntas de clientes ou outros servidores que querem saber coisas como "Quem é google.com?". Se o servidor de nomes não souber a resposta para essa consulta, ele redirecionará a solicitação para outros servidores de nomes. Servidores de nomes podem ser "autoritativos", o que significa que eles armazenam os registros DNS que você está procurando, ou "recursivos", o que significa que perguntariam a outros servidores e os servidores perguntariam a outros servidores até encontrarem um servidor autoritativo contendo os registros DNS . Servidores recursivos também podem ter as informações que queremos armazenadas em cache, em vez de atingir um servidor autoritativo.

<b> Arquivo de Zona </ b>

Dentro de um servidor de nomes vive algo chamado arquivos de zona. Arquivos de zona são como o servidor de nomes armazena informações sobre o domínio ou como chegar ao domínio se ele não souber.

<b> Registros de recursos </ b>

Um arquivo de zona é composto de entradas de registros de recursos. Cada linha é um registro e contém informações sobre hosts, servidores de nomes, outros recursos, etc. Os campos consistem no seguinte:

<ul>
<li> Nome do registro </ li>
<li> TTL - O tempo após o qual descartamos o registro e obtemos um novo, no DNS TTL é indicado por horário, portanto, os registros podem ter um TTL de uma hora. A razão pela qual fazemos isso é porque a Internet está em constante mudança, um minuto em que um host pode ser mapeado para o endereço IP X e, em seguida, pode estar no endereço IP Y </ li>
<li> Classe - O espaço para nome das informações de registro, mais comumente, é usado para Internet </ li>
<li> Tipo - Tipo de informação armazenada nos dados do registro. Nós não vamos entrar em tipos de registro, mas você provavelmente já viu os comuns como A para endereço, MX ou trocador de e-mail, etc. </ li>
<li> Dados - Esse campo pode conter um endereço IP se for um registro A ou algo diferente, dependendo do tipo de registro. </ li>
</ ul>
<pre>
patty em um 192.168.0.4
</ pre>

## Exercício

Nenhum exercício para esta lição.

## Questionário

Qual tipo de registro de recurso é usado para trocadores de mensagens?

## Resposta do questionário

MX
