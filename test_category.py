from selenium.webdriver.common.by import By
from pages import wait_for

def test_category(driver):
    if "google_vignette" in driver.current_url:
        driver.get("https://automationexercise.com")
    
    wait_for(driver, By.CSS_SELECTOR, ".left-sidebar")
    assert "Category" in driver.page_source

    women = driver.find_element(By.CSS_SELECTOR, "a[href='#Women']")
    driver.execute_script("arguments[0].click();", women)
      
    tops = wait_for(driver, By.CSS_SELECTOR, "a[href='/category_products/2']")
    driver.execute_script("arguments[0].click();", tops)

    title = wait_for(driver, By.CSS_SELECTOR, ".title.text-center")
    assert title.text == "WOMEN - TOPS PRODUCTS"

    men = wait_for(driver, By.CSS_SELECTOR,"a[href='#Men']")
    driver.execute_script("arguments[0].click();", men)
    wait_for(driver, By.CSS_SELECTOR, "#Men")

    tshirts = wait_for(driver, By.CSS_SELECTOR, "a[href='/category_products/3']")
    driver.execute_script("arguments[0].click();", tshirts)
    print(driver.current_url)

    title = wait_for(driver, By.CSS_SELECTOR, ".title.text-center")
    assert " ".join(title.text.split()) == "MEN - Tshirts PRODUCTS"
    #split()이 공백을 모두 정리하고, join()이 한 칸으로 다시 합쳐준다.

#id 있나?
#↓
#있으면 By.ID

#없음
#   ↓
#a 태그인가?
#   ↓
#href로 찾기

#없음
#   ↓
#class 있나?
#   ↓
#CSS(.class)

#없음
#   ↓
#name 사용



