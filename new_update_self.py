# cd /content/LLaMA-Factory/

import json

NAME = "Llama-Chinese"
AUTHOR = "LLaMA Factory"

with open("data/identity.json", "r", encoding="utf-8") as f:
  dataset = json.load(f)

for sample in dataset:
  sample["output"] = sample["output"].replace("{{"+ "name" + "}}", NAME).replace("{{"+ "author" + "}}", AUTHOR)

with open("data/identity.json", "w", encoding="utf-8") as f:
  json.dump(dataset, f, indent=2, ensure_ascii=False)