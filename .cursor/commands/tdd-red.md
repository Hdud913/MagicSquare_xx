# TDD RED — 실패 테스트 먼저

MagicSquare_xx **Dual-Track TDD** — RED Phase만 수행한다.  
`.cursorrules`·`docs/PRD.md`·`.cursor/skills/magic-square-tdd/reference.md`를 따른다.  
**프로덕션 코드(`src/`)는 작성·수정하지 않는다.**

명령 뒤에 붙은 텍스트(예: `D-AC1`, `control`)가 있으면 **대상 ID·Layer**로 사용한다.

---

## 필수 선언

응답 **첫 줄** (소문자 `red`):

```
Phase: red | Layer: entity|control|boundary | Track: Logic|UI | ID: D-*|U-*
```

---

## 절차

1. **ID 확인** — `reference.md`의 `D-AC1`~`D-AC4`(또는 사용자 지정 `D-*`/`U-*`) 1개만 선택. AC·Mom Test 매핑 확인.
2. **파일** — Logic: `tests/{entity,control}/test_d_<id>.py` · UI: `tests/boundary/test_u_<id>.py` (없으면 생성, **1 ID = 1 파일**).
3. **AAA 테스트** — Arrange(격자·입력 fixture) / Act(호출 대상 import·함수명만, **구현 없으면 import 실패로 RED**) / Assert(기대값, **의도적 실패**).
4. **실행** — 대상 파일만 pytest → **FAIL** 확인 (ImportError·AssertionError 모두 RED 증거).
5. **중단** — GREEN(`src/` 구현)은 하지 않는다. git commit은 사용자 요청 시만.

---

## pytest 예시 (bash)

```bash
# Logic — 단일 ID (M1 예: D-AC1)
python -m pytest tests/control/test_d_ac1.py -v

# UI Track
python -m pytest tests/boundary/test_u_e001.py -v

# RED 직전 구조 확인 (선택)
python -m pytest tests/ --collect-only -q
```

**기대:** `FAILED` 또는 `ERROR` (import). `PASSED`면 RED 아님 — assert·기대값을 재검토.

---

## 보고

```markdown
## RED 완료
- ID: D-AC?
- pytest: `...` → FAIL (한 줄 요약)
- 실패: test_xxx — AssertionError|ImportError: ...
- 변경 파일: tests/... 만 (tests/ 외 변경 없음 ☐)
- 다음: GREEN (사용자 요청 또는 /tdd-green)
```

---

## 금지

- `src/` **어떤 파일도** 작성·수정·삭제
- Logic Track **Domain Mock** (Validator/MagicSquare Fake, 규칙 우회 stub)
- assert **완화**·삭제, `@pytest.mark.skip`, `xfail`, 테스트 삭제로 FAIL 회피
- RED 1턴에 **복수 ID** 또는 GREEN·REFACTOR 혼합
- Solver 전체, PyQt, Entity의 E001~E005 처리
