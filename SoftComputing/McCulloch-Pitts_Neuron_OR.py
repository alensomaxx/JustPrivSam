def mcp_or(x1,x2):
    w1 = 1
    w2 = 1
    weighted_sum =(x1*w1)+(x2*w2)
    if weighted_sum >=1:
        return 1 #does fire
    else:
        return 0 #doesn't fire
    
#Testing the OR function for all combinations of inputs
print("OR Gate using McCulloch-Pitts Neuron:")
print(f"Input: (0,0) -> Output: {mcp_or(0,0)}") 
print(f"Input: (0,1) -> Output: {mcp_or(0,1)}")
print(f"Input: (1,0) -> Output: {mcp_or(1,0)}")
print(f"Input: (1,1) -> Output: {mcp_or(1,1)}")

