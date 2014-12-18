module.exports = (grunt) ->
    ###
    ## configuration
    ###
    ## grunt configuration
    grunt.initConfig
        pkg: grunt.file.readJSON( 'package.json' )

        files:
            stylus:     [ '*.styl', '!default.styl' ]
            wrkdep:     [
                'static/css/processed'
                'static/html/generated'
                'static/html/processed'
            ]
            wrkvenv:    [
                '../deploy'
                'builder/{bin,include,lib*}'
            ]

        clean:
            neaten:
                src: [
                    '<%= files.wrkdep %>'
                ]
            purge:
                src: [
                    '<%= files.wrkdep %>'
                    '<%= files.wrkvenv %>'
                ]

        htmlmin:
            compress:
                options:
                    collapseBooleanAttributes: true
                    collapseWhitespace: true
                    keepClosingSlash: true
                    removeComments: true
                    removeEmptyAttributes: true
                    removeRedundantAttributes: true
                files: [
                    expand: true
                    cwd: 'static/html/generated/'
                    src: [ '**/*.html' ]
                    dest: 'static/html/processed/'
                    ext: '.html'
                ]

        shell:
            build:
                command: [
                    'cd builder'
                    '. bin/activate'
                    './builder.py -g'
                    'deactivate'
                    'cd -'
                ].join( '&&' )
            compress:
                command: [
                    'cd builder'
                    '. bin/activate'
                    './builder.py -c'
                    'deactivate'
                    'cd -'
                ].join( '&&' )
            install:
                options:
                    force: true
                command: [
                    'virtualenv builder'
                    '. builder/bin/activate'
                    'pip install -r requirements.txt'
                    'deactivate'
                ].join( '&&' )

        stylus:
            compile:
                files: [
                    expand: true
                    flatten: true
                    cwd: 'static/css/dev/'
                    src: '<%= files.stylus %>'
                    dest: 'static/css/processed/'
                    ext: '.css'
                ]


    ###
    ## plugins
    ###
    ## grunt plugin loading; see package.json
    grunt.loadNpmTasks 'grunt-contrib-clean'
    grunt.loadNpmTasks 'grunt-contrib-htmlmin'
    grunt.loadNpmTasks 'grunt-contrib-stylus'
    grunt.loadNpmTasks 'grunt-force'
    grunt.loadNpmTasks 'grunt-shell'


    ###
    ## tasks
    ###
    ## grunt default task
    grunt.registerTask 'default', [
        ## process css
        'stylus:compile'

        ## generate html files
        'shell:build'
        'htmlmin:compress'

        ## generate deploy files
        'shell:compress'
    ]

    ## grunt install task
    grunt.registerTask 'install', [
        'force:on'
        'shell:install'
        'force:off'
    ]

    ## grunt cleanup task
    grunt.registerTask 'neaten', [
        'force:on'
        'clean:neaten'
        'force:off'
    ]
    grunt.registerTask 'purge', [
        'force:on'
        'clean:purge'
        'force:off'
    ]