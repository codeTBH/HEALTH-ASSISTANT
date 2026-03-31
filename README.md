# 🧑‍⚕️ Health Assistant — Disease Prediction Web App

## 🚀 Overview
**Health Assistant** is a multi-disease prediction system built using **Streamlit** and **Machine Learning**. It enables clinicians and users to input patient data and receive diagnostic predictions for:

- 🩸 Diabetes  
- ❤️ Heart Disease  
- 🧠 Parkinson's Disease  

This tool leverages pre-trained ML models and provides an intuitive interface with dynamic visuals and easy navigation.

---

## 🎯 Features
- 🎨 Custom background images for each prediction page  
- 🧠 ML-powered predictions using saved `.sav` models  
- 🧪 Interactive form inputs for patient data  
- 🧭 Sidebar navigation using `streamlit-option-menu`  
- 💾 Modular code structure with session state handling  

---

## 📁 Project Structure

```
HEALTH-ASSISTANT/
│
├── main.py                     # Main Streamlit app
├── saved_models/              # Contains .sav files for ML models
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
├── images/                    # Background images for each page
│   ├── landingimg.png
│   ├── diabetesimg.png
│   ├── heartimg.png
│   └── parkinsonimg.png
├── .gitignore                 # Git ignored files
├── LICENSE                    # MIT License
└── README.md                  # Project documentation
```

---

## 🧠 Models Used
- **Diabetes**: Trained on PIMA Indian dataset  
- **Heart Disease**: Based on UCI Heart Disease dataset  
- **Parkinson's**: Trained using voice measurements dataset  

> All models are pre-trained and stored in the `saved_models/` directory.

---

## 🛠️ Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/codeTBH/HEALTH-ASSISTANT.git
   cd HEALTH-ASSISTANT
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   streamlit run main.py
   ```


## Health Assistant 2.0 — Major Upgrade Memo

### Technical Summary of Enhancements, Features, and Architecture

---

# 1. Project Overview
**Health Assistant 2.0** is an AI-powered clinical decision support system designed to predict the risk of multiple diseases using machine learning models. The system allows clinicians or users to input patient data manually or in batches, generates predictions, calculates risk levels, stores results in a database, and provides analytics through an interactive dashboard.

The project evolved from a basic prediction system into a **multi-disease, database-driven, analytics-enabled healthcare assistant** with an improved modern frontend interface.

---

# 2. Core System Capabilities
- Multi-disease prediction
- Risk percentage calculation
- Risk level classification
- Patient history storage
- Batch prediction using CSV files
- Analytics dashboard with visualizations
- Searchable patient records
- Downloadable reports
- Responsive landing page with animation
- Modern UI styling

---

# 3. Machine Learning Components
- Diabetes Prediction
- Heart Disease Prediction
- Parkinson’s Disease Prediction

Each model accepts structured medical parameters, produces binary classification, generates risk probability, and outputs a risk level.

---

# 4. Risk Calculation Logic
- **Sigmoid Conversion** for decision scores  
- **Direct Probability** for probability outputs  
- Thresholds: Low (<40%), Medium (40–70%), High (≥70%)

---

# 5. Recommendation Engine
Rule-based recommendations tailored to disease type and risk level.  
Example: *Diabetes + High Risk → Consult physician, reduce sugar intake, exercise regularly.*

---

# 6. Database Integration
SQLite database with functions for initialization, saving predictions, retrieving records, searching, filtering, and CSV export.

---

# 7. Batch Prediction System
CSV upload → validation → prediction per row → risk calculation → storage → summary table.

---

# 8. Analytics Dashboard
Visualizations for disease distribution, risk levels, patient visits, and monthly trends.

---

# 9. Patient History System
Searchable records, filters by patient/disease, CSV export.

---

# 10. Frontend Enhancements
Responsive landing page, animations, modern UI styling, sidebar navigation.

---

# 11. Error Handling
Structured exception handling for invalid inputs, CSV errors, missing columns, prediction failures.

---

# 12. System Architecture
- `app.py` — main controller  
- `database.py` — database management  
- `utils.py` — risk calculation utilities  
- `saved_models/` — ML models  
- `images/` — assets  

---

# 13. Technology Stack
- Python, Scikit-learn, Pandas, NumPy  
- Streamlit (UI, dashboard, visualization)  
- SQLite (database)  
- Custom CSS (styling, animations)  

---

# 14. Current System Status
Feature-complete, database-integrated, analytics-enabled, batch-capable, responsive, production-ready for academic submission.

---

# 15. Future Enhancements
- PDF report generation  
- User authentication  
- Cloud deployment  
- API integration  
- Model retraining  
- Advanced visualization  
- Mobile app interface  

---

# Version
Latest release: **v2.0 — Health Assistant Major Upgrade**

---

## 📦 Dependencies

Make sure your `requirements.txt` includes:
```
streamlit
streamlit-option-menu
scikit-learn
pandas
numpy
```

---

## 📜 License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## ✨ Credits
Built by **Subhankar**  
Powered by **Streamlit** and **Machine Learning**  
© 2026 Health Assistant App 2.0

