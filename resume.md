# Abhinav Pabba — Senior GenAI Engineer

**Contact:** abhinavpabba1402@gmail.com  •  +1 (469) 850-2895  •  Dallas, TX

## Professional Summary

Senior GenAI Engineer with 8 years of progression from data engineering and ML/NLP into production agentic AI systems, delivering across banking, healthcare, and CX technology under HIPAA, GDPR, and financial services compliance, with end-to-end ownership from prototype through enterprise rollout.

Built and operated enterprise agentic AI platforms on Anthropic Claude with LangGraph supervisor and sub-agent topologies, MCP-based tool registration, working memory backed by Redis, and structured fallback handling for autonomous multi-step research and compliance workflows across thousands of internal users.

Expert in LLM orchestration with deep hands-on experience across Anthropic Claude (Opus, Sonnet, Haiku) and OpenAI GPT-4 family, applying ReAct, Chain-of-Thought, and structured prompt engineering with version-controlled prompt libraries, function calling, and JSON-mode output parsing for enterprise AI applications.

Hands-on architect of production RAG pipelines spanning dense vector retrieval, hybrid BM25 plus vector search with cross-encoder re-ranking, and GraphRAG for multi-hop reasoning, building scalable retrieval systems across Pinecone, AWS OpenSearch, FAISS, ChromaDB, and Azure Cognitive Search.

Deep expertise in Agentic AI workflow development with dynamic tool calling, multi-step reasoning chains, and autonomous decision-making orchestration, building production multi-agent systems on LangGraph, LangChain, LangSmith, LangFlow, AutoGen, and CrewAI with Pydantic validation and enterprise-grade observability.

Hands-on with Model Context Protocol (MCP) server development, exposing internal enterprise systems as LLM-callable tool endpoints with standardized schema validation, hot-swappable routing, and OAuth2-scoped per-tool access controls for secure multi-agent consumption.

## Technical Skills

- **Languages & Frameworks:** Python, SQL, FastAPI, ReactJS, PyTorch, SpaCy, Pydantic
- **Agentic AI & Orchestration:** LangGraph, LangChain, LangSmith, AutoGen, CrewAI, MCP
- **LLMs & Models:** Anthropic Claude (Opus/Sonnet/Haiku), OpenAI GPT-4, BERT, T5
- **Cloud & Infrastructure:** AWS (Bedrock, SageMaker, EKS, Lambda, OpenSearch), Azure (AI Studio, ADF, Databricks, AKS), GCP Vertex AI, Docker
- **Vector Stores & Data:** Pinecone, FAISS, ChromaDB, AWS OpenSearch, Azure Cognitive Search, Snowflake, Delta Lake, Kafka, Spark
- **MLOps & Observability:** MLflow, LangSmith, Langfuse, GitHub Actions, Azure DevOps, BLEU/ROUGE/MRR evaluation

## Work Experience

### Citi Bank — Senior GenAI Engineer
*Dallas, TX | Oct 2025 – Present*

Contributed to and extended the agent orchestration layer for Citi Stylus Workspaces, Citi's internal agentic AI platform built on Anthropic Claude, collapsing multi-step research workflows into single-prompt executions for phased rollout to thousands of employees across global lines of business.

Designed LangGraph supervisor and sub-agent topology with specialized agents for intent routing, document retrieval, compliance cross-checks, and multilingual summarization, replacing manual multi-tool analyst workflows with autonomous agent execution governed by structured state transitions.

Implemented structured agent handoff patterns for cross-agent delegation, building structured handoff contracts with explicit state transfer, context preservation, and result schema validation so specialist agents could chain into multi-stage research and compliance pipelines without context drift.

Engineered agent handoff orchestration between supervisor and specialist agents using LangGraph conditional edges, implementing handoff guardrails that captured invoking agent identity, prior reasoning trace, and structured handoff payload to preserve auditability across agent boundaries.

Built LangChain orchestration chains for deterministic high-confidence intents within the broader LangGraph topology, combining sequential chain logic with retrieval-grounded responses to handle workflows that did not require full agentic branching, optimizing for latency and predictability.

