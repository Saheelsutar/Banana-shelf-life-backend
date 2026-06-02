# Banana Shelf Life Prediction Backend

A Flask-based REST API that predicts banana ripeness and estimated shelf life using a TensorFlow EfficientNetB0 deep learning model.

## Features

* Upload a banana image
* Predict ripeness stage:

  * Unripe
  * Ripe
  * Overripe
  * Rotten
* Return prediction confidence
* Estimate remaining shelf life

---

## Tech Stack

* Python
* Flask
* TensorFlow
* EfficientNetB0
* NumPy

---

## Project Structure

```text
backend/
│
├── app.py
├── requirements.txt
├── model_export/
│   ├── assets/
│   ├── variables/
│   ├── saved_model.pb
│   └── fingerprint.pb
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Saheelsutar/Banana-shelf-life-backend.git
cd Banana-shelf-life-backend
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Locally

```bash
python app.py
```

Server starts at:

```text
http://127.0.0.1:5000
```

---

## API Endpoint

### Predict Banana Ripeness

**POST**

```http
/predict
```

### Request

Content-Type:

```text
multipart/form-data
```

Body:

| Key   | Type |
| ----- | ---- |
| image | File |

### Example Response

```json
{
  "ripeness": "ripe",
  "shelf_life": "3-5 days",
  "confidence": 98.71
}
```

---

## Shelf Life Mapping

| Ripeness | Estimated Shelf Life |
| -------- | -------------------- |
| Unripe   | 6-9 days             |
| Ripe     | 3-5 days             |
| Overripe | 1-2 days             |
| Rotten   | 0 days               |

---
