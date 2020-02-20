# ProofYw7 (yWriter-zu-LibreOffice-Konvertierer)

Einen Roman aus [yWriter 7](http://www.spacejock.com/yWriter7.html) in eine OpenDocument-Textdatei exportieren.

Mehr Informationen finden Sie im [Wiki (deutsch)](https://github.com/peter88213/ProofYw7/wiki/Deutsch). 

## Voraussetzungen

* Windows.

* yWriter 7.

* Eine reguläre LibreOffice 5 oder 6-Installation (nicht "portable").

## Download

Die ProofYw7 Software kommt als ZIP-Archiv `ProofYw7_Versionsnummer.zip`. 

[Download-Seite](https://github.com/peter88213/ProofYw7/releases)

## ProofYw7 installieren

1. Falls Sie bereits eine Version von PyWriter installiert haben, führen Sie bitte das Deinstallationsprogramm dafür aus. 

2. Entpacken Sie das Archiv `ProofYw7_<Versionsnummer>.zip` irgendwo in Ihrem Benutzerbereich.  

3. Öffnen Sie den Ordner `ProofYw7_<Versionsnummer>` und führen Sie `Install.bat` aus (Doppelklick). Dadurch werden alle Programmdateien an den richtigen Ort kopiert.

4. __Optional:__ ffnen Sie den Ordner `ProofYw7_<Versionsnummer>\fonts` und entpacken Sie das Archiv `CourierPrime.zip`. Installieren Sie die `.ttf`-Dateien (Rechtsklick -> Installieren).


## ProofYw7 benutzen

1. Verfassen Sie Ihren Roman mit yWriter 7. Schauen Sie nach, ob der Ordner `<Ihr yWriter Projekt>.yw` eine Datei namens `proof.bat` enthält. Falls nicht, kopieren Sie sie von `ProofYw7_<Versionsnummer>\setup` hierher.

2. Schließen Sie yWriter und öffnen Sie den Ordner `<Ihr yWriter Projekt>.yw7` und führen Sie `proof.bat` aus (Doppelklick). Wenn alles klappt, wird LibreOffice Writer automatisch starten und das Dokument im OpenDocument-Format als `<Ihr yWriter Projekt>.odt` mit hierarchischer Struktur und mit den richtigen Absatz-/Zeichenvorlagen anzeigen.

3. Bringen Sie Ihr Manuskript mit Hilfe von [OOTyW](https://github.com/peter88213/OOTyW/wiki/Deutsch) typographisch auf Vordermann.

## ProofYw7 deinstallieren

1. Öffnen Sie den Ordner `ProofYw7_<Versionsnummer>` und führen Sie `Uninstall.bat` aus (Doppelklick).

