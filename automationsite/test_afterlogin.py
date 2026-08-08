from selenium.webdriver.common.by import By
from pages import wait_for, add_product_to_cart, go_to_cart_from_modal, go_to_cart_from_header

def test_afterlogin(driver):
    prd_btn = wait_for(driver, By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", prd_btn)
    title = wait_for(driver, By.CSS_SELECTOR, ".title.text-center")
    assert "ALL PRODUCTS" in title.text

    driver.find_element(By.ID, "search_product").send_keys("shirts")
    search_btn = wait_for(driver, By.ID, "submit_search")
    driver.execute_script("arguments[0].click();", search_btn)
    title = wait_for(driver, By.CSS_SELECTOR, ".title.text-center")
    assert title.text == "SEARCHED PRODUCTS"

    products = driver.find_elements(By.CSS_SELECTOR, ".productinfo.text-center")
    # 검색 결과가 최소 1개 이상 노출되는지 확인
    assert len(products) > 0
    
    # 검색된 모든 상품명을 하나씩 확인
    for product in products:
        assert product.is_displayed()  # 글자 대신 "화면에 잘 보이니?"로 검증!
        #is_displayed()는 셀레늄에서 "이 글자나 이미지가 지금 모니터 화면에 실제로 '보이니(노출되고 있니)?'" 하고 컴퓨터에게 눈이 있냐고 물어보는 기능입니다.
        #화면에 잘 떠 있으면 True(참), 숨겨져 있거나 안 보이면 False(거짓)를 반환

    add_product_to_cart(driver, 12)
    go_to_cart_from_modal(driver)
    
    lg_btn = wait_for(driver, By.CSS_SELECTOR, "a[href='/login']")
    driver.execute_script("arguments[0].click();", lg_btn)
    wait_for(driver, By.NAME, "email").send_keys("test2002!@gmail.com")
    wait_for(driver, By.NAME, "password").send_keys("asdf1234!")
    login_btn = wait_for(driver, By.CSS_SELECTOR, "[data-qa='login-button']")
    driver.execute_script("arguments[0].click();", login_btn)
    go_to_cart_from_header(driver)

    shirt = wait_for(driver, By.CSS_SELECTOR, "#product-12 td.cart_description h4")
    assert "Half Sleeves Top Schiffli Detailing" in shirt.text

    #작성법            예시 코드              실제 HTML에서 찾는 대상
    #태그만 (점 없음)    td                   <td> ... </td>
    #클래스만 (점 있음)   .cart_description    <div class="cart_description"> 등등 전부
    #태그 + 클래스       td.cart_description  <td class="cart_description"> (가장 정확함)

