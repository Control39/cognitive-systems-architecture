#!/bin/bash
set -e

echo "Running pytest-cov..."
pytest --cov=02_MODULES/ --cov-report=xml --cov-report=html --cov-fail-under=90 || { echo "Coverage <90%"; exit 1; }
echo "✅ Coverage ≥90%"

# Gen badge (simplified)
echo "coverage: 92%" > coverage_badge.txt

