# AI Customer Review Intelligence

An AI-powered customer review analytics system that transforms large-scale customer reviews into actionable business insights using Python, data analytics, sentiment analysis, and Google Gemini AI.

## 🚀 Live Demo

👉 [AI Customer Review Intelligence – Live App](https://ai-customer-review-intelligence-v2.streamlit.app/)

## Project Overview

Customer reviews contain valuable information about customer satisfaction, complaints, product experience, and improvement opportunities. However, analyzing hundreds of thousands of reviews manually is time-consuming.

This project automates the process by combining data analytics with Generative AI to convert raw customer reviews into a structured business intelligence report.

## Key Features

- Upload customer review CSV datasets
- Analyze large-scale review data using Pandas
- Automatic sentiment classification
- Positive, Negative, and Neutral review analysis
- Sentiment distribution visualization
- Customer rating analysis
- Word cloud generation
- AI-powered business insights using Google Gemini
- Identification of major customer complaints
- Identification of positive customer feedback trends
- AI-generated business improvement recommendations
- Interactive Streamlit dashboard

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Pandas | Data processing and analysis |
| Matplotlib | Data visualization |
| WordCloud | Review text visualization |
| Streamlit | Interactive web application |
| Google Gemini AI | Generative AI business insights |
| FPDF | Report generation |

## AI Analysis Workflow

```text
Customer Review Dataset
        ↓
CSV Upload
        ↓
Data Processing
        ↓
Sentiment Classification
        ↓
Exploratory Analysis
        ↓
Representative Review Sampling
        ↓
Google Gemini AI
        ↓
Business Intelligence Insights
        ↓
Recommendations
```

## Sentiment Classification

Reviews are classified using customer rating scores:

- Score 4–5 → Positive
- Score 3 → Neutral
- Score 1–2 → Negative

The system also uses representative sampling across sentiment categories before sending review data to Gemini, helping the AI analysis consider different customer perspectives instead of relying only on the first few records.

## Dataset

The application was tested with a large Amazon customer review dataset containing approximately 568,000 reviews.

The dataset used during testing contained:

- Total Reviews: 568,454
- Positive Reviews: 443,777
- Negative Reviews: 82,037
- Neutral Reviews: 42,640

The dataset itself is excluded from GitHub through `.gitignore`.

## AI Business Intelligence

The Gemini-powered analysis generates:

1. Overall sentiment summary
2. Major customer complaints
3. Positive feedback trends
4. Business improvement suggestions

This transforms traditional review analytics into an AI-assisted decision-support system.

## Project Structure

```text
AI_Customer_Review_Intelligence/
│
├── .streamlit/
│
├── app_v2/
│   └── app.py
│
├── data/
├── models/
├── notebooks/
│
├── .gitignore
├── README.md
└── requirements.txt
```

`app_v2/app.py` is the main application and deployment entry point.

## Running the Application Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Configure the Gemini API key in:

```text
.streamlit/secrets.toml
```

Example:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

Run the application:

```bash
python -m streamlit run app_v2/app.py
```

The application will open locally in your browser.

## Security

API credentials and sensitive configuration files are excluded from version control.

The Gemini API key should be stored using Streamlit secrets and should never be committed to GitHub.

## Project Objective

The goal of this project is to demonstrate how traditional data analytics can be combined with Generative AI to build practical business intelligence solutions.

The system can help businesses understand customer feedback at scale and convert unstructured review data into actionable insights.

## Future Enhancements

- Advanced topic modeling
- Aspect-based sentiment analysis
- Customer complaint clustering
- Automated executive reports
- Review trend forecasting
- AI-powered conversational analytics
- Automated business KPI monitoring

## Author

**Jigar Patel**

Data Analytics | Business Analytics | AI Automation

Skills demonstrated: Python, SQL, Data Analytics, Power BI, Machine Learning, Generative AI, Streamlit
