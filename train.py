import argparse
import os
import importlib
from accelerate.utils import set_seed

import dotenv

dotenv.load_dotenv()

global_seed = int(os.getenv("GLOBAL_SEED", 42))
print(f"Setting global seed to {global_seed}")
set_seed(global_seed)

parser = argparse.ArgumentParser()
parser.add_argument("exp_name", help="path to experiment file")
args = parser.parse_args()

exp_name = args.exp_name
path = os.path.join('configs', exp_name)
path = path.replace('/', '.')

trainer = importlib.import_module(path).trainer
trainer.train()