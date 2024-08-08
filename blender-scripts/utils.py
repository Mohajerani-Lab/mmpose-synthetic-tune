# Utility functions to be used in blender Python Console
import json

def get_scene_properties(scene_number):
    scene_settings = {
        'collection': f'scene{scene_number}',
        'background': {
            'file': D.cameras['Camera'].background_images[0].image.filepath_from_user()
        },
        'env': {
            'file': D.worlds['World'].node_tree.nodes['Environment Texture'].image.filepath_from_user(),
            'rotation_euler': list(D.worlds['World'].node_tree.nodes['Mapping'].inputs['Rotation'].default_value),
            'strength': D.worlds['World'].node_tree.nodes['Background'].inputs['Strength'].default_value
        },
        'camera': {
            'location': list(D.objects['Camera'].location),
            'rotation_euler': list(D.objects['Camera'].rotation_euler)
        }
    }
    print(json.dumps(scene_settings))
