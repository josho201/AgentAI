# Deep Research Agent (Qwen 235B + Web Scraping + Prompt Orchestration)

## 🚀 Overview
This project is an experiment in building an **AI-powered research assistant** based on **Qwen-Agent** capable of producing long-form, reference-backed reports.  

- ✅ Scrapes web content  
- ✅ Extracts, organizes, and embeds knowledge  
- ✅ Synthesizes into structured multi-page reports  
- ✅ Includes references and comparative analysis  

In my test run, I burned through ~**800,000 tokens** with Qwen 235B to generate an **8-page comparative analysis of global AI regulation (EU, US, China, 2025)**.  
👉  (see examples folder)

---

## 🛠 How It Works
1. **Scraping**: Pulls clean text from given URLs.  
   *(todo: add which library/tool you used here)*  

2. **Chunking + Embeddings**: Splits text into chunks and stores embeddings for retrieval.  
   *(todo: mention FAISS or whatever you used)*  

3. **Prompt Orchestration**: Dynamically builds prompts to guide synthesis.  
   *(todo: add sample system prompt / agent logic)*  

4. **Report Generation**: Produces structured Markdown → can export to PDF/Docx.  

---

## 📊 Example Output
- **Topic:** Comparative Analysis of AI Regulation  
- **Length:** ~8 pages  
- **Sources:** 14 references (EU Parliament, NIST, White & Case, Carnegie, etc.)  
- **Output:** Structured like a professional policy brief with sections, tables, and conclusions.  

👉 See the full report here: [link]  

---

## 🌍 Why It’s Cool
- Most AI outputs = shallow summaries.  
- This system = **multi-layered analysis with citations**, closer to real research.  
- Great for policy, consulting, academic review, or market analysis.  

---

## 🗺 Roadmap
- [ ] Downscale for offline use (Qwen 7B/14B, local embeddings)  
- [ ] Add UI demo (Streamlit/Gradio)  
- [ ] Make it configurable for any research domain  
- [ ] (stretch) Agents that continue research iteratively across sessions  

---

## ⚡️ Try It Yourself
*(todo: add install instructions and example run command here)*  

---

## 🙌 Contribute / Contact
I’m building towards an **offline, lightweight research agent** that anyone can run locally.  
If you’re into applied AI, research automation, or just want to talk nerd stuff:  
- 🐦 Twitter: [your handle]  
- 💼 Upwork: [your profile link]  
- 📬 GitHub Issues / PRs welcome!  



shitty .md made by chatgpt
