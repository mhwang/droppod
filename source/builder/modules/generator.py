from . import common
from jinja2 import Environment, FileSystemLoader

def generator( theme ):
    if theme != 'all' and common.isTheme( theme ):
        create( theme )
    else:
        for theme in common.getThemes():
            create( theme )

def create( theme ):
    name = theme
    theme = common.getTheme( theme )

    try:
        css = open( 'source/css/processed/{}.css'.format( name ) ).read()
    except:
        css = ''

    common.makeDest( 'source/html/generated/{}'.format( name ) )

    template = Environment( loader = FileSystemLoader( 'source/html/dev' ) )
    template = template.get_template( '{}.html'.format( name ) )

    print( 'Generating {} theme'.format( name ) )

    for page in theme:
        page[ 'css' ] = css
        output = template.render( page = page )

        filename = page[ 'filename' ] if 'filename' in page else page[ 'code' ]

        with open( 'source/html/generated/{}/{}.html'.format( name, filename ), 'wb' ) as result:
            print( '  --{}.html'.format( filename ) )
            result.write( output.encode( 'utf-8' ) )