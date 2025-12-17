# Fake News Detection API

A Flask-based REST API for detecting fake news using machine learning. This project uses a trained classification model with TF-IDF vectorization to predict whether a given news article is real or fake.

## Features

- **Real-time Prediction**: Classify news articles as REAL or FAKE
- **Confidence Scores**: Get probability scores with each prediction
- **Text Preprocessing**: Automatic text cleaning and normalization
- **RESTful API**: Easy-to-use HTTP endpoints
- **CORS Enabled**: Ready for frontend integration

## Project Structure

```
fake_News/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── model/
│   ├── fake_news_model.pkl    # Trained ML model
│   └── tfidf_vectorizer.pkl   # TF-IDF vectorizer
└── utils/
    └── text_cleaner.py        # Text preprocessing utilities
```

## Installation

1. **Clone or download the project**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

- Flask - Web framework
- Flask-CORS - Cross-Origin Resource Sharing support
- scikit-learn - Machine learning library
- joblib - Model persistence


## Usage

### Starting the Server

Run the Flask application:
```bash
python app.py
```

The server will start on `http://localhost:5000`

### API Endpoints

#### 1. Health Check
**Endpoint**: `GET /health`

**Response**:
```json
{
  "status": "Fake News API running"
}
```

#### 2. Predict News Authenticity
**Endpoint**: `POST /predict`

**Request Body**:
```json
{
  "text": "Your news article text here..."
}
```

**Response**:
```json
{
  "prediction": "REAL",
  "confidence": 0.87
}
```

**Fields**:
- `prediction`: Either "REAL" or "FAKE"
- `confidence`: Probability score (0-1) indicating model confidence

### Example Usage

Using `curl`:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Breaking news: Scientists discover new planet in our solar system"}'
```

Using Python `requests`:
```python
import requests

url = "http://localhost:5000/predict"
data = {
    "text": "Your news article text here..."
}

response = requests.post(url, json=data)
print(response.json())
```

Using JavaScript `fetch`:
```javascript
fetch('http://localhost:5000/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: 'Your news article text here...'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Text Preprocessing

The API automatically preprocesses input text by:
- Converting to lowercase
- Removing URLs
- Removing special characters and numbers
- Trimming whitespace

## Model Information

This project uses:
- **Classification Model**: Pre-trained machine learning model (saved as `fake_news_model.pkl`)
- **Vectorizer**: TF-IDF vectorizer for text feature extraction (saved as `tfidf_vectorizer.pkl`)

## Error Handling

The API returns appropriate error messages:

- **400 Bad Request**: When the `text` field is missing
  ```json
  {
    "error": "Text field is required"
  }
  ```

## Development

To run in development mode with auto-reload:
```bash
python app.py
```

The debug mode is enabled by default in [app.py](app.py).

## License

This project is for educational and research purposes.

## Contributing

Feel free to submit issues and enhancement requests!

---

**Note**: Ensure that the model files (`fake_news_model.pkl` and `tfidf_vectorizer.pkl`) are present in the `model/` directory before running the application.
