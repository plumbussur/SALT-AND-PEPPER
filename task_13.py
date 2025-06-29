import time

def cached(max_size=None, seconds=None):
    if max_size is not None:
        if not isinstance(max_size, int) or max_size <= 0:
            max_size = None
    
    if seconds is not None:
        if not isinstance(seconds, int) or seconds <= 0:
            seconds = None

    def decorator(func):
        cache = {}
        
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            current_time = time.time()
            
            if key in cache:
                result, save_time, last_used = cache[key]
                
                if seconds is not None and (current_time - save_time) > seconds:
                    del cache[key]
                else:
                    cache[key] = (result, save_time, current_time)
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, current_time, current_time)
            
            if max_size is not None and len(cache) > max_size:
                oldest_key = None
                oldest_time = float('inf')
                
                for k, v in cache.items():
                    if v[2] < oldest_time:
                        oldest_key = k
                        oldest_time = v[2]
                
                if oldest_key is not None:
                    del cache[oldest_key]
            
            return result
        
        return wrapper
    
    return decorator


#Done