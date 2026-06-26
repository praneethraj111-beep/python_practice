import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_risk_report(df: pd.DataFrame, output_image_path: str):
    """
    Aggregates risk score distribution and exports an automated 
    executive risk profile visualization.
    """
    print(f"[ANALYTICS] Synthesizing risk score metric distribution...")
    
    if 'risk_score' not in df.columns:
        print("[WARNING] Analytics terminated: Missing 'risk_score' column.")
        return

    # Count the frequencies of each risk grade
    risk_counts = df['risk_score'].value_counts()
    
    # Clear active plotting environments
    plt.clf()
    plt.figure(figsize=(7, 4.5))
    
    # Map colors systematically based on risk significance
    color_map = {
        'LOW_RISK': 'mediumseagreen',
        'FAILED_TX_FLAG': 'orange',
        'HIGH_VALUE_ALERT': 'crimson'
    }
    colors = [color_map.get(node, 'gray') for node in risk_counts.index]
    
    # Generate bar chart
    plt.bar(risk_counts.index, risk_counts.values, color=colors, edgecolor='black', width=0.5)
    
    plt.title('Security Monitoring: Transaction Risk Profile', fontsize=12, fontweight='bold')
    plt.xlabel('Assigned Risk Category', fontsize=10)
    plt.ylabel('Transaction Count', fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    # Save chart image asset
    plt.savefig(output_image_path, dpi=100)
    print(f"[ANALYTICS] Success! Risk visualization report saved at: {output_image_path}")