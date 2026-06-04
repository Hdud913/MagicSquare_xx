# MagicSquare_xx

4×4 **마방진(Magic Square)** 과제를 ECB(Entity–Control–Boundary) 패턴으로 설계·구현하는 프로젝트입니다.  
Mom Test로 검증한 **진짜 문제**(검증 누락·잘못된 완료)를 먼저 정의하고, 1차로 **`SquareValidator`**(10선 합 34 검증)를 구현합니다.

| 항목 | 내용 |
|------|------|
| **별칭** | MagicSquare_1004 (세션·워크북) |
| **도메인** | 4×4, 빈칸 2개(`0`), 1~16, **합 34**, **10선** 검증 |
| **상태** | 문제 정의·PRD 완료 — 구현(M1) 대기 |

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
├── docs/
│   └── PRD.md                                      # 제품 요구사항 (M1~M4)
├── Report/
│   ├── 01.REPORT.md                                # STEP 1 Mom Test 로그
│   └── 01.MagicSquare_ProblemDefinition_Report.md  # 문제 정의
├── Prompting/
│   ├── 01.REPORT.md                                # 대화 transcript
│   └── 01.MagicSquare_ProblemDefinition_Report.md  # 구현용 프롬프트
└── assets/                                         # 슬라이드·이미지 (workspace)
```

> `src/`, `tests/` — M1(`SquareValidator`) 구현 시 추가 예정.

---

## 문서

| 문서 | 설명 |
|------|------|
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test, 실패 조건, 세션 3 범위 |
| [docs/PRD.md](docs/PRD.md) | FR/AC, ECB 마일스톤, 1차 비목표 |
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

## 시작하기 (구현 후)

```powershell
cd C:\DEV\MagicSquare_xx
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pytest
python -m pytest -v
```

구현 전에는 문서만 있습니다. M1 작업 시 [Prompting/01.MagicSquare_ProblemDefinition_Report.md](Prompting/01.MagicSquare_ProblemDefinition_Report.md)의 지시 템플릿을 참고하세요.

---

## 라이선스

미정 (교육·과제 프로젝트).
