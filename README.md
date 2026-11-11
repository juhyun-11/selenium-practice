# QA Automation Practice

Python, Selenium, pytest로 [SauceDemo](https://www.saucedemo.com/)의 로그인·장바구니 기능을 검증하는 웹 UI 자동화 프로젝트입니다.

`main` 브랜치에 Push하면 GitHub Actions에서 테스트가 자동 실행됩니다.

버튼 클릭 성공 여부뿐 아니라 화면에 표시된 수량·상품명이 기대 결과와 일치하는지 검증하는 데 중점을 두었습니다.

## Tech Stack

Python / Selenium WebDriver / pytest / GitHub Actions

## Project Structure

```text
saucedomosite/
├── conftest.py             # driver fixture (브라우저 생성·종료, Headless 설정)
├── pages.py                # 명시적 대기 공통 함수 (wait_for)
├── test_swag_login.py      # 로그인 테스트
├── test_removecart.py      # 상품 1개 추가·삭제 테스트
└── test_cart_two_items.py  # 상품 2개 추가·삭제 테스트
```

## Test Scenarios

| 테스트 파일 | 검증 내용 |
|---|---|
| `test_swag_login.py` | 정상 계정 로그인 후 상품 목록 페이지(`inventory.html`) 진입 |
| `test_removecart.py` | 상품 1개 추가 → 배지·상품명 확인 → 삭제 → 배지 제거 → 쇼핑 계속하기 |
| `test_cart_two_items.py` | 상품 2개 추가 → 배지 `1`, `2` 확인 → 장바구니 상품 2개·상품명 확인 → 1개 삭제 → 배지 `1`·잔여 상품명 확인 |

## Troubleshooting

### 1. 장바구니 상품 개수 검증 실패 (`assert 6 == 2`)

- **현상:** 상품 2개를 추가했으나 장바구니 상품 개수 검증 시 상품명 요소가 6개 조회됨
- **원인 분석:** 장바구니 아이콘 클릭 직후 `find_elements()`를 호출해 화면 전환이 완료되기 전에 조회한 것으로 판단. 장바구니 화면 전환 완료를 확인하는 별도의 대기 조건이 없었으며, 조회된 6개는 상품 목록 페이지의 상품 수와 같음
- **해결:** 장바구니 페이지에만 있는 Checkout 버튼이 나타날 때까지 대기한 뒤 상품 목록을 조회하도록 수정. 이후 테스트 통과

```python
cart.click()
wait_for(driver, By.CSS_SELECTOR, "[data-test='checkout']")

items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
assert len(items) == 2
```

### 2. GitHub Actions에서 로그인 테스트 실패 (`session not created`)

- **현상:** 로컬에서는 통과하던 로그인 테스트가 GitHub Actions 환경에서 실패
- **원인 분석:** 로그인 테스트만 공통 fixture를 사용하지 않고 `webdriver.Chrome()`을 직접 실행해 Headless 옵션이 적용되지 않았음. 이전 workflow는 특정 테스트 파일만 실행해 CI에서 해당 문제가 드러나지 않았으며, 로컬과 CI의 실행 환경 차이로 실패한 것으로 판단
- **해결:** 로그인 테스트도 공통 `driver` fixture를 사용하도록 변경하고, workflow를 전체 테스트 실행으로 수정. 이후 테스트 3건 통과

## CI - GitHub Actions

`main` 브랜치에 Push하면 다음 순서로 자동화 테스트가 실행됩니다.

1. 저장소 코드 Checkout
2. Python 3.12 및 의존성 설치
3. Headless Chrome에서 `python -m pytest -v` 실행
4. GitHub Actions 로그에서 PASS/FAIL 결과 확인

특정 테스트 파일을 개별 지정하지 않고 pytest의 자동 수집 기능을 사용했습니다. 새로운 `test_*.py` 파일을 추가하면 workflow를 수정하지 않고도 함께 실행할 수 있습니다.

**최근 실행 결과**

| 실행 환경 | Python | 테스트 결과 |
|---|---|---|
| Ubuntu Linux | 3.12 | `3 passed` |
[![Selenium E2E Test](https://github.com/juhyun-11/selenium-practice/actions/workflows/selenium.yml/badge.svg)](https://github.com/juhyun-11/selenium-practice/actions/workflows/selenium.yml)

## Run Tests

**준비**

- Python 3.12 (CI 검증 환경), Chrome 브라우저
- 의존성 설치: `pip install pytest selenium`

`saucedomosite` 폴더에서 실행합니다.

```bash
# 전체 테스트 실행
python -m pytest -v

# 특정 테스트 파일 실행
python -m pytest test_removecart.py -v
```

로그인 계정은 SauceDemo가 공개한 테스트 계정(`standard_user`)을 사용합니다.

## Related

- [automation-exercise-api-testing](https://github.com/juhyun-11/automation-exercise-api-testing): Postman 기반 API 응답 검증 프로젝트 (GitHub Actions 미연동)

## Improvements

- **Page Object 패턴 적용:** 로케이터와 페이지별 동작을 분리하여 코드 재사용성 및 유지보수성 개선
- **테스트 시나리오 확장:** 상품 정렬, 추가·삭제 조합 등 검증 조건 확대
- **테스트 리포트 생성:** pytest-html 또는 Allure를 활용한 실행 결과 시각화
