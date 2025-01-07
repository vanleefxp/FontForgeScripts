try:
    import fontforge as ff # type: ignore
except ImportError:
    print ( "You're not running this script via FontForge. This will take no effect." )
    exit ( 1 )

import os

DIR = os.path.dirname ( __file__ ) if "__file__" in locals ( ) else os.getcwd ( )

lilypondMapping = { }
lilypondFont = ff.open ( f"{DIR}/assets/fonts/emmentaler-20.otf" )

for glyph in lilypondFont.glyphs ( ):
    if glyph.unicode > 0:
        lilypondMapping [ glyph.unicode ] = glyph.glyphname

print ( lilypondMapping )
input ( "Press Enter to exit." )