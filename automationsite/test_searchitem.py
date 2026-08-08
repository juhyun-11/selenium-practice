from selenium.webdriver.common.by import By
from pages import add_product_to_cart,go_to_cart_from_header,go_to_cart_from_modal, wait_for

def test_searchitem(driver):
    prd_btn = wait_for(driver, By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", prd_btn)

    title = wait_for(driver, By.CSS_SELECTOR, "h2.title.text-center")
    assert "ALL PRODUCTS" in title.text

    driver.find_element(By.ID, "search_product").send_keys("maxi")
    search_btn = wait_for(driver, By.ID, "submit_search")
    driver.execute_script("arguments[0].click();", search_btn)

    title = wait_for(driver, By.CSS_SELECTOR, "h2.title.text-center")
    assert "SEARCHED PRODUCTS" in title.text

    products = driver.find_elements(By.CSS_SELECTOR, ".productinfo.text-center p")
    #상품명(p 태그)을 전부 찾아서 리스트에 저장한다
    #products안에는 상품들이 들어간다. elements 여러개라 -s가 붙는다

    assert len(products) > 0
    #len = Length(길이) 리스트 안에 몇 개가 들어있는지 알려준다.
    #검색 결과가 최소 1개 이상 있어야 한다.

    for product in products: #products 안에 있는 상품을 하나씩 꺼내라.
        assert "maxi" in product.text.lower()
    #검색 결과는 개수가 변경될 수 있기 때문에 find_elements()로 모든 상품을 가져옴
    #len()으로 검색 결과가 존재하는지 먼저 확인하고, 
    #for문으로 상품을 하나씩 반복하면서 상품명이 검색어(Dress)와 일치하는지 검증

    add_product_to_cart(driver,22)
    continue_btn = wait_for(driver,By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")
    driver.execute_script("arguments[0].click();", continue_btn)

    add_product_to_cart(driver,38)
    go_to_cart_from_modal(driver)
    
    page = driver.page_source.lower()
    assert "long maxi tulle fancy dress up outfits" in page
    assert "rose pink embroidered maxi dress" in page

    lg_btn = wait_for(driver, By.CSS_SELECTOR, "a[href='/login']")
    driver.execute_script("arguments[0].click();", lg_btn)
    driver.find_element(By.NAME, "email").send_keys("test2002!@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("asdf1234!")
    
    login_btn = wait_for(driver, By.CSS_SELECTOR, "[data-qa='login-button']")
    driver.execute_script("arguments[0].click();", login_btn)
    go_to_cart_from_header(driver)

    assert "Shopping Cart" in driver.page_source
