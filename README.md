# Data-analysis-for-house-price

A complete end-to-end data analysis and machine learning project based on the Ames Housing Dataset. This project covers exploratory data analysis (EDA), feature engineering, traditional machine learning models, neural networks, model comparison, and model interpretation with SHAP.

---

## Dataset

**Ames Housing Dataset**

- 2930 houses
- 80+ features
- Target variable: `SalePrice`

Source:

https://www.kaggle.com/datasets/shashanknecrotthapa/ames-housing-dataset

---

## Project Structure

```
house-price/

├── data
│     feature_engineered.csv
│
├── figures
│
├── notebooks
│     01_eda.ipynb
│     02_feature_engineering.ipynb
│     03_model.ipynb
│     04_pytorch.ipynb
│     05_comparison.ipynb
│     06_shap.ipynb
│
├── src
│
├── requirements.txt
└── README.md
```

---

## Workflow

```
Raw Data
↓
Exploratory Data Analysis (EDA)
↓
Feature Engineering
↓
Linear Regression
↓
Random Forest
↓
PyTorch MLP
↓
Model Comparison
↓
SHAP Interpretation
```

---

## Feature Engineering

Created several domain-inspired features:

- House Age
- Total Area
- Total Bath
- Quality_Area

Missing values and categorical variables were handled using:

- Median imputation
- One-hot encoding

---

## Models

### Linear Regression

Used as a baseline model.

### Random Forest

Captures nonlinear relationships and interactions between features.

### PyTorch MLP

Implemented a fully connected neural network using PyTorch.

Architecture:

```
Input
↓
128
↓
64
↓
32
↓
1
```

---

## Model Performance

| Model | RMSE ↓ | MAE ↓ | R² ↑ |
|---------|--------:|--------:|--------:|
| Linear Regression | 37935 | - | - |
| Random Forest | 24530 | 14842 | 0.925 |
| PyTorch MLP | 31813 | 17617 | 0.874 |

Random Forest achieved the best performance on this relatively small tabular dataset.

---

## Model Interpretation

SHAP was used to interpret the Random Forest model.

Main findings:

- Overall Quality is the most influential feature.
- Larger houses generally have higher prices.
- House age tends to reduce the predicted price.
- Feature engineering significantly improved model performance.

---

## Key Findings

- Feature engineering improves predictive performance.
- Tree-based models outperform neural networks on small tabular datasets.
- Random Forest provides the best trade-off between accuracy and interpretability.
- SHAP offers insights into how individual features contribute to predictions.

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- PyTorch
- SHAP

---

## Future Work

- XGBoost
- LightGBM
- Cross Validation
- Error Analysis
- Hyperparameter Tuning
- Advanced Tabular Deep Learning Models
