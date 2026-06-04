# MagicSquare_xx — RED 단계 ToDo List

| 항목 | 내용 |
|------|------|
| **버전** | 0.1 |
| **작성일** | 2026-06-04 |
| **프로젝트** | MagicSquare_xx |
| **근거** | [PRD.md](PRD.md) AC-1~4, `.cursorrules` E001~E007, [reference.md](../.cursor/skills/magic-square-tdd/reference.md) |
| **상태** | Harness 완료 · 테스트 본문 ⏳ 미착수 |

Dual-Track TDD **RED Phase** 설계표. 각 항목은 **1 ID = 1 파일**, RED → GREEN → REFACTOR 한 사이클씩 진행한다.

---

## 진행 순서 (M1 우선)

| 순서 | Track | ID | 파일 (예정) |
|:---:|:---|:---|:---|
| 1 | Logic | D-AC1 | `tests/control/test_d_ac1.py` |
| 2 | Logic | D-AC2 | `tests/control/test_d_ac2.py` |
| 3 | Logic | D-AC3 | `tests/control/test_d_ac3.py` |
| 4 | Logic | D-AC4 | `tests/control/test_d_ac4.py` |
| 5+ | Boundary | U-IN-01 ~ | `tests/boundary/test_u_*.py` |

---

## Logic Track (control · `D-*`)

`SquareValidator.validate(grid)` — PRD AC-1~4. **도메인 Mock 금지**, 정적 격자 fixture만 사용.

| Test ID | Given | Then (기대값) | Expected RED Failure |
|:---|:---|:---|:---|
| D-AC1 | 정답 완성 격자 **G1** (10선=34) | `ok=true`, `failures=[]` | `ModuleNotFoundError` |
| D-AC2 | **G2**: 행·열만 34, 주대각선 ≠34 | `ok=false`, `diag_main` ∈ failures | `AssertionError` |
| D-AC3 | **G2** (또는 임의 fail 격자) | `ok=false`, `len(failures)≥1`, 축 식별자 명시 | `AssertionError` |
| D-AC4a | **G4a**: 1~16 중복 포함 | `ok=false` | `AssertionError` |
| D-AC4b | **G4b**: `0` 잔존 완성 격자 | `ok=false` | `AssertionError` |
| D-AC4c | **G4c**: 값 범위 위반 (예: `17`) | `ok=false` | `AssertionError` |

### ToDo

- [ ] **D-AC1** — `tests/control/test_d_ac1.py` 작성 · Given **G1** · Then `ok=true`, `failures=[]` · RED: `ModuleNotFoundError`
- [ ] **D-AC1 GREEN** — `SquareValidator` 최소 구현 · pytest PASS
- [ ] **D-AC2** — `tests/control/test_d_ac2.py` 작성 · Given **G2** · Then `ok=false`, `diag_main` ∈ failures · RED: `AssertionError`
- [ ] **D-AC2 GREEN** — 대각선 실패 판정 구현 · pytest PASS + Logic suite 회귀
- [ ] **D-AC3** — `tests/control/test_d_ac3.py` 작성 · Then `len(failures)≥1` · RED: `AssertionError`
- [ ] **D-AC3 GREEN** — 실패 축 목록 반환 구현 · pytest PASS + Logic suite 회귀
- [ ] **D-AC4a** — 중복 격자 **G4a** · Then `ok=false` · RED: `AssertionError`
- [ ] **D-AC4b** — `0` 잔존 **G4b** · Then `ok=false` · RED: `AssertionError`
- [ ] **D-AC4c** — 범위 위반 **G4c** · Then `ok=false` · RED: `AssertionError`
- [ ] **D-AC4 GREEN** — R1·R2 위반 판정 구현 · pytest PASS + Logic suite 회귀

---

## Boundary Track (boundary · `U-*`)

입력 검증(E001~E005), 출력·좌표, ECB 흐름. M1 1차 이후 또는 M4 전 확장.

