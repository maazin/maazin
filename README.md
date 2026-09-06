<div align="center">

<h1>Maazin Shaikh</h1>

<p><b>Software Engineer · AI/ML Engineer</b></p>

<p>
I build ML and LLM systems that reach real users — a deal-ranking model that lifted<br>
Publix app click-through <b>12%</b>, and retrieval systems serving <b>800+</b> students.
</p>

<p>
<a href="https://www.maazin.site"><img src="https://img.shields.io/badge/Portfolio-18181B?style=flat-square&logo=googlechrome&logoColor=white" alt="Portfolio"></a>
<a href="https://www.linkedin.com/in/maazin-shaikh"><img src="https://img.shields.io/badge/LinkedIn-18181B?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="mailto:contactmaazin@gmail.com"><img src="https://img.shields.io/badge/Email-18181B?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
</p>

<p><sub>Tampa, FL &nbsp;·&nbsp; B.S. Computer Science, University of South Florida &nbsp;·&nbsp; Open to full-time roles</sub></p>

</div>

<br>

## Selected Work

### WeakPoint &nbsp;<sub>[Code](https://github.com/maazin/Weak_Spot) · [Live](https://weakspot-web.fly.dev/)</sub>

Diagnoses *why* a code submission failed, not just that it did. A five-node LangGraph
pipeline classifies failures into **51 conceptual modes** at **75% top-1 accuracy**, for
**$0.0084 per request** through prompt caching and cheap-tier-first model routing.

Hybrid retrieval fuses PostgreSQL full-text search with pgvector cosine similarity through
weighted Reciprocal Rank Fusion — **0.412 precision@3**, beating keyword-only and vector-only
baselines on both metrics. A lexical vaulting layer strips attacker-controlled text before
inference, blocking **40/40** prompt-injection attempts across **155 CI tests**.

<sub>`Python` · `FastAPI` · `LangGraph` · `MCP` · `pgvector` · `Redis` · `Docker` · `Fly.io`</sub>

<br>

### Overlap &nbsp;<sub>[Code](https://github.com/maazin/Overlap) · [Live](https://overlap-flax-psi.vercel.app/)</sub>

Group scheduling with no accounts and no login — **6 taps** to respond. A dominance-analysis
solver proves when a meeting time is mathematically unbeatable regardless of who hasn't
replied yet, so the organizer can lock a slot early.

Replacing materialized response matrices with closure-based resolvers cut solver runtime
**45%** (18.3ms → 10.0ms) and memory **73%** (12.4MB → 3.4MB). TTL caching and single-flight
deduplication collapsed 100 concurrent requests from 100 outbound fetches to **1**, closing an
unauthenticated amplification vector.

<sub>`Go` · `SvelteKit` · `PostgreSQL` · `sqlc` · `SSE` · `Docker` · `GitHub Actions`</sub>

<br>

### Recall Radar &nbsp;<sub>[Code](https://github.com/maazin/Recall_Radar) · [Live](https://recallradar-web.onrender.com/)</sub>

One searchable feed for federal food-recall data. An ETL pipeline unifies **4 sources**
(FDA, USDA/FSIS, CDC) into a normalized schema, indexing **2,000+ advisories** with
**sub-200ms** filtered search and cutting duplicates **39%** through language-aware
deduplication and idempotent upserts.

Fail-fast schema validation rejects malformed upstream payloads before any database write,
covered by **186 tests** across every source's failure path.

<sub>`Python` · `FastAPI` · `React` · `PostgreSQL` · `Docker` · `CI/CD`</sub>

<br>

<details>
<summary><b>More projects</b></summary>

<br>

