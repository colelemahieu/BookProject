# makes summary book plots (pages per year, avg pages per year, books per year)

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Load the CSV file
df = pd.read_csv("books.csv")

# Ensure 'Year' and 'Pages' are numeric
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['Pages'] = pd.to_numeric(df['Pages'], errors='coerce')

# Drop rows with missing year or page data
df = df.dropna(subset=['Year', 'Pages'])

# Group by Year and sum Pages
pages_per_year = df.groupby('Year')['Pages'].sum().reset_index()
# Group by Year and calculate average Pages
avg_pages_per_year = df.groupby('Year')['Pages'].mean().reset_index()
# Group by Year and count number of books
books_per_year = df.groupby('Year').size().reset_index(name='BookCount')
books_per_year = books_per_year.sort_values('Year')

# Sort by Year
pages_per_year = pages_per_year.sort_values('Year')
avg_pages_per_year = avg_pages_per_year.sort_values('Year')

# Highlight College Region
years = pages_per_year['Year']
pages = pages_per_year['Pages']
college_mask = (years >= 2015) & (years <= 2018)
band_width = 500
upper = pages + band_width
lower = pages - band_width

# Plot Total Pages per Year
plt.figure(figsize=(10, 6))
plt.plot(pages_per_year['Year'], pages_per_year['Pages'], marker='o', linestyle='-')
plt.fill_between(years[college_mask], lower[college_mask], upper[college_mask], color='gray', alpha=0.3, label='College Years')
plt.xlabel('Year', fontsize=16)
plt.ylabel('Pages', fontsize=16)
plt.ylim(0,23000)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tick_params(axis='both', labelsize=14)
#plt.grid(True)
plt.legend(frameon=False, fontsize=16)
plt.tight_layout()
plt.savefig("total_pages_per_year.png", dpi=300)
plt.show()

# Plot Average Pages per Year
plt.figure(figsize=(10, 6))
plt.plot(avg_pages_per_year['Year'], avg_pages_per_year['Pages'], marker='o', linestyle='-', color='orange', label='Average Pages')
plt.xlabel('Year', fontsize=16)
plt.ylabel('Avg book length [pages]', fontsize=16)
plt.ylim(0,600)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tick_params(axis='both', labelsize=14)
#plt.grid(True)
plt.tight_layout()
plt.savefig("average_pages_per_year.png", dpi=300)
plt.show()


# Plot Total Books per Year
plt.figure(figsize=(10, 6))
plt.plot(books_per_year['Year'], books_per_year['BookCount'], marker='o', linestyle='-', color='green', label='Books Read')
plt.xlabel('Year', fontsize=16)
plt.ylabel('Fiction Books Read', fontsize=16)
plt.ylim(0, books_per_year['BookCount'].max() + 5)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tick_params(axis='both', labelsize=14)
plt.tight_layout()
plt.savefig("books_per_year.png", dpi=300)
plt.show()
