# Textcraft Environment

This is the Pypi implementation and packaging of the environment Textcraft introduced in the paper ADaPT.

## Getting started:
The package comes with all the data already, so usage is super easy.

1. Installation:
```bash
pip3 install textcraft
```

2. Usage:
```python
from textcraft import TextCraft


env = TextCraft()
obs, info = env.reset(seed=42)
print(obs)
action = input("> ")
(observation, reward, terminated, truncated, info) = env.step(action)
print(observation, reward, sep="\n")
```


## Acknowledgements
We thank the authors and contributors of [ADaPT](https://allenai.github.io/adaptllm/) for their public code release. 

## Reference
Please cite StateAct:
```bibtex
@article{rozanov2024stateactstatetrackingreasoning,
      title={StateAct: State Tracking and Reasoning for Acting and Planning with Large Language Models}, 
      author={Nikolai Rozanov and Marek Rei},
      year={2024},
      eprint={2410.02810},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2410.02810}, 
}
```

ADaPT
```bibtex

@article{prasad2023adapt,
      author    = "Prasad, Archiki and Koller, Alexander and Hartmann, Mareike and Clark, Peter and Sabharwal, Ashish and Bansal, Mohit and Khot, Tushar",
      title     = "ADaPT: As-Needed Decomposition and Planning with Language Models",
      journal   = "arXiv",
      year      = "2023",}
}
```
