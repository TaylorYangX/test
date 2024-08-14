import torch
import time

# 创建两个二维张量
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])

start_time = time.time()
# 求和
result = tensor1 + tensor2
end_time = time.time()

print("the model run time is ",end_time - start_time)
print("the tensor 1 is \n",tensor1)
print("the tensor 2 is \n",tensor2)

print("Sum:")
print(result)
