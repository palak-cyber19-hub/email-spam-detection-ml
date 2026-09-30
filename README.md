# Email Spam Detection Using Logistic Regression

## Project Type
Machine Learning / Binary Classification

## Dataset
`spam_detection_dataset.csv`

The supplied dataset contains 20,000 records and the following columns:

- `num_links`
- `num_words`
- `has_offer`
- `sender_score`
- `all_caps`
- `is_spam`

## Important Scope Note
The supplied dataset is a **spam detection** dataset. It does not contain raw email text or a threat-specific target. Therefore this project does not claim to perform threat classification or NLP-based threat-keyword detection.

## Workflow
1. Load dataset
2. Inspect structure
3. Check missing values and duplicates
4. Remove duplicate records
5. Handle numeric missing values
6. Analyze class balance
7. Perform EDA
8. Prepare features
9. Split data into train/test sets
10. Standardize features
11. Train Logistic Regression with balanced class weights
12. Evaluate Accuracy, Precision, Recall, F1 and ROC-AUC
13. Plot Confusion Matrix and ROC Curve
14. Inspect Logistic Regression coefficients
15. Save trained model
16. Run Streamlit prototype

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Put the dataset in the project folder

The CSV must be named:

`spam_detection_dataset.csv`

### 3. Run the notebook

Open:

`email_spam_detection_submission.ipynb`

Run all cells from top to bottom. This creates:

`email_spam_model.pkl`

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

## Files

- `email_spam_detection_submission.ipynb` - complete analysis and model development
- `app.py` - Streamlit prototype
- `requirements.txt` - Python dependencies
- `email_spam_model.pkl` - generated trained model
- `spam_detection_dataset.csv` - original dataset

## Evaluation
The notebook reports:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix
- ROC Curve

## Limitations
The supplied dataset contains engineered numerical features instead of raw email text. NLP features such as TF-IDF, word embeddings, and keyword extraction therefore cannot be honestly included without a text column.

## Future Scope
- Add raw email text and NLP features
- Compare multiple classifiers
- Hyperparameter tuning and cross-validation
- Larger and more diverse datasets
- Model explainability
- Production deployment with security controls
