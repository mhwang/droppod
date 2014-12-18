from datetime import *
import glob, os, re, yaml

def isTheme( theme ):
    return os.path.isfile( 'source/yaml/{}.yaml'.format( theme ) )

def getTheme( theme ):
    return yaml.load( getThemeFile( theme ) )

def getThemeFile( theme ):
    return open( 'source/yaml/{}.yaml'.format( theme ), 'r' ).read()

def getThemes():
    themes = []
    for theme in glob.glob( 'source/yaml/*.yaml' ):
        themes.append( theme.split( '/' ).pop().split( '.' ).pop( 0 ) )
    return themes

def getVersion( theme ):
    return '{}.{}'.format( date.today().strftime( '%y%m%d' ), re.search( '# (v|V)ersion ([0-9].*?)', getThemeFile( theme ) ).group(0).split( ' ' ).pop() )

def makeDest( path ):
    if not os.path.isdir( path ):
        os.makedirs( path, exist_ok = True )
