from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from datetime import datetime

from ml.model import predict_category

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
DATA_FILE = 'data/issues.csv'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('data', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_issue():
    description = request.form.get('description')
    photo = request.files.get('photo')
    
    if not description or not photo:
        return "Please provide both description and photo.", 400

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{photo.filename}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    photo.save(filepath)

    # ✅ ML prediction
    category = predict_category(description)

    # ✅ Save to CSV
    new_entry = {
        "timestamp": timestamp,
        "description": description,
        "category": category,
        "image_path": filepath.replace('\\', '/')
    }

    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        df = pd.read_csv(DATA_FILE)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    else:
        df = pd.DataFrame([new_entry])

    df.to_csv(DATA_FILE, index=False)

    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    selected_category = request.args.get('category', 'all')

    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        df = pd.read_csv(DATA_FILE)
        if selected_category != 'all':
            df = df[df['category'].str.lower() == selected_category.lower()]
        issues = df.to_dict(orient='records')
    else:
        issues = []

    categories = ['all', 'roads', 'water', 'sanitation', 'electricity']
    return render_template('dashboard.html', issues=issues, categories=categories, selected=selected_category)

if __name__ == '__main__':
    app.run(debug=True)
