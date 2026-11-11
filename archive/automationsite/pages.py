#pages.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value)))

def wait_invisible(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((by, value)))

def go_to_cart(driver):
    btn = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", btn)

def add_product_to_cart(driver, product_id):
    btn = driver.find_element(By.CSS_SELECTOR, f"a[data-product-id='{product_id}']")
    driver.execute_script("arguments[0].click();", btn)

def go_to_cart_from_modal(driver):
    btn = wait_for(driver, By.CSS_SELECTOR, "#cartModal a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", btn)


def go_to_cart_from_header(driver):
    btn = wait_for(driver, By.CSS_SELECTOR, "header a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", btn)

def add_recommend_to_cart(driver, product_id):
    # 추천상품 영역(recommended-item-carousel) 안에서
    # data-product-id가 일치하는 Add to Cart 버튼을 찾는다.
    btn = driver.find_element( By.CSS_SELECTOR,
        f"#recommended-item-carousel a[data-product-id='{product_id}']")
    driver.execute_script("arguments[0].click();", btn)

#외우는 규칙
# HTML                                                  | CSS Selector                      |
# ----------------------------------------------------- | --------------------------------- |
# `<div id="cartModal">`                                | `#cartModal`                      |
# `<div class="productinfo">`                           | `.productinfo`                    |
# `<a href="/login">`                                   | `a[href='/login']`                |
# `<input name="email">`                                | `input[name='email']`             |
# `<div id="cartModal"><a href="/view_cart"></a></div>` | `#cartModal a[href='/view_cart']` |

#id 있나?
#   ↓
#id

#없다
#   ↓
#class 있나?
#   ↓
#.class

#클래스가 여러 개다
#   ↓
#.class1.class2

#특정 태그다
#   ↓
#a[href='...']

#같은 게 여러 개다
#   ↓
#부모를 붙인다 ->  #recommended-item-carousel a[data-product-id='5']