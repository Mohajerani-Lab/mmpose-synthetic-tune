import glob
import os
import argparse
import shutil
import numpy as np
import random
import json

def extract_samples(sample_size, out_dir):
    all_samples = []

    for folder in os.listdir('frames'):
        files = sorted(glob.glob(f'frames/{folder}/*.png'))

        indices = np.round(np.linspace(0, len(files) - 1, sample_size)).astype(int)

        samples = [ files[indices[i]] for i in range(sample_size) ]

        all_samples.extend(samples)

    [ shutil.copy(t, f'{out_dir}/images') for t in all_samples ]

    add_previous_annotations(all_samples, out_dir)


def add_previous_annotations(samples, out_dir):
    sample_names = list(map(lambda x: x.split('/')[-1], samples))

    with open('annotations/combined.json') as json_file:
        prev_labels = json.loads(json_file.read())

    prev_images: list = prev_labels['images']
    prev_annots: list = prev_labels['annotations']

    new_images = []
    new_annots = []

    for idx, prev_image in enumerate(prev_images):
        if not prev_image['file_name'] in sample_names:
            continue

        assert prev_image['id'] == prev_annots[idx]['image_id']

        new_images.append(prev_image)
        new_annots.append(prev_annots[idx])

    print(f'Found {len(new_images)} frames already labeled')

    prev_labels['images'] = new_images
    prev_labels['annotations'] = new_annots

    with open(f'{out_dir}/annotations/{out_dir}.json', 'w') as file:
        file.write(json.dumps(prev_labels))


def main():
    parser = argparse.ArgumentParser(description="Extract samples by the given size, defaults to 10")
    parser.add_argument('train_size', type=str, help='Size of the training samples extracted')
    args = parser.parse_args()

    sample_name = f'sample-{args.train_size}'

    if not os.path.isdir(sample_name):
        os.makedirs(sample_name)
        os.makedirs(f'{sample_name}/images')
        os.makedirs(f'{sample_name}/annotations')

    extract_samples(sample_size=int(args.train_size), out_dir=sample_name)


if __name__ == "__main__":
    main()