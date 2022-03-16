def timer(func):
  from datetime import datetime

  def wrapper(*args, **kwargs):
    print(f"Function Name: {getattr(func, '__name__')}")
    start = datetime.now()
    func(*args, **kwargs)
    end = datetime.now()
    time_to_run = end - start

    print(f'Time to run: {time_to_run}')
  
  return wrapper


@timer
def wait_5_seconds():
  from time import sleep
  sleep(5)

wait_5_seconds()
