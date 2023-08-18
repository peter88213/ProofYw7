[project homepage](https://peter88213.github.io/ProofYw7) > Instructions for use

---

Import and export ywriter7 scenes for proof reading (file format: **ODT**  (OASIS Open Document format) as used with *LibreOffice Writer* and *OpenOffice Writer*).


## Instructions for use

### Intended usage

Create a shortcut to **proofyw7.pyw**  on the desktop. You can launch the program by dragging either a **yw7** or **odt** file and dropping it on the shortcut icon. 

### Command line usage

Alternatively, you can

- launch the program on the command line passing the **yw7** or **odt** file as an argument, or
- launch the program via a batch file.

usage: `proofyw7.pyw [--silent] Sourcefile`

#### positional arguments:

`Sourcefile` 

The path of the file to convert (either .yw7, or .odt).

#### optional arguments:

`--silent`  suppress error messages and the request to confirm overwriting

---

## Workflow

1.  Move into your yWriter project folder, drag your *.yw7* project file and drop it on the *proofyw7* icon. 

2. If everything goes well, you find an OpenDocument file named `<your yw7 project>_proof.odt`. 
You can upload it for online editing, if the word processor can read and write the *.odt* file format.

4. After editing online, be sure to place the downloaded file in the same folder as your yw7 project. 

5. Drag `<your yw7 project>_proof.odt` and drop it on the *proofyw7* icon. This will update the yw7 project file.

---

## Specification of the odt document

*proofyw7* will write parts, chapters, and scenes into a new OpenDocument
text document (odt) with visible scene markers. File name suffix is
`_proof`.

-   Only "normal" chapters and scenes are exported. Chapters and
    scenes marked "unused", "todo" or "notes" are not exported.
-   Scenes beginning with `<HTML>` or `<TEX>` are not exported.
-   Interspersed HTML, TEX, or RTF commands are taken over unchanged.
-   The document contains chapter and scene headings. However, changes will not be written back.
-   The document contains scene `[ScID:x]` markers.
    **Do not touch lines containing the markers** if you want to
    be able to write the document back to *yw7* format.
-   Chapters and scenes can neither be rearranged nor deleted. 
-   When editing the document, you can split scenes by inserting headings or a scene divider:
    -   *Heading 1* → New part title. Optionally, you can add a description, separated by `|`.
    -   *Heading 2* → New chapter title. Optionally, you can add a description, separated by `|`.
    -   `###` → Scene divider. Optionally, you can append the 
        scene title to the scene divider. You can also add a description, separated by `|`.
    -   **Note:** Export documents with split scenes from *Writer* to yw7 not more than once.      
-   Text markup: Bold and italics are supported. Other highlighting such
    as underline and strikethrough are lost.

---

## License

ProofYw7 is distributed under the [MIT License](http://www.opensource.org/licenses/mit-license.php).
