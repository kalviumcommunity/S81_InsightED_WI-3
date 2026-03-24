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
