#%%

from mmpose.apis import MMPoseInferencer
import matplotlib.pyplot as plt

#%%
# Pose models
ap10k = dict(
    pose2d          = '../../configs/animal_2d_keypoint/topdown_heatmap/ap10k/td-hm_hrnet-w48_8xb64-210e_ap10k-256x256.py',
    pose2d_weights  = '../../checkpoints/hrnet_w48_ap10k_256x256-d95ab412_20211029.pth',
)
vitpose_plus = dict(
    pose2d          = '../../configs/animal_2d_keypoint/topdown_heatmap/ViTPose/ViTPose_huge_ap10k_256x192.py',
    pose2d_weights  = '../../checkpoints/vitpose+_huge.pth',
)

animalpsoe = dict(
    pose2d          = '../../configs/animal_2d_keypoint/topdown_heatmap/animalpose/td-hm_hrnet-w48_8xb64-210e_animalpose-256x256.py',
    pose2d_weights  = '../../checkpoints/hrnet_w48_animalpose_256x256-34644726_20210426.pth'
)

# Det models
rtmdet = dict(
    det_model       = '../../mmdetection/configs/rtmdet/rtmdet_l_swin_b_p6_4xb16-100e_coco.py',
    det_weights     = '../../checkpoints/rtmdet_l_swin_b_p6_4xb16-100e_coco-a1486b6f.pth',
)

poser_model         = ap10k
detector_model      = rtmdet
    
inferencer = MMPoseInferencer(**poser_model, **detector_model, device='cuda:0')

#%%
file = 'synthetic.mp4'
input_path = f'../../data/{file}'
output_path = '../../vis_results/mmpose/'

result_generator = inferencer(
    input_path,
    radius=3,
    thickness=2,
    vis_out_dir=output_path,
    draw_heatmap=True,
    det_cat_ids=5
)

results = [res for res in result_generator]

#%%

img = plt.imread(f'{output_path}/{file}')
pose = img[:img.shape[0]//2, :, :]
heatmap = img[img.shape[0]//2:, :, :]

fig = plt.figure(figsize=(15, 15))
ax_array = fig.subplots(2, 1)
ax_array[0].imshow(pose)
ax_array[1].imshow(heatmap)
# %%
results[0]['predictions'][0][0].keys()