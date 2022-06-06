#-*- coding:utf-8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.demoProject.elements.homePageElements import homePageElements
class HomePage:
    def __init__(self,browserOperator):
        self._browserOperator=browserOperator
        self._homePageElements=homePageElements()
        #self._homePageElements.title.wait_expected_value=title
        self._browserOperator.explicit_wait_page_title(self._homePageElements.title)
        #self._browserOperator.explicit_wait_page_title(self._indexPageElements.title)
        self._browserOperator.get_screenshot('homePage')

    def _check_yuyue(self):
        self._browserOperator.click(self._homePageElements.check_yuyue)
        self._browserOperator.get_screenshot('check_yuyue')
    def _check(self):
        self._check_yuyue()

    def getElements(self):
        return self._homePageElements