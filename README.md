# AIFundamentals

This repository contains code and resources for the AI Fundamentals course. The course covers the basics of artificial intelligence, including machine learning, deep learning, and natural language processing.

## Course Content
- Introduction to AI
- Types of Learning
- Understanding the Machine Learning Process
- Neural Networks and Generative AI
- Prompt Engineering and AI Agents
- Using AI as a Competitive Edge

## Codespaces Setup
This repository includes Codespaces-ready configuration:
- VS Code extension recommendations in `.vscode/extensions.json` for Python, Jupyter, and Markdown WYSIWYG preview.
- Dev container config in `.devcontainer/devcontainer.json` that installs notebook kernel support (`jupyterlab`, `notebook`, `ipykernel`) after creation.
- Automatic MLflow startup on container start (`postStartCommand`) at port `8885`, matching the exercises.
- A manual fallback task in `.vscode/tasks.json` to start MLflow UI on port `8885`.

### Simple Browser
Simple Browser is built into VS Code (no extra extension install required).

To open MLflow from Codespaces:
1. MLflow starts automatically when the Codespace starts.
2. Open command palette and run: `Simple Browser: Show`.
3. Enter URL: `http://127.0.0.1:8885`.

If MLflow does not come up automatically, check logs at `/tmp/mlflow.log` and run task `Start MLflow UI (port 8885)`.