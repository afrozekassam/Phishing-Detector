# Phishing Email Detector

A web application that classifies emails as **Phishing** or **Safe** using machine learning.  
Built with a Logistic Regression model and TF-IDF vectorizer for text processing, served via a Flask backend with a user-friendly HTML/CSS frontend.

---

## Features

- Loads a trained Logistic Regression model and TF-IDF vectorizer.
- Users can paste email content on a web page and get instant phishing predictions.
- Simple, clean web UI built with Flask templating and CSS.


---

## Requirements

- Python 3.x  
- Flask  
- scikit-learn  
- pandas  
- numpy  

Install dependencies via:

```bash
pip install -r requirements.txt
