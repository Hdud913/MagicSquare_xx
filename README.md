# MagicSquare_xx

4×4 **마방진(Magic Square)** 과제를 ECB(Entity–Control–Boundary) 패턴으로 설계·구현하는 프로젝트입니다.  
Mom Test로 검증한 **진짜 문제**(검증 누락·잘못된 완료)를 먼저 정의하고, 1차로 **`SquareValidator`**(10선 합 34 검증)를 구현합니다.

| 항목 | 내용 |
|------|------|
| **별칭** | MagicSquare_1004 (세션·워크북) |
| **도메인** | 4×4, 빈칸 2개(`0`), 1~16, **합 34**, **10선** 검증 |
| **상태** | Harness·`.cursorrules` 완료 — M1 **RED** 단계 진행 중 |

---

## 진짜 문제 (Mom Test)

**페르소나:** 4×4 격자, 빈칸 2개(0), 1~16, 합 34를 맞추는 학습자.

**한 문장:** 지난 4×4 마방진 과제에서 빈칸 2개와 합 34를 맞추다 **행·열·대각선을 모두 검증하지 못해** 잘못 완료한 뒤 **20분**을 썼다.

**1차 목표:** 행 4 + 열 4 + 주·부대각선(**10선**)이 모두 34인지 판정하고, 틀리면 **어느 축**이 깨졌는지 알려 준다.

---

## 도메인 규칙

| 규칙 | 값 |
|------|-----|
| 격자 | 4×4 |
| 빈칸 | `0` (과제: 2개) |
| 완성 시 숫자 | 1~16, 중복 없음, `0` 없음 |
| 목표 합 | **34** (각 행·열·대각선) |
| **10선** | 행 4 + 열 4 + 주대각선 + 부대각선 |

**예시 (슬라이드):** (2,4), (3,3)이 빈칸인 4×4 격자에서 위치 특정 후 1~16으로 완성.

---

## 프로젝트 구조

```
MagicSquare_xx/
├── README.md
├── .cursorrules                                    # ECB · Dual-Track TDD 규칙
├── pyproject.toml
├── src/
│   ├── entity/
│   ├── control/
│   └── boundary/
├── tests/
│   ├── entity/
│   ├── control/                                    # Logic Track — test_d_*.py
│   └── boundary/                                   # UI Track — test_u_*.py
├── docs/
│   ├── PRD.md                                      # 제품 요구사항 (M1~M4)
│   └── TODO-RED.md                                 # RED 단계 설계표 · ToDo SSOT
├── Report/
│   ├── 01.REPORT.md                                # STEP 1 Mom Test 로그
│   ├── 02.REPORT.md                                # STEP 2 Harness · Cursor Rules
│   └── 01.MagicSquare_ProblemDefinition_Report.md  # 문제 정의
└── Prompting/
    ├── 01.REPORT.md
    └── 01.MagicSquare_ProblemDefinition_Report.md
```

---

## 문서

| 문서 | 설명 |
|------|------|
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test, 실패 조건, 세션 3 범위 |
| [docs/PRD.md](docs/PRD.md) | FR/AC, ECB 마일스톤, 1차 비목표 |
| [docs/TODO-RED.md](docs/TODO-RED.md) | RED 단계 설계표 · Fixture · Expected Failure |
| [Prompting/01.MagicSquare_ProblemDefinition_Report.md](Prompting/01.MagicSquare_ProblemDefinition_Report.md) | Cursor·에이전트용 프롬프트 |
| [Report/01.REPORT.md](Report/01.REPORT.md) | STEP 1 인터뷰·보고 이력 |

---

## ECB 로드맵

| 단계 | 구성 요소 | 상태 |
|------|-----------|------|
| **M1** | `SquareValidator`, Rule, Test Loop | ⏳ PRD P1 |
| **M2** | `MissingFinder` (빈칸 2개) | 계획 |
| **M3** | `Solver`, Entity (`MagicSquare`, `Cell`, `SolveResult`) | 계획 |
| **M4** | Boundary (`GridUI`, `InputHandler`, `ResultDisplay`) | 계획 |

**1차에서 하지 않음:** 전체 Solver, PyQt UI, 「프로그램/앱 완성」을 목표 문장으로 쓰는 것 (Mom Test 표면 문제).

