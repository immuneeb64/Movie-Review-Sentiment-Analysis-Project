from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    sentiment = predict_sentiment(review)
    return render_template('index.html', prediction=sentiment)

def predict_sentiment(review):
    # Dummy implementation for sentiment prediction
    if 'good' in review.lower():
        return 'Positive'
    else:
        return 'Negative'

if __name__ == '__main__':
    app.run(debug=True)