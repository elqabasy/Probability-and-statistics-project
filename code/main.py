import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "/mnt/data/violent_games_impact_dataset.csv"
df = pd.read_csv(file_path)

# Descriptive statistics
desc_stats = df.describe(include="all")

# Frequency analysis for categorical variables
freq_analysis = {
    "Plays_Violent_Games": df["Plays_Violent_Games"].value_counts(),
    "Favorite_Game_Genre": df["Favorite_Game_Genre"].value_counts(),
    "Grade_Level": df["Grade_Level"].value_counts(),
    "Gender": df["Gender"].value_counts(),
}

# Correlation matrix for numerical variables
correlation_matrix = df.select_dtypes(include=["int64", "float64"]).corr()

# Visualizations
# 1. Bar chart: Plays Violent Games
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Plays_Violent_Games", palette="viridis")
plt.title("Frequency of Children Playing Violent Games")
plt.xlabel("Plays Violent Games")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("/mnt/data/plays_violent_games_bar_chart.png")
plt.close()

# 2. Histogram: Hours Played Per Week
plt.figure(figsize=(6, 4))
sns.histplot(df["Hours_Played_Per_Week"], kde=True, color="blue", bins=10)
plt.title("Distribution of Hours Played Per Week")
plt.xlabel("Hours Played Per Week")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("/mnt/data/hours_played_histogram.png")
plt.close()

# 3. Heatmap: Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix of Numerical Variables")
plt.tight_layout()
plt.savefig("/mnt/data/correlation_matrix_heatmap.png")
plt.close()

# Results summary
summary = {
    "Descriptive Statistics": desc_stats,
    "Frequency Analysis": freq_analysis,
    "Correlation Matrix": correlation_matrix,
    "Generated Visualizations": [
        "/mnt/data/plays_violent_games_bar_chart.png",
        "/mnt/data/hours_played_histogram.png",
        "/mnt/data/correlation_matrix_heatmap.png",
    ],
}

# summary
print(summary)
