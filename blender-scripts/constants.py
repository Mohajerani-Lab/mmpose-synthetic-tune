scene_settings = [
    # Scene 0
    {
        'collection': 'scene0',
        'background': {
            'file': r'c:\Users\Ali Goldani\projects-win\blender\Blender_Reqs\backgrounds\0.png'
        },
        'env': {
            'file': r'c:\Users\Ali Goldani\projects-win\blender\Blender_Reqs\HDRIs\evening_meadow_4k.exr',
            'rotation_euler': [0.7731807827949524, 1.3020155429840088, 0.0],
            'strength': 5.0
        },
        'camera': {
            'location': [6.934477806091309, -0.567044734954834, 2.016144037246704],
            'rotation_euler': [1.4630913734436035, -5.920300338857487e-08, 1.5707963705062866]
        }
    },
    # Scene 2
    {
        'collection': 'scene2',
        'background': {
            'file': r'c:\Users\Ali Goldani\projects-win\blender\Blender_Reqs\backgrounds\2.png'
        },
        'env': {
            'file': r'c:\Users\Ali Goldani\projects-win\blender\Blender_Reqs\HDRIs\overcast_soil_puresky_4k.exr',
            'rotation_euler': [1.2042770385742188, 1.9582593441009521, 0.0],
            'strength': 5.0
        },
        'camera': {
            'location': [11.108087539672852, -1.7524324655532837, 1.9575519561767578],
            'rotation_euler': [1.457517385482788, -5.890601784130922e-08, 1.5707963705062866]
        }
    },
    # Scene 3
    {'collection': 'scene3',
 'background': {'file': 'C:\\Users\\Ali '
                        'Goldani\\projects-win\\blender\\Blender_Reqs\\backgrounds\\3.png'},
 'env': {'file': 'C:\\Users\\Ali '
                 'Goldani\\projects-win\\blender\\Blender_Reqs\\HDRIs\\scythian_tombs_2_4k.exr',
         'rotation_euler': [0.7679448127746582, 0.3490658402442932, 0.0],
         'strength': 1.0},
 'camera': {'location': [8.086649894714355,
                         -2.374967098236084,
                         1.6400210857391357],
            'rotation_euler': [1.4844555854797363,
                               -6.006775521427699e-08,
                               1.5707963705062866]}},
                               
]

frames_to_render = [0]

categories = [
    {
        "id": 1,
        "name": "cow",
        "supercategory": "",
        "keypoints": [
            "Back1",
            "Back2",
            "Back3",
            "Back4",
            "Head",
            "Nose",
            "Neck",
            "L_Shoulder",
            "L_Elbow",
            "L_F_Paw",
           "R_Shoulder",
            "R_Elbow",
            "R_F_Paw",
            "Belly",
            "L_Hip",
            "L_Knee",
            "L_H_Paw",
            "R_Hip",
           "R_Knee",
            "R_H_Paw"
        ],
        "skeleton": [
            [
                3,
                4
            ],
            [
                16,
                17
            ],
            [
                12,
                13
            ],
            [
                8,
                9
            ],
            [
                11,
                14
            ],
            [
                18,
                1
            ],
            [
                6,
                5
            ],
            [
                18,
                19
            ],
            [
                14,
                18
            ],
            [
                14,
                15
            ],
            [
                9,
                10
            ],
            [
                8,
                14
            ],
            [
                1,
                2
            ],
            [
                19,
                20
            ],
            [
                15,
                1
            ],
            [
                15,
                16
            ],
            [
                7,
                6
            ],
            [
                4,
                7
            ],
            [
                11,
                12
            ],
            [
                2,
                3
            ],
            [
                7,
                11
            ],
            [
                7,
                8
            ]
        ]
    }
]

img_template = {
    "id": 0,
    "width": 0,
    "height": 0,
    "file_name": "",
    "license": 0
}

ann_template = {
    "id": 0,
    "image_id": 0,
    "category_id": 1,
    "segmentation": [],
    "area": 0,
    "bbox": [],
    "iscrowd": 0,
    "attributes": {
        "occluded": False,
        "keyframe": False
    },
    "keypoints": [],
    "num_keypoints": 20
}


bones = [
    'bptr1-Back1',
    'bptr2-Back2',
    'bptr3-Back3',
    'bptr4-Back4',
    'bptr5-Head',
    'bptr6-Nose',
    'bptr7-Neck',
    'bptr8-L_Shoulder',
    'bptr9-L_Elbow',
    'bptr10-L_F_Paw',
    'bptr11-R_Shoulder',
    'bptr12-R_Elbow',
    'bptr13-R_F_Paw',
    'bptr14-Belly',
    'bptr15-L_Hip',
    'bptr16-L_Knee',
    'bptr17-L_H_Paw',
    'bptr18-R_Hip',
    'bptr19-R_Knee',
    'bptr20-R_H_Paw'
]
