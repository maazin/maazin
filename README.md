<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="hero-dark.svg">
  <img src="hero-light.svg" alt="Maazin Shaikh — Software Engineer, AI/ML Engineer" width="100%">
</picture>

<p>
<a href="https://www.maazin.site"><img src="https://img.shields.io/badge/Portfolio-18181B?style=flat-square&logo=googlechrome&logoColor=white" alt="Portfolio"></a>
<a href="https://www.linkedin.com/in/maazin-shaikh"><img src="https://img.shields.io/badge/LinkedIn-18181B?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="mailto:contactmaazin@gmail.com"><img src="https://img.shields.io/badge/Email-18181B?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
</p>

<p><sub>Tampa, FL &nbsp;·&nbsp; B.S. Computer Science, University of South Florida &nbsp;·&nbsp; <b>Open to full-time roles</b></sub></p>

</div>

<br>

## Selected Work

<table>
<tr>
<td width="50%" valign="top">

<sub><b>RETRIEVAL · LLM PIPELINES</b></sub><br>
<a href="https://github.com/maazin/Weak_Spot"><b>WeakPoint</b></a> &nbsp;<sub><a href="https://weakspot-web.fly.dev/">live&nbsp;&#8599;</a></sub>
<br><br>
Diagnoses <i>why</i> a code submission failed, not just that it did. Five LangGraph nodes classify failures into <b>51 conceptual modes</b> at <b>75% top-1 accuracy</b> for <b>$0.0084 per request</b>.
<br><br>
Hybrid retrieval fuses Postgres full-text with pgvector through weighted Reciprocal Rank Fusion - <b>0.412 precision@3</b>, beating both baselines. A lexical vaulting layer blocked <b>40/40</b> injection attempts across <b>155 CI tests</b>.
<br><br>
<sub><code>Python</code> <code>FastAPI</code> <code>LangGraph</code> <code>MCP</code> <code>pgvector</code> <code>Redis</code></sub>

</td>
<td width="50%" valign="top">

<sub><b>SYSTEMS · PERFORMANCE</b></sub><br>
<a href="https://github.com/maazin/Overlap"><b>Overlap</b></a> &nbsp;<sub><a href="https://overlap-flax-psi.vercel.app/">live&nbsp;&#8599;</a></sub>
<br><br>
Group scheduling with no accounts and no login <b>6 taps</b> to respond. A dominance-analysis solver proves when a time is mathematically unbeatable regardless of who hasn't replied.
<br><br>
Closure-based resolvers cut solver runtime <b>45%</b> and memory <b>73%</b>. TTL caching and single-flight dedup collapsed 100 concurrent requests from 100 outbound fetches to <b>1</b>.
<br><br>
<sub><code>Go</code> <code>SvelteKit</code> <code>PostgreSQL</code> <code>sqlc</code> <code>SSE</code> <code>Docker</code></sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<sub><b>DATA ENGINEERING · ETL</b></sub><br>
<a href="https://github.com/maazin/Recall_Radar"><b>Recall Radar</b></a> &nbsp;<sub><a href="https://recallradar-web.onrender.com/">live&nbsp;&#8599;</a></sub>
<br><br>
One searchable feed for federal food-recall data. An ETL pipeline unifies <b>4 sources</b> (FDA, USDA/FSIS, CDC) into a normalized schema, indexing <b>2,000+ advisories</b> with <b>sub-200ms</b> search and cutting duplicates <b>39%</b>.
<br><br>
Fail-fast validation rejects malformed payloads before any write, covered by <b>186 tests</b>.
<br><br>
<sub><code>Python</code> <code>FastAPI</code> <code>React</code> <code>PostgreSQL</code> <code>CI/CD</code></sub>

</td>
<td width="50%" valign="top">

<sub><b>RAG · PRODUCTION</b></sub><br>
<a href="https://github.com/maazin/AskRocky"><b>AskRocky</b></a> &nbsp;<sub><a href="https://askrocky.vercel.app/">live&nbsp;&#8599;</a></sub>
<br><br>
RAG chatbot answering campus questions for <b>800+ USF freshmen</b>. Scraped and chunked <b>3,575 pages</b> into 384-dimensional BGE embeddings in Pinecone, citing the top 4 cosine matches on every reply.
<br><br>
Held latency near <b>4 seconds</b> by preloading the embedding model behind a readiness probe, serving a degraded answer during cold start.
<br><br>
<sub><code>Python</code> <code>Flask</code> <code>LangChain</code> <code>Pinecone</code> <code>Hugging Face</code></sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<sub><b>APPLIED LLM</b></sub><br>
<a href="https://github.com/maazin/StudyPDF"><b>StudyPDF</b></a> &nbsp;<sub><a href="https://studypdf.streamlit.app">live&nbsp;&#8599;</a></sub>
<br><br>
Upload a PDF, get summaries, auto-generated quizzes, and grounded Q&amp;A, with Groq handling low-latency inference.
<br><br>
<sub><code>Python</code> <code>Streamlit</code> <code>Groq</code></sub>

</td>
<td width="50%" valign="top">

<sub><b>RESEARCH · EVALUATION</b></sub><br>
<a href="https://github.com/maazin/LLM_Project"><b>LLM Prompting Study</b></a>
<br><br>
Benchmarked zero-shot vs. few-shot vs. chain-of-thought prompting of Gemma 3 against an RNN baseline on IMDB sentiment — a controlled look at when prompting beats fine-tuning.
<br><br>
<sub><code>PyTorch</code> <code>Transformers</code> <code>NLP</code></sub>

