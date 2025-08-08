from flask import Flask, render_template, request
import pickle

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    lg_model = pickle.load(f)
with open("tfidf.pkl", "rb") as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email_text = request.form['email_text']
        # check if email_text is not empty
        if email_text.strip():
            # Vectorize the input email text
            email_vectorized = vectorizer.transform([email_text])
            # Predict using the loaded model
            prediction = lg_model.predict(email_vectorized)
            if prediction[0] == 1:
                result = " This email is likely a Phishing attempt."
            else:
                result = " This email is likely Safe."
            return render_template('index.html', result=result)
        else:
            return render_template('index.html', result="Please enter valid email text.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
