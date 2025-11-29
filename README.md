# FlowStack Reminders Service

A minimal FastAPI-based microservice for scheduling reminders.

This repository is used to demonstrate an AI-powered pull-request review agent.
The agent:

- Fetches pull requests and diffs from GitHub.
- Reads relevant files in the PR.
- Uses a RAG index over `docs_rag/` to understand API specs, style guides, and logging rules.
- Generates review comments and suggests documentation updates.

Initially the service is just a skeleton; features are added over several pull requests.
