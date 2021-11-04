import functools
import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from fruitpal.db import get_db

bp = Blueprint('hello', __name__, url_prefix='/hello')
# a simple page that says hello
@bp.route('', methods=['GET'])
def hello():
    #db = get_db()
    #
    
    # rows  = db.execute("select * from price_check").fetchall()
    
    # return json.dumps([dict(ix) for ix in rows])
    return "hello world!"