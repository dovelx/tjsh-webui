#-*- coding:utf-8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.demoProject.elements.jsamubanElements import jsamubanPageElements
class jsamubanPage:
    def __init__(self,browserOperator,title):
        self._browserOperator=browserOperator
        self._jsamubanElements=jsamubanPageElements
        self._jsamubanElements.title.wait_expected_value=title
        #self._browserOperator.explicit_wait_page_title(self._jsamubanElements.title)
        self._browserOperator.get_screenshot('jsamuban')

    def _tianjia(self):
        self._browserOperator.click(self._jsamubanElements.tianjia_button)
        self._browserOperator.get_screenshot('tianjia_button')

    def _xiugai(self):
        self._browserOperator.click(self._jsamubanElements.xiugai_button)
        self._browserOperator.get_screenshot('tianjia_button')

    def _fuxuankuang(self):
        self._browserOperator.click(self._jsamubanElements.fuxuankuang)
        self._browserOperator.get_screenshot('fuxuankuang')
    def _suoshubumen(self):
        self._browserOperator.click(self._jsamubanElements.suoshubumen)
        self._browserOperator.get_screenshot('suoshubumen')
    def _mubanmingcheng(self):
        self._browserOperator.sendText(self._jsamubanElements.mubanmingcheng)
        self._browserOperator.get_screenshot('mubanmingcheng')
    def _chaxun(self):
        self._browserOperator.click(self._jsamubanElements.chaxun_button)
        self._browserOperator.get_screenshot('chaxun')

    def chaxun(self,mubanmingcheng):
        self._mubanmingcheng(mubanmingcheng)
        self._chaxun()
    def tianjia(self):
        self._tianjia()
    def xiugai(self):
        self._fuxuankuang()
        self._xiugai()
    def getElements(self):
        return self._jsamubanElements