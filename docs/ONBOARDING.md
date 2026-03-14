# Onboarding & Cognitive-Drift Mitigation

## Formal Onboarding Checklist

1. **Clone & Setup**:
   ```
   git clone https://github.com/leadarchitect-ai/portfolio-system-architect.git
   cd portfolio-system-architect
   git lfs install
   ```

2. **Verify LFS**: `./scripts/check-lfs.sh`

3. **Local CI**:
   ```
   pip install -r requirements-dev.txt
   pytest BENCHMARK_SUITE/
   chmod +x BENCHMARK_SUITE/*.sh && BENCHMARK_SUITE/test_coverage.sh
   ```

4. **Run Stack**: `docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up -d`

5. **Verify**: http://localhost:8501 (IT-Compass), :8000/docs (Cloud-Reason), Grafana dashboards.

## Cognitive-Drift Mitigation

**Daily Protocol**:
- Run `./07_TOOLS/run_daily.ps1` → Review output.
- Check `low_energy_mode.log` in it-compass logs.
- Update `02_MODULES/it-compass/support/resources/crisis_contacts.json` if needed.

**Crisis Response**:
- `low_energy_mode.py` → Generate report: `python 02_MODULES/it-compass/src/core/mental/support.py`.
- Contacts from `crisis_contacts.json`.

**Mental Load Testing**:
1. Simulate 100RPS → Grafana RPS/CPU.
2. If CPU>70% or latency>200ms → Activate low_energy_mode.

## ADR Template

**Title**: [Short Title]

**Status**: Proposed | Accepted | Deprecated

**Context**: ...

**Decision**: ...

**Consequences**: ...

**Module Manifest Update**:
```json
{"adr": "path/to/adr.md", "version": "1.0"}
```

Sign-off: Signed-off-by: Name <email>

