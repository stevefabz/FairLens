import matplotlib.pyplot as plt
import seaborn as sns

def calculate_bias_metrics(data, target_col, sensitive_col):
    """Calculate bias metrics based on sensitive attributes."""
    try:
        groups = data[sensitive_col].unique()
        metrics = {}
        for group in groups:
            group_data = data[data[sensitive_col] == group]
            rate = group_data[target_col].mean()
            metrics[group] = rate
        return metrics
    except Exception as e:
        raise ValueError(f"Failed to calculate bias metrics: {e}")

def generate_heatmap(data, sensitive_col, target_col):
    """Generate and save a heatmap to visualize bias."""
    try:
        heatmap_path = "static/heatmap.png"
        pivot_table = data.pivot_table(values=target_col, index=sensitive_col)
        plt.figure(figsize=(8, 6))
        sns.heatmap(pivot_table, annot=True, cmap="coolwarm")
        plt.title(f'Bias Heatmap: {sensitive_col} vs {target_col}')
        plt.savefig(heatmap_path)
        plt.close()
        return heatmap_path
    except Exception as e:
        raise ValueError(f"Heatmap generation failed: {e}")
