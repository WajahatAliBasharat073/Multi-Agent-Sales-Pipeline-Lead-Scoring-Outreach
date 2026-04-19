# Multi-Agent Sales Pipeline: Lead Scoring & Outreach

An advanced multi-agent system built with [CrewAI](https://crewai.com) that automates lead profiling, strategic qualification scoring, and personalized outreach campaigns.

## Advanced Features
- **Hierarchical Process**: Orchestrated by a `manager_llm` (GPT-4 Turbo) to dynamically coordinate agent activities.
- **Lead Qualification Strategist**: A specialized agent that assigns priority scores (1-10) to leads based on B2B strategic fit.
- **Advanced Sentiment Analysis**: A custom Pydantic-validated tool using `TextBlob` to ensure outreach tone aligns with corporate identity.
- **Structured Output**: Generates production-ready JSON data for seamless CRM integration.

## Project Structure
- `main.py`: Entry point for the sales pipeline.
- `src/`: Modular core package.
  - `agents.py`: Agent configurations.
  - `tasks.py`: Task definitions with JSON output schemas.
  - `tools.py`: Search and custom sentiment tools.
  - `crew.py`: Hierarchical crew orchestration.
  - `utils.py`: API key and environment management.

## Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/WajahatAliBasharat073/Multi-Agent-Sales-Pipeline-Lead-Scoring-Outreach.git
   ```
2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Environment Setup**:
   Copy `.env.example` to `.env` and add your `OPENAI_API_KEY` and `SERPER_API_KEY`.
