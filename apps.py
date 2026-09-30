import streamlit as st
import pandas as pd
import joblib

MODEL_PATH = "email_spam_model.pkl"

st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="centered"
)

@st.cache_resource
def load_model():
    artifact = joblib.load(MODEL_PATH)
    return artifact

artifact = load_model()
model = artifact["model"]
features = artifact["features"]

st.title("📧 Email Spam Detection")
st.write(
    "Enter the measurable email characteristics below. "
    "The trained Logistic Regression model will estimate whether the email is Spam or Not Spam."
)

st.info(
    "This prototype matches the supplied dataset, whose target is `is_spam`."
)

num_links = st.number_input(
    "Number of links",
    min_value=0,
    value=0,
    step=1
)

num_words = st.number_input(
    "Number of words",
    min_value=0,
    value=50,
    step=1
)

has_offer = st.selectbox(
    "Does the email contain an offer?",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

sender_score = st.number_input(
    "Sender score",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

all_caps = st.selectbox(
    "Does the email contain all-capital text?",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

if st.button("Analyze Email", type="primary"):
    input_data = pd.DataFrame([{
        "num_links": num_links,
        "num_words": num_words,
        "has_offer": has_offer,
        "sender_score": sender_score,
        "all_caps": all_caps
    }])[features]

    prediction = int(model.predict(input_data)[0])
    spam_probability = float(model.predict_proba(input_data)[0, 1])

    st.divider()

    if prediction == 1:
        st.error("⚠️ Prediction: SPAM")
    else:
        st.success("✅ Prediction: NOT SPAM")

    st.metric(
        "Spam Probability",
        f"{spam_probability:.2%}"
    )

    st.caption(
        "This is an academic machine-learning prototype. "
        "It should not be used as the sole basis for real-world security decisions."
    )
