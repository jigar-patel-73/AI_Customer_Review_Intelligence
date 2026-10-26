
import streamlit as st
import pandas as pd
from google import genai
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from fpdf import FPDF


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Customer Review Intelligence",
    page_icon="🤖",
    layout="wide"
)


# =========================================
# GEMINI CONFIGURATION
# =========================================

gemini_client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


# =========================================
# CUSTOM CSS
# =========================================
 
st.markdown("""
<style>

/* TAB STYLING */
.stTabs [data-baseweb="tab-list"] {
    gap: 20px;
}

.stTabs [data-baseweb="tab"] {
    height: 55px;
    padding-left: 25px;
    padding-right: 25px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    background-color: #111827;
    color: white;
}

/* DASHBOARD ACTIVE */
button[aria-selected="true"]:nth-of-type(1) {
    background-color: #2563eb !important;
    color: white !important;
}

/* VISUALIZATION ACTIVE */
button[aria-selected="true"]:nth-of-type(2) {
    background-color: #7c3aed !important;
    color: white !important;
}

/* AI INSIGHTS ACTIVE */
button[aria-selected="true"]:nth-of-type(3) {
    background-color: #ec4899 !important;
    color: white !important;
}

/* EXPORT REPORT ACTIVE */
button[aria-selected="true"]:nth-of-type(4) {
    background-color: #16a34a !important;
    color: white !important;
}

/* BUTTONS */
.stButton>button {
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

/* MAIN BACKGROUND */
.main {
    background-color: #020817;
}

            /* KPI METRIC CARDS */
[data-testid="metric-container"] {

    background: linear-gradient(
        145deg,
        #111827,
        #1f2937
    );

    border: 1px solid #374151;

    padding: 18px;

    border-radius: 18px;

    box-shadow:
        0 4px 15px rgba(0,0,0,0.35);

    transition: 0.3s;
}

/* METRIC HOVER EFFECT */
[data-testid="metric-container"]:hover {

    transform: translateY(-4px);

    box-shadow:
        0 8px 22px rgba(59,130,246,0.35);
}
        
/* SUCCESS BOX */
.stSuccess {
    border-radius: 10px;
}

/* INFO BOX */
.stInfo {
    border-radius: 10px;
}

            /* KPI METRIC CARDS */
[data-testid="metric-container"] {

    background: linear-gradient(
        145deg,
        #111827,
        #1f2937
    );

    border: 1px solid #374151;

    padding: 18px;

    border-radius: 18px;

    box-shadow:
        0 4px 15px rgba(0,0,0,0.35);

    transition: 0.3s;
}

/* METRIC HOVER EFFECT */
[data-testid="metric-container"]:hover {

    transform: translateY(-4px);

    box-shadow:
        0 8px 22px rgba(59,130,246,0.35);
}
            
</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("🤖 AI Customer Review Intelligence")

st.sidebar.markdown("""
---
### 🚀 Features

✅ AI Review Analysis  
✅ Sentiment Dashboard  
✅ Business Insights  
✅ Word Cloud Analytics  
✅ PDF Report Export  

---
### 🛠 Tech Stack

- Streamlit
- Python
- Gemini AI
- Pandas
- Matplotlib
- NLP

---
""")

st.sidebar.success(
    "✅ System Ready"
)

# =========================================
# HERO SECTION
# =========================================

# =========================================
# HERO SECTION
# =========================================

st.markdown("""
<div style="
    background: linear-gradient(90deg, #111827, #1e3a8a);
    padding: 35px;
    border-radius: 20px;
    border: 1px solid #374151;
    margin-bottom: 25px;
">

<h1 style="
    color:white;
    font-size:42px;
    margin-bottom:10px;
">
🤖 AI Customer Review Intelligence
</h1>

<p style="
    color:#d1d5db;
    font-size:20px;
    line-height:1.8;
">
Analyze customer reviews using AI-powered business intelligence,
sentiment analysis, visualization dashboards, and automated PDF reporting.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("📌 Navigation")

st.sidebar.info("""
AI-Powered Review Analytics Platform

Features:
- Sentiment Analysis
- AI Insights
- Complaint Detection
- Business Recommendations
""")


# =========================================
# FILE UPLOAD
# =========================================

st.markdown(
    """
    <div style='background-color:#0f172a;
                padding:35px;
                border-radius:20px;
                border:1px solid #374151;
                margin-bottom:25px;'>

    <h2 style='color:white; margin-bottom:15px;'>
    📂 Upload Customer Review Dataset
    </h2>

    <p style='color:#cbd5e1; font-size:17px;'>
    Upload a CSV dataset containing customer reviews and ratings
    to generate AI-powered business insights.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)


# =========================================
# MAIN PROCESSING
# =========================================

if uploaded_file is not None:

    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Dashboard",
        "📈 Visualizations",
        "🤖 AI Insights",
        "📥 Export Reports"
    ])
        

    # =====================================
    # READ DATA
    # =====================================

    df = pd.read_csv(uploaded_file)

    st.divider()

    # =========================================
    # CREATE SENTIMENT COLUMN
    # =========================================

    df["Sentiment"] = df["Score"].apply(
        lambda x:
        "Positive" if x >= 4
        else "Negative" if x <= 2
        else "Neutral"
    )

    # =========================================
    # INTERACTIVE REVIEW FILTERS
    # =========================================

    st.sidebar.markdown("### 🔎 Review Filters")

    selected_sentiments = st.sidebar.multiselect(
        "Sentiment",
        ["Positive", "Neutral", "Negative"],
        default=["Positive", "Neutral", "Negative"]
    )

    min_score, max_score = st.sidebar.slider(
        "Rating Range",
        min_value=1,
        max_value=5,
        value=(1, 5)
    )

    df = df[
        df["Sentiment"].isin(selected_sentiments) &
        df["Score"].between(min_score, max_score)
    ].copy()

    with tab1:
        
        st.header("📊 Analytics Dashboard")
        
        

        # =========================================
        # KPI METRICS
        # =========================================

        positive_count = (df["Sentiment"] == "Positive").sum()
        negative_count = (df["Sentiment"] == "Negative").sum()
        neutral_count = (df["Sentiment"] == "Neutral").sum()

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "📝 Total Reviews",
                f"{len(df):,}"
            )

        with col2:
            st.metric(
                "😊 Positive",
                f"{positive_count:,}"
            )

        with col3:
            st.metric(
                "😡 Negative",
                f"{negative_count:,}"
            )

        with col4:
            st.metric(
                "😐 Neutral",
                f"{neutral_count:,}"
            )

        st.divider()

        # =====================================
        # DATASET SUMMARY
        # =====================================

        st.subheader("📂 Dataset Summary")

        st.success("✅ CSV File Uploaded Successfully!")

        # =========================================
        # DATASET PREVIEW
        # =========================================

        st.write("### 📋 Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )
        # =====================================
        # REVIEW SCORE DISTRIBUTION
        # =====================================

        sentiment_counts = df['Score'].value_counts()

        st.divider()

        st.subheader("📊 Review Score Distribution")

        st.bar_chart(sentiment_counts)


        # =====================================
        # SENTIMENT CLASSIFICATION
        # =====================================

        def classify_sentiment(score):

            if score >= 4:
                return "Positive"

            elif score == 3:
                return "Neutral"

            else:
                return "Negative"


        df['Sentiment'] = df['Score'].apply(classify_sentiment)


        # =====================================
        # SENTIMENT COUNTS
        # =====================================

        positive_count = (df['Sentiment'] == 'Positive').sum()

        negative_count = (df['Sentiment'] == 'Negative').sum()

        neutral_count = (df['Sentiment'] == 'Neutral').sum()

        total_reviews = len(df)

        positive_percent = round((positive_count / total_reviews) * 100, 2)

        negative_percent = round((negative_count / total_reviews) * 100, 2)

        neutral_percent = round((neutral_count / total_reviews) * 100, 2)


        # =====================================
        # METRICS
        # =====================================

        st.divider()

        st.subheader("📈 Customer Sentiment Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "😊 Positive Reviews",
            f"{positive_percent}%"
        )

        col2.metric(
            "😐 Neutral Reviews",
            f"{neutral_percent}%"
        )

        col3.metric(
            "😡 Negative Reviews",
            f"{negative_percent}%"
        )


        # =====================================
        # BAR CHART
        # =====================================

        st.divider()

        st.subheader("📊 Sentiment Distribution")

        st.bar_chart(df['Sentiment'].value_counts())

        
    with tab2:

        st.header("📈 Advanced Visualizations")

        # =====================================
        # PIE CHART
        # =====================================

        fig, ax = plt.subplots(figsize=(2.5, 2.5))

        df['Sentiment'].value_counts().plot.pie(
            autopct='%1.1f%%',
            ax=ax,
            radius=0.65,
            textprops={'fontsize': 8}
        )

        ax.set_ylabel("")

        plt.tight_layout()

        st.subheader("🥧 Sentiment Distribution Pie Chart")

        st.pyplot(fig, use_container_width=False)
        
        # =========================================
        # SENTIMENT BAR CHART
        # =========================================

        st.divider()

        st.subheader("📈 Sentiment Comparison")

        sentiment_counts = df["Sentiment"].value_counts()

        fig2, ax2 = plt.subplots(figsize=(6, 3))

        ax2.bar(
            sentiment_counts.index,
            sentiment_counts.values
        )

        ax2.set_xlabel("Sentiment")
        ax2.set_ylabel("Number of Reviews")

        st.pyplot(fig2, use_container_width=True)

        # =====================================
        # WORD CLOUD
        # =====================================

        st.divider()

        st.subheader("☁️ Customer Review Word Cloud")

        text = " ".join(df['Text'].astype(str))

        wordcloud = WordCloud(
            width=500,
            height=250,
            background_color='white'
        ).generate(text)

        fig_wc, ax_wc = plt.subplots(figsize=(4.4, 2.2))

        ax_wc.imshow(wordcloud, interpolation='bilinear')

        ax_wc.axis("off")

        st.pyplot(fig_wc)

    # =====================================
    # TAB 3 - AI INSIGHTS
    # =====================================

    with tab3:

        st.header("🤖 AI Business Intelligence")

        st.info("""
        🤖 Generate AI-powered business insights from customer reviews.

        Features:
        • Sentiment Summary
        • Complaint Detection
        • Customer Feedback Analysis
        • Business Recommendations
        """)

        if st.button("🚀 Generate AI Insights"):

            
            # Create a representative sample instead of using only the first 20 reviews
            reviews_df = df[df["Text"].notna()].copy()

            if "Sentiment" in reviews_df.columns:
                positive_reviews = reviews_df[reviews_df["Sentiment"] == "Positive"].sample(
                    min(40, len(reviews_df[reviews_df["Sentiment"] == "Positive"])),
                    random_state=42
                )

                negative_reviews = reviews_df[reviews_df["Sentiment"] == "Negative"].sample(
                    min(40, len(reviews_df[reviews_df["Sentiment"] == "Negative"])),
                    random_state=42
                )

                neutral_reviews = reviews_df[reviews_df["Sentiment"] == "Neutral"].sample(
                    min(20, len(reviews_df[reviews_df["Sentiment"] == "Neutral"])),
                    random_state=42
                )

                ai_sample = pd.concat([
                    positive_reviews,
                    negative_reviews,
                    neutral_reviews
                ])
            else:
                ai_sample = reviews_df.sample(
                    min(100, len(reviews_df)),
                    random_state=73
                )

            sample_reviews = "\n".join(
                ai_sample["Text"].astype(str)
            )    
            

            prompt = f"""
            You are an AI Customer Review Intelligence analyst.

            Analyze the following representative customer reviews and generate a concise business intelligence report.

            Provide the analysis in exactly these sections:

            1. Overall Sentiment Summary
            - Summarize the overall customer sentiment.
            - Mention the dominant sentiment and key observations.

            2. Top Customer Complaints
            - Identify the most common customer pain points.
            - Focus on recurring issues rather than isolated comments.

            3. Positive Feedback Trends
            - Identify the main aspects customers appreciate.
            - Highlight recurring positive themes.

            4. Product / Service Insights
            - Identify important patterns related to product quality, pricing, delivery, service, or customer experience.

            5. Business Improvement Recommendations
            - Provide practical and actionable recommendations.
            - Prioritize the issues that could have the greatest business impact.

            6. Executive Summary
            - Give a short management-level summary of the most important findings.

            Base your conclusions only on the provided customer reviews. Do not invent information.

            Customer Reviews:
            {sample_reviews}
            """

            with st.spinner(
                "🤖 Gemini AI is generating business insights..."
            ):

                try:

                    response = gemini_client.models.generate_content(
                       model="gemini-2.5-flash",
                       contents=prompt
                    )
                    st.success(
                        "✅ AI Analysis Completed!"
                    )

                    st.divider()

                    st.subheader(
                        "🤖 AI Business Intelligence Report"
                    )

                    st.markdown(f"""
                    <div style="
                        background-color:#111827;
                        padding:25px;
                        border-radius:15px;
                        border:1px solid #374151;
                        line-height:1.8;
                        font-size:18px;
                    ">
                    {response.text}
                    </div>
                    """, unsafe_allow_html=True)

                    st.balloons()

                except Exception as e:

                    st.error(
                        f"⚠️ Error occurred: {e}"
                    )


    # =====================================
    # TAB 4 - EXPORT REPORTS
    # =====================================

    with tab4:

        st.header("📥 Export Reports")

        st.info("""
        📄 Download professional AI-generated business reports.

        Included in report:
        • Sentiment Analysis
        • Customer Insights
        • Complaint Summary
        • Business Recommendations
        """)

        if st.button("📄 Generate PDF Report"):

            try:

                pdf = FPDF()

                pdf.set_auto_page_break(
                    auto=True,
                    margin=15
                )

                pdf.add_page()

                pdf.set_font(
                    "Arial",
                    "B",
                    18
                )

                pdf.cell(
                    200,
                    10,
                    "AI Business Intelligence Report",
                    ln=True,
                    align="C"
                )

                pdf.ln(10)

                pdf.set_font(
                    "Arial",
                    "",
                    12
                )

                pdf.multi_cell(
                    0,
                    8,
                    response.text if 'response' in locals()
                    else "Generate AI insights first."
                )

                pdf.output(
                    "AI_Business_Report.pdf"
                )

                st.success(
                    "✅ PDF Generated Successfully!"
                )

                with open(
                    "AI_Business_Report.pdf",
                    "rb"
                ) as file:

                    st.download_button(
                        label="📥 Download PDF Report",
                        data=file,
                        file_name="AI_Business_Report.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error(
                    f"⚠️ PDF Error: {e}"
                )

# =========================================
# FOOTER
# =========================================

st.divider()

st.markdown("""
<center>

Made with ❤️ using Streamlit + Gemini AI

AI Customer Review Intelligence System 

</center>
""", unsafe_allow_html=True)

