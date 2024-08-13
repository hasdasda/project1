import torch

tensor = torch.arange(0, 10)
print(tensor)

one_to_ten = torch.arange(start=0,end=11, step = 1)
print(one_to_ten)

# Creating tensors like
ten_zeros = torch.zeros_like(input=one_to_ten)
print(ten_zeros)