import bpy, os, sys, datetime, json
C = bpy.context
D = bpy.data
O = bpy.ops

scripts_path = r'\\wsl.localhost\Ubuntu\home\galiold\projects\mmpose-synthetic-tune\blender-scripts'

if scripts_path not in sys.path:
    sys.path.append(scripts_path)

from constants import frames_to_render

with open(f'{scripts_path}/scene_settings.json') as f:
    scene_settings = json.loads(f.read())

init_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
out_path = f"{os.path.dirname(D.filepath)}/renders/{init_time}"
os.makedirs(out_path)


def rebuild_softbody_cache():
    with bpy.context.temp_override( point_cache=D.objects['BlackCattle_Body'].modifiers['Softbody'].point_cache ):
        bpy.ops.ptcache.free_bake()
        bpy.ops.ptcache.bake_all(bake=True)


def rebuild_hair_cache():
    with bpy.context.temp_override( point_cache=D.objects['BlackCattle_Body'].particle_systems['BlackCattle_Hair_Tail_Long'].point_cache ):
        bpy.ops.ptcache.free_bake()
        bpy.ops.ptcache.bake(bake=True)


def show_scene_collection(settings):
    D.collections[settings['collection']].hide_viewport = False
    D.collections[settings['collection']].hide_render = False


def adjust_cow_root(settings):
    D.objects['BlackCattle_Rig_grp'].pose.bones['Root'].rotation_quaternion = settings['cow_root']['rotation_quaternion']
    rebuild_softbody_cache()
    rebuild_hair_cache()


def hide_scene_collection(settings):
    D.collections[settings['collection']].hide_viewport = True
    D.collections[settings['collection']].hide_render = True


def adjust_camera(settings):
    D.objects['Camera'].rotation_euler = settings['camera']['rotation_euler']
    D.objects['Camera'].location = settings['camera']['location']


def adjust_background(settings):
    C.scene.node_tree.nodes['Background'].image = D.images.load(settings['background']['file'])


def adjust_world(settings):
    D.worlds['World'].node_tree.nodes['Environment Texture'].image = D.images.load(settings['env']['file'])
    D.worlds['World'].node_tree.nodes['Mapping'].inputs['Rotation'].default_value = settings['env']['rotation_euler']
    D.worlds['World'].node_tree.nodes['Background'].inputs['Strength'].default_value = settings['env']['strength']


# Applying scene settings
def setup_scene(settings):
    show_scene_collection(settings)
    adjust_cow_root(settings)
    adjust_camera(settings)
    adjust_world(settings)


def render_frame(frame_number, outpath):
    C.scene.frame_set(f)
    C.scene.render.filepath = f'{out_path}/{file_name}'
    bpy.ops.render.render(write_still=True)

for settings in scene_settings:
    setup_scene(settings)
    
    for f in frames_to_render:
        file_name = f"synthetic-{settings['collection']}-img{f:03d}.png"
        render_frame(f, file_name)

    hide_scene_collection(settings)
