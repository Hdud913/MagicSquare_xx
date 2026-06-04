# D-* 테스트 ID (Logic Track)

M1 `SquareValidator` · PRD AC-1~4. 파일: `tests/control/test_d_<id>.py` (entity 분리 시 `tests/entity/`).

| ID | AC | 검증 요약 |
|----|-----|-----------|
| **D-AC1** | AC-1 | 정답 완성 격자 → `ok=true` (10선=34) |
| **D-AC2** | AC-2 | 행·열만 34, 대각선 1개 ≠34 → `ok=false`, 대각선 ∈ failures |
| **D-AC3** | AC-3 | `ok=false` 시 failures ≥1 (축 명시) |
| **D-AC4** | AC-4 | 중복·0 잔존·범위 위반 → `ok=false` |

**순서:** D-AC1 → D-AC2 → D-AC3 → D-AC4 (RED 1 ID당 1 사이클).

**예비 (M2+, 미착수):** D-M2-01 `MissingFinder`, D-E06 Entity 도메인 사유.
