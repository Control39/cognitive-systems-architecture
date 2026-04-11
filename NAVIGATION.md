# 🗺️ Repository Navigation Guide

Welcome! This repository contains **8 microservices** + architecture/documentation. Use this map to find what you need.

---

## 🚀 Quick Paths by Goal

### 🎯 "I want to understand what this is"
1. **Start**: [README.md](README.md) – 5 minute overview
2. **Deep dive**: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) – System design
3. **See services**: [docs/PROJECTS-MATRIX.md](docs/PROJECTS-MATRIX.md) – All 10 services
4. **For hiring managers**: [docs/EMPLOYER_ONE_PAGER.md](docs/EMPLOYER_ONE_PAGER.md) – 1-page summary

**Time investment**: 15 minutes | **Outcome**: Understand architecture & value

---

### 💻 "I want to run it locally"
1. **Quick Start** (top of [README.md](README.md))
   ```bash
   git clone https://github.com/Control39/cognitive-systems-architecture.git
   cd cognitive-systems-architecture
   docker-compose up
   ```
2. **What you'll see**:
   - 🌐 Dashboard: http://localhost (Traefik GUI)
   - 📊 Grafana: http://localhost:3000 (admin/admin)
   - 🔌 APIs: http://localhost:8001/docs (Cloud-Reason)
   - 🧭 UI: http://localhost:8501 (IT-Compass)

