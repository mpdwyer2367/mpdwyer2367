import random
import datetime
import textwrap

# Generate dummy sentiment data for 5 sectors over the last 10 days
sectors = ['Retail REIT', 'Office REIT', 'Industrial REIT', 'Hotel REIT', 'Residential REIT']
num_days = 10
base_date = datetime.date.today()
dates = [base_date - datetime.timedelta(days=i) for i in range(num_days)][::-1]

# Generate sentiment scores between -1 (negative) and 1 (positive)
sentiment_data = {
    sector: [round(random.uniform(-1, 1), 2) for _ in range(num_days)]
    for sector in sectors
}

# Create ASCII line graphs for each sector

def draw_line_graph(values, width=40, height=10):
    """Return a string with an ASCII line graph for the given values."""
    min_val = min(values)
    max_val = max(values)
    span = max_val - min_val or 1.0
    scaled = [int((v - min_val) / span * (height - 1)) for v in values]
    lines = [[' ' for _ in range(len(values))] for _ in range(height)]
    for i, y in enumerate(scaled):
        lines[height - 1 - y][i] = '*'
    graph_lines = [''.join(line) for line in lines]
    return '\n'.join(graph_lines)

# Create color-coded heatmap string
COLORS = {
    'green': '\033[92m',
    'red': '\033[91m',
    'end': '\033[0m'
}

def heatmap_cell(value):
    color = COLORS['green'] if value >= 0 else COLORS['red']
    return f"{color}{value:>5.2f}{COLORS['end']}"

# Generate simple AI insight

def ai_insight():
    averages = {sector: sum(vals) / len(vals) for sector, vals in sentiment_data.items()}
    top_sector = max(averages, key=averages.get)
    return (
        f"AI Insight: {top_sector} is experiencing a surge in positive sentiment "
        f"due to recent earnings beat."
    )

# Display dashboard

def display_dashboard():
    print("Sentiment Over Time (line graphs)\n")
    for sector, values in sentiment_data.items():
        print(f"-- {sector} --")
        print(draw_line_graph(values))
        print()

    print("Sentiment Heatmap by Sector\n")
    header = ' '.join([d.strftime('%m-%d') for d in dates])
    print(' ' * 20 + header)
    for sector, values in sentiment_data.items():
        cells = ' '.join(heatmap_cell(v) for v in values)
        print(f"{sector:<20}{cells}")
    print()

    print("News Feed\n")
    news_items = [
        "REIT A beats earnings expectations, stock surges.",
        "Sector rotation draws attention to industrial properties.",
        "Analysts predict strong demand for residential rentals.",
    ]
    for item in news_items:
        print(f"- {item}")
    print()

    print(ai_insight())

if __name__ == '__main__':
    display_dashboard()
