# CivicPulse – Real-Time Civic Issue Analyzer & Reporter

CivicPulse is a web application that enables citizens to report civic issues (e.g., potholes, water leaks, garbage) by uploading a description and image. The system uses a machine learning model to automatically categorize the issue type and stores all reports in a local database for visualization.

## Features

- Citizens can submit civic issues via a simple form with image upload.
- Machine Learning model auto-classifies issues (roads, water, sanitation, electricity, etc.).
- Real-time dashboard to view reported issues in a card-based layout.
- Category filters for easy browsing.
- Simple navigation between submission and dashboard pages.

## Tech Stack

- Backend: Flask
- Frontend: HTML, CSS, (optionally Bootstrap)
- Machine Learning: scikit-learn, pandas, joblib
- Storage: Local CSV file and image folder
- Visualization (optional): Chart.js

## Folder Structure

civicpulse/
├── app.py
├── requirements.txt
├── static/
│ ├── css/style.css
│ └── uploads/
├── templates/
│ ├── index.html
│ ├── dashboard.html
│ └── admin.html (optional)
├── ml/
│ ├── train.ipynb
│ ├── model.py
│ └── issue_classifier.pkl
├── data/
│ ├── issues.csv
│ └── sample_issues.csv
└── README.md

## Installation

1. Clone the repository:
   git clone https://github.com/ashmithhmaddala/civicpulse.git
   cd civicpulse

2. Set up a virtual environment:
   python -m venv venv
   venv\Scripts\activate # On Windows
   source venv/bin/activate # On Unix/macOS

3. Install dependencies:
   pip install -r requirements.txt

4. Train the ML model (run `ml/train.ipynb`) to generate `issue_classifier.pkl`.

5. Start the Flask application:
   python app.py

6. Open the application in your browser:
   http://127.0.0.1:5000

## Future Improvements

- Location mapping with Leaflet.js
- Severity detection from text and image
- Admin panel for city officials
- Analytics dashboard (charts, trends, heatmaps)

## Author

Ashmith Maddala – [[GitHub link](https://github.com/ashmithhmaddala)]

## License

MIT License
