#!/usr/bin/python
# encoding: utf8

# Smith configuration file for EastSyriacMarcusNew

# set the default output folders
DOCDIR = ["documentation", "web"]
genout = "generated/"

# set the font name and description
APPNAME = 'EastSyriacMarcusNew'
FAMILY = APPNAME
DESC_SHORT = "Font for the East Syriac script"

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/masters/' + FAMILY + '-Regular' + '.ufo')

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

# APs to omit:
omitaps = '--omitaps "L,O,R"'

designspace('source/EastSyriacMarcusNew.designspace',
    target = process('${DS:FILENAME_BASE}.ttf',
        cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}'),
        cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${source}']),
    ),
    version=VERSION,  # Needed to ensure dev information on version string
    opentype = fea("generated/${DS:FILENAME_BASE}.fea", 
        mapfile = genout + "${DS:FILENAME_BASE}.map",
        master="source/opentype/main.feax", to_ufo = 'True'),
#    typetuner = typetuner("source/typetuner/feat_all.xml"),
    script='syrc',
    pdf = fret(params='-oi'),
    woff = woff('web/${DS:FILENAME_BASE}.woff',
        metadata=f'../source/{FAMILY}-WOFF-metadata.xml',
        ),
    )
