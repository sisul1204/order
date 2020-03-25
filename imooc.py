# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/25 20:44

from flask import Blueprint

route_imooc = Blueprint('imooc_page', __name__)

@route_imooc.route('/')
def index():
    return 'imooc index page'

@route_imooc.route('/hello')
def hello():
    return 'imooc hello world'
