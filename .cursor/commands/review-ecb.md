# Review ECB — 계약 리뷰 (코드 수정 금지)

MagicSquare_xx **Review Loop** — ECB·도메인 계약 **위반만** 표로 보고한다.  
`.cursorrules`·`docs/PRD.md`·Report/01~02를 SSOT로 삼는다.

**파일·코드·테스트를 작성·수정·삭제하지 않는다.**  
리뷰 대상이 없으면 `@src/` `@tests/` 또는 명령 뒤 경로를 읽어 분석한다.

명령 뒤 텍스트(예: `src/control`, `tests/control/test_d_ac1.py`)가 있으면 **범위**로 한정한다.

---

## 필수 선언

응답 **첫 줄**:

```
Phase: review | Scope: src/|tests/|path | Track: Logic|UI|both
```

---

## 절차

1. **범위** — `src/{entity,control,boundary}`, `tests/` (또는 사용자 지정) 읽기만.
2. **5항목 스캔** — 아래 체크리스트 각각 **PASS / VIOLATION / N/A**.
3. **위반만 표** — VIOLATION 행만 상세 표; PASS는 한 줄 요약.
4. **pytest** — 실행 **선택**. 구조 확인만 필요 시 `python -m pytest tests/ --collect-only -q` (수정 없음).
5. **중단** — 수정 제안은 **문장**으로만; 패치·커밋·GREEN/RED **금지**.

---

## 체크리스트 (계약)

| # | 항목 | PASS 기준 |
|---|------|-----------|
| 1 | **ECB import 방향** | Boundary→Control, Control→Entity만. Entity→Boundary/Control **금지**. Boundary→Entity·Control→Boundary **금지**. |
| 2 | **Entity E001~E005** | Entity에 입력·형식·좌표·범위 오류(E001~E005) 처리·문자열·raise **없음**. E006·E007 **도메인 사유**만. |
| 3 | **int[6] 1-index** | Solver/Boundary 출력 `[r1,c1,n1,r2,c2,n2]`, 행·열 **1~4**. Entity 내부 0-index 사용 시 Boundary에서만 변환. |
| 4 | **MagicConstant SSOT** | `34`/`16`/`4` 등 **단일 모듈** 정의; `src/`·`tests/`에 리터럴 **산재 없음**. |
| 5 | **Logic Track Domain Mock** | `tests/entity`·`tests/control`에 Validator/MagicSquare **Fake·규칙 우회 stub 없음**. 정적 격자 fixture는 허용. |

---

## 보고 형식 (위반만)

위반이 **없으면**:

```markdown
## ECB 리뷰 — 위반 없음
| # | 항목 | 판정 |
|---|------|------|
| 1~5 | (전 항목) | PASS |
```

위반이 **있으면** (VIOLATION 행만):

```markdown
## ECB 리뷰 — 위반 N건

| # | 항목 | 파일:줄 | 위반 내용 | 계약 (`.cursorrules`) |
|---|------|---------|-----------|------------------------|
| 1 | import 방향 | `src/entity/foo.py:3` | `from boundary import ...` | Entity → Boundary 금지 |
| … | … | … | … | … |
```

마지막 1줄: **다음 권장** — (GREEN 대상 Layer / Boundary 좌표 변환 / MagicConstant 모듈 추가 등, **코드 작성 없이**).

---

## 금지

- `src/`·`tests/`·설정 파일 **수정**
- 위반을 고치기 위한 **구현·테스트 추가** (별도 `/tdd-red`, `/tdd-green` 사용)
- VIOLATION 없는데 PASS 상세 나열로 **본문 장황화**
- git commit / push (사용자 요청 전)
