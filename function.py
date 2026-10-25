path = "/Users/tarun/DevOps/python-learning/dataStructures.py"

def IsStale(path, maxAge) :
    import os
    import time

    if not os.path.exists(path) :
        raise FileNotFoundError("the file at this {path} does not exist")

    lastModifiedTime = os.path.getmtime(path)
    currentTime = time.time()

    age = currentTime - lastModifiedTime

    return age > maxAge

if IsStale(path,300) :
    print(f"Hi, the file at this {path} is stale.")


else :
    print(f"Hi, the file at this {path} is not stale.")   

    print("yess")