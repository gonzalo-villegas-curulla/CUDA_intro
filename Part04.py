# %% Profile a cuda kernel: nvprof, nvvp
with open('cuda_convo.py','r') as f:
    # print(f.read())
    !nvprof python cuda_convo.py