# Music Font Scripts

This folder contains FontForge scripts tailored to music font processing, which involves mainstream music font formats such as the widely used SMuFL mapping, Sibelius and (older versions of) Finale's *Sonata* Layout (which has its root in the first music symbol font, *Sonata*), and the LilyPond music font layout.

To run the scripts, you have to put the parent directory of FontForge's executable file into your system's environmental variables to ensure that you can invoke FontForge by the `fontforge` command in command line. Then directly click on the `run.bat` file in each folder and follow the instruction.

The scripts are listed as follows:

* `smufl-glyph-rename`

    This script renames the glyphs in an SMuFL-compatible music font by the standard name specified in SMuFL's `glyphnames.json` file. It also maps the glyphs with Unicode-encoding counterparts (most of which locate in the "Musical Symbols" region ranging from `U+1D100` to `U+1D1FF`) to their corresponding codepoints. In addition, time signature numbers are mapped to digits `0` - `9`, and the dynamic single letters ***p***, ***m***, ***f***, ***s***, ***z***, ***n*** are mapped to the lower case letters.