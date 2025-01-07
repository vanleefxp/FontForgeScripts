try:
    import fontforge as ff # type: ignore
except ImportError:
    print ( "You're not running this script via FontForge. This will take no effect." )
    exit ( 1 )

import json
import os

DIR = os.path.dirname ( __file__ ) if "__file__" in locals ( ) else os.getcwd ( )

smuflGlyphNameTable = json.loads ( open ( f"{DIR}/../assets/glyphnames.json" ).read ( ) )
smuflMapping = { }
smufl2Unicode = { }
for glyphName, info in smuflGlyphNameTable.items ( ):
    codepoint = int ( info [ "codepoint" ] [ 2: ], 16 )
    smuflMapping [ codepoint ] = glyphName
    if ( unicodeCodepoint := info.get ( "alternateCodepoint" ) ) is not None:
        unicodeCodepoint = int ( unicodeCodepoint [ 2: ], 16 )
        smufl2Unicode [ codepoint ] = unicodeCodepoint

def merge ( target, source ):
    for k, v in source.items ( ):
        if ( oldValue := target.get ( k ) ) is not None:
            if isinstance ( oldValue, int ):
                if isinstance ( v, int ):
                    target [ k ] = ( oldValue, v )
                else:
                    target [ k ] = ( oldValue, *v )
            else:
                if isinstance ( v, int ):
                    target [ k ] = ( *oldValue, v )
                else:
                    target [ k ] = ( *oldValue, *v )
        else:
            target [ k ] = v

merge ( smufl2Unicode, {
    0xECA6: 0x2669, # quarter note
    0xECA7: 0x266A, # eighth note
    0xECB7: ord ( "." ), # dot
    
    # dynamic letters
    0xE520: ord ( "p" ),
    0xE521: ord ( "m" ),
    0xE522: ord ( "f" ),
    0xE523: ord ( "r" ),
    0xE524: ord ( "s" ),
    0xE525: ord ( "z" ),
    0xE526: ord ( "n" ),
    
    # time signature numbers
    0xE080: ord ( "0" ),
    0xE081: ord ( "1" ),
    0xE082: ord ( "2" ),
    0xE083: ord ( "3" ),
    0xE084: ord ( "4" ),
    0xE085: ord ( "5" ),
    0xE086: ord ( "6" ),
    0xE087: ord ( "7" ),
    0xE088: ord ( "8" ),
    0xE089: ord ( "9" ),
} )

font = ff.open ( input ( "Enter font file path: " ).strip ( ) )
for glyph in font.glyphs ( ):
    smuflGlyphName = smuflMapping.get ( glyph.unicode )
    if smuflGlyphName is not None:
        # SMuFL glyph
        glyph.glyphname = smuflGlyphName
        if ( unicodeCodepoint := smufl2Unicode.get ( glyph.unicode ) ) is not None:
            if isinstance ( unicodeCodepoint, int ):
                glyph.altuni = ( ( unicodeCodepoint, -1, 0 ), )
            else:
                glyph.altuni = tuple ( ( cp, -1, 0 ) for cp in unicodeCodepoint )
font.save ( )
print ( "Done!" )
input ( "Press Enter to exit." )
