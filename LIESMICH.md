# ProofYw7 (yWriter 7-Szenen mit LibreOffice korrekturlesen)

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw7/master/docs/Screenshots/screenshot1d.png)

## Voraussetzungen

* Windows.

* yWriter 7.

* Eine reguläre LibreOffice 5 oder 6-Installation (nicht "portable").

## Download

Die ProofYw7 Software kommt als ZIP-Archiv `ProofYw7_Versionsnummer.zip`. 

[Download-Seite](https://github.com/peter88213/ProofYw7/releases)

## ProofYw7 installieren

1. Falls Sie bereits eine Version von ProofYw7 installiert haben, führen Sie bitte das Deinstallationsprogramm dafür aus. 

2. Entpacken Sie das Archiv `ProofYw7_<Versionsnummer>.zip` irgendwo in Ihrem Benutzerbereich.  

3. Öffnen Sie den Ordner `ProofYw7_<Versionsnummer>` und führen Sie `Install.bat` aus (Doppelklick). Dadurch werden alle Programmdateien an den richtigen Ort kopiert.

4. LibreOffice Writer starten. Sie sollten ein kleines Symbolleisten-Fenster sehen, das einen Button mit einem yWriter-Logo enthält. Dieser Button ist für das Zurückschreiben der korrekturgelesenen Datei in das yWriter Projekt. Docken Sie diese Symbolleiste irgendwo an. 

4. __Optional:__  Laden Sie die Schriftart [Courier Prime](https://quoteunquoteapps.com/courierprime) herunter und installieren sie sie.



## ProofYw7 benutzen

1. Verfassen Sie Ihren Roman mit yWriter 7. Schauen Sie nach, ob der Ordner `<Ihr yWriter Projekt>.yw` eine Datei namens `proof.bat` enthält. Falls nicht, kopieren Sie sie von `ProofYw7_<Versionsnummer>\setup` hierher.

2. Schließen Sie yWriter und öffnen Sie den Ordner `<Ihr yWriter Projekt>.yw7` und führen Sie `proof.bat` aus (Doppelklick). Schließen Sie yWriter, gehen Sie in den Ordner `<Ihr yWriter Projekt>.yw`, und führen Sie `proof.bat` aus (Doppelklick). 

3. Wenn alles gut geht, werden Sie eine OpenDocument-Datei mit dem Namen `<Ihr yWriter Projekt>_proof.odt` sehen. Öffnen sie es (Doppelklick) zum Korrekturlesen. Es enthält Markieringen für Kapitel `[ChID:x]` und Szenen `[ScID:y]` nach dem yWriter 5 Standard.  Ändern Sie die Zeilen, die diese Markierungen enthalten, nicht, wenn Sie das Dokument in yWriter reimportieren wollen. 

3. Um die korrekturgelesenen Szenen in das yWriter-Projekt zurückzuschreiben, klicken Sie den Button mit dem yWriter-Logo, oder wählen Sie den Menüeintrag  _Extras > Add-ons > ProofYw7 > Korrigierte Szenen nach yWriter zurückschreiben_.

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw7/master/docs/Screenshots/screenshot2d.png)

Wenn alles geklappt hat, öffnet sich ein Fenster mit einer Erfolgsmeldung.

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw7/master/docs/Screenshots/screenshot3d.png)



## ProofYw7 deinstallieren

1. Öffnen Sie den Ordner `ProofYw7_<Versionsnummer>` und führen Sie `Uninstall.bat` aus (Doppelklick).