</td>
</tr>
</table>

<details>
<summary><b>More machine learning work</b></summary>

<br>

**[Airline Satisfaction Prediction](https://github.com/maazin/Airline-Passanger-Satisfaction-Prediction)** - Random Forest classifier predicting passenger satisfaction from **100k+** survey records.
<br><sub>`Python` · `scikit-learn`</sub>

<br>

**[Movie Recommender](https://github.com/maazin/Movie-Recommendation)** — Collaborative-filtering recommender (KNN) on MovieLens, served through Streamlit.
<br><sub>`Python` · `scikit-learn` · `Streamlit`</sub>

<br>

**[Score Predictor](https://github.com/maazin/score-predictor)** — Linear regression predicting exam scores from study hours.
<br><sub>`Python` · `Streamlit`</sub>

<br>

**[SQL Projects](https://github.com/maazin/SQL-Projects)** — Fortune 500 analysis of benefits, sustainability, and satisfaction by sector.
<br><sub>`SQL`</sub>

</details>

<br>

## Experience

<table>
<tr>
<td valign="top" width="34%">

<b>Data Science &amp; ML Intern</b><br>
<sub>Publix &nbsp;·&nbsp; May 2025 – Jul 2025</sub>

</td>
<td valign="top">

Deployed a personalized deal-ranking model in Azure Databricks with PySpark — <b>+12%</b> app click-through, <b>+9%</b> engagement in pilot.<br>
Engineered <b>20+</b> customer and product features (purchase frequency, category affinity, deal scarcity) for <b>+15%</b> precision offline.<br>
Ran predictive and causal analysis on <b>500K+</b> transactions, surfacing four stockout drivers and cutting out-of-stocks <b>10%</b>.

</td>
</tr>
<tr>
<td valign="top">

<b>AI Research Assistant</b><br>
<sub>University of South Florida &nbsp;·&nbsp; Jan 2025 – Apr 2025</sub>

</td>
<td valign="top">

Built an AI grader for Algorithms coursework with multi-agent LLMs — <b>90%</b> agreement with human graders.<br>
Implemented the grading workflow in Python with LangChain and RAG, generating feedback on <b>100+</b> submissions and cutting grading time <b>70%</b>.

</td>
</tr>
<tr>
<td valign="top">

<b>Data Analyst Intern</b><br>
<sub>The Global Tech Experience &nbsp;·&nbsp; Jan 2024 – May 2024</sub>

</td>
<td valign="top">

Analyzed <b>2M+</b> monthly web-traffic and energy records to define 5 KPIs — <b>+28%</b> visitor engagement.<br>
Shipped <b>8+</b> interactive Tableau dashboards, cutting report turnaround <b>30%</b>.<br>
Planned and executed A/B tests driving a <b>20%</b> lift in conversion.

</td>
</tr>
</table>

<br>

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="stack-dark.svg">
  <img src="stack-light.svg" alt="Languages, AI and ML, Backend, Frontend, Infrastructure" width="100%">
</picture>

<br>

## Leadership &amp; Honors

<table>
<tr>
<td valign="top" width="58%">

<b>Head Director</b> &nbsp;<sub>SHPE Jr &nbsp;·&nbsp; Jun 2025 – May 2026</sub><br>
Lead a team of 5 delivering <b>10+ STEM workshops per semester</b> to <b>150+ students</b>, driving a <b>25%</b> increase in CS and engineering pathway engagement.
<br><br>
<b>Vice President</b> &nbsp;<sub>Data Science Club at USF &nbsp;·&nbsp; May 2024 – Apr 2025</sub><br>
Ran hackathons and ML workshops with an 8-member executive board, engaging <b>200+ students</b> through partnerships with Bank of America, Citi, and Amgen.
<br><br>
<b>Director of Events</b> &nbsp;<sub>AI Society at USF &nbsp;·&nbsp; Aug 2024 – Dec 2024</sub><br>
Directed 7 technical events and secured <b>$6,000</b> in funding, driving a <b>30%</b> increase in member retention.
<br><br>
<b>Resident Assistant</b> &nbsp;<sub>University of South Florida &nbsp;·&nbsp; Aug 2025 – May 2026</sub><br>
Named <b>Student Staff of the Year</b> with an Exemplary performance rating and a 100% on-time completion rate across all operational reports.

</td>
<td valign="top">

<b>USF Presidential Scholarship</b><br>
<sub>University of South Florida</sub>
<br><br>
<b>Green &amp; Gold Scholarship</b><br>
<sub>University of South Florida</sub>
<br><br>
<b>NSBE International Scholarship</b><br>
<sub>National Society of Black Engineers</sub>
<br><br>
<b>USF Engineering Dean's Scholarship</b><br>
<sub>USF College of Engineering</sub>
<br><br>
<b>Judy Genshaft Honors Scholar</b><br>
<sub>University of South Florida &nbsp;·&nbsp; GPA 3.87</sub>

</td>
</tr>
</table>

<br>

<div align="center">

<b>Building something at the intersection of AI and real users? Let's talk.</b>

<sub><a href="mailto:contactmaazin@gmail.com">contactmaazin@gmail.com</a> &nbsp;·&nbsp; <a href="https://www.linkedin.com/in/maazin-shaikh">LinkedIn</a> &nbsp;·&nbsp; <a href="https://www.maazin.site">maazin.site</a></sub>

</div>
