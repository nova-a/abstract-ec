import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define phi as the golden ratio
phi = (1 + np.sqrt(5)) / 2

# Vertices of a dodecahedron based on phi
vertices = np.array([
    [1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
    [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1],
    [0, phi, 1/phi], [0, phi, -1/phi], [0, -phi, 1/phi], [0, -phi, -1/phi],
    [1/phi, 0, phi], [-1/phi, 0, phi], [1/phi, 0, -phi], [-1/phi, 0, -phi],
    [phi, 1/phi, 0], [-phi, 1/phi, 0], [phi, -1/phi, 0], [-phi, -1/phi, 0]
])

# Indices of the vertices for each face of the pentagon
faces = [
    [0, 12, 13, 4, 8],
    [0, 12, 2, 18, 16],
    [13, 12, 2, 10, 6],
    [18, 2, 10, 11, 3],
    [4, 13, 6, 19, 17],
    [6, 10, 11, 7, 19],
    [17, 19, 7, 15, 5],
    [0, 8, 9, 1, 16],
    [8, 4, 17, 5, 9],
    [9, 5, 15, 14, 1],
    [7, 15, 14, 3, 11],
    [18, 16, 1, 14, 3]
]
# Indices of the vertices for each face in each cube
cubes = [[
    [0, 4, 6, 2],
    [0, 2, 3, 1],
    [3, 1, 5, 7],
    [7, 5, 4, 6],
    [2, 6, 7, 3],
    [0, 4, 5, 1]
],[
    [8, 12, 6, 17],
    [6, 17, 15, 11],
    [11, 15, 1, 18],
    [1, 18, 12, 8],
    [8, 17, 15, 1],
    [6, 12, 18, 11]
],[
    [0, 13, 10, 18],
    [10, 18, 14, 7],
    [14, 7, 17, 9],
    [9, 17, 13, 0],
    [18, 0, 9, 14],
    [13, 10, 7, 17]
],[
    [2, 13, 8, 16],
    [8, 16, 14, 5],
    [5, 14, 11, 19],
    [11, 19, 13, 2],
    [11, 14, 16, 2],
    [8, 13, 19, 5]
],[
    [10, 12, 4, 19],
    [4, 19, 15, 9],
    [15, 9, 16, 3],
    [16, 3, 10, 12],
    [10, 3, 15, 19],
    [4, 9, 16, 12]
]]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# show cubes
for cube, color in zip(cubes, ['red','orange','green','blue','purple']):
    for face in cube:
        polygon = Poly3DCollection([vertices[face]], alpha=0.2, edgecolor='k')
        polygon.set_facecolor(color)
        ax.add_collection3d(polygon)

# show the dodecahedron
for i, face in enumerate(faces):
    polygon = Poly3DCollection([vertices[face]], alpha=0.05, edgecolor='k')
    polygon.set_facecolor([0.5, 0.5, 1])  # Light blue
    ax.add_collection3d(polygon)
    # labels for images
    # center = np.mean(vertices[face], axis=0)
    # ax.text(*center, f'{i+1}', color='red', fontsize=64, ha='center')

# show dodecahedron vertices
ax.scatter(vertices[:,0],vertices[:,1],vertices[:,2], color='b', s=50)

# plot settings
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Dodecahedron')

# setting the aspect ratio for all axes
ax.set_box_aspect([1, 1, 1])  

plt.show()