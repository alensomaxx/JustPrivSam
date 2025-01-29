def mcp_nand(x1,x2):
    w1 = -2
    w2 = -2
    weighted_sum =(x1*w1)+(x2*w2)
    if weighted_sum >= -3:
        return 1 #does fire
    else:
        return 0 #doesn't fire
    
#Testing the NAND function for all combinations of inputs
print("NAND Gate using McCulloch-Pitts Neuron:")
print(f"Input: (0,0) -> Output: {mcp_nand(0,0)}") 
print(f"Input: (0,1) -> Output: {mcp_nand(0,1)}")
print(f"Input: (1,0) -> Output: {mcp_nand(1,0)}")
print(f"Input: (1,1) -> Output: {mcp_nand(1,1)}")

