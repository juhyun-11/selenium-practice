#conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    #1.설정 준비
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)
    #2.준비된 설정으로 크롬을 "한 번만"켬
    driver = webdriver.Chrome(options=options)
#options는 Chrome 실행에 관련된 모든 커맨드라인 인자와 설정을 모아두는 컨테이너예요. 
#우리가 만든 prefs 딕셔너리를, options라는 더 큰 상자 안에 "이건 prefs 항목이야"라는 이름표를 붙여서 넣어요. 
#그리고 그 상자 전체를 webdriver.Chrome(options=options)처럼 Chrome을 켜는 그 명령어에 함께 넘겨줘요.

    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    yield driver #테스트한테 넘겨줌
    
    driver.quit() #테스트 끝난 뒤 정리