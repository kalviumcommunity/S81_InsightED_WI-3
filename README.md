# 📊 InsightED: Academic Data Analytics System


## Project Overview
InsightED is a decision-support data analytics system designed for universities. Its primary objective is to process raw student feedback data, extract meaningful insights using data analysis and NLP, and present highly actionable conclusions to help university administrators and faculty improve academic performance and student satisfaction.


## Core Features
* **Insight-First Dashboard**: Highlights critical issues rather than just displaying raw data.
* **KPI Tracking**: Monitors Average Satisfaction Score, Negative Feedback percentage, Course Difficulty, and Faculty Ratings.
* **Sentiment Analysis**: Processes text-based feedback to classify student comments as Positive, Neutral, or Negative.
* **Automated Insights Panel**: Generates critical text insights automatically (e.g., "Data Structures has 40% negative feedback").


## Tech Stack
* **Frontend**: Streamlit
* **Data Processing**: Python, Pandas, NumPy
* **NLP & Data Science**: NLTK, TextBlob, Scikit-learn
* **Visualizations**: Matplotlib, Plotly

---

## 📚 Learning Milestone Submission: Understanding the Data Science Lifecycle


### 1. Explaining the Lifecycle (Question -> Data -> Insight)
* **The Question**: The data science lifecycle must always begin with a carefully targeted question. Jumping directly into a dataset without a clear goal leads to aimless exploration. Formulating a specific question acts as a compass—it defines the scope, restricts us to relevant data, and gives the project a concrete definition of success.
* **Data as Evidence**: Data is the objective evidence we need to answer our question. Before writing complex algorithms, we have to understand where the data came from, its biases, and its format. We have to ensure that the data actually represents the real-world academic environment we are trying to analyze.
* **Generating Insight**: Insights are not simply charts or raw numbers; they are the conclusions we draw when we interpret the data *through the lens of our core question*. True insight shifts the focus from "What happened?" to "Why did it happen, and what decision should we make to fix it?"

### 2. Applying the Lifecycle to InsightED
* **The Question:** "Which specific courses are causing the highest rate of negative student feedback, and what specific topics or teaching styles are driving this dissatisfaction?"
* **The Type of Data Needed:** We need end-of-semester student survey feedback. This comes directly from the university's evaluation systems. It represents quantitative metrics (ratings from 1-5 on faculty and course difficulty) and qualitative metrics (open-ended text comments from students).
* **The Useful Insight:** Simply stating "Data Structures has a 2.5 rating" is just a fact, not an insight. An actionable insight would be: *"Data Structures has a 40% negative feedback rate specifically because students are frequently using the phrases 'fast teaching' and 'too theoretical' in their reviews, indicating the curriculum pace must be adjusted immediately."*

---

## 📚 Learning Milestone 2: Reading & Interpreting a Sample Data Science Project Repository

### 1. Project Intent & High-Level Flow
* **Problem Addressed**: The repository aims to address poor academic performance and student dissatisfaction by analyzing university feedback. Its overarching goal is to transform subjective student surveys into objective, actionable recommendations for administrators.
* **Data Science Workflow**: The workflow follows a structured pipeline: collecting raw survey evidence, preprocessing the text, applying NLP models (Sentiment Analysis/Keyword Extraction), computing KPIs, and deploying findings to a visual dashboard.
* **Structure & Lifecycle**: The folders mirror the lifecycle stages: `data/` represents "Data Gathering", `processing/` and `notebooks/` represent "Exploration and Modeling", and `dashboard/` represents the "Deployment and Insight Delivery" stage.

### 2. Repository Structure & File Roles
* **Folder Roles**:
  * `data/`: Stores immutable raw dataset inputs (e.g., `feedback.csv`).
  * `notebooks/`: Serves as a sandbox for exploratory data analysis (EDA), drafting charts, and testing algorithms loosely.
  * `processing/` (Scripts): Contains finalized, version-controlled Python modules (`clean_data.py`, `sentiment.py`) used by the main application.
  * `dashboard/`: Houses the final deployment app (`app.py`), directly serving the generated insights to end-users.
* **Exploratory vs. Finalized Work**: Exploratory work happens in notebooks—it is experimental, messy, and meant for the scientist's eyes. Finalized analysis is ported into `.py` scripts (`processing/`) which are modular, optimized, and heavily tested for production use.
* **Cautious Areas for New Contributors**: A contributor should be highly cautious when modifying files in `processing/`. Because these scripts handle core programmatic data transformations, a breaking change here will silently cascade and crash the downstream `dashboard/`.

### 3. Assumptions, Gaps, and Open Questions
* **Assumptions Made**: The codebase assumes all `feedback.csv` files follow an identical, predefined column format and that textual feedback is predominantly English (as basic NLTK/TextBlob operations are utilized).
* **Missing Documentation/Gaps**: The repository currently lacks explicit documentation on the data cleaning rules—specifically, how missing ratings are handled mathematically (e.g., dropping vs. imputing).
* **One Improvement**: Introducing thorough function docstrings outlining exact input/output shapes for functions in `processing/`, alongside a step-by-step developer setup guide (`CONTRIBUTING.md`), would significantly improve onboarding times.
