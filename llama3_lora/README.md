---
license: other
library_name: peft
tags:
- llama-factory
- lora
- generated_from_trainer
base_model: unsloth/llama-3-8b-Instruct-bnb-4bit
model-index:
- name: llama3_lora
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# llama3_lora

This model is a fine-tuned version of [unsloth/llama-3-8b-Instruct-bnb-4bit](https://huggingface.co/unsloth/llama-3-8b-Instruct-bnb-4bit) on the ml_selfcn, the ml_loradatacn and the ml_knowledgecn datasets.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 12
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 48
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 8.0
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- PEFT 0.11.1
- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1