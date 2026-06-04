---
name: magic-square-tdd
description: MagicSquare_xx Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. MagicSquare M1 구현, SquareValidator, RED/GREEN/REFACTOR, D-*/U-* 테스트, Logic/UI Track, ECB 계층 작업 시 사용.
---

# MagicSquare Dual-Track TDD

`.cursorrules`·`docs/PRD.md`·Report/01~02와 충돌 시 **`.cursorrules` 우선**. 테스트 ID 목록은 [reference.md](reference.md).

## 언제 이 Skill을 켜는지

| 트리거 | 예 |
|--------|-----|
| 사용자가 Skill·TDD·M1·SquareValidator를 명시 | 「magic-square-tdd로 RED」, 「AC-1 테스트」 |
| MagicSquare_xx에서 **Logic/UI Track** pytest 작성·구현 | `test_d_*`, `test_u_*` |
| **RED / GREEN / REFACTOR** Phase 작업 | Phase 선언이 필요한 모든 TDD 턴 |
| ECB 계층(`entity`/`control`/`boundary`) 코드 추가 | import·Mock·E00x 경계 확인 |
| **Review Loop** (계약 점검) 후 구현 재개 | ECB·AC 매핑 확인만 요청 |

**끄거나 Skill 없이:** 일반 문서 편집, git, README, Report 작성만 할 때.

---

## 매 턴 선언 (필수)

응답 맨 앞 1줄:

```
Phase: RED|GREEN|REFACTOR | Layer: entity|control|boundary | Track: Logic|UI | ID: D-*|U-*
```

---

## Logic Track vs UI Track

| | **Logic Track** | **UI Track** |
|---|-----------------|--------------|
| **Layer** | `entity`, `control` | `boundary` |
| **테스트 ID** | `D-*` | `U-*` |
| **파일** | `tests/{entity,control}/test_d_*.py` | `tests/boundary/test_u_*.py` |
| **Mock** | **도메인 Mock 금지** — 실제 규칙·객체·격자 fixture | Control·I/O **Mock/Stub 허용** |
| **M1 우선** | `SquareValidator`, AC-1~4 | E001~E007·좌표 변환 (2차 확장) |
| **금지** | `MagicSquare`/`Validator` Fake, 규칙 우회 stub | — |

---

## ECB · Mock · E001~E007

### ECB import (허용 그래프)

| 허용 | 금지 |
|------|------|
| Boundary → Control | Boundary → Entity |
| Control → Entity | Entity → Boundary, Entity → Control |
| | Control → Boundary |

### Mock

| 허용 | 금지 |
|------|------|
| Logic: **정적 격자 데이터**·순수 입력 fixture | Logic: Entity/Control **판정·규칙** 대체 Mock |
| UI: Control·stdin·display Stub | UI: Entity 규칙을 Boundary에서 재구현 |

### E001~E007 (Boundary SSOT)

| 코드 | 계층 | Entity |
|------|------|--------|
| E001~E005 | Boundary — 입력·형식·좌표·범위 | **처리 금지** |
| E006~E007 | Boundary 노출; **사유**는 Entity 도메인 | Entity가 **도메인 사유**만 반환 (코드 문자열 금지) |

Control: Entity 결과 → Boundary용 E006/E007 **매핑**만. E001~E005는 Boundary 입력 검증 단계.

---

## RED (5~7단계)

1. **선언** — Phase=RED, Layer·Track·`D-*`/`U-*` ID 확정 ([reference.md](reference.md)).
2. **범위** — PRD AC·Mom Test와 ID 1:1 매핑 확인; Solver·PyQt·Entity E001~E005 **범위 밖**.
3. **파일** — `test_d_*` 또는 `test_u_*` **1 ID만** 추가; 프로덕션 코드 **작성 금지**.
4. **assert** — 실패가 **의도된** 검증만; `skip`/`xfail`/완화 assert **금지**.
5. **실행** — 대상 테스트만 pytest → **FAIL 확인** (import error도 RED로 기록).
6. **증거** — 실패 테스트명·assert 메시지·명령어를 완료 보고에 포함.
7. **중단** — GREEN 코드 작성은 **다음 턴**(사용자 요청 또는 GREEN Phase)까지 보류.

