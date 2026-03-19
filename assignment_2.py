
import numpy as np
import pandas as pd

print("### Environment Check ###")
print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print() 

def check_la_size(dataset):
    
    return len(dataset)

data = np.random.rand(5, 3)  

print("### Function check_la_size ###")
print("Dataset size:", check_la_size(data))
print()


print("### Dictionary Manipulation ###")


results = {
    "Small dataset": "The number is less than 1000",
    "Medium dataset": "The number is between 1,000 and 10,000 (inclusive)",
    "Large dataset": "The number is greater than 10,000"
}


results['Precision'] = 0.925


results['Accuracy'] = 0.855


print(results)
print()


print("### SAMPLE OUTPUTS ###")
print("NumPy version: 1.22.3")
print("Pandas version: 1.4.2")
print("Dataset size: 5")
print({
    "Small dataset": "The number is less than 1000",
    "Medium dataset": "The number is between 1,000 and 10,000 (inclusive)",
    "Large dataset": "The number is greater than 10,000",
    "Precision": 0.925,
    "Accuracy": 0.855
})
