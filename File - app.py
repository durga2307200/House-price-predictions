from flask import Flask, render_template, request  # Add render_template
import joblib

app = Flask(__name__)

# Load your model
model = joblib.load('house_price_model.pkl')

# 🔥 Update this route to render index.html
@app.route('/')
def home():
    return render_template('index.html')  # Fix: Render HTML template

# 🔥 Ensure this route accepts POST requests
@app.route('/predict', methods=['POST'])
def predict():
    try:
        size = float(request.form['size'])
        prediction = model.predict([[size]])[0]
        return render_template('index.html', 
                             prediction_text=f'Predicted Price: ${prediction:,.2f}')
    except:
        return render_template('index.html', 
                             prediction_text='Error: Invalid input!')

if __name__ == '__main__':
    app.run(debug=True)