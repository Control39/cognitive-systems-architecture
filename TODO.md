# Monitoring + GitHub Mirroring Implementation TODO

## [x] 1. Create monitoring stack files
- monitoring/prometheus/prometheus.yml
- monitoring/grafana/dashboards/portfolio.json  
- monitoring/grafana/provisioning/datasources/prometheus.yml
- docker-compose.monitoring.yml

## [x] 2. Create documentation
- 05_DOCUMENTATION/docs/monitoring.md

## [x] 3. Create GitHub Actions mirroring
- .github/workflows/mirror.yml (push to main trigger)

## [x] 4. Add Prometheus instrumentation to services (FastAPI apps; it-compass Streamlit optional)
- Edit cloud-reason FastAPI app + requirements.txt
- Edit ml-model-registry/src/api/main.py + requirements.txt
- it-compass /metrics endpoint if needed

## [ ] 5. Update README.md (monitoring section, badges, launch cmd)

## [ ] 6. Test
- docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up -d
- Verify Prometheus targets UP, Grafana dashboard
- docker compose down

## [ ] 7. Push to main → verify mirror Actions runs (user checks GitHub sync)
