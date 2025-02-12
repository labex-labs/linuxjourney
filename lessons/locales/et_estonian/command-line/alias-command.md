# alias

## Tunni sisu

Mõnikord võib muutuda käskude sisestamine sageli korduvaks või on vaja kirjutada väga pikka käsku mitu korda. Sellisel juhul oleks parem kasutada aliast. Käsule aliase loomiseks peab lihtsalt täpsustama aliase nime ja seostama selle käsuga.

<pre>$ alias foobar='ls -la'</pre>

Nüüd võid ls -ls asemel kirjutada foobar ja see käivitab ülakomade vahel oleva käsu või käskude jada. See on kiire ja mugav. Tuleb aga meeles pidada, et aliased ei säili kui peab arvuti taaskäivitama. Selleks peab looma püsivad aliased:

<pre>~/.bashrc</pre>

või mõnda teise sarnasesse faili kui soovitakse, et see säiliks ka pärast taaskäivitamist. Tavaliselt on ~/.bashrc failis olemas juba mõned aliased:
<pre>
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
</pre>

Tavaliselt on failis ~/.bashrc read:
<pre>
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
</pre>

Seega on mõistlikum kasutaja aliased kirjutada eraldi faili ~/.bash_aliases
Kui see fail kopeerida ka /etc/skel/ kataloogi siis on ka kõikidel uutel või esimest korda sisse logivatel domeenikasutajatel sama aliaste fail olemas.

Aliase saab eemaldada unalias käsuga:

<pre>$ unalias foobar</pre>

Lisainfot aliaste kohta<br />
<a href="https://viki.pingviin.org/Alias" target="_blank">Pingviini viki artikkel</a><br />
<a href="https://wiki.itcollege.ee/index.php/Alias_bash_shellis" target="_blank">IT Kolledži viki artikkel</a>

## Harjutus

Luua mõned aliased ja eemalda need.

## Küsimus

Millise käsuga luuakse alias?

## Vastus

alias
