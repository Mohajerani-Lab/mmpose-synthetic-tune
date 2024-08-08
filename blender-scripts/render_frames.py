import bpy, bgl, gpu, blf, math, os, sys, datetime, time
C = bpy.context
D = bpy.data
O = bpy.ops

scripts_path = r'\\wsl.localhost\Ubuntu\home\galiold\projects\mmpose-synthetic-tune\blender-scripts'

if scripts_path not in sys.path:
    sys.path.append(scripts_path)

from constants import frames_to_render, scene_settings

init_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
out_path = f"{os.path.dirname(D.filepath)}/renders/{init_time}"
os.makedirs(out_path)


# Applying scene settings
def setup_scene(settings):
    D.collections[settings['collection']].hide_viewport = False
    D.collections[settings['collection']].hide_render = False

    D.objects['Camera'].rotation_euler = settings['camera']['rotation_euler']
    D.objects['Camera'].location = settings['camera']['location']

    C.scene.node_tree.nodes['Background'].image = D.images.load(settings['background']['file'])
    D.worlds['World'].node_tree.nodes['Environment Texture'].image = D.images.load(settings['env']['file'])
    D.worlds['World'].node_tree.nodes['Mapping'].inputs['Rotation'].default_value = settings['env']['rotation_euler']
    D.worlds['World'].node_tree.nodes['Background'].inputs['Strength'].default_value = settings['env']['strength']


def clear_scene(options):
    D.collections[settings['collection']].hide_viewport = True
    D.collections[settings['collection']].hide_render = True


for settings in scene_settings:
    setup_scene(settings)
    
    for f in frames_to_render:
        C.scene.frame_set(f)
        file_name = f"synthetic-{settings['collection']}-img{f:03d}.png"
        C.scene.render.filepath = f'{out_path}/{file_name}'
        bpy.ops.render.render(write_still=True)

    clear_scene(settings)