| Test ID | Given | Then (기대값) | Expected RED Failure |
|:---|:---|:---|:---|
| U-IN-01 | `grid=None` | `E003` `INVALID_NULL` | `ModuleNotFoundError` |
| U-IN-02 | `grid=3×4` | `E001` `INVALID_SIZE` | `AssertionError` |
| U-IN-03 | 빈칸 0개 | `E002` `INVALID_BLANKS` | `AssertionError` |
| U-IN-04 | 빈칸 3개 이상 | `E002` `INVALID_BLANKS` | `AssertionError` |
| U-IN-05 | 셀 값 `17` 또는 `-1` | `E005` `INVALID_VALUE` | `AssertionError` |
| U-IN-06 | 좌표 `(r,c)=(5,1)` | `E004` `INVALID_COORD` | `AssertionError` |
| U-OUT-01 | 유효 부분 격자 **G0** | E00x 없음, Handler 통과 | `pytest.fail()` RED |
| U-OUT-02 | Solver 결과 `[r1,c1,n1,r2,c2,n2]` | `len(result)==6`, 좌표 1~4 | `pytest.fail()` RED |
| U-OUT-03 | validate fail + failures | `ResultDisplay` 축 목록 표시 | `pytest.fail()` RED |
| U-FLOW-01 | `grid=None` | `control.validate()` 0회 | `pytest.fail()` RED |
| U-FLOW-02 | `E001` 발생 입력 | `control.validate()` 0회 | `pytest.fail()` RED |
| U-FLOW-03 | 유효 **G0** | `control.validate()` 1회 | `pytest.fail()` RED |

### ToDo

- [ ] **U-IN-01** — `tests/boundary/test_u_in_01.py` · `grid=None` → `E003` · RED: `ModuleNotFoundError`
- [ ] **U-IN-02** — `test_u_in_02.py` · `grid=3×4` → `E001` · RED: `AssertionError`
- [ ] **U-IN-03** — `test_u_in_03.py` · 빈칸 0개 → `E002` · RED: `AssertionError`
- [ ] **U-IN-04** — `test_u_in_04.py` · 빈칸 3개+ → `E002` · RED: `AssertionError`
- [ ] **U-IN-05** — `test_u_in_05.py` · 범위 밖 값 → `E005` · RED: `AssertionError`
- [ ] **U-IN-06** — `test_u_in_06.py` · 좌표 범위 밖 → `E004` · RED: `AssertionError`
- [ ] **U-OUT-01** — `test_u_out_01.py` · **G0** 통과 · RED: `pytest.fail()`
- [ ] **U-OUT-02** — `test_u_out_02.py` · `int[6]` 출력 형식 · RED: `pytest.fail()`
- [ ] **U-OUT-03** — `test_u_out_03.py` · 실패 축 표시 · RED: `pytest.fail()`
- [ ] **U-FLOW-01** — `test_u_flow_01.py` · `grid=None` → validate 0회 · RED: `pytest.fail()`
- [ ] **U-FLOW-02** — `test_u_flow_02.py` · `E001` → validate 0회 · RED: `pytest.fail()`
- [ ] **U-FLOW-03** — `test_u_flow_03.py` · **G0** → validate 1회 · RED: `pytest.fail()`

---

## Fixture 참조

### G0 — 슬라이드 부분 격자 (빈칸 2)

```
16  3  2 13
 5 10 11  0
 9  6  0 12
 4 15 14  1
```

### G1 — 정답 완성 격자 (D-AC1)

```
16  3  2 13
 5 10 11  8
 9  6  7 12
 4 15 14  1
```

### G2 — 대각선만 실패 (D-AC2·AC-3)

G1 기준으로 주대각선만 깨지도록 구성 (행·열 34 유지).

### G4a / G4b / G4c — D-AC4

| ID | 조건 |
|:---|:---|
| G4a | 1~16 중복 포함 |
| G4b | `0` 잔존 (완성 격자) |
| G4c | 셀 값 범위 위반 (예: `17`) |

---

## Expected RED Failure 유형

| 유형 | 발생 시점 | 의미 |
|:---|:---|:---|
| `ModuleNotFoundError` / `ImportError` | `src/`에 대상 모듈 없음 | import 자체가 RED |
| `AssertionError` | 모듈은 있으나 판정·오류코드 불일치 | assert RED |
| `pytest.fail()` RED | ECB 배선·출력 형식 미구현 | 의도적 RED (U-OUT / U-FLOW) |

---

## RED 실행 명령 (참고)

```powershell
# Logic — 단일 ID
python -m pytest tests/control/test_d_ac1.py -v

# Boundary — 단일 ID
python -m pytest tests/boundary/test_u_in_01.py -v

# RED 직전 구조 확인
python -m pytest tests/ --collect-only -q
```

**기대:** `FAILED` 또는 `ERROR`. `PASSED`면 RED 아님.

---

## 변경 이력

| 버전 | 날짜 | 변경 |
|------|------|------|
| 0.1 | 2026-06-04 | RED 설계표 Boundary / Logic ToDo 초안 |
