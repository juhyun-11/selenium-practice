from selenium.webdriver.common.by import By
from pages import add_recommend_to_cart, wait_for, go_to_cart_from_modal

def test_recommend(driver):
   # 페이지 맨 아래
   # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   # # 특정 요소까지
   # driver.execute_script("arguments[0].scrollIntoView();", element)
   # 조금만 내리기
   # driver.execute_script("window.scrollBy(0,500)") 

    recommend = wait_for(driver, By.ID, "recommended-item-carousel")
    driver.execute_script("arguments[0].scrollIntoView();", recommend)

    title = wait_for(driver, By.CSS_SELECTOR, ".recommended_items h2.title.text-center")
    #부모 안에서 찾는 게 가장 안정적
    assert title.text == "RECOMMENDED ITEMS"

    add_recommend_to_cart(driver, 5)
    go_to_cart_from_modal(driver)

    product = wait_for(driver, By.CSS_SELECTOR, ".cart_description")
    assert "Winter Top" in product.text