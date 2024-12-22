import shap
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def analyze_model(data, target_col):
    """Train a model and generate SHAP values for explainability."""
    try:
        X = data.drop(columns=[target_col])
        y = data[target_col]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # SHAP explainability
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_test)
        shap_path = "static/shap_summary.png"
        shap.summary_plot(shap_values, X_test, show=False)
        os.makedirs("static", exist_ok=True)
        plt.savefig(shap_path)
        plt.close()
        
        return model, shap_path
    except Exception as e:
        raise ValueError(f"Model analysis failed: {e}")
