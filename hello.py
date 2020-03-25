# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/25 20:32

from flask import Flask, url_for
from imooc import route_imooc
from common.libs.UrlManager import UrlManager

app = Flask(__name__)
app.register_blueprint(route_imooc, url_prefix='/imooc')

@app.route('/')
def hello_world():
    url = url_for('index')

    url_1 = UrlManager.buildUrl('/api')

    url_2 = UrlManager.buildStaticUrl('/css/bootstrap.css')

    msg = 'hello world, url:%s, url_1:%s, url_2:%s' % (url, url_1, url_2)
    app.logger.debug(msg)
    app.logger.info(msg)
    app.logger.error(msg)

    return msg

@app.route('/api')
def index():
    return 'Index page'

@app.route('/api/hello')
def hello():
    return 'hello'


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return 'This page does not exist', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)