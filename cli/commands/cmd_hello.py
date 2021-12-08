import subprocess

import click


@click.command()
@click.option('--name', default=True, help='command return a name')
@click.argument('path', default='snakegame')
def cli(name, path):
    """
    :param skip_init: Skip checking __init__.py files
    :param path: Test coverage path
    :return: Subprocess call result
    """
    # name = ''
    if name:
        message = 'Hello {0}'.format(path)
    cmd = print(message)
    return subprocess.call(cmd, shell=True)