```powershell
python -m pytest tests/control/test_d_<id>.py -v
```

---

## GREEN (5~7단계)

1. **선언** — Phase=GREEN, 동일 ID·Layer·Track 유지.
2. **최소 구현** — 해당 RED 1개를 통과시키는 **최소** 코드만; 올바른 ECB Layer에만 추가.
3. **SSOT** — `34`/`16`/`4` 리터럴 금지; MagicConstant 단일 모듈 import.
4. **ECB** — import 그래프·Entity E001~E005 금지 준수.
5. **실행** — 대상 `D-*`/`U-*` pytest → **PASS**.
6. **회귀** — Logic Track 전체: `tests/entity` + `tests/control` **전부 PASS**.
7. **중단** — REFACTOR는 suite green 확인 후; assert·테스트 삭제로 통과 **금지**.

```powershell
python -m pytest tests/control/test_d_<id>.py -v
python -m pytest tests/entity tests/control -v
```

---

## REFACTOR (5~7단계)

1. **선언** — Phase=REFACTOR; **동작 변경 없음** 명시.
2. **대상** — 중복 제거·이름 정리·MagicConstant·ECB 경계 정리만.
3. **금지** — assert 완화·테스트 삭제·`skip`/`xfail`·기능 추가.
4. **ECB 재확인** — import 역방향·Layer 침범 없음.
5. **실행** — **전체** pytest suite → **ALL PASS**.
6. **UI 포함** — boundary touched 시 `tests/boundary` 포함.
7. **보고** — 구조 변경 요약·pytest 결과·다음 RED ID 제안.

```powershell
python -m pytest tests/ -v
```

---

## Test Loop · Review Loop · pytest

### 개발 Test Loop (TDD)

```
RED → pytest FAIL → GREEN → pytest PASS (ID + Logic suite)
    → REFACTOR → pytest ALL PASS → 다음 RED (reference.md)
```

### 제품 Test Loop (PRD §5.4)

```
grid → validate → pass 종료
              → fail → failures 확인 → grid 수정 → validate
```

Logic Track `D-*`가 위 루프를 **자동화**한다. UI Track `U-*`는 Boundary 표현·E00x·좌표 변환.

### Review Loop (pytest 최소)

| 시점 | pytest | 목적 |
|------|--------|------|
| 큰 설계 변경·ECB 리뷰 **전** | `python -m pytest tests/ --collect-only -q` | ID·파일 구조만 |
| 구현 **없는** 계약 리뷰 | 기존 suite 있으면 `python -m pytest tests/ -v` | 회귀 없음 확인 |
| RED **직전** | collect-only + reference.md 대조 | AC↔D-* 매핑 |
| RED | 대상 1파일 `-v` | **FAIL 기대** |
| GREEN | 대상 1파일 + Logic suite | **PASS** |
| REFACTOR | `tests/` 전체 | **ALL PASS** |
| UI 작업 | `tests/boundary/ -v` | U-* PASS |

---

## TDD 금지 (Skill 집행)

- assert 완화·삭제, `@pytest.mark.skip`, `xfail`, RED 없이 GREEN
- Logic Track 도메인 Mock, Entity의 E001~E005, golden/snapshot **사용자 승인 없이** 갱신
- git commit/push — **사용자 명시 요청 시만**

---

## 완료 보고 항목

매 Phase 종료 시 아래 체크리스트로 보고:

```markdown
## TDD 완료 보고
- Phase / Layer / Track / ID:
- 변경 파일:
- pytest 명령 + 결과 (FAIL|PASS|ALL PASS):
- ECB: import 위반 없음 ☐
- Mock: Logic 도메인 Mock 없음 ☐ / UI Stub만 ☐
- E00x: Entity E001~E005 미처리 ☐
- 금지 사항 위반 없음 ☐
- 다음: (RED 다음 ID | GREEN 동 ID | REFACTOR 후 RED)
```

---

## 참조

- 테스트 ID: [reference.md](reference.md)
- 헌법: `.cursorrules`
- AC·FR: `docs/PRD.md` §5~6
- Mom Test: `Report/01.MagicSquare_ProblemDefinition_Report.md`
