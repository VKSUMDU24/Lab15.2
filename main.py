import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('comptagevelo2014.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

monthly_counts = df.groupby('Month').count()
most_popular_month = monthly_counts['Date'].idxmax()

plt.figure(figsize=(10, 6))
monthly_counts['Date'].plot(kind='bar', color='skyblue')
plt.title('Кількість велосипедистів за місяць у 2014 році')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.xticks(rotation=0)
plt.show()

print(f"Найпопулярніший місяць у велосипедистів: {most_popular_month}")