#-*- coding:utf-8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.demoProject.elements.indexPageElements import IndexPageElements
#from page_objects.web_ui.demoProject.pages.homePage import HomePage
class IndexPage:
    def __init__(self,browserOperator):
        self._browserOperator=browserOperator
        self._indexPageElements=IndexPageElements()
        self._browserOperator.explicit_wait_page_title(self._indexPageElements.title)
        self._browserOperator.get_screenshot('indexPage')


    def _input_username(self,username):
        self._browserOperator.sendText(self._indexPageElements.username_input,username)
        self._browserOperator.get_screenshot('input_username')

    def _input_password(self,password):
        self._browserOperator.sendText(self._indexPageElements.password_input,password)
        self._browserOperator.get_screenshot('input_password')

    def _click_denglu_button(self):
        self._browserOperator.click(self._indexPageElements.denglu_button)
        self._browserOperator.get_screenshot('click_denglu_button')

    # def _get_home_pages(self):
    #     self._browserOperator.click(self._indexPageElements.homepage())
    #     self._browserOperator.get_screenshot('get_home_pages')

    def login(self, username,password):
        self._input_username(username)
        self._input_password(password)
        self._click_denglu_button()
        #self._get_home_pages()
        #if username.strip():
        #    return SearchPage(self._browserOperator,username+'_现场总管')
        return IndexPage(self._browserOperator)

    def getElements(self):
        return self._indexPageElements