---

## 1차 수용 기준 (요약)

| ID | 조건 |
|----|------|
| AC-1 | 정답 완성 격자 → `ok=true` |
| AC-2 | 대각선만 틀린 격자 → `ok=false`, 대각선 ∈ failures |
| AC-3 | `ok=false` 시 실패 축 ≥1개 명시 |
| AC-4 | 중복·0 잔존·범위 위반 → `ok=false` |

자세한 내용은 [docs/PRD.md](docs/PRD.md) §6.

---

## RED 단계 체크리스트

> **규칙:** 1 ID = 1 파일 · RED → GREEN → REFACTOR 순 · RED에서 `src/` 수정 금지  
> 상세 설계·Fixture(G0~G4)는 [docs/TODO-RED.md](docs/TODO-RED.md) 참조.

### Logic Track (`tests/control/test_d_*.py`) — M1 우선

- [ ] **D-AC1** — `test_d_ac1.py` · Given **G1** · Then `ok=true`, `failures=[]` · RED: `ModuleNotFoundError`
- [ ] **D-AC2** — `test_d_ac2.py` · Given **G2** · Then `ok=false`, `diag_main` ∈ failures · RED: `AssertionError`
- [ ] **D-AC3** — `test_d_ac3.py` · Then `ok=false`, `len(failures)≥1` · RED: `AssertionError`
- [ ] **D-AC4a** — 중복 격자 **G4a** · Then `ok=false` · RED: `AssertionError`
- [ ] **D-AC4b** — `0` 잔존 **G4b** · Then `ok=false` · RED: `AssertionError`
- [ ] **D-AC4c** — 범위 위반 **G4c** · Then `ok=false` · RED: `AssertionError`

### Boundary Track (`tests/boundary/test_u_*.py`) — M1 이후

**입력 (U-IN)**

- [ ] **U-IN-01** — `test_u_in_01.py` · `grid=None` → `E003` · RED: `ModuleNotFoundError`
- [ ] **U-IN-02** — `test_u_in_02.py` · `grid=3×4` → `E001` · RED: `AssertionError`
- [ ] **U-IN-03** — `test_u_in_03.py` · 빈칸 0개 → `E002` · RED: `AssertionError`
- [ ] **U-IN-04** — `test_u_in_04.py` · 빈칸 3개+ → `E002` · RED: `AssertionError`
- [ ] **U-IN-05** — `test_u_in_05.py` · 범위 밖 값 → `E005` · RED: `AssertionError`
- [ ] **U-IN-06** — `test_u_in_06.py` · 좌표 범위 밖 → `E004` · RED: `AssertionError`

**출력 (U-OUT)**

- [ ] **U-OUT-01** — `test_u_out_01.py` · **G0** 통과 · RED: `pytest.fail()`
- [ ] **U-OUT-02** — `test_u_out_02.py` · `int[6]` 출력 형식 · RED: `pytest.fail()`
- [ ] **U-OUT-03** — `test_u_out_03.py` · 실패 축 표시 · RED: `pytest.fail()`

**흐름 (U-FLOW)**

- [ ] **U-FLOW-01** — `test_u_flow_01.py` · `grid=None` → `validate()` 0회 · RED: `pytest.fail()`
- [ ] **U-FLOW-02** — `test_u_flow_02.py` · `E001` → `validate()` 0회 · RED: `pytest.fail()`
- [ ] **U-FLOW-03** — `test_u_flow_03.py` · **G0** → `validate()` 1회 · RED: `pytest.fail()`

---

## 시작하기

```powershell
cd C:\DEV\MagicSquare_xx
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"

# RED — 단일 ID (예: D-AC1)
python -m pytest tests/control/test_d_ac1.py -v

# RED 직전 구조 확인
python -m pytest tests/ --collect-only -q
```

RED 기대 결과: `FAILED` 또는 `ERROR` (import·assert). M1 작업 시 [docs/TODO-RED.md](docs/TODO-RED.md)와 [Prompting/01.MagicSquare_ProblemDefinition_Report.md](Prompting/01.MagicSquare_ProblemDefinition_Report.md)를 참고하세요.

---

## 라이선스

미정 (교육·과제 프로젝트).
