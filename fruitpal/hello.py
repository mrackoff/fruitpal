import functools
import json
from typing import KeysView
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from fruitpal import db
from fruitpal.db import get_db

bp = Blueprint('hello', __name__, url_prefix='/hello')
# a simple page that says hello
@bp.route('', methods=['GET'])
def hello():
    return "hello world!"

@bp.route('/pricecheck', methods=['GET'])
def pricecheck():
    request.args.getlist("quantity")
    quantity= request.args.get("quantity",1)
    price = request.args.get("price",1)
    commodity=request.args.get("commodity","")
    if commodity== "":
        return 400
    #error check for null/0 values 
    #think potential about limiting commodity so that people aren't doing silly things that would cuase integer overflow

    db =get_db()
    rows = db.execute(
        "select  variable_price, country from price_check where commodity = ? ", ( commodity.upper(), ) ).fetchall()
    rows_dict = [dict(ix) for ix in rows]
    
    for l in rows_dict:
        print(l.keys())
        #print(l['VARIABLE_PRICE'])
        l["VARIABLE_PRICE"]=float(quantity)*l["VARIABLE_PRICE"]
    return json.dumps( rows_dict), 404
    
#db = get_db()
# rows  = db.execute("select * from price_check").fetchall()
#  return json.dumps([dict(ix) for ix in rows])