# codingchaos-scoreboard

Das Live-Scoringboard für den Programmierwettberwerb des Chaostreff
Osnabrücks.

## Config

In der Config-Datei wird das Master-Repository und Zugangsdaten angegeben. Hier
werden alle Einstellungen vorgenommen, damit das Projekt funktionieren kann.

## Aussehen

| Aufgaben  | 1   | 2   | 3   | 4   |
|-----------|-----|-----|-----|-----|
| Spieler 1 | ()  | (d) | (a) | ()  |
| Spieler 2 | (d) | (s) | (a) | (a) |
| Spieler 3 | ()  | (a) | (s) | ()  |

Es werden alle Forks zu dem Main-Repository gesucht und "analysiert". Die
Ergebnisse der Analyse werden dann in der Tabelle dargestellt. Analysiert
heißt in dem Fall, dass jeder Aufgabenordner Standardmäßig die Datei 
"NOTYETSTARTED" enthält. Wenn diese Datei in dem Aufgabenordner gefunden wird,
wird ein "()" (Oder Grafik) angezeigt. Wenn der Teilnehmer die Datei löscht,
ändert sich die Anzeige zu einem "(s)" (Oder Grafik). Wenn der Teilnehmer
fertig mit der Aufgabe ist, erstellt er die datei "DONE" direkt im 
Aufabenordner und die Anzeige ändert sich auf "(d)" (Oder Grafik). Wenn
der Teilnehme eine Aufgabe abbrechen möchte, dann erstellt er die Datei
"WHITEFLAG" in seinem Ordner und es wird ein "(a)" (Oder Grafik).
