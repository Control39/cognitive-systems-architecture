# System Architecture Overview

*How chaos becomes intelligence*

---

## The Problem We're Solving

You have:
- **25,000+ scattered notes** across clouds, drives, local folders
- **Conversations with AI** that contain insights but are scattered across platforms
- **Code and projects** that evolved together but lack clear lineage
- **Decisions made** but never documented ("why did we choose this?")

**Result**: Knowledge exists but is inaccessible. You can't learn from your own patterns.

---

## The System (High Level)

```
Raw Data (Notes, Conversations, Code)
        ↓
    [RAG Layer] — Index & Retrieve
        ↓
  Relevant Context
        ↓
  [Reasoning Layer] — Analyze & Understand
        ↓
  Patterns & Insights
        ↓
[Classification Layer] — Organize & Map
        ↓
Competency Markers (Evidence)
        ↓
[Output Layer] — Generate Artifacts
        ↓
Portfolio / Reports / Decision Archive
```

---

## Layer 1: RAG (Retrieval-Augmented Generation)

### What It Does
Indexes all your data and makes it searchable by **meaning**, not just keywords.

### Example
```
User: "What did I learn about system design?"

RAG searches:
- Notes mentioning "system", "design", "architecture"
- Code comments about architectural decisions
- Conversation transcripts where you discussed systems
- Project evolution showing learning progression

Result: Returns 10 most relevant fragments from 5000+ files
```

### Key Features
- **Semantic search** — finds meaning, not just keywords
- **Local processing** — your data stays on your machine
- **Scalable** — works with 100s or millions of documents
- **Runs offline** — no API calls, privacy-first

### Technology
- **Chromadb** — vector database for semantic search
- **Ollama** — local LLM for embeddings (or Yandex GPT API)
- **Python** — orchestration

### Why This Layer Matters
Without RAG, the next layer (Reasoning) would be blind. You need good context before analysis.

---

## Layer 2: Reasoning Layer

### What It Does
Takes the context from RAG and **reasons over it** to extract patterns and insights.

### Example
```
RAG returns: [10 text fragments about your learning path]

Reasoning asks:
"What patterns do you see in how this person approaches problems?"
"What evidence of systems thinking appears in these documents?"
"What was the decision-making process?"

Result: Structured analysis with citations
```

### Key Features
- **Deterministic output** — same input always produces same output
- **Chainable** — output from one reasoning cycle becomes input to the next
- **Auditable** — traces back to source documents
- **Model-agnostic** — works with any LLM (Ollama, Yandex GPT, Claude, etc.)

### Technology
- **LLM** — Ollama (local), Yandex GPT (API), or any OpenAI-compatible API
- **Prompt engineering** — structured prompts for consistent output
- **Python** — orchestration

### Why This Layer Matters
RAG gives you data. Reasoning tells you what it means.

---

## Layer 3: Classification Layer

### What It Does
Organizes reasoning output into a **taxonomy** (hierarchy of skills, competencies, patterns).

### Example
```
Reasoning found: "You designed a Docker setup for a Python app"

Classification asks:
"Which competency markers does this satisfy?"
- ✅ Docker: Create Dockerfile
- ✅ Docker: Run container
- ✅ Systems: Design for scalability

Updates:
- Competency "Docker" now shows 2/5 markers complete
- Competency "Systems" shows progress
```

### Key Features
- **Taxonomy-driven** — every finding is classified
- **Auto-generated** — happens without manual work
- **Updatable** — taxonomies can be adapted (finance, research, etc.)
- **Feedback loop** — classifications become new data for RAG

### Technology
- **YAML definitions** — taxonomies defined as config files
- **Python** — matching engine
- **Database** — stores classifications and relationships

### Why This Layer Matters
Classification turns loose insights into actionable, measurable competencies.

---

## Layer 4: Output Generation Layer

### What It Does
Takes everything (raw data, reasoning, classifications) and generates **artifacts**:
- Portfolio pages
- Hiring briefs
- Decision archives
- Roadmaps
- Reports

### Example
```
Portfolio auto-generated from:
- All RAG findings about your work
- Reasoning analysis of your thinking patterns
- Classification markers you've satisfied
- Evidence links back to source documents

Result: Markdown portfolio that's always up-to-date
```

### Key Features
- **Auto-updated** — runs after each reasoning cycle
- **Multi-format** — Markdown, JSON, PDF, HTML
- **Templatable** — customize outputs per audience
- **Linked** — every claim traces back to evidence

### Technology
- **Jinja2** — templating
- **Python** — generation logic
- **Git** — stores outputs for versioning

### Why This Layer Matters
Output is where the system's value becomes visible. Bad output = nobody believes the system works.

---

## The Feedback Loop

```
Reasoning generates insights
    ↓
Classification organizes them
    ↓
Output presents them
    ↓
You review and find NEW questions
    ↓
New questions go back to RAG
    ↓
Repeat (Cycle 2, 3, 4, ...)
```

Each cycle:
- Extracts deeper insights
- Builds on previous findings
- System learns about itself

---

## System Design Principles

### 1. Layered (Not Monolithic)
Each layer has clear input/output. Swap any layer without breaking others.

**Example**: Replace Ollama with Yandex GPT? Just change the Reasoning layer.

### 2. Local-First (With Cloud Option)
Default: Everything runs on your machine (privacy, speed).  
Option: Cloud APIs available for scale.

**Example**: Personal use case → laptop + Ollama. Enterprise → Kubernetes + Yandex GPT API.

### 3. Auditable (Every Decision Logged)
Every output links back to:
- Source document
- Reasoning process
- Classification decision

**Example**: "Why do I have the 'Docker' marker?" → System shows exact evidence.

### 4. Feedback-Driven (System Learns)
Output of one cycle becomes input to the next. System gets better over time.

**Example**: First cycle finds "Docker basics". Second cycle finds "Docker optimization patterns". Third cycle finds "Docker architectural patterns".

### 5. Methodology First (Code Second)
The methodology (what constitutes a competency) is more important than the code (how you implement it).

**Example**: Company can modify our code freely (MIT), but must credit methodology (CC BY-ND).

---

## Deployment Models

### Model 1: Local Development
```
Your Machine
├── Ollama (local LLM)
├── Chromadb (vector DB)
├── Python scripts
└── Your data (local files)

Start: docker-compose up -d
```

### Model 2: Team
```
Docker Host
├── Ollama (shared)
├── PostgreSQL (persistence)
├── API server
└── Multiple users

Scale: docker-compose scale
```

### Model 3: Enterprise
```
Kubernetes Cluster (Yandex Cloud)
├── RAG service (replicated)
├── Reasoning service (GPUs)
├── Classification service
├── Output service
├── PostgreSQL (managed)
└── Multiple teams

Scale: HPA + load balancing
```

---

## Data Flow Example

### Scenario: "What did I learn about system architecture?"

1. **RAG Layer**
   - Query: "system architecture"
   - Search vector database
   - Return: 5 notes + 3 code samples + 2 conversation fragments

2. **Reasoning Layer**
   - Input: Those 10 documents
   - Analysis: "What architectural principles are demonstrated?"
   - Output: Structured analysis with citations

3. **Classification Layer**
   - Find matches to: "System Architecture" competency markers
   - Mark completed: "Design layered systems", "Handle component decoupling"
   - Progress: "3/5 markers complete"

4. **Output Layer**
   - Generate: Portfolio entry "System Architecture: 3/5"
   - Include: Evidence links, explanation, learning path
   - Publish: Markdown to docs/portfolio/system-architecture.md

5. **Feedback Loop**
   - You read portfolio
   - You think: "But I haven't done failure analysis..."
   - Add new marker: "Analyze system failures"
   - Next cycle includes new searches for that topic
   - RAG finds relevant conversations
   - Cycle repeats with more depth

---

## Why This Architecture Works

| Problem | Layer Solution |
|---------|---|
| "I have data but can't find it" | RAG layer makes it searchable |
| "I can find it but don't know what it means" | Reasoning layer analyzes it |
| "I have analysis but can't measure it" | Classification layer formalizes it |
| "I have evidence but nobody sees it" | Output layer presents it |
| "Each cycle I find more, but lose insights" | Feedback loop refines understanding |

---

## Next: How to Use It

See: `docs/GETTING_STARTED.md`

For methodology details: `METHODOLOGY/it-compass/METHODOLOGY.md`

For code: `01_CORE/apps/`

---

**This architecture proves:** Chaos can become system. Thinking can be measured. Intelligence can be automated.
