import torch
try:
  assert torch.cuda.is_available() is True
except AssertionError:
  print("需要 GPU 环境，申请教程：https://zhuanlan.zhihu.com/p/642542618")