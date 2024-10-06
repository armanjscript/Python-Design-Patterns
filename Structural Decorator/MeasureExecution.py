import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        
        print(f"{func.__name__} executed in {(end_time - start_time):.5f}")
        
        return result
    return wrapper

#Apply time_it decorator
@time_it
def slow_function(duration):
    time.sleep(duration)
    return duration

@time_it
def fast_function():
    print("This is fast function")
    
    
if __name__ == "__main__":
    slow_function(2)
    fast_function()