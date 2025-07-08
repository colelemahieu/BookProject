# makes plots for genre by books and genre by pages

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Load CSV
df = pd.read_csv("books.csv")

# Count books
total_books = len(df)
# Count genres
genre_counts = df['Genre'].value_counts()
# Sum pages per genre
genre_page_totals = df.groupby('Genre')['Pages'].sum().sort_values(ascending=False)
total_pages = genre_page_totals.sum()

# Color Map
genre_color_map = {
    'scifi': '#0077b6',       # Blue
    'fantasy': '#2b9348',     # Green
    'classic': '#a11d33',     # Red
    'fiction': '#8e9aaf',     # Gray
    'mystery': '#9d4edd',     # Purple
    'historical': '#7f4f24'   # Brown
}

# Map original labels to legend
label_map = {
    'scifi': 'Sci-fi',
    'classic': 'Classic Lit',
    'fantasy': 'Fantasy',
    'fiction': 'General',
    'mystery': 'Mystery',
    'historical': 'Historical'
}

# Legend labels applying mapping (fallback to original if not mapped)
colors = [genre_color_map[genre] for genre in genre_counts.index]
legend_labels = [label_map.get(genre, genre) for genre in genre_counts.index]

# Plot pie chart: Genre by books
plt.figure(figsize=(8, 8))
plt.pie(genre_counts, startangle=140, colors=colors, autopct=lambda p: f'{p:.1f}%', textprops={'fontsize': 15})
# legend
legend_elements = [Patch(facecolor=colors[i], label=legend_labels[i]) for i in range(len(genre_counts))]
plt.legend(handles=legend_elements, title="Genres", prop={'size': 14}, title_fontsize=16, loc="center left", bbox_to_anchor=(1, 0.5))

plt.axis('equal')
plt.text(0, 1.15, f'Grand total: {total_books} fiction books', fontsize=18, fontweight='bold', ha='center', va='center')
plt.tight_layout()
plt.savefig("genre_distribution_all.png", dpi=300, bbox_inches='tight')
plt.show()


# Colors and labels for Genre by pages
page_colors = [genre_color_map[genre] for genre in genre_page_totals.index]
page_legend_labels = [label_map.get(genre, genre) for genre in genre_page_totals.index]
# Plot pie chart: Genre by pages
plt.figure(figsize=(8, 8))
plt.pie(genre_page_totals, startangle=140, colors=page_colors, autopct=lambda p: f'{p:.1f}%', textprops={'fontsize': 15})
page_legend_elements = [Patch(facecolor=page_colors[i], label=page_legend_labels[i]) for i in range(len(genre_page_totals))]
plt.legend(handles=page_legend_elements, title="Genres", prop={'size': 14}, title_fontsize=16, loc="center left", bbox_to_anchor=(1, 0.5))
plt.axis('equal')
plt.text(0, 1.15, f'Grand total: {total_pages:,} fiction pages', fontsize=18, fontweight='bold', ha='center', va='center')
plt.tight_layout()
plt.savefig("genre_distribution_by_pages.png", dpi=300, bbox_inches='tight')
plt.show()
