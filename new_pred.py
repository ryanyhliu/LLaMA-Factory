from llamafactory.chat import ChatModel
from llamafactory.extras.misc import torch_gc

# %cd /content/LLaMA-Factory/

args = dict(
  model_name_or_path="unsloth/llama-3-8b-Instruct-bnb-4bit", # 使用 4 比特量化版 Llama-3-8b-Instruct 模型
  adapter_name_or_path="llama3_lora",            # 加载之前保存的 LoRA 适配器
  template="llama3",                     # 和训练保持一致
  finetuning_type="lora",                  # 和训练保持一致
  quantization_bit=4,                    # 加载 4 比特量化模型
)
chat_model = ChatModel(args)

messages = []
print("使用 `clear` 清除对话历史，使用 `exit` 退出程序。")
while True:
  query = input("\nUser: ")
  if query.strip() == "exit":
    break
  if query.strip() == "clear":
    messages = []
    torch_gc()
    print("对话历史已清除")
    continue

  messages.append({"role": "user", "content": query})
  print("Assistant: ", end="", flush=True)

  response = ""
  for new_text in chat_model.stream_chat(messages):
    print(new_text, end="", flush=True)
    response += new_text
  print()
  messages.append({"role": "assistant", "content": response})

torch_gc()