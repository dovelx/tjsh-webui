#-*- coding:utf-8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.demoProject.elements.shigongzuoyepiaoElements import shigongzuoyepiaoPageElements
class shigongzuoyepiaoPage:
    def __init__(self,browserOperator):
        self._browserOperator=browserOperator
        self._shigongzuoyepiaoElements=shigongzuoyepiaoPageElements()
        #self._homePageElements.title.wait_expected_value=title
        self._browserOperator.explicit_wait_page_title(self._shigongzuoyepiaoElements.title)
        #self._browserOperator.explicit_wait_page_title(self._indexPageElements.title)
        self._browserOperator.get_screenshot('zouyexiangmupage')

    def _tianjia(self):
        self._browserOperator.click(self._shigongzuoyepiaoElements.tianjia_button)
        self._browserOperator.get_screenshot('tianjia_button')
    def _fuxuankuang(self):
        self._browserOperator.click(self._shigongzuoyepiaoElements.fuxuankuang)
        self._browserOperator.get_screenshot('fuxuankuang')
    def _xiugai(self):
        self._browserOperator.click(self._shigongzuoyepiaoElements.xiugai_button)
        self._browserOperator.get_screenshot('xiugai')
    def _suoshubumen(self):
        self._browserOperator.click(self._shigongzuoyepiaoElements.suoshubumen)
        self._browserOperator.get_screenshot('suoshubumen')
    def _zuoyemingcheng(self,zuoyemingcheng):
        self._browserOperator.sendText(self._shigongzuoyepiaoElements.zuoyemingcheng,zuoyemingcheng)
        self._browserOperator.get_screenshot('zuoyemingcheng')
    def _chaxun(self):
        self._browserOperator.click(self._shigongzuoyepiaoElements.chaxun_button)
        self._browserOperator.get_screenshot('chaxun')
    def chaxun(self,zuoyemingcheng):
        self._zuoyemingcheng( zuoyemingcheng)
        self._chaxun()
    def tianjia(self):
        self._tianjia()
    def xiugai(self):
        self._fuxuankuang()
        self._xiugai()

    def getElements(self):
        return self._shigongzuoyepiaoElements