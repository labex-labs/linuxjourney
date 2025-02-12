# syslog

## Tunni sisu

Syslog teenus haldab ja saadab logisid süsteemi logijale. *Rsyslog* on *syslog*'i edasiarendatud versioon, mida peaksid kasutama enamik Linux'i väljalaskeid. Kõikide *syslog*'i teenuste poolt kogutud logide väljundit võib näha failis */var/log/syslog* (kõik teated peale *auth* teadete).

Et tuvastada, milliseid faile süsteemi logija haldab, võib vaadata sätete faile */etc/rsyslog.d/* kataloogis:

<pre>
pete@icebox:~$ less /etc/rsyslog.d/50-default.conf 
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log
</pre>

Logifailide reeglid on ära toodud vasakus tulbas ja tegevused paremas. Parem tulp ütleb, kuhu tuleb saata logi informatsioon (faili, konsooli või kuhugi mujale). Meenutame, et mitte kõik rakendused ja teenused ei kasuta *rsyslog*'i enda logide haldamiseks mistõttu peab vaatama just sellesse kataloogi, kui on soov teada saada täpselt mida logitakse.

Vaatame logimist tegevuses. Käsitsi saab logi saata *logger* käsuga:

<pre>
logger -s Hello
</pre>

Kui nüüd vaadata faili */var/log/syslog*, võib seda kannet logis näha.

## Harjutus

Vaadata */etc/rsyslog.d/* kaustas sätete faile ja tuvastada mida veel süsteemi logijaga logitase.

## Küsimus

Millise käsuga saab teate logida käsitsi?

## Vastus

*logger*
