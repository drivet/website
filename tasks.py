# -*- coding: utf-8 -*-

import os
import shutil
import sys

from invoke import task
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    # Port for `serve`
    'port': 8000,
    'ssh_host': 'desmondrivet.com',
    'ssh_user': 'dcr',
    'ssh_target_dir': '/home/dcr/wwwroot/pelican_blog'
}


@task
def clonedeps(c):
    """Clone non-pip dependencies"""
    c.run('rm -rf repos')
    c.run('mkdir -p repos')
    c.run('git clone '
          'https://github.com/drivet/pelican_notedown.git '
          'repos/pelican_notedown')
    c.run('git clone '
          'https://github.com/getpelican/pelican-plugins.git '
          'repos/pelican-plugins')
    c.run('git clone '
          'https://github.com/drivet/pelican-indieweb-kit.git '
          'repos/pelican-indieweb-kit')


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])


@task
def build(c):
    """Build local version of site"""
    c.run('pelican -s {settings_base}'.format(**CONFIG))


@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run('pelican -d -s {settings_base}'.format(**CONFIG))


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run('pelican -r -s {settings_base}'.format(**CONFIG))


@task
def serve(c):
    """Serve site at http://localhost:$PORT/ (default port is 8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        ('', CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {port} ...\n'.format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    c.run('pelican -s {settings_publish}'.format(**CONFIG))


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build(c))
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    server.watch('{}/templates/*.html'.format(theme_path), lambda: build(c))
    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file = '{0}/static/**/*{1}'.format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured port
    server.serve(port=CONFIG['port'], root=CONFIG['deploy_path'])


@task
def publish(c):
    """Publish to production via rsync"""
    c.run('pelican -s {settings_publish}'.format(**CONFIG))
#    c.run(
#        'rsync --delete --exclude ".DS_Store" -pthrvz -c '
#        '{} {production}:{dest_path}'.format(
#            CONFIG['deploy_path'].rstrip('/') + '/',
#            **CONFIG))
    c.run('rsync -avzh -O -e \'ssh -o "StrictHostKeyChecking=no"\' '
          '{deploy_path}/* {ssh_user}@{ssh_host}:{ssh_target_dir}'
          .format(**CONFIG))
