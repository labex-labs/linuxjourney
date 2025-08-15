# diretório / dev

## Conteúdo da lição

Quando você conecta um dispositivo à sua máquina, geralmente ele precisa de um driver de dispositivo para funcionar corretamente. Você pode interagir com drivers de dispositivo por meio de arquivos de dispositivos ou nós de dispositivos, esses são arquivos especiais que se parecem com arquivos comuns. Como esses arquivos de dispositivos são exatamente como arquivos comuns, você pode usar programas como ls, cat, etc. para interagir com eles. Esses arquivos de dispositivos geralmente são armazenados no diretório / dev. Vá em frente e no diretório / dev do seu sistema, você verá uma grande quantidade de arquivos de dispositivos que estão no seu sistema.

<pre> $ ls / dev </ pre>

Alguns desses dispositivos que você já usou e interagiu, como / dev / null. Lembre-se de quando enviamos a saída para / dev / null, o kernel sabe que este dispositivo recebe todas as nossas entradas e apenas as descarta, então nada é retornado.

Antigamente, se você quisesse adicionar um dispositivo ao seu sistema, você adicionaria o arquivo do dispositivo em / dev e provavelmente o esqueceria. Bem, repita isso um par de vezes e você pode ver onde houve um problema. O diretório / dev ficaria cheio de arquivos de dispositivos estáticos de dispositivos que você já atualizou há muito tempo, parou de usar, etc. Os dispositivos também são designados a arquivos de dispositivos na ordem em que o kernel os encontra. Portanto, se toda vez que você reinicializar o sistema, os dispositivos poderão ter arquivos de dispositivo diferentes, dependendo de quando foram descobertos.

Felizmente não usamos mais esse método, agora temos algo que usamos para adicionar e remover dinamicamente dispositivos que estão sendo usados atualmente no sistema e discutiremos isso nas próximas lições.

## Exercício

Confira o conteúdo do diretório / dev, você reconhece algum dispositivo familiar?

## Questionário

Onde os arquivos do dispositivo são armazenados no sistema?

## Resposta do questionário

/ dev