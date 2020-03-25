# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/25 21:21


class UrlManager:
    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        path = path + '?ver=' + '201805021500'
        return UrlManager.buildUrl(path)

