import random
import time

servicesAreUp = True

def getData50():
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'

def getData25():
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'    

def getData10():
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'
    
# Your code here!
def getWithRetry(dataFunc):
    maxRetries = 10

    for _ in range(0, maxRetries):
        response = dataFunc()
        if response:
            return response



# # 1. SCENARIO
# # Should return 'You got the data! That only happens 50% of the time!'
# print(getWithRetry(getData50))

# # Should return 'You got the data! That only happens 25% of the time!'
# print(getWithRetry(getData25))

# # Should return 'You got the data! That only happens 10% of the time!'
# print(getWithRetry(getData10))

# # 2. SCENARIO
# servicesAreUp = False

# # Returns None
# print(getWithRetry(getData50))

# # Returns None
# print(getWithRetry(getData25))

# # Returns None
# print(getWithRetry(getData10))


# 3. SCENARIO
def getData50():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'

def getData25():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'    

def getData10():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'
    
# Returns None
print(getWithRetry(getData50))

print(getWithRetry(getData25))

print(getWithRetry(getData10))