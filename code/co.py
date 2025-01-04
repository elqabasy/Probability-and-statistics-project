import pandas as pd

# Creating the dataset from the provided data
data = {
    "Age": [8, 7, 11, 10, 10, 9, 8, 15, 8, 16, 13, 7, 7, 8, 10, 10, 15, 16, 7, 10, 15, 10, 14, 16, 11, 7, 9, 13, 12, 11, 9, 10, 12, 8, 8, 13, 8, 8, 13, 8, 12, 12, 12, 12, 16, 11, 7, 14, 15, 8],
    "Plays_Violent_Games": ['No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes'],
    "Aggressive_Tendencies": [3, 2, 4, 5, 3, 5, 5, 1, 5, 3, 4, 2, 3, 1, 2, 5, 2, 1, 5, 3, 5, 3, 4, 3, 3, 1, 1, 4, 5, 1, 1, 3, 2, 1, 3, 4, 5, 3, 4, 5, 4, 1, 2, 5, 3, 4, 5, 3, 4],
    "Social_Interaction_Quality": [2, 4, 2, 1, 3, 3, 1, 3, 2, 2, 2, 3, 5, 1, 4, 2, 4, 3, 2, 4, 3, 2, 3, 2, 2, 3, 4, 1, 1, 3, 1, 5, 3, 4, 2, 2, 4, 5, 3, 2, 1, 2, 2, 3, 1, 3, 4, 5, 3],
    "Empathy_Level": [1, 1, 3, 2, 5, 3, 1, 1, 5, 4, 5, 3, 1, 4, 1, 5, 4, 2, 1, 1, 4, 5, 4, 3, 4, 4, 1, 3, 1, 3, 1, 5, 4, 1, 3, 4, 2, 5, 5, 3, 5, 2, 3, 4, 5, 2, 1, 2, 4],
    "Academic_Grades": ['F', 'A', 'C', 'C', 'B', 'D', 'F', 'F', 'C', 'D', 'D', 'D', 'F', 'F', 'B', 'B', 'A', 'C', 'F', 'C', 'A', 'B', 'B', 'C', 'B', 'A', 'A', 'B', 'C', 'B', 'C', 'C', 'A', 'B', 'C', 'C', 'A', 'D', 'B', 'A', 'B', 'C', 'F', 'B', 'A', 'B', 'F', 'D', 'C'],
    "Stress_Levels": [5, 2, 1, 4, 2, 4, 5, 1, 4, 5, 3, 5, 1, 4, 5, 2, 2, 1, 3, 4, 3, 4, 2, 4, 4, 4, 5, 2, 1, 4, 5, 5, 2, 2, 3, 5, 3, 5, 5, 5, 3, 3, 5, 4, 2, 2, 4, 3, 4],
    "Sleep_Hours_Per_Day": [10, 10, 7, 6, 10, 4, 7, 4, 9, 8, 10, 6, 7, 6, 10, 10, 9, 8, 10, 10, 5, 5, 10, 8, 5, 4, 7, 8, 8, 7, 5, 4, 8, 10, 6, 7, 6, 9, 7, 4, 9, 8, 6, 9, 7, 9, 5, 6, 9]
}

# beautify data

column_lengths = {column: len(values) for column, values in data.items()}

print(column_lengths)



exit()

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert categorical variables into numeric for correlation calculation
df['Plays_Violent_Games'] = df['Plays_Violent_Games'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Academic_Grades'] = df['Academic_Grades'].apply(lambda x: {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}[x])

# Compute Pearson correlation matrix
correlation_matrix = df.corr(method='pearson')
print(correlation_matrix)
