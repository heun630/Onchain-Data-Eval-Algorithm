## Random Test Data Generator

이 스크립트는 지정된 코인명과 데이터 타입에 대해 랜덤 테스트 데이터를 생성하고, 이를 `data/test` 디렉토리에 CSV 파일로 저장합니다.

## 사용 방법

다음 명령어를 사용하여 랜덤 테스트 데이터를 생성할 수 있습니다:

```bash
python3 make_test_results.py <result_count> <coin_name> <data_name>
```

## 인자 설명

- <result_count>: 생성할 데이터 행의 수.
- <coin_name>: 암호화폐의 이름 (e,g: BTC, ETH).
- <data_name>: 데이터의 종류 (e.g: active_address, transaction_count).