**[AskRocky](https://github.com/maazin/AskRocky)** · [Live](https://askrocky.vercel.app/) — RAG chatbot
answering campus questions for **800+ USF freshmen**. Scraped and chunked 3,575 USF pages into
384-dimensional BGE embeddings in Pinecone, returning the top 4 cosine matches as citations on
every reply. Held end-to-end latency near 4 seconds by preloading the embedding model behind a
readiness probe.
<br><sub>`Python` · `Flask` · `LangChain` · `Pinecone` · `Hugging Face` · `Vercel`</sub>

<br>

**[StudyPDF](https://github.com/maazin/StudyPDF)** · [Live](https://studypdf.streamlit.app) — Upload a
PDF, get summaries, auto-generated quizzes, and grounded Q&A, with Groq handling low-latency inference.
<br><sub>`Python` · `Streamlit` · `Groq`</sub>

<br>

**[LLM Prompting Study](https://github.com/maazin/LLM_Project)** — Benchmarked zero-shot vs. few-shot
vs. chain-of-thought prompting of Gemma 3 against an RNN baseline on IMDB sentiment. A controlled
look at when prompting beats fine-tuning.
<br><sub>`PyTorch` · `Transformers` · `NLP`</sub>

<br>

**[Airline Satisfaction Prediction](https://github.com/maazin/Airline-Passanger-Satisfaction-Prediction)**
— Random Forest classifier predicting passenger satisfaction from **100k+** survey records.
<br><sub>`Python` · `scikit-learn` · `Random Forest`</sub>

<br>

**[Movie Recommender](https://github.com/maazin/Movie-Recommendation)** — Collaborative-filtering
recommender (KNN) on the MovieLens dataset, served through Streamlit.
<br><sub>`Python` · `scikit-learn` · `Streamlit`</sub>

</details>

<br>

## Experience

**Data Science & ML Intern** — Publix <sub>May 2025 – Jul 2025</sub>

- Deployed a personalized deal-ranking model in Azure Databricks with PySpark — **+12%** app click-through, **+9%** engagement in pilot
- Engineered **20+** customer and product features (purchase frequency, category affinity, deal scarcity) — **+15%** model precision offline
- Ran predictive and causal analysis on **500K+** transactions, surfacing four stockout drivers and cutting out-of-stocks **10%**

**AI Research Assistant** — University of South Florida <sub>Jan 2025 – Apr 2025</sub>

- Built an AI grader for Algorithms coursework with multi-agent LLMs — **90%** agreement with human graders
- Implemented the grading workflow in Python with LangChain and RAG, generating feedback on **100+** submissions and cutting grading time **70%**

**Data Analyst Intern** — The Global Tech Experience <sub>Jan 2024 – May 2024</sub>

- Analyzed **2M+** monthly web-traffic and energy records to define 5 KPIs — **+28%** visitor engagement
- Shipped **8+** interactive Tableau dashboards, cutting report turnaround **30%**
- Planned and executed A/B tests driving a **20%** lift in conversion

<br>

## Stack

**Languages** &nbsp; Python · Go · TypeScript · SQL · Java · C++ · C# · R · Bash

**AI & ML** &nbsp; LangGraph · LangChain · RAG · MCP · PyTorch · Hugging Face · scikit-learn · PySpark · Databricks

**Backend** &nbsp; FastAPI · Flask · Node.js · PostgreSQL · pgvector · Redis · MongoDB · REST · SSE

**Frontend** &nbsp; React · Next.js · SvelteKit · Tailwind · Vite

**Infrastructure** &nbsp; Docker · GitHub Actions · AWS · Azure · GCP · Fly.io · Vercel

<br>

## Leadership

**Head Director** — SHPE Jr <sub>Jun 2025 – May 2026</sub><br>
Lead a team of 5 delivering **10+ STEM workshops per semester** to **150+ students**, driving a **25%** increase in CS and engineering pathway engagement.

**Vice President** — Data Science Club at USF <sub>May 2024 – Apr 2025</sub><br>
Ran hackathons and ML workshops with an 8-member executive board, engaging **200+ students** through partnerships with Bank of America, Citi, and Amgen.

**Director of Events** — AI Society at USF <sub>Aug 2024 – Dec 2024</sub><br>
Directed 7 technical events and secured **$6,000** in funding, driving a **30%** increase in member retention for a 100+ member organization.

**Resident Assistant** — University of South Florida <sub>Aug 2025 – May 2026</sub><br>
Named **Student Staff of the Year** with an "Exemplary" performance rating and a 100% on-time completion rate across all operational reports and duty logs.

<br>

## Honors

**USF Presidential Scholarship** &nbsp;<sub>University of South Florida</sub><br>
**NSBE International Scholarship** &nbsp;<sub>National Society of Black Engineers</sub><br>
**USF Engineering Dean's Scholarship** &nbsp;<sub>College of Engineering</sub><br>
**Judy Genshaft Honors Scholar** &nbsp;<sub>University of South Florida</sub><br>
**Green & Gold Scholarship** &nbsp;<sub>University of South Florida</sub>

<br>

## GitHub

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=maazin&show_icons=true&hide_border=true&hide_title=true&theme=transparent&text_color=c9d1d9&icon_color=58a6ff">
  <img src="https://github-readme-stats.vercel.app/api?username=maazin&show_icons=true&hide_border=true&hide_title=true&theme=transparent&text_color=24292f&icon_color=0969da" alt="GitHub stats">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=maazin&layout=compact&hide_border=true&hide_title=true&langs_count=8&theme=transparent&text_color=c9d1d9">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=maazin&layout=compact&hide_border=true&hide_title=true&langs_count=8&theme=transparent&text_color=24292f" alt="Top languages">
</picture>

</div>

<br>

<div align="center">

**Building something at the intersection of AI and real users? Let's talk.**

<sub><a href="mailto:contactmaazin@gmail.com">contactmaazin@gmail.com</a> &nbsp;·&nbsp; <a href="https://www.linkedin.com/in/maazin-shaikh">LinkedIn</a> &nbsp;·&nbsp; <a href="https://www.maazin.site">maazin.site</a></sub>

</div>
