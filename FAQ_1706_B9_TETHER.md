# FAQ — Tether (B9)

## Q1. Have you built or contributed to systems involving asynchronous workflows? Explain your experience with queues like SQS, Kafka, or Pub/Sub.

Yes. I have hands-on experience designing and operating asynchronous, event-driven workflows in production-style environments for high-load backend and data platforms. In practice, I worked with queue-based processing patterns (including Kafka/RabbitMQ-class setups and cloud-queue analogs such as SQS/Pub/Sub style semantics): event contracts, retries with backoff, dead-letter queues, idempotent consumers, outbox/inbox patterns, and monitoring of consumer lag/throughput/error rate.

My role typically combined architecture and delivery leadership: breaking synchronous bottlenecks into resilient async stages, setting SLO/SLA guardrails, and building observability and runbooks for incident response. This helped improve throughput and system stability under peak load, while keeping business-critical flows predictable and auditable.

## Q2. Have you worked with vector databases (Pinecone, Weaviate, Qdrant, Elastic Vectors)? Describe the use case. What is your approach to reducing cost of operation for an AI pipeline? How do you work with ambiguous requirements and turn them into clear deliverables?

Yes. I have production-oriented experience with vector-search/RAG pipelines, including embeddings, chunking/indexing, retrieval tuning, and hybrid retrieval patterns (vector + lexical + structured filters). Typical use cases included enterprise knowledge search and AI assistant scenarios where relevance, latency, and answer grounding were critical. Depending on architecture constraints, I used dedicated vector stores and vector-capable search engines (for example, Qdrant/Elastic-style setups) as part of the same retrieval platform.

For AI pipeline cost optimization, I use a layered approach: right-size model selection by task, cache aggressively (embedding cache + response cache), reduce unnecessary token/context usage, apply retrieval filtering before generation, batch/background non-urgent jobs, and track cost-per-request as a first-class metric together with latency and quality.

For ambiguous requirements, I follow a structured conversion flow into deliverables: align on business outcomes and constraints, define measurable acceptance criteria, decompose into milestones with RACI ownership, and run short validation loops (MVP -> feedback -> refinement). This approach keeps execution transparent and allows iterative delivery without losing architectural integrity.
