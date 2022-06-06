#-*- coding:utf-8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.demoProject.elements.hseElements import hsePageElements
class hsePage:
    def __init__(self,browserOperator,title):
        self._browserOperator=browserOperator
        self._hseElements=hsePageElements
        self._hseElements.title.wait_expected_value=title
        #self._browserOperator.explicit_wait_page_title(self._hseElements.title)
        self._browserOperator.get_screenshot('hse')

    def _tianjia(self):
        self._browserOperator.click(self._hseElements.tianjia_button)
        self._browserOperator.get_screenshot('tianjia_button')

    def _xiugai(self):
        self._browserOperator.click(self._hseElements.xiugai_button)
        self._browserOperator.get_screenshot('tianjia_button')

    def _fuxuankuang(self):
        self._browserOperator.click(self._hseElements.fuxuankuang)
        self._browserOperator.get_screenshot('fuxuankuang')
    def _suoshubumen(self):
        self._browserOperator.click(self._hseElements.suoshubumen)
        self._browserOperator.get_screenshot('suoshubumen')
    def _zuoyemingcheng(self):
        self._browserOperator.sendText(self._hseElements.zuoyemingcheng)
        self._browserOperator.get_screenshot('zuoyemingcheng')
    def _chaxun(self):
        self._browserOperator.click(self._hseElements.chaxun_button)
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
        return self._hseElements