# QA Automation Practice

## Overview

Python, Selenium, pytest를 활용한 웹 UI 자동화 테스트 프로젝트입니다.

QA 업무에서 반복적인 UI 기능 검증을 자동화하고, GitHub 저장소에 코드가 Push되면 테스트가 자동 실행되도록 GitHub Actions 기반 CI 환경을 구성했습니다.

현재 SauceDemo의 장바구니 기능을 대상으로 테스트를 작성하고 있으며, 테스트 조건과 실행 결과를 확인하면서 자동화 범위를 확장하고 있습니다.

## Tech Stack

- Python
- Selenium WebDriver
- pytest
- GitHub Actions

## Test Scenario

### 장바구니 상품 추가 및 삭제

**검증 목적**

상품 추가·삭제 후 장바구니 수량과 상품 정보가 기대결과에 맞게 변경되는지 검증합니다.

**검증 항목**

| 테스트 단계 | 기대결과 |
|---|---|
| 정상 계정 로그인 | 상품 목록 진입 |
| Bike Light 상품 추가 | 장바구니 배지 `1` 표시 |
| 장바구니 이동 | 추가한 상품명과 표시된 상품명 일치 |
| 상품 삭제 | 장바구니 배지 제거 |
| 쇼핑 계속하기 | 상품 목록 정상 복귀 |

**테스트 코드:** `saucedomosite/test_removecart.py`

## Test Implementation

### 1. 검증 조건 구체화

상품 추가 버튼 클릭 여부만 확인하지 않고, 장바구니 배지 수량과 실제 표시된 상품명을 함께 검증하도록 작성했습니다.

이를 통해 화면상 수량은 정상이어도 다른 상품이 표시되는 경우를 구분할 수 있도록 했습니다.

### 2. 테스트 실행 환경 분리

pytest fixture를 활용해 브라우저 실행과 종료를 관리하고, 화면이 로딩되거나 전환되는 과정에서 발생할 수 있는 오류를 줄이기 위해 필요한 화면 요소가 나타날 때까지 기다린 후 검증하도록 작성했습니다.

## CI - GitHub Actions

로컬에서만 테스트를 실행하는 방식에서 확장해, `main` 브랜치에 Push하면 GitHub Actions에서 테스트가 자동 실행되도록 설정했습니다.

**실행 흐름**

1. 저장소 코드 가져오기
2. Python 및 의존성 설치
3. Headless Chrome에서 Selenium 테스트 실행
4. pytest 결과를 GitHub Actions 로그에서 확인

**실행 결과**

- Ubuntu Linux / Python 3.12
- `test_removecart.py::test_remove_cart`
- `1 passed`

현재 CI는 장바구니 테스트 1건을 실행하도록 설정되어 있습니다.

## Run Tests

`saucedomosite` 폴더에서 실행:

```bash
python -m pytest test_removecart.py -v
```

## Improvements

- 복수 상품 추가·삭제 시 수량 변경 검증
- 로그인 및 장바구니 테스트의 재사용 구조 개선
- 자동화 대상 시나리오 확대
- CI 실패 로그를 활용한 원인 분석 연습