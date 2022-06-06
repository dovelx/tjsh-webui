# conftest.py

driver = None


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver

    if driver is None:
        driver = webdriver.Chrome()  # GUI界面运行
        driver.maximize_window()

    return driver  # 返回驱动