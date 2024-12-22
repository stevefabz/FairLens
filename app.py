from flask import Flask, request, render_template, redirect, url_for
import os
from utils.data_processor import load_data
from utils.model_analysis import analyze_model
from utils.bias_metrics import calculate_bias_metrics, generate_heatmap
from utils.recommendations import get_recommendations

# Flask app configuration
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    """Render the home page with the file upload form."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle dataset upload and initiate bias analysis."""
    try:
        # Ensure a file is uploaded
        if 'file' not in request.files:
            return "No file uploaded.", 400
        
        file = request.files['file']
        if file.filename == '':
            return "No selected file.", 400
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Get form inputs
        target_col = request.form.get('target_col')
        sensitive_col = request.form.get('sensitive_col')

        # Perform analysis
        data = load_data(file_path)
        model, shap_path = analyze_model(data, target_col)
        bias_metrics = calculate_bias_metrics(data, target_col, sensitive_col)
        heatmap_path = generate_heatmap(data, sensitive_col, target_col)
        recommendations = get_recommendations(f"How to mitigate bias in {sensitive_col} for AI models?")

        return render_template(
            'results.html', 
            bias_metrics=bias_metrics,
            heatmap_path=heatmap_path,
            shap_path=shap_path,
            recommendations=recommendations
        )
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)


#"C:\Users\steve\AppData\Local\Microsoft\WindowsApps\python.exe" -m pip install distutils flask pandas numpy scikit-learn shap matplotlib seaborn openai