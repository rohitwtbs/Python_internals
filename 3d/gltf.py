from pygltflib import GLTF2
filename = "/Users/rohitwtbs/Documents/github/Python_internals/3d/endlessrunnerset/scene.gltf"
gltf = GLTF2().load(filename)


import trimesh

# Load GLTF/GLB file
scene = trimesh.load(filename)

# Preview in a window using pyglet or OpenGL
scene.show()
