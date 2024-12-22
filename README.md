# **FairLens: AI Model Bias Evaluator**

BiasLens is a Python-based tool designed to help identify and mitigate biases in AI models and datasets. It uses machine learning techniques and integrates OpenAI's API for actionable recommendations to improve fairness in AI systems. The tool provides explainability through SHAP visualizations and compliance checks for legal and ethical standards.

## **Features**
- **Bias Insights**: Generate reports on biases across sensitive attributes like gender, race, and age.
- **Explainability**: Visualize how models make decisions using SHAP values.
- **Actionable Recommendations**: Receive suggestions for mitigating bias using OpenAI’s API.
- **Compliance Checks**: Evaluate models against legal and ethical AI guidelines.
- **Interactive Heatmaps**: Understand which data attributes contribute most to bias.

## **Folder Structure**

```
fairlens/
├── app.py                     # Flask application (entry point)
├── requirements.txt           # Dependencies for the project
├── .env                       # Environment file for API keys (ignored in GitHub)
├── static/                    # Static files (CSS, JavaScript, images)
│   ├── css/
│   │   └── styles.css         # Custom CSS for web interface
├── templates/                 # HTML templates for Flask
│   ├── index.html             # Upload page
│   └── results.html           # Results display page
├── utils/                     # Utility modules for modularity
│   ├── data_processor.py      # Data loading and processing functions
│   ├── model_analysis.py      # Model training and SHAP explanations
│   ├── bias_metrics.py        # Bias computation and heatmap functions
│   └── recommendations.py     # OpenAI API integration for recommendations
├── uploads/                   # Temporary folder for uploaded files
├── training_files/            # Preloaded datasets and resources
│   ├── generate_csv.py        # CSV generation script
│   ├── adult.data             # Raw training data (original)
│   ├── adult.test             # Raw test data (original)
│   ├── adult_combined.csv     # Generated combined dataset (output)
```

## **Setup Instructions**
1. **Clone the Repository**:
2. **Install Dependencies**: pip install -r requirements.txt
3. **Generate Dataset** (Optional): If you need the UCI Adult Dataset in CSV format, run: python training_files/generate_csv.py
4. **Add Your OpenAI API Key**:
- Create a `.env` file in the project root.
- Add your OpenAI API key:
  ```
  OPENAI_API_KEY=your-api-key
  ```
5. **Run the Application**: python app.py

6. **Access the Web Interface**:
Open your browser and navigate to: http://127.0.0.1:5000

----

## **Contributing**
Feel free to fork the repository, raise issues, or submit pull requests to improve BiasLens.

 
