from . import common
import glob, lzma, shutil, tarfile

def compressor( theme ):
    if theme != 'all' and common.isTheme( theme ):
        compress( theme )
    else:
        for theme in common.getThemes():
            compress( theme )

def compress( theme ):
    dest = '../../releases'
    name = theme
    theme = common.getTheme( theme )

    common.makeDest( dest )

    print( 'Compressing {} theme'.format( name ) )
    shutil.copyfile( 'source/raw/robots.txt', 'source/html/processed/{}/robots.txt'.format( name ) )

    theme_files = glob.glob( 'source/html/processed/{}/*'.format( name ) )

    cfile = tarfile.open( '{}/{}-{}.tar.xz'.format( dest, name, common.getVersion( name ) ), 'w:xz' )
    for theme_file in theme_files:
        cfile.add( theme_file, theme_file.split( '/' ).pop() )
    cfile.close()