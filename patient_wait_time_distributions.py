import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────
# STEP 1: Load external Excel file
# ──────────────────────────────────────────────

print("Loading Excel file...")

file_path = "patient_wait_times.xlsx"   # <-- make sure this file is in the same folder
df = pd.read_excel(file_path)

print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ──────────────────────────────────────────────
# STEP 2: Plot histograms with KDE curves
# ──────────────────────────────────────────────

print("Generating graphs...")

palette = ["#1D9E75", "#378ADD", "#BA7517", "#D4537E", "#7F77DD"]

sns.set(style="whitegrid")
fig, axes = plt.subplots(3, 2, figsize=(14, 12))
axes = axes.flatten()

for i, col in enumerate(df.columns):
    sns.histplot(
        df[col],
        kde=True,
        bins=30,
        ax=axes[i],
        color=palette[i],
        edgecolor="white",
        linewidth=0.4,
        line_kws={"linewidth": 2.5}
    )
    axes[i].set_title(col, fontsize=10, fontweight="bold", pad=8)
    axes[i].set_xlabel("Wait Time (minutes)", fontsize=8)
    axes[i].set_ylabel("Frequency", fontsize=8)
    axes[i].tick_params(axis="both", labelsize=8)
    axes[i].set_xlim(0, 120)

    mean_val = df[col].mean()
    median_val = df[col].median()
    axes[i].axvline(mean_val, color="black", linestyle="--", linewidth=1, alpha=0.6)
    axes[i].axvline(median_val, color="gray", linestyle=":", linewidth=1, alpha=0.6)
    axes[i].legend(
        [f"Mean: {mean_val:.1f}", f"Median: {median_val:.1f}"],
        fontsize=7, loc="upper right"
    )

fig.delaxes(axes[-1])

fig.suptitle(
    "Patient Wait Time Distribution Analysis\nSimulated Hospital Data (n=300 per scenario)",
    fontsize=13, fontweight="bold", y=1.01
)

plt.tight_layout(pad=2.0)

output_path = "patient_wait_time_histograms.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.show()

print(f"All graphs generated successfully!")
print(f"Output saved as: {output_path}")
print("Code execution complete.")
