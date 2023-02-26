import sqlite3

import click

# current_app is a special object that points to the Flask application handling the request. Since you used an application factory, there is no application object when writing the rest of your code.
# g is a special object that is unique for each request. It is used to store data that might be accessed by multiple functions during the request. The connection is stored and reused instead of creating a new connection if get_db is called a second time in the same request.
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Tells the connnection to return rows that behave like dicts. This allows accessing the columns by name.
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    '''Clear the existing data and create new tables.'''
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    '''
    The close_db and init_db_command functions need to be registered with the application instance; otherwise, they won't be used by the application. However, since you're using a factory function, that instance isn't available when writing the functions. Instead, write a function that takes an application and does the registration.
    '''
    app.teardown_appcontext(close_db) # tells Flask to call that function when cleaning up after returning the response.
    app.cli.add_command(init_db_command) # adds a new command that can be called with the flask command. e.g. flask -app flaskr init-db