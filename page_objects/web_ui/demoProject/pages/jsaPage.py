#-*- coding:utf-8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.demoProject.elements.jsaElements import jsaPageElements
class jsaPage:
    def __init__(self,browserOperator,title):
        self._browserOperator=browserOperator
        self._jsaElements=jsaPageElements
        self._jsaElements.title.wait_expected_value=title
        #self._browserOperator.explicit_wait_page_title(self._jsaElements.title)
        self._browserOperator.get_screenshot('jsamuban')

    def _tianjia(self):
        self._browserOperator.click(self._jsaElements.tianjia_button)
        self._browserOperator.get_screenshot('tianjia_button')

    def _xiugai(self):
        self._browserOperator.click(self._jsaElements.xiugai_button)
        self._browserOperator.get_screenshot('tianjia_button')

    def _fuxuankuang(self):
        self._browserOperator.click(self._jsaElements.fuxuankuang)
        self._browserOperator.get_screenshot('fuxuankuang')
    def _suoshubumen(self):
        self._browserOperator.click(self._jsaElements.suoshubumen)
        self._browserOperator.get_screenshot('suoshubumen')
    def _zuoyemingcheng(self):
        self._browserOperator.sendText(self._jsaElements.zuoyemingcheng)
        self._browserOperator.get_screenshot('mubanmingcheng')
    def _chaxun(self):
        self._browserOperator.click(self._jsaElements.chaxun_button)
        self._browserOperator.get_screenshot('chaxun')

    def chaxun(self,zuoyemingcheng):
        self._zuoyemingcheng(zuoyemingcheng)
        self._chaxun()
    def tianjia(self):
        self._tianjia()
    def xiugai(self):
        self._fuxuankuang()
        self._xiugai()
    def getElements(self):
        return self._jsaElements