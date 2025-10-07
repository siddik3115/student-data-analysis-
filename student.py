Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import matplotlib.pyplot as plt

# Ask user for number of students
n_students = int(input("Enter the number of students: "))

# Initialize lists to store user input
student_ids = []
math_scores = []
science_scores = []
english_scores = []
attendance = []

# Take input for each student
for i in range(1, n_students + 1):
    print(f"\nEnter details for Student {i}:")
    student_ids.append(i)
    
    math = float(input("Enter Math Score: "))
    science = float(input("Enter Science Score: "))
    english = float(input("Enter English Score: "))
    attend = float(input("Enter Attendance Percentage (0–100): "))
    
    math_scores.append(math)
    science_scores.append(science)
    english_scores.append(english)
    attendance.append(attend)

# Create DataFrame
data = {
    'Student_ID': student_ids,
    'Math_Score': math_scores,
    'Science_Score': science_scores,
    'English_Score': english_scores,
    'Attendance': attendance
}

df = pd.DataFrame(data)

# Display basic information
print("\nDataset Overview:")
print(df.head())

print("\nBasic Statistics:")
print(df.describe())

# Calculate average scores
print("\nAverage Scores:")
print(df[['Math_Score', 'Science_Score', 'English_Score']].mean())

# Find top performers
print("\nTop 5 Students Overall:")
top_students = df.nlargest(5, 'Math_Score')
print(top_students[['Student_ID', 'Math_Score', 'Science_Score', 'English_Score']])

# Calculate correlations
correlation_matrix = df[['Math_Score', 'Science_Score', 'English_Score']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Create visualizations
plt.figure(figsize=(15, 5))

# 1. Box plot for score distribution
plt.subplot(1, 3, 1)
... df[['Math_Score', 'Science_Score', 'English_Score']].boxplot()
... plt.title('Score Distribution')
... plt.ylabel('Scores')
... plt.xticks(rotation=45)
... 
... # 2. Scatter plot for Math vs Science scores
... plt.subplot(1, 3, 2)
... plt.scatter(df['Math_Score'], df['Science_Score'], color='teal')
... plt.title('Math vs Science Scores')
... plt.xlabel('Math Scores')
... plt.ylabel('Science Scores')
... 
... # 3. Bar chart for average scores
... plt.subplot(1, 3, 3)
... df[['Math_Score', 'Science_Score', 'English_Score']].mean().plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
... plt.title('Average Scores')
... plt.ylabel('Average Score')
... plt.xticks(rotation=45)
... 
... plt.tight_layout()
... plt.show()
... 
... # Calculate performance metrics
... df['Overall_Average'] = df[['Math_Score', 'Science_Score', 'English_Score']].mean(axis=1)
... df['Performance_Category'] = pd.qcut(
...     df['Overall_Average'],
...     q=4,
...     labels=['Below Average', 'Average', 'Above Average', 'Excellent']
... )
... 
... # Display performance summary
... print("\nPerformance Summary:")
... print(df['Performance_Category'].value_counts())
... 
... # Identify students needing improvement
... print("\nStudents Needing Improvement (Overall Average < 80):")
... improvement_needed = df[df['Overall_Average'] < 80]
