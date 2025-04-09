import trimesh
import pybullet as p
import pybullet_data
import time

# Start PyBullet simulation in GUI mode
filename = "/Users/rohitwtbs/Documents/github/Python_internals/3d/endlessrunnerset/scene.gltf"
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Load a plane for objects to fall on
plane_id = p.loadURDF("plane.urdf")

# Load mesh using trimesh
mesh = trimesh.load(filename)
mesh.apply_translation(-mesh.center_mass)

# Export mesh to a temporary .obj so pybullet can load it
mesh.export("temp.obj")

# Load mesh as a collision object in pybullet
collision_shape_id = p.createCollisionShape(p.GEOM_MESH, fileName="temp.obj", meshScale=[1, 1, 1])
visual_shape_id = p.createVisualShape(p.GEOM_MESH, fileName="temp.obj", meshScale=[1, 1, 1])

body_id = p.createMultiBody(
    baseMass=1,
    baseCollisionShapeIndex=collision_shape_id,
    baseVisualShapeIndex=visual_shape_id,
    basePosition=[0, 0, 1]  # Drop above the ground
)

# Run the simulation
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/240)

p.disconnect()
