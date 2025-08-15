# / etc / hosts

## Conteúdo da lição

Antes que nossa máquina realmente atinja o DNS para fazer uma consulta, ela primeiro pesquisa localmente em nossas máquinas.

<b> / etc / hosts </ b>

O arquivo / etc / hosts contém mapeamentos de alguns nomes de hosts para endereços IP. Os campos são bastante auto-explicativos, existe um para o endereço IP, o nome do host e, em seguida, qualquer alias para o host.

<pre>
pete @ icebox: ~ $ cat / etc / hosts
127.0.0.1 localhost
127.0.1.1 icebox
</ pre>

Você normalmente verá seu endereço de host local listado por padrão neste arquivo. Você também pode gerenciar o acesso a hosts modificando os arquivos /etc/hosts.deny ou /etc/hosts.allow. No entanto, se você for conciente em relação à segurança, esse não é o caminho a seguir e, em vez disso, você deve modificar suas regras de firewall.

Vamos ver um bom exemplo de / etc / hosts. Modifique o arquivo e adicione uma linha para:

<pre>
123.45.6.7 www.google.com
</ pre>

Salve o arquivo e vá para www.google.com.br. Você está tendo problemas, não é mesmo? Bem, isso é porque acabamos de mapear www.google.com para um endereço IP completamente errado. Como os nossos anfitriões primeiro procuram localmente pelos mapeamentos de endereços IP, nunca chegam ao DNS para encontrar o google.com.

<b> /etc/resolv.conf </ b>

Tradicionalmente, usamos um arquivo chamado /etc/resolv.conf para mapear servidores de nomes DNS para pesquisas mais eficientes, no entanto, com as melhorias feitas no DNS, esse arquivo é muitas vezes irrelevante, de fato, você pode ver no meu exemplo abaixo O /etc/resolv.conf não é gerenciado manualmente. Consulte as configurações específicas da distribuição para gerenciar os mapeamentos do servidor de nomes DNS.

<pre>
conf (5) arquivo para glibc resolver (3) gerado pelo resolvconf (8)
# NÃO EDITAR ESTE ARQUIVO POR MÃO - SUAS MUDANÇAS SERÃO SUBSIDIADAS
servidor de nomes 127.0.1.1
pesquisar domínio local
</ pre>

## Exercício

Nenhum exercício para esta lição.

## Questionário

Qual arquivo é usado para mapear nomes de host para endereços IP em nossas máquinas?

## Resposta do questionário

/ etc / hosts