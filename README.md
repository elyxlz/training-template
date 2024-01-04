A minimalistic and hackable template for developing, training, and sharing deep learning models.


## Stack
- Pytorch
- Accelerate
- Huggingface hub
- Wandb


## Install
```sh
# for training/development
pip install -e '.[train]'

# for inference
pip install .
```

## Structure
```
├── package_name
│   ├── config.py # model config
│   ├── data.py # data processing logic
│   ├── model.py # model definition
│   └── trainer.py # trainer class and train config
```

## Usage
```py
from package_name import (
    DemoModel,
    DemoModelConfig,
    Trainer,
    TrainConfig,
    DemoDataset,
)

model = DemoModel(DemoModelConfig(xxx))

# push, and load models to/from HF Hub
model.push_to_hub(xxx)
model = DemoModel.from_pretrained(xxx)

# train
dataset = DemoDataset(xxx)
trainer = Trainer(model, dataset, TrainConfig(xxx))
trainer.train()
```

You can optionally add more files outside the package, e.g. a 'train.py' entrypoint, 'configs/' dir to store .py training/model runs, etc...