Designed MCP (Model Context Protocol) server integrations exposing internal Citi systems including the global employee directory, risk APIs, and project management tools as LLM-callable tool endpoints with standardized schema validation, hot-swappable routing, and OAuth2-scoped per-tool access controls.

Implemented LangChain ConversationBufferMemory and ConversationSummaryMemory for short-term turn-level context, paired with Redis-backed working memory for multi-turn agent sessions, eliminating session state loss that caused repeated failures in pre-production testing.

Engineered vector store-backed long-term memory using Pinecone alongside LangChain memory abstractions, allowing agents to recall prior research artifacts and user preferences across sessions without inflating context window usage on every invocation.

Migrated agent retrieval from single-pass dense vector search to a hybrid BM25 plus vector search pipeline on Pinecone and AWS OpenSearch, adding a cross-encoder re-ranker before LLM context injection, resolving agent accuracy failures on regulatory and compliance document corpora.

Designed RAG ingestion pipelines for Citi policy, regulatory, and internal knowledge corpora with semantic chunking, embedding versioning, and incremental re-indexing, supporting the agent layer with grounded answers and citation-backed responses for compliance-sensitive queries.

Instrumented LangSmith tracing and Langfuse logging across production agent pipelines, capturing per-step latency, retrieval precision, tool call sequences, and LLM invocation patterns to enable proactive issue detection and regression analysis before rollout to new user cohorts.

Built LangFlow-based agent prototype environment for rapid iteration on supervisor topology and sub-agent prompts, enabling product and compliance stakeholders to validate agent behavior visually before promotion to the production LangGraph deployment.

Developed agent tool-use pipelines combining native Claude function calling with MCP-registered tools, implementing Pydantic argument validation, structured fallback handling, and retry logic for clean error recovery within autonomous agent loops.

Implemented Amazon Bedrock Guardrails with PII redaction, topic restrictions, and output grounding checks, mapping each control to specific Citi governance policy requirements in coordination with the enterprise AI risk team to satisfy pre-rollout compliance review.

Instrumented Kafka event streams feeding real-time transactional signals into the agent compliance layer, ensuring regulatory checks ran on live data and eliminating false-clear results caused by stale snapshot ingestion.

Built FastAPI microservice layer connecting internal banking systems to the agent orchestration backend, handling OAuth2 token lifecycle, per-route rate limiting, structured request logging, and audit trail persistence to satisfy pre-rollout security audit requirements.

Deployed all agent services as Dockerized microservices on AWS EKS with horizontal pod autoscaling, health-check probes, and blue-green deployment pipelines, enabling live agent logic updates with zero platform downtime during business hours.

Designed agent evaluation harness with BLEU, ROUGE, MRR, and Claude-based factuality checks for grounded retrieval responses, wiring evaluation gates into the CI/CD promotion flow so regressions in agent quality blocked promotion to the production user cohort.

Partnered with Citi enterprise AI risk and model governance teams to define agent observability requirements, audit trail retention policies, and Claude model selection criteria, translating governance needs into concrete instrumentation and logging contracts enforced at the LangGraph node level.

Established prompt versioning and prompt registry conventions using YAML-based prompt templates with semantic versioning, enabling controlled rollouts, A/B testing of prompt variants, and rollback paths when downstream agent behavior shifted unexpectedly.

### TTEC Digital — AI Engineer
*Dallas, TX | Apr 2023 – Sep 2025*

Built LangChain-based RAG pipelines for contact center AI products from role inception, combining deterministic chain logic for high-confidence intents with retrieval-grounded responses across enterprise knowledge bases, reducing live-agent escalation rates and improving first-contact resolution.

Deployed BERT and T5 transformer models for entity extraction and summarization on contact center transcripts, serving structured output to client analytics dashboards via REST APIs for real-time intent trend and resolution pattern reporting across enterprise customer service teams.

Built a full-stack AI application with a ReactJS frontend and FastAPI backend, serving inference through AWS SageMaker endpoints with session management, input sanitization, and response streaming for sub-second perceived latency on agent-assist surfaces.

Automated the SageMaker training and deployment pipeline using SageMaker Pipelines with S3-triggered execution and MLflow registry promotion, reducing model deployment cycle from multiple days of manual steps to under two hours.

Migrated the RAG pipeline from single-pass dense retrieval to hybrid BM25 plus vector search with cross-encoder re-ranking, resolving hallucinated policy citations flagged in QA and achieving production-grade answer grounding for client-facing knowledge surfaces.

Adopted LangGraph to introduce conditional graph routing for multi-step branching customer workflows, extending the existing LangChain pipelines with stateful agent topologies for cases that exceeded linear chain logic and required dynamic tool selection.

Piloted and integrated Microsoft GraphRAG pipelines, indexing entity-relationship graphs over product catalogs and policy hierarchies to enable multi-hop reasoning that flat chunk retrieval could not support.

Engineered an AutoGen planner and executor multi-agent workflow for back-office automation, decomposing multi-part client requests across specialist sub-agents for data lookup, calculation, and formatting.

Contributed to internal MCP integration patterns within TTEC's emerging agentic architecture, establishing tool schema conventions, error-contract standards, and authentication patterns adopted across subsequent agent deployments.

Implemented vector store-backed long-term memory using FAISS alongside LangChain ConversationBufferMemory for short-term context, resolving multi-turn session coherence failures and driving measurable improvement in self-service channel NPS scores.

Built CI/CD pipelines on GitHub Actions for model promotion from staging to production, integrating MLflow model registry stages, automated regression evaluation on held-out transcripts, and Slack-based approval gates for human review.

Mentored junior engineers on LangChain chain design, RAG retrieval tuning, and production FastAPI service patterns, codifying internal best practices into onboarding documentation.

### Accenture — Data Scientist / NLP Engineer
*Hyderabad, India | Jun 2021 – Aug 2022*

Led end-to-end development of AutoCoder, a BERT-based ICD-10 classification system for a major U.S. healthcare client, automating code assignment from unstructured clinical notes and achieving substantial reduction in manual coding effort.

Built SpaCy and regex-based NLP preprocessing pipelines extracting structured medical entities including diagnoses, symptoms, and medications from raw clinical notes.

Conducted GPU-based distributed training on PyTorch fine-tuning BERT across 20,000 de-identified clinical notes, benchmarking against rule-based and traditional ML baselines.

Applied post-training quantization to reduce production model memory footprint with negligible accuracy loss, enabling deployment on the client's existing Azure compute tier without additional infrastructure spend.

Built an ICD-10 semantic search assistant on Azure Cognitive Search indexed against the full code corpus, surfacing predicted codes with confidence scores alongside model output.

Secured all data access via Azure Key Vault secret management and AAD-based RBAC for compute and storage resources, implementing HIPAA compliance controls at project start.

Delivered Power BI dashboards surfacing real-time model accuracy, code coverage by diagnosis category, inference latency, and end-user feedback.

### Serendebyte Technology Solutions — Senior Data Engineer
*Tamil Nadu, India | May 2018 – May 2021*

Designed and deployed ADF and Apache Spark ETL pipelines on Databricks ingesting multi-source educational data into Delta Lake tables, implementing schema drift handling and late-arrival record management.

Architected hybrid on-premise to Azure and AWS data migration, building incremental load logic and cross-system reconciliation checks.

Built a Kafka-based real-time event streaming pipeline for student activity ingestion, replacing overnight batch jobs with low-latency data availability.

Optimized Spark transformations achieving 30% reduction in pipeline processing time on feature engineering workflows feeding model training.

Built Snowflake-based aggregate and dimensional layers on top of Delta Lake bronze and silver tables, enabling self-service BI access through Power BI and Tableau.

Established CI/CD for data pipelines using Azure DevOps with environment-aware parameterization, automated unit and integration testing of transformation logic.

## Education

- Master of Science in Computer Science, USA (2022–2024)
- Bachelor of Technology in Computer Science, India (2014–2018)
