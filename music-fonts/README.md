# Music Font Scripts

This folder contains FontForge scripts tailored to music font processing, which involves mainstream music font formats such as the widely used [SMuFL](https://w3c.github.io/smufl/latest/index.html) mapping, Sibelius and (older versions of) Finale's [*Sonata* layout](https://w3c.github.io/smufl/latest/about/brief-history.html) (which has its root in the first music symbol font, [*Sonata*](http://www.identifont.com/show?12A)), and the [LilyPond music font](https://github.com/OpenLilyPondFonts) layout.

The scripts are listed as follows:

* `smufl-glyph-rename`

    This script renames the glyphs in an SMuFL-compatible music font by the standard name specified in SMuFL's `glyphnames.json` file. It also maps the glyphs with Unicode-encoding counterparts (most of which locate in the "Musical Symbols" region ranging from `U+1D100` to `U+1D1FF`) to their corresponding codepoints. In addition, time signature numbers are mapped to digits `0` - `9`, and the dynamic single letters ***p***, ***m***, ***f***, ***s***, ***z***, ***n*** are mapped to the lower case letters.

* `music-font-format-convert` (currently under construction)