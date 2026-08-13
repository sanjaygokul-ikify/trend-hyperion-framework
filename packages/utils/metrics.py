import time
from packages.utils.logging import log_info
def track_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        log_info(f'Executed {func.__name__} in {execution_time:.2f} seconds')
        return result
    return wrapper