3. **Troubleshooting**: See [TROUBLESHOOTING.md](#) (or create issue)

**Time investment**: 5 minutes to run | **Outcome**: Working local environment

---

### 🔧 "I want to contribute code"
1. **Setup dev environment**: [CONTRIBUTING.md](CONTRIBUTING.md)
   - Fork the repo
   - Install dependencies: `pip install -e .`
   - Run tests: `pytest tests/`

2. **Understand code structure**:
   - Each service has own README in [apps/{name}/README.md](apps/)
   - Shared code: [src/](src/) (utilities, schemas, infrastructure)

3. **Make changes**:
   - Branch: `git checkout -b feature/my-feature`
   - Test: `pytest tests/unit/ && pytest tests/e2e/`
   - PR: Create PR with description

4. **Deploy your PR**:
   - CI runs automatically (.github/workflows/)
   - Merge triggers docker build + K8s deployment

**Time investment**: 2 hours setup | **Outcome**: Contributing ready

---

### ☁️ "I want to deploy to production"
1. **Requirements**:
   - Kubernetes cluster (or Yandex Cloud)
   - `kubectl` configured
   - Docker registry access

2. **Deployment docs**: [docs/DEVOPS_GITOPS_GUIDE.md](docs/DEVOPS_GITOPS_GUIDE.md)
   - Using GitOps (ArgoCD)
   - Manual `kubectl apply`
   - Terraform for infrastructure

3. **Infrastructure**:
   - K8s manifests: [deployment/k8s/](deployment/k8s/)
   - Terraform modules: [packages/terraform/](packages/terraform/)
   - Secrets: [deployment/secrets/](deployment/secrets/)

4. **Scaling**: [docs/scaling-plan.md](docs/scaling-plan.md)

**Time investment**: 2-4 hours setup | **Outcome**: Production deployment

---

### 📖 "I want to learn best practices"
1. **Architecture decisions**: [docs/adr/](docs/) – All ADRs (Architectural Decision Records)
2. **Git workflow**: [CONTRIBUTING.md](CONTRIBUTING.md)
3. **Security guidelines**: [docs/security/SECRETS-MANAGEMENT.md](docs/security/)
4. **Testing strategy**: [docs/testing/](docs/)
5. **DevOps patterns**: [docs/DEVOPS_GITOPS_GUIDE.md](docs/DEVOPS_GITOPS_GUIDE.md)

**Time investment**: Variable | **Outcome**: Learn patterns used here

---

## 📂 Directory Structure

### Core Directories

```
cognitive-systems-architecture/
│
├── 📦 apps/                       ← 10 MICROSERVICES (START HERE for code)
│   ├── it-compass/                (Skill tracking + Streamlit UI)
│   ├── cloud-reason/              (RAG API + YandexGPT — main AI service)
│   ├── career-development/        (AI-powered career planning)
│   ├── ml-model-registry/         (ML versioning + MLflow)
│   ├── portfolio-organizer/       (Auto-generate resume + portfolio)
│   ├── arch-compass-framework/    (Architectural framework)
│   ├── system-proof/              (Formal verification engine)
│   ├── job-automation-agent/      (Job automation workflows)
│   ├── auth-service/              (OAuth2 + JWT)
│   └── thought-architecture/      (Knowledge collections)
│
├── 🧠 src/                        ← SHARED UTILITIES (626 KB)
│   ├── ai/                        (LLM integration, prompts)
│   ├── core/                      (Domain models, business logic)
│   ├── common/                    (Async helpers, health checks)
│   ├── infrastructure/            (Logging, monitoring)
│   ├── security/                  (Auth middleware, RBAC)
│   └── [4 more]
│
├── ✔️ tests/                        ← TEST SUITE (95%+ coverage)
│   ├── unit/                      (Isolated unit tests)
│   ├── integration/               (Component integration)
│   └── e2e/                       (End-to-end workflows)
│
├── 🚀 deployment/                 ← INFRASTRUCTURE AS CODE (432 KB)
│   ├── k8s/                       (Kubernetes manifests + HPA)
│   ├── gitops/                    (ArgoCD configuration)
│   ├── secrets/                   (Encrypted credentials)
│   └── terraform/                 (Yandex Cloud, AWS templates)
│
├── 📚 docs/                       ← DOCUMENTATION (37 MB)
│   ├── ARCHITECTURE.md            ✅ START HERE (system overview)
│   ├── PROJECTS-MATRIX.md         (All services explained)
│   ├── EMPLOYER_ONE_PAGER.md      (For hiring managers)
│   ├── CONTRIBUTING.md            (Contributing guide)
│   ├── adr/                       (Architectural decisions)
│   ├── security/                  (Compliance, secrets)
│   ├── cases/                     (Case studies)
│   ├── api/                       (API documentation)
│   └── [13 more subdirs]
│
├── 🛠️ tools/                       ← UTILITY SCRIPTS (432 KB)
│   ├── repo_audit/                (Repository audit tool + checks)
│   └── scripts/                   (Helper scripts)
│
├── 📊 monitoring/                 ← OBSERVABILITY STACK
│   ├── prometheus/                (Metrics collection)
│   ├── grafana/                   (Dashboards)
│   └── alertmanager/              (Alerting)
│
├── 🔧 .github/                    ← CI/CD WORKFLOWS
│   └── workflows/                 (GitHub Actions configs)
│
├── [Other]: packages/, scripts/, analysis/, samples/, templates/
│
└── 📋 ROOT-LEVEL FILES (Config & README)
    ├── README.md                  ← MAIN ENTRY POINT
    ├── pyproject.toml             (Python dependencies)
    ├── docker-compose.yml         (Local dev stack)
    ├── project-config.yaml        (Project settings)
    └── [6 other configs]
```

---

## 🎯 Recommended Reading Order

### For New users (20 minutes)
1. [ ] [README.md](README.md) – "Quick Start" section (5 min)
2. [ ] Run `docker-compose up` and see it work (5 min)
3. [ ] Browse [docs/PROJECTS-MATRIX.md](docs/PROJECTS-MATRIX.md) (10 min)

**Result**: Understand what it does + it's running locally

### For contributors (1 hour)
1. [ ] [CONTRIBUTING.md](CONTRIBUTING.md)
2. [ ] [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
3. [ ] Pick a service in [apps/](apps/) and read its README
4. [ ] Run `pytest tests/unit/` to see test suite

**Result**: Ready to make first contribution

### For DevOps/Architects (2-3 hours)
1. [ ] [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
2. [ ] [docs/DEVOPS_GITOPS_GUIDE.md](docs/DEVOPS_GITOPS_GUIDE.md)
3. [ ] [deployment/k8s/](deployment/k8s/) manifests
4. [ ] [docs/security/SECRETS-MANAGEMENT.md](docs/security/) compliance

**Result**: Can review architecture + deploy to prod

### For Hiring Managers (5 minutes)
1. [ ] [docs/EMPLOYER_ONE_PAGER.md](docs/EMPLOYER_ONE_PAGER.md)
2. [ ] [docs/PROJECTS-MATRIX.md](docs/PROJECTS-MATRIX.md) (scan service list)
3. [ ] [README.md](README.md) (skim key stats)

**Result**: Understand technical depth + value

---

## 🔍 Finding Specific Things

### "Where is the IT-Compass code?"
- **App code**: [apps/it-compass/src/](apps/it-compass/)
- **Tests**: [apps/it-compass/tests/](apps/it-compass/)
- **API docs**: [apps/it-compass/README.md](apps/it-compass/README.md)
- **Docker build**: [apps/it-compass/Dockerfile](apps/it-compass/)

### "Where is the API documentation?"
- **Sphinx docs**: [docs/api/](docs/api/)
- **Swagger UI**: Run app and go to `/docs` (e.g., `localhost:8001/docs`)
- **OpenAPI schemas**: Each app has `openapi.json`

### "Where are the security policies?"
- **Security guidelines**: [docs/security/SECURITY.md](docs/security/SECURITY.md)
- **Secrets management**: [docs/security/SECRETS-MANAGEMENT.md](docs/security/)
- **Compliance**: [docs/security/COMPLIANCE.md](docs/security/)

### "Where are the deployment scripts?"
- **Kubernetes**: [deployment/k8s/](deployment/k8s/)
- **Terraform**: [packages/terraform/](packages/terraform/)
- **Docker Compose**: [docker-compose.yml](docker-compose.yml)
- **CI/CD workflows**: [.github/workflows/](github/workflows/)

### "Where is monitoring configured?"
- **Prometheus**: [monitoring/prometheus/](monitoring/prometheus/)
- **Grafana**: [monitoring/grafana/](monitoring/grafana/)
- **Alerting rules**: [monitoring/alertmanager/](monitoring/alertmanager/)
- **Dashboards**: Browse after running `docker-compose up`

### "Where are the tests?"
- **Unit tests**: [tests/unit/](tests/unit/)
- **Integration tests**: [tests/integration/](tests/integration/)
- **E2E tests**: [tests/e2e/](tests/e2e/)
- **Run all**: `pytest tests/`

---

## 📌 Most Important Files to Know

| File | Purpose | When to Read |
|------|---------|------------|
| [README.md](README.md) | Project overview + quick start | First thing |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute | Before making changes |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | System design | Understanding implementation |
| [docs/PROJECTS-MATRIX.md](docs/PROJECTS-MATRIX.md) | All services explained | Learning about features |
| [docs/DEVOPS_GITOPS_GUIDE.md](docs/DEVOPS_GITOPS_GUIDE.md) | Deployment instructions | Going to production |
| [docker-compose.yml](docker-compose.yml) | Local dev environment | Setting up locally |
| [pyproject.toml](pyproject.toml) | Python dependencies | Installing packages |
| [.github/workflows/](github/workflows/) | CI/CD pipelines | Understanding automation |

---

## 💡 Pro Tips

### Speed up navigation with aliases
```bash
alias csa="cd ~/cognitive-systems-architecture"
alias csa-app="cd ~/cognitive-systems-architecture/apps"
alias csa-docs="cd ~/cognitive-systems-architecture/docs"
```

### Quick checks
```bash
# See all services
ls -1 apps/

# Run tests
pytest tests/unit/ -v

# Check code quality
ruff check apps/ src/

# See services running locally
docker ps | grep portfolio

# Tail logs from one service
docker logs -f portfolio-cloud-reason
```

### Common commands
```bash
# Start development environment
docker-compose up -d

# Stop everything
docker-compose down

# Rebuild one service
docker-compose up -d --build cloud-reason

# Run full test suite
pytest tests/ --cov=apps --cov=src

# Format code
black apps/ src/

# Type check
mypy apps/ src/
```

---

## ❓ Stuck? Try These

### Problem: "I don't know where to start"
→ Read [README.md](README.md) "Quick Start" (5 min)

### Problem: "I want to contribute but don't know how"
→ Read [CONTRIBUTING.md](CONTRIBUTING.md)

### Problem: "I cloned but `docker-compose up` failed"
→ Check [docker-compose.yml](docker-compose.yml) and environment variables
→ See [TROUBLESHOOTING.md](#) (or create GitHub issue)

### Problem: "I need to understand the architecture"
→ Read [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

### Problem: "I want to deploy to K8s"
→ Read [docs/DEVOPS_GITOPS_GUIDE.md](docs/DEVOPS_GITOPS_GUIDE.md)

### Problem: "I found a bug"
→ Create [GitHub Issue](https://github.com/Control39/cognitive-systems-architecture/issues/new)

### Problem: "Security concern"
→ See [docs/security/SECURITY.md](docs/security/SECURITY.md) then create private advisory

---

## 🎯 Next Steps

**Just starting**?
- [ ] Clone: `git clone https://github.com/Control39/cognitive-systems-architecture.git`
- [ ] Run: `cd cognitive-systems-architecture && docker-compose up`
- [ ] Explore: Open http://localhost in browser

**Want to contribute**?
- [ ] Fork the repo
- [ ] Read [CONTRIBUTING.md](CONTRIBUTING.md)
- [ ] Pick an issue or feature
- [ ] Submit PR

**Want to deploy**?
- [ ] Read [docs/DEVOPS_GITOPS_GUIDE.md](docs/DEVOPS_GITOPS_GUIDE.md)
- [ ] Set up Kubernetes cluster
- [ ] Configure secrets
- [ ] Deploy with GitOps

**Have questions**?
- 💬 [Open a discussion](https://github.com/Control39/cognitive-systems-architecture/discussions)
- 🐛 [Report a bug](https://github.com/Control39/cognitive-systems-architecture/issues)
- 📧 Contact: leadarchitect@yandex.ru

---

**Last updated**: April 11, 2026  
**Maintainer**: @Control39  
**License**: MIT – see [LICENSE](LICENSE)
