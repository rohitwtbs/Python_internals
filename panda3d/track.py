


from panda3d.core import (
    loadPrcFileData, WindowProperties, GraphicsPipe, GraphicsEngine,
    FrameBufferProperties, GraphicsOutput, GraphicsStateGuardian,
    GraphicsWindow, NodePath, AmbientLight, DirectionalLight, LVector3
)
from panda3d.core import Filename
from panda3d.assimp import load_model
import sys

# Basic configuration
loadPrcFileData("", """
    win-title Panda3D Custom Window
    win-size 1280 720
    fullscreen 0
""")

from direct.showbase.GraphicsEngine import GraphicsEngine
from direct.showbase.Loader import Loader
from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import ClockObject

# Create graphics engine and window
props = WindowProperties()
props.setSize(1280, 720)
fb_props = FrameBufferProperties()
fb_props.setRgbColor(True)
fb_props.setDepthBits(1)

engine = GraphicsEngine.getGlobalPtr()
pipe = GraphicsPipe.Selection.getDefaultPipe()
window = engine.makeOutput(pipe, "main_window", 0, fb_props, props,
                           GraphicsPipe.BF_require_window)

# Set up the scene graph
render = NodePath("render")
camera = NodePath("camera")
lens = camera.attachNewNode("lens")

# Attach camera to window
cam = engine.makeCamera(window)
cam.reparentTo(camera)
camera.reparentTo(render)
camera.setPos(0, -50, 20)
camera.lookAt(0, 0, 0)

# Load your 3D road track
track = load_model("track/asset/gltf/road_I_1.glb")
track.reparentTo(render)
track.setScale(1)
track.setPos(0, 0, 0)

# Add lighting
ambient = AmbientLight("ambient")
ambient.setColor((0.4, 0.4, 0.4, 1))
ambient_np = render.attachNewNode(ambient)
render.setLight(ambient_np)

directional = DirectionalLight("directional")
directional.setDirection(LVector3(-1, -1, -1))
directional.setColor((0.8, 0.8, 0.8, 1))
directional_np = render.attachNewNode(directional)
render.setLight(directional_np)

# Set up a manual loop
globalClock = ClockObject.getGlobalClock()

def update(task):
    dt = globalClock.getDt()
    engine.renderFrame()
    return Task.cont

# Add the update task
taskMgr.add(update, "update-task")

# Run the loop
try:
    while True:
        taskMgr.step()
except KeyboardInterrupt:
    print("Exiting.")
    sys.exit()
