# Cloud-Reason: AI Reasoning Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Cloud-Reason is an AI-powered reasoning engine designed for system architects and cognitive thinkers. Built on Yandex Cloud's serverless infrastructure, it leverages YandexGPT to analyze contexts, extract systemic thinking markers, and generate actionable insights.

## 🚀 Technology Stack
- **Serverless Architecture**: Yandex Cloud Functions + API Gateway
- **AI Engine**: YandexGPT for natural language understanding and reasoning
- **Storage**: Yandex Object Storage for context persistence
- **Language**: Python 3.11

## 📚 Documentation
Comprehensive documentation is available in the [docs/](docs/) directory:
- [INSTRUCTIONS.md](docs/INSTRUCTIONS.md) - Detailed setup and usage guide
- [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) - Common issues and solutions

## ⚙️ Setup & Installation

```bash
# Clone the repository
git clone https://sourcecraft.dev/leadarchitect-ai/cloud-reason.git

cd cloud-reason

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Copy .env.example to .env and update with your credentials
cp .env.example .env
```

## 🌐 API Usage

The engine provides a REST API for integration:

```python
import requests

# Send context for reasoning
data = {
    "context": "Your architectural context or problem statement here",
    "prompt": "Analyze the systemic thinking patterns in this context"
}

response = requests.post("https://your-api-gateway.cloud.yandex.net/reason", json=data)
print(response.json())
```

## 📂 Project Structure
```
cloud-reason/
├── api/                    # Reasoning API endpoints
├── docs/                   # Comprehensive documentation
├── scripts/                # Utility and deployment scripts
├── configs/                # Configuration files
├── tests/                  # Unit and integration tests
├── requirements.txt        # Python dependencies
└── .env.example            # Environment variables template
```

## 🤝 Contributing
Contributions are welcome! Please read our [contribution guidelines](CONTRIBUTING.md) before submitting pull requests.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏗️ Part of Cognitive-Architecture Ecosystem
This repository is a core component of the [Cognitive-Architecture](https://sourcecraft.dev/leadarchitect-ai/my-ecosystem) ecosystem, demonstrating systemic thinking through integrated AI-assisted development.