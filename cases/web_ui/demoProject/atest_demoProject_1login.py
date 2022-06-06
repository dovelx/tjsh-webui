# -*- coding:utf8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from base.web_ui.demoProject.web_ui_demoProject_client import WEB_UI_DemoProject_Client
from page_objects.web_ui.demoProject.pages.indexPage import IndexPage
from page_objects.web_ui.demoProject.pages.tongzhidanPage import TongzhidanPage
from assertpy import assert_that
class Test_Indexpage_login:
    def setup_class(self):
        self.demoProjectClient = WEB_UI_DemoProject_Client()
        self.indexPage=IndexPage(self.demoProjectClient.browserOperator)
        #self.tongzhidanPage = TongzhidanPage(self.demoProjectClient.browserOperator)
    # def test_open_url(self):
    #     self.indexPage.login('')
    #     assert_that(self.indexPage.getElements().title.wait_expected_value).is_equal_to(self.demoProjectClient.browserOperator.getTitle())

    def test_login(self):
        self.indexPage.login('liyh490','123456')
        assert_that('现场总管-欢迎登录').is_equal_to(self.demoProjectClient.browserOperator.getTitle())

        #assert_that('天津石化公司').is_equal_to(self.demoProjectClient.browserOperator.getTitle())
    # def tongzhidan(self):
    #     self.tongzhidanPage.chakantongzhidan()
    #     self.tongzhidanPage.chaxuntongzhidan("test")

    # def teardown_class(self):
    #     self.demoProjectClient.browserOperator.close()
