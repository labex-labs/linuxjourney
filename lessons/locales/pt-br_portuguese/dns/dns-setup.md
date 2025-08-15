# Configurações DNS

## Conteúdo da lição

Nós não passaremos pela configuração de um servidor DNS, pois isso seria um tutorial bastante longo. Em vez disso, aqui está uma lista de comparação rápida dos servidores DNS populares para usar com o Linux.

<b> BIND </ b>

O servidor DNS mais popular da Internet, é o padrão usado nas distribuições do Linux. Foi originalmente desenvolvido na Universidade da Califórnia em Berkeley, daí o nome BIND (Berkeley Internet Name Domain). Se você precisa de poder e flexibilidade com todos os recursos, não há como errar com o BIND.

<b> DNSmasq </ b>

Leve e muito mais fácil de configurar do que o BIND. Se você quer simplicidade e não precisa de todos os sinos e assobios do BIND, use o DNSmasq. Ele vem com todas as ferramentas que você precisa para configurar o DHCP e DNS, recomendado para uma rede menor.

<b> PowerDNS </ b>

Completo e semelhante ao BIND, oferece um pouco mais de flexibilidade com as opções. Ele lê informações de vários bancos de dados, como MySQL, PostgreSQL, etc., para facilitar a administração. Só porque o BIND tem sido o jeito que fazemos as coisas, isso não significa que ele precisa continuar assim.

Esta não é uma lista completa, mas deve dar uma idéia de onde procurar se você estiver configurando seu próprio servidor DNS.

## Exercício

Nenhum exercício para esta lição.

## Questionário

Qual é o servidor DNS de fato para o Linux?

## Resposta do questionário

BIND