# Ferramentas DNS

## Conteúdo da lição

<b> nslookup </ b>

A ferramenta "lookup do servidor de nomes" é usada para consultar servidores de nomes para localizar informações sobre registros de recursos. Vamos encontrar onde o servidor de nomes do google.com é:

<pre>
pete @ icebox: ~ $ nslookup www.google.com
Servidor: 127.0.1.1
Endereço: 127.0.1.1 # 53

Resposta não autoritativa:
Nome: www.google.com.br
Endereço: 216.58.192.4
</pre>

<b> dig </ b>

O Dig (domain information groper) é uma ferramenta poderosa para obter informações sobre servidores de nomes DNS, é mais flexível do que o nslookup e ótimo para solucionar problemas de DNS.


<pre>
pete @ icebox: ~ $ dig www.google.com

; << >> DiG 9.9.5-3-Ubuntu << >> www.google.com.br
;; opções globais: + cmd
;; Resposta obtida:
;; - >> HEADER << - opcode: QUERY, status: NOERROR, id: 42376
;; sinalizadores: qr rd ra; CONSULTA: 1, RESPOSTA: 5, AUTORIDADE: 0, ADICIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: versão: 0, sinalizadores :; MBZ: 0005, udp: 512
;; SEÇÃO DE PERGUNTA:
www.google.com. EM UM

;; SEÇÃO DE RESPOSTA:
www.google.com. 5 EM UM 74.125.239.147
www.google.com. 5 EM A 74.125.239.144
www.google.com. 5 EM A 74.125.239.146
www.google.com. 5 EM UM 74.125.239.145
www.google.com. 5 EM A 74.125.239.148

;; Tempo de consulta: 27 ms
;; SERVIDOR: 127.0.1.1 # 53 (127.0.1.1)
;; QUANDO: Dom 07 de fevereiro 10:14:00 PST 2016
;; TAMANHO DO MSG rcvd: 123
</pre>

## Exercício

Leia sobre dig na manpage.

## Questionário

Qual ferramenta é usada para obter informações detalhadas sobre servidores de nomes DNS?

## Resposta do questionário

dig