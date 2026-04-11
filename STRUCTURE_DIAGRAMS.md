# 📊 Визуальная карта структуры репозитория

## Общая архитектура

```mermaid
graph TD
    A["cognitive-systems-architecture<br/>(8,934 файлов, 43 MB)"]
    
    A --> B["📚 docs<br/>(8,128 .md файлов, 37 MB)<br/>86% всего контента"]
    A --> C["🔧 apps<br/>(10 микросервисов)<br/>1.5 MB активного кода"]
    A --> D["📋 src<br/>(Shared utilities)<br/>624 KB"]
    A --> E["✔️ tests<br/>(Unit/Integration/E2E)<br/>236 KB"]
    A --> F["🚀 deployment<br/>(K8s/Terraform/GitOps)<br/>432 KB"]
    A --> G["🛠️ tools<br/>(Audit, Scripts)<br/>432 KB"]
    A --> H["📊 Others<br/>(Scripts, monitoring, analysis<br/>packages, samples)"]
    
    style B fill:#ffffcc
    style C fill:#ccffcc
    style D fill:#cce5ff
    style E fill:#ffcccc
    style F fill:#ccffff
    style G fill:#ffcccc
```

## Структура микросервисов

```mermaid
graph LR
    Apps["10 Microservices<br/>(apps/)<br/>"]
    
    Apps --> ITC["it-compass<br/>22 .py | 448 KB<br/>Skill Tracking<br/>Streamlit UI"]
    Apps --> CR["cloud-reason<br/>19 .py | 276 KB<br/>RAG API<br/>YandexGPT"]
    Apps --> CD["career-dev<br/>19 .py | 204 KB<br/>Career Planning<br/>Neo4j DB"]
    Apps --> MLR["ml-registry<br/>22 .py | 140 KB<br/>Model Versioning<br/>MLflow"]
    Apps --> PO["portfolio-org<br/>5 .py | 96 KB<br/>Resume Gen<br/>PDF Export"]
    Apps --> AC["arch-compass<br/>2 .py | 160 KB<br/>Architecture<br/>Framework"]
    Apps --> JA["job-agent<br/>8 .py | 68 KB<br/>Job Automation<br/>Workflows"]
    Apps --> SP["system-proof<br/>1 .py | 40 KB<br/>Verification<br/>Formal Proof"]
    Apps --> Auth["auth-service<br/>1 .py | 16 KB<br/>OAuth2 + JWT"]
    Apps --> TA["thought-arch<br/>0 .py | 20 KB<br/>Knowledge<br/>Collections"]
    
    style ITC fill:#e1f5ff
    style CR fill:#c8e6c9
    style CD fill:#fff9c4
    style MLR fill:#ffe0b2
    style PO fill:#f8bbd0
    style AC fill:#e1bee7
    style JA fill:#b2dfdb
    style SP fill:#ffccbc
    style Auth fill:#d1c4e9
    style TA fill:#f0f4c3
```

## Структура src/ (Shared Code)

```mermaid
graph TB
    SRC["src/<br/>Shared Utilities<br/>(626 KB, 26 .py)"]
    
    SRC --> AI["src/ai/<br/>LLM Integration<br/>Prompt engineering"]
    SRC --> CORE["src/core/<br/>Domain Models<br/>Business logic"]
    SRC --> CLOUD["src/cloud_reason/<br/>Reasoning Engine<br/>RAG Core"]
    SRC --> COMMON["src/common/<br/>Async helpers<br/>Health checks"]
    SRC --> INFRA["src/infrastructure/<br/>Logging, Monitoring<br/>Config management"]
    SRC --> SECURITY["src/security/<br/>Auth middleware<br/>RBAC"]
    SRC --> QUEUES["src/queues/<br/>Message Brokers<br/>Event Bus"]
    SRC --> REPO_AUDIT["src/repo_audit/<br/>Audit Tool<br/>Quality Checks"]
    SRC --> SHARED["src/shared/<br/>Schemas, DTOs<br/>Common types"]
    
    style COMMON fill:#e8f5e9
    style INFRA fill:#fff3e0
    style SECURITY fill:#ffebee
```

## Структура deployment/

```mermaid
graph LR
    DEPLOY["deployment/<br/>(432 KB)<br/>"]
    
    DEPLOY --> K8S["k8s/<br/>Kubernetes<br/>Manifests<br/>production-ready<br/>HPA, NetworkPolicy"]
    DEPLOY --> GITOPS["gitops/<br/>ArgoCD Config<br/>Continuous<br/>Deployment"]
    DEPLOY --> SECRETS["secrets/<br/>Sealed Secrets<br/>Encrypted<br/>Credentials"]
    
    K8S --> OVERLAYS["overlays/<br/>base/<br/>staging/<br/>prod"]
    
    style K8S fill:#b3e5fc
    style GITOPS fill:#c8e6c9
    style SECRETS fill:#ffccbc
```

