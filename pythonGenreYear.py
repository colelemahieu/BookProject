# makes genre plots for each year 
# linux command to run: for Y in {2008..2024}; do python3 pythonGenreYear.py "$Y"; done

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Generate a genre pie chart for a specific year.")
parser.add_argument("year", type=int, help="The year to generate the genre distribution for")
args = parser.parse_args()

# Load CSV
df = pd.read_csv("books.csv")

# Color Map
genre_color_map = {
    'scifi': '#0077b6',       # Blue
    'fantasy': '#2b9348',     # Green
    'classic': '#a11d33',     # Red
    'fiction': '#8e9aaf',     # Gray
    'mystery': '#9d4edd',     # Purple
    'historical': '#7f4f24'   # Brown
}

# Genre label mapping
label_map = {
    'scifi': 'Sci-fi',
    'classic': 'Classic Lit',
    'fantasy': 'Fantasy',
    'fiction': 'General',
    'mystery': 'Mystery',
    'historical': 'Historical'
}

def plot_genre_distribution_by_year(year):
    # Filter DataFrame by year
    df_year = df[df['Year'] == year]

    # Check if any data exists for that year
    if df_year.empty:
        print(f"No data available for the year {year}.")
        return

    # Count books
    total_books = len(df_year)
    # Count genres
    genre_counts = df_year['Genre'].value_counts()

    # Legend labels
    colors = [genre_color_map[genre] for genre in genre_counts.index]
    legend_labels = [label_map.get(genre, genre) for genre in genre_counts.index]

    # Plot pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(genre_counts, startangle=140, colors=colors, autopct=lambda p: f'{p:.1f}%', textprops={'fontsize': 15})

    legend_elements = [Patch(facecolor=colors[i], label=legend_labels[i]) for i in range(len(genre_counts))]
    plt.legend(handles=legend_elements, title="Genres", prop={'size': 14}, title_fontsize=16, loc="center left", bbox_to_anchor=(1, 0.5))

    plt.axis('equal')
    plt.text(0, 1.15, f'{year}: {total_books} fiction books', fontsize=18, fontweight='bold', ha='center', va='center')
    plt.tight_layout()
    plt.savefig(f"genre_distribution_{year}.png", dpi=300, bbox_inches='tight')
    #plt.show()

# Call function with year argument
plot_genre_distribution_by_year(args.year)

