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
© 2025 Health Assistant App

