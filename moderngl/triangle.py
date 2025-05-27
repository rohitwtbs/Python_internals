import moderngl
import moderngl_window
from moderngl_window import geometry

class TriangleApp(moderngl_window.WindowConfig):
    title = "ModernGL Triangle"
    window_size = (800, 600)
    resource_dir = '.'  # Not used here, but good practice

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Vertex shader
        vertex_shader = """
        #version 330
        in vec2 in_position;
        void main() {
            gl_Position = vec4(in_position, 0.0, 1.0);
        }
        """

        # Fragment shader
        fragment_shader = """
        #version 330
        out vec4 fragColor;
        void main() {
            fragColor = vec4(1.0, 0.3, 0.2, 1.0);  // red-orange color
        }
        """

        self.prog = self.ctx.program(
            vertex_shader=vertex_shader,
            fragment_shader=fragment_shader
        )

        # Triangle vertices (NDC coordinates)
        vertices = self.ctx.buffer(
            data=b'-1.0 -1.0  3.0 -1.0  -1.0 3.0'  # 3 points, 2D
        )

        self.vao = self.ctx.vertex_array(
            self.prog,
            [(vertices, '2f', 'in_position')]
        )

    def on_render(self, time: float, frame_time: float):
        self.ctx.clear(0.1, 0.1, 0.1)
        self.vao.render(mode=moderngl.TRIANGLES)


if __name__ == '__main__':
    moderngl_window.run_window_config(TriangleApp)
