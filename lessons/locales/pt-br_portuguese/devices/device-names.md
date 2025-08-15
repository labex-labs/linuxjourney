# Nomes de dispositivos

## Conteúdo da lição

Aqui estão os nomes de dispositivos mais comuns que você encontrará:

<b> Dispositivos SCSI </ b>

Se você tem algum tipo de armazenamento em massa em sua máquina, é provável que esteja usando o protocolo SCSI (pronuncia-se "scâzy"). SCSI significa Small Computer System Interface(Pequena interface de sistema de computador), é um protocolo usado para permitir a comunicação entre discos, impressoras, scanners e outros periféricos em seu sistema. Você pode ter ouvido falar de dispositivos SCSI que não estão realmente em uso em sistemas modernos, no entanto, nossos sistemas Linux correspondem a discos SCSI com unidades de disco rígido em / dev. Eles são representados por um prefixo de sd (disco SCSI):

Arquivos de dispositivos SCSI comuns:

<ul>
<li> / dev / sda - Primeiro disco rígido </ li>
<li> / dev / sdb - Segundo disco rígido </ li>
<li> / dev / sda3 - Terceira partição no primeiro disco rígido </ li>
</ ul>

<b> Pseudo Dispositivos </ b>

Como discutimos anteriormente, os pseudo-dispositivos não estão fisicamente conectados ao seu sistema, os pseudo-dispositivos mais comuns são dispositivos de caractere:

<ul>
<li> / dev / zero - aceita e descarta todas as entradas, produz um fluxo contínuo de bytes NULL (valor zero) </ li>
<li> / dev / null - aceita e descarta todas as entradas, não produz saída </ li>
<li> / dev / random - produz números aleatórios </ li>
</ ul>

<b> Dispositivos PATA </ b>

Às vezes, em sistemas mais antigos, você pode ver discos rígidos sendo referidos com um prefixo hd:

<ul>
<li> / dev / hda - Primeiro disco rígido </ li>
<li> / dev / hdd2 - Segunda partição no 4º disco rígido </ li>
</ ul>

## Exercício

Escreva nos pseudo dispositivos e veja o que acontece, tenha cuidado para não gravar seus discos nesses dispositivos!

## Questionário

Qual seria normalmente o nome do dispositivo para a primeira partição no segundo disco SCSI?

## Resposta do questionário

sdb1