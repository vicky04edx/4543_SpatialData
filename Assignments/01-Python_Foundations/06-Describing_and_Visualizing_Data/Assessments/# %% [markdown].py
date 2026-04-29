# %% [markdown]
# # 🧪 Pandas Wrangle Lab: Clean & Explore a Real Dataset
# 
# ## 🔹 LEARNING GOALS:
# - Practice loading, cleaning, and exploring real-world data
# - Apply column creation, renaming, sorting, and filtering
# - Use `.info()`, `.describe()`, and `.query()` fluently
# 

# %% [markdown]
# ### 📥 1. Load the Dataset

# %%
import pandas as pd
df = pd.read_csv("../../data/students.csv")
df.head()

# %% [markdown]
# ### 🔎 2. Inspect and Audit the Data

# %%
# Basic overview
df.info()

# %%
# Summary stats
df.describe()

# %% [markdown]
# ### 🧼 3. Clean Missing or Invalid Data

# %%
# Check for missing values
df.isnull().sum()

# %%
# Drop rows with missing names
df.dropna(subset=["first_name", "last_name"], inplace=True)

# Fill any missing scores with column average
df["math_score"].fillna(df["math_score"].mean(), inplace=True)
df["science_score"].fillna(df["science_score"].mean(), inplace=True)


# %% [markdown]
# ### 🧠 4. Feature Engineering (New Columns)

# %%
# Add average and grade
df["average_score"] = (df["math_score"] + df["science_score"]) / 2

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

df["grade"] = df["average_score"].apply(grade)
df.head()

# %% [markdown]
# ### 🔽 5. Sorting and Filtering

# %%
# Top performers
df[df["average_score"] > 90].sort_values(by="average_score", ascending=False).head()

# %% [markdown]
# ### 📊 6. Group and Describe by Grade

# %%
# How many of each grade?
df["grade"].value_counts()

# %%
# Average scores per grade group
df.groupby("grade")[["math_score", "science_score", "average_score"]].mean()

# %% [markdown]
# ### 💾 7. Save the Cleaned Dataset

# %%
df.to_csv("student_scores_cleaned.csv", index=False)

# %% [markdown]
# ### 🧠 Challenge Task
# 
# > Your turn! Filter out students who got a D, sort by last name, and export to a new file:
# - Only include columns: `first_name`, `last_name`, `grade`
# - Save it as `"d_students.csv"`
# 

# %%
import pandas as pd

# Load dataset
df = pd.read_csv(r"c:\Users\Victoria Heredia\Downloads\4543_SpatialData\Assignments\01-Python_Foundations\04-Foundations\Lessons\04-Data_Input_Output\students.csv")

# Clean columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# -----------------------
# 🎯 Create grade
# -----------------------
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

df["grade"] = df["score"].apply(assign_grade)

# -----------------------
# ✅ FIXED name splitting
# -----------------------
df["first_name"] = df["name"].str.split().str[0]
df["last_name"] = df["name"].str.split().str[-1]

# -----------------------
# Filter D students
# -----------------------
d_students = df[df["grade"] == "D"]

# Sort by last name
d_students = d_students.sort_values(by="last_name")

# Keep required columns
d_students = d_students[["first_name", "last_name", "grade"]]

# Save file
d_students.to_csv("d_students.csv", index=False)

print(d_students)

# %% [markdown]
# ### 📝 Summary
# 
# This lab gave you hands-on experience with:
# - Cleaning nulls and type mismatches
# - Creating new columns
# - Filtering and sorting real data
# - Grouping and summarizing by categorical features
# 
# Your data wrangling toolbox is now ready for real-world messiness. 🧹🛠️
# 

