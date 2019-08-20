from flask import Blueprint
import click

bp = Blueprint('flask_cmd', __name__, cli_group='other')

# type 'flask other create alice'
@bp.cli.command('create')
@click.argument('name')
def create(name):
    print(name + ' separately')
