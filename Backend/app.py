from flask import Flask, render_template, request
import pickle

# Load the model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email_text = request.form['email']
        transformed_text = tfidf.transform([email_text])
        prediction = model.predict(transformed_text)[0]

        if prediction == 1:
            result = "🚨 Phishing Email"
        else:
            result = "✅ Safe Email"

        return render_template('index.html', prediction=result, input=email_text)

if __name__ == '__main__':
    app.run(debug=True)
