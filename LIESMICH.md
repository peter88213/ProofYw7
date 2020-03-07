# ProofYw7 (yWriter 7-Szenen mit LibreOffice korrekturlesen)

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw7/master/docs/Screenshots/screenshot1d.png)



## Voraussetzungen

* Windows.

* yWriter 7.

* Eine reguläre LibreOffice 5 oder 6-Installation (nicht "portable").



## Download

Die ProofYw7 Software kommt als ZIP-Archiv `ProofYw7_Versionsnummer.zip`. 

[Download-Seite](https://github.com/peter88213/ProofYw7/releases/latest)



## ProofYw7 installieren

1. Falls Sie bereits eine Version von ProofYw7 installiert haben, führen Sie bitte das
   Deinstallationsprogramm dafür aus. 

2. Entpacken Sie das Archiv `ProofYw7_<Versionsnummer>.zip` irgendwo in Ihrem Benutzerbereich.  

3. Öffnen Sie den Ordner `ProofYw7_<Versionsnummer>` und führen Sie `Install.bat` aus 
   (Doppelklick). Dadurch werden alle Programmdateien an den richtigen Ort kopiert und es wird
   eine LibreOffice-Extension installiert. 
   Möglicherweise werden Sie um Erlaubnis gebeten, die Windows-Registry zu ändern. 
   Bitte stimmen Sie zu, um für yWriter7-Dateien einen Explorer-Kontextmenüeintrag 
   "Proof read with LibreOffice" zu installieren. 

4. LibreOffice Writer starten. Sie sollten ein kleines Symbolleisten-Fenster sehen, das einen
   Button mit einem yWriter-Logo enthält. Dieser Button ist für das Zurückschreiben der
   korrekturgelesenen Datei in das yWriter Projekt. Docken Sie diese Symbolleiste irgendwo an. 

4. __Optional:__  Laden Sie die Schriftart [Courier Prime](https://quoteunquoteapps.com/courierprime) herunter und installieren sie sie.



## ProofYw7 benutzen

1. Verfassen Sie Ihren Roman mit yWriter7. Bitte beachten Sie die folgenden Konventionen:
   * Textauszeichung: Fettschrift (Bold) und Kursivschrift (Italics) werden unterstützt. Andere Hervorhebungen wie Unterstreichung (Underline) und Durchstreichung (Strikethrough) gehen verloren. 
   * Alle Kapitel und Szenen werden exportiert, egal ob "used" oder "unused". 
   * Wenn `This chapter begins a new section` in _Chapter/Details_ ausgewählt ist, ist die Überschrift auf der ersten Ebene. Andernfalls ist sie auf der zweiten Ebene.
   * Wenn `Suppress chapter title when exporting` in _Chapter/Details_ ausgewählt ist, entfernt ProofYw7 "Chapter" aus den automatisch nummerierten Kapitelüberschriften. Die Nummern bleiben erhalten, ebenso die anderen Kapitelüberschriften. Diese Änderungen haben keine Auswirkung auf den Reimport.

   Machen Sie ein Backup des gesamten Projekts und schließen sie yWriter.

2. Öffnen Sie den Ordner Ihres yWriter-Projekts und machen Sie einen Rechtsklick auf die
   .yw7-Projektdatei. Im Kontextmenü wählen Sie `Proof read with LibreOffice`.
   
![Screenshot: Windows Explorer context menu](https://raw.githubusercontent.com/peter88213/ProofYw7/master/docs/Screenshots/ProofYw7_cm.png)

3. Wenn alles gut geht, finden Sie eine OpenDocument-Datei mit dem Namen 
   `<Ihr yWriter Projekt>_proof.odt`. Öffnen Sie sie (Doppelklick) zum Korrekturlesen. 
   Sie enthält Markieringen für Kapitel `[ChID:x]` und Szenen `[ScID:y]` nach dem yWriter5-
   Standard.  Ändern Sie die Zeilen, die diese Markierungen enthalten, nicht, wenn Sie das 
   Dokument in yWriter reimportieren wollen. 

3. Um die korrekturgelesenen Szenen in das yWriter-Projekt zurückzuschreiben, klicken Sie den 
   Button mit dem yWriter-Logo, oder wählen Sie den Menüeintrag  
   `Extras > Add-ons > ProofYw7 > Korrigierte Szenen nach yWriter zurückschreiben`.

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw7/master/docs/Screenshots/screenshot2d.png)

Wenn alles geklappt hat, öffnet sich ein Fenster mit einer Erfolgsmeldung.

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw7/master/docs/Screenshots/screenshot3d.png)



## ProofYw7 deinstallieren

1. Öffnen Sie den Ordner `ProofYw7_<Versionsnummer>` und führen Sie `Uninstall.bat` aus 
   (Doppelklick). Möglicherweise werden Sie  um Erlaubnis gebeten, die Windows-Registry zu ändern. 
   Bitte stimmen Sie zu, um den Explorer-Kontextmenüeintrag zu entfernen.

