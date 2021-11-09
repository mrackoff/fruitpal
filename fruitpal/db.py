import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
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

    prices=[]
    with open('./fruitpal/fruitpal/pricedata.txt',"r") as f:  
        curPrice=0
        curCountry=""
        curCommodity=""
        for l in f.readlines():
            if l[0:13]=="COMMODITY = \"":
                curCommodity=l[13:len(l)-2]
            elif l[0:18]=="VARIABLE_PRICE = \"":
                curPrice=l[18:len(l)-2]
            elif l[0:11]=="COUNTRY = \"":
                curCountry=l[11:len(l)-2]
            else:
                print(curCountry)
                print(curPrice)
                print(curCommodity)
                prices.append([curCountry,curCommodity,curPrice])
    db.executemany("insert into price_check (country, commodity, variable_price) VALUES (?,?,?)",(prices))
    db.commit()    
           


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
