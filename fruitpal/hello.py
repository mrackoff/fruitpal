import functools
import json
import re
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