import matplotlib.pyplot as plt
from collections import defaultdict
import itertools
import matplotlib.cm as cm
import numpy as np




# Data
data = [
    ("RM11-2_S1", 0.603, 0.509),
    ("RM11-2_S2", 0.596, 0.506),
    ("RM11-2_S3", 0.6, 0.502),
    ("RM11-2_S4", 0.577, 0.493),
    ("RM11-2_S5", 0.563, 0.502),
    ("RM11-3_S1", 0.693, 0.19),
    ("RM11-3_S2", 0.693, 0.192),
    ("RM11-3_S3", 0.69, 0.207),
    ("RM11-3_S4", 0.695, 0.187),
    ("RM11-3_S5", 0.697, 0.189),
    ("RM11-3_S6", 0.693, 0.195),
    ("RM11-4_S1", 0.695, 0.2),
    ("RM11-4_S2", 0.717, 0.196),
    ("RM11-4_S3", 0.716, 0.226),
    ("RM04_S1", 0.698856229, 0.268334293),
    ("RM04_S2", 0.695557653, 0.222197769),
    ("RM04_S3", 0.714624791, 0.247063677),
    ("RM04_S4", 0.69147622, 0.242078922),
    ("RM04_S5", 0.705965839, 0.248401409),
    ("RM04_S6", 0.696374906, 0.244911619),
    ("RM01_S1", 0.718585033, 0.258967316),
    ("RM01_S2", 0.713605864, 0.241541201),
    ("RM01_S3", 0.720612113, 0.259287922),
    ("RM01_S4", 0.704293948, 0.251697133),
    ("RM02_S1", 0.687333403, 0.224199388),
    ("RM02_S2", 0.695606554, 0.250510928),
    ("RM02_S3", 0.697692237, 0.253083223),
    ("RM05_S1", 0.679679638, 0.258967316),
    ("TR05_S1", 0.707596953, 0.311543302),
    ("TR05_S2", 0.683678302, 0.255833917),
    ("TR05_S3", 0.66702195, 0.300860966),
    ("TR05_S4", 0.668885559, 0.238139236),
    ("TR05_S5", 0.65585498, 0.321632946),
    ("TR05_S6", 0.669247851, 0.231349905),
    ("TR05_S7", 0.669949181, 0.299403375),
    ("TR05_S8", 0.681997344, 0.311097849),
    ("TR05_S9", 0.683706074, 0.316966626),
    ("TR05_S10", 0.696756082, 0.224491151),
    ("RM14_S1", 0.717846435, 0.255345255),
    ("RM14_S2", 0.722981847, 0.252793394),
    ("RM14_S3", 0.717089348, 0.251881493),
    ("RM14_S4", 0.704293948, 0.251697133),
    ("RM14_S5", 0.721182666, 0.257347756),
    ("RM14_S6", 0.724971242, 0.201524269),
    ("RM11_S1", 0.702878702, 0.215809414),
    ("RM11_S2", 0.683772844, 0.205561415),
    ("RM11_S3", 0.689644112, 0.203012559),
    ("RM11_S4", 0.690049248, 0.202636543),
    ("RM11_S5", 0.687672644, 0.211033788),
    ("RM11_S6", 0.681997692, 0.202836714),
    ("RM11_S7", 0.693119016, 0.19174593),
    ("RM11_S8", 0.700634112, 0.343560491),
    ("RM11_S9", 0.680701308, 0.189332139),
    ("RM11_S10", 0.703037983, 0.212561904),
    ("RM18_S1", 0.72045702, 0.2454232),
    ("RM18_S2", 0.71543734, 0.2398455),
    ("RM18_S3", 0.6988324, 0.24158684),
]


# Group the data by all the letters before the underscore
grouped_data = defaultdict(list)
for name, mg, cr in data:
    key = '_'.join(name.split('_')[:-1])  # Get all the letters before the underscore
    grouped_data[key].append((mg, cr))

# Create a scatter plot
fig, ax = plt.subplots(figsize=(8, 8 * 1.6))  # Adjust the figsize to maintain the desired aspect ratio

# Define a color map
color_map = cm.get_cmap('tab10', len(grouped_data))

# Define a list of marker shapes
marker_shapes = ['o', 's', '^', 'D', 'v', 'p', 'H', 'X', '<', '>']

for index, (key, values) in enumerate(grouped_data.items()):
    mg_values, cr_values = zip(*values)
    color = color_map(index)
    marker = np.random.choice(marker_shapes)  # Randomly select a marker shape
    ax.scatter(mg_values, cr_values, label=key, color=color, marker=marker, s=40)  # Reduce marker size by 20%

# Set labels for the x and y axes
ax.set_xlabel('Mg# in spinel', weight='bold', size=14)
ax.set_ylabel('Cr# in spinel', weight='bold', size=14)

# Set axis ranges and invert x-axis
ax.set_xlim(1, 0)  # Reverse x-axis range
ax.set_ylim(0, 1)  # Set y-axis range

# Set ticks at 0.0, 0.5, and 1.0 on both axes
ax.set_xticks([0.0, 0.5, 1.0])
ax.set_yticks([0.0, 0.5, 1.0])

# Adjust tick direction inward and make ticks longer and bold
ax.tick_params(direction='in', length=12, width=1.5, labelsize=12)

# Set spines (borders) of the plot bold
for spine in ax.spines.values():
    spine.set_linewidth(2.5)

# Remove interior grid
ax.grid(False)

# Add a legend
ax.legend()

# Save the plot as a PDF in the current directory
plt.tight_layout()
plt.savefig('./scatter_plot.pdf', format='pdf')

# Show the plot
plt.show()