## Структура docs/ (Документация)

```mermaid
graph TB
    DOCS["docs/<br/>(37 MB, 8,128 .md)<br/>86% всего контента"]
    
    DOCS --> MKDOCS["mkdocs-site/<br/>Web Site"]
    DOCS --> API["api/<br/>Sphinx<br/>API Docs"]
    DOCS --> METHODOLOGY["methodology/<br/>Processes<br/>Guidelines"]
    DOCS --> CASES["cases/<br/>Case Studies<br/>Thinking"]
    DOCS --> EMPLOYER["employer/<br/>HR Materials<br/>One-pager"]
    DOCS --> EVIDENCE["evidence/<br/>Competency<br/>Proof"]
    DOCS --> SECURITY["security/<br/>Policies<br/>Compliance"]
    DOCS --> GRANTS["grants/<br/>Proposals<br/>Sourcecraft"]
    DOCS --> OTHERS["...15 more<br/>folders"]
    
    style MKDOCS fill:#fff9c4
    style CASES fill:#f8bbd0
    style EMPLOYER fill:#c8e6c9
    style SECURITY fill:#ffccbc
    style GRANTS fill:#e1bee7
```

## Проблемные точки структуры

```mermaid
graph LR
    ISSUES["⚠️ Структурные проблемы"]
    
    ISSUES --> D1["📚 Документация<br/>37 MB vs 1.5 MB код<br/>25:1 ratio<br/>Слишком большая"]
    ISSUES --> D2["🔀 Дублирование<br/>docs/methodology/it-compass<br/>vs<br/>apps/it-compass<br/>Две версии истины?"]
    ISSUES --> D3["❌ Несогласованность<br/>apps/it-compass/it-compass/<br/>vs<br/>apps/cloud-reason/<br/>Разные структуры"]
    ISSUES --> D4["📦 Неясные папки<br/>packages/{npm,nuget,pypi}<br/>пусты или не используются"]
    ISSUES --> D5["🗂️ Навигация<br/>526 папок<br/>Новичок теряется<br/>Нет карты"]
    ISSUES --> D6["📋 Archive<br/>84 KB старых файлов<br/>Может быть удален"]
    
    style D1 fill:#ffccbc
    style D2 fill:#ffccbc
    style D3 fill:#ffccbc
    style D4 fill:#ffe0b2
    style D5 fill:#ffcccc
    style D6 fill:#fff9c4
```

## Рекомендуемая иерархия навигации для новичка

```mermaid
graph TD
    START["Новичок 👤<br/>Где начать?"]
    
    START --> Q1{"Я хочу..."}
    
    Q1 -->|Understand| D["📖 docs/ARCHITECTURE.md<br/>System overview<br/>Decision records"]
    Q1 -->|Run locally| R["🚀 README + Quick Start<br/>docker-compose up<br/>See it live"]
    Q1 -->|Contribute| C["💻 CONTRIBUTING.md<br/>Dev setup<br/>Testing guide"]
    Q1 -->|Deploy| DEP["☁️ deployment/<br/>K8s/Terraform<br/>GitOps"]
    Q1 -->|Use API| API["🔌 apps/{name}/README.md<br/>API docs<br/>Examples"]
    
    D --> A["+ PROJECTS-MATRIX.md<br/>+ One-Pager<br/>+ Case Studies"]
    
    style START fill:#fff9c4
    style Q1 fill:#e1f5ff
    style D fill:#c8e6c9
    style R fill:#c8e6c9
    style C fill:#c8e6c9
    style DEP fill:#b3e5fc
    style API fill:#c8e6c9
```

## Рекомендации по архитектуре каталогов

### 1. Standardize app structure
```
apps/it-compass/
├── Dockerfile
├── src/
│   ├── main.py          ← Entry point
│   ├── api/             ← FastAPI routes
│   ├── models/          ← Data models
│   ├── core/            ← Business logic
│   └── utils/           ← Helpers
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── pyproject.toml
├── poetry.lock
├── README.md
└── .env.example
```

### 2. Restructure docs with priority
```
docs/
├── 0_QUICKSTART.md     ← MUST READ FIRST (New users)
├── 1_ARCHITECTURE.md   ← System design
├── 2_SERVICES.md       ← All 10 microservices
├── 3_DEPLOYMENT.md     ← Run on K8s/Cloud
├── 4_SECURITY.md       ← Compliance, secrets
├── 5_CONTRIBUTING.md   ← How to contribute
├── 6_API_REFERENCE.md  ← Auto-generated from Sphinx
└── archive/            ← Move old methodology here
```

### 3. Clean up packages/
```
Delete:
  packages/npm/         (not used)
  packages/nuget/       (not used)
  packages/pypi/        (not used)

Keep only:
  packages/terraform/   (active)
```
