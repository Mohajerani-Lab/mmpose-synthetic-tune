from datetime import datetime
import pytz
import subprocess

montreal_tz = pytz.timezone('America/Montreal')
now_utc = datetime.now(pytz.utc)
now_montreal = now_utc.astimezone(montreal_tz)
current_time = now_montreal.strftime('%Y-%m-%d_%H-%M-%S')

notes = 'trained-on-ap10k'

args = [
    'python',
    'tools/train.py',
    'mmpose-synthetic-tune/dataset-coco/custom-configs/td-hm_hrnet-w48_8xb64-210e_20kp-256x256.py',
    '--work-dir',
    f'mmpose-synthetic-tune/models/train-{current_time}-{notes}',
    '--resume',
]

subprocess.run(args)