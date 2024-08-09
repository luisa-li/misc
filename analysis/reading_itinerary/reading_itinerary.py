import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import pandas as pd 

# plotting the basic map of the earth
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# the locations of interest

locations = {
    'Location': ['Lisbon', 'Lima', 'Boston', 'Amsterdam', 'Washington DC', 'Paris', 'Budapest', 'Vienna', 'Salzburg', 'Innsbruck'],
    'Latitude': [38.7223, -12.0464, 42.3601, 52.3676, 38.9072, 48.8566, 47.4979, 48.2082, 47.8095, 47.2692],
    'Longitude': [-9.1393, -77.0428, -71.0589, 4.9041, -77.0369, 2.3522, 19.0402, 16.3738, 13.0550, 11.4041]
}
locations_df = pd.DataFrame(locations)

x = locations_df['Longitude']
y = locations_df['Latitude']

# plotting the locations for each book

hg_drop = world["continent"].isin([
    "Antarctica",
    "Seven seas (open ocean)",
    "Africa",
    "Asia",
    "Oceania", 
    "Europe"
])
hg = world.drop(world[hg_drop].index)

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot()

hg.plot(
    ax=ax,
    color="lightgray",
    edgecolor="black",
    alpha=0.5
)

ax.set_xticks([])
ax.set_yticks([])

plt.scatter(x, y, s=5)

plt.title("Luisa's reading map as of July 2024")
plt.show()
