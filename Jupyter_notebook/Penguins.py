import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("penguins")
data.head()

plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='species', kde=True, hue='sex')
plt.title('Species Distribution by Gender')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='island', y='body_mass_g', hue='sex')
plt.title('Body mass rate by Island and Gender')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='species', y='flipper_length_mm', hue='sex')
plt.title('Species rate by flipper length and Gender')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='sex', y='bill_depth_mm', hue='bill_length_mm')
plt.title('Gender rate by bill depth and bill length')
plt.show()