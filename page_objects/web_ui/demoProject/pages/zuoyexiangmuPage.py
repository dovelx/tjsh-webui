#-*- coding:utf-8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.demoProject.elements.zouyexiangmuElements import zuoyexiangmuPageElements
class ZuoyexiangmuPage:
    def __init__(self,browserOperator):
        self._browserOperator=browserOperator
        self._zouyexiangmuElements=zuoyexiangmuPageElements()
        #self._homePageElements.title.wait_expected_value=title
        self._browserOperator.explicit_wait_page_title(self._zouyexiangmuElements.title)
        #self._browserOperator.explicit_wait_page_title(self._indexPageElements.title)
        self._browserOperator.get_screenshot('zouyexiangmupage')

    def _tianjia(self):
        self._browserOperator.click(self._zouyexiangmuElements.tianjia_button)
        self._browserOperator.get_screenshot('tianjia_button')
    def _fuxuankuang(self):
        self._browserOperator.click(self._zouyexiangmuElements.fuxuankuang)
        self._browserOperator.get_screenshot('fuxuankuang')
    def _suoshubumen(self):
        self._browserOperator.click(self._zouyexiangmuElements.suoshubumen)
        self._browserOperator.get_screenshot('suoshubumen')
    def _suoshudanwei(self):
        self._browserOperator.click(self._zouyexiangmuElements.suoshudanwei)
        self._browserOperator.get_screenshot('suoshudanwei')
    def _chaxun(self):
        self._browserOperator.click(self._zouyexiangmuElements.chaxun_button)
        self._browserOperator.get_screenshot('chaxun')

    def getElements(self):
        return self._zouyexiangmuElements