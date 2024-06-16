import json

args = dict(
  stage="sft",                        # 进行指令监督微调
  do_train=True,
  model_name_or_path="unsloth/llama-3-8b-Instruct-bnb-4bit", # 使用 4 比特量化版 Llama-3-8b-Instruct 模型
  dataset="ml_selfcn,ml_loradatacn,ml_knowledgecn",      # 使用 alpaca 和自我认知数据集
  template="llama3",                     # 使用 llama3 提示词模板
  finetuning_type="lora",                   # 使用 LoRA 适配器来节省显存
  lora_target="all",                     # 添加 LoRA 适配器至全部线性层
  output_dir="llama3_lora",                  # 保存 LoRA 适配器的路径
  per_device_train_batch_size=16,               # 批处理大小
  gradient_accumulation_steps=4,               # 梯度累积步数
  lr_scheduler_type="cosine",                 # 使用余弦学习率退火算法
  logging_steps=1,                      # 每 10 步输出一个记录
  warmup_ratio=0.1,                      # 使用预热学习率
  save_steps=1000,                      # 每 1000 步保存一个检查点
  learning_rate=1e-4,                     # 学习率大小
  num_train_epochs=8.0,                    # 训练轮数
  max_samples=300,                      # 使用每个数据集中的 300 条样本
  max_grad_norm=1.0,                     # 将梯度范数裁剪至 1.0
  quantization_bit=8,                     # 使用 4 比特 QLoRA
  loraplus_lr_ratio=16.0,                   # 使用 LoRA+ 算法并设置 lambda=16.0
  fp16=True,                         # 使用 float16 混合精度训练
  logging_dir="tensorLogs",                     # 日志保存路径
)

json.dump(args, open("train_llama3.json", "w", encoding="utf-8"), indent=2)

# %cd /content/LLaMA-Factory/

# !llamafactory-cli train train_llama3.json