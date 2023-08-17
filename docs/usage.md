[project homepage](https://peter88213.github.io/ProofYw7) > Instructions for use

---

Import and export ywriter7 scenes for proof reading (file format: **ODT**  (OASIS Open Document format) as used with *LibreOffice Writer* and *OpenOffice Writer*).


## Instructions for use

### Intended usage

Create a shortcut on the desktop. You can launch the program by dragging either a **yw7** or **odt** file and dropping it on the shortcut icon. 

### Command line usage

Alternatively, you can

- launch the program on the command line passing the **yw7** or **odt** file as an argument, or
- launch the program via a batch file.

usage: `proofyw7.py [--silent] Sourcefile`

#### positional arguments:

`Sourcefile` 

The path of the file to convert (either .yw7, or .odt).

#### optional arguments:

`--silent`  suppress error messages and the request to confirm overwriting

---

### Workflow

1. Write your novel with yWriter7. Please consider the following conventions:
   * Text markup: Bold and italics are supported. Other highlighting such as underline and strikethrough are lost.
   * All "normal" chapters and scenes will be exported. 

2.  Move into your yWriter project folder, drag your .yw7 project file and drop it on the *proofyw7* icon. 

3. If everything goes well, you find an OpenDocument file named `<your yw7 project>_proof.odt`.

4. Edit this file. After editing, make sure it is still in the same folder as your yw7 project.

5. Drag `<your yw7 project>_proof.odt` and drop it on the *proofyw7* icon. This will update the yw7 project file.

## License

ProofYw7 is distributed under the [MIT License](http://www.opensource.org/licenses/mit-license.php).
