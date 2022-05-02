import psutil
import GPUtil
import pandas as pd
import time
import signal
import sys

results = []
def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    pd.DataFrame(results).to_csv('results.csv', header=['time','cpu','gpu','mem'],index=None)
    sys.exit(0)

def main():
    mem = psutil.virtual_memory()
    total_mem = psutil.virtual_memory().total
    GPUs = GPUtil.getGPUs()

    while True:
        time.sleep(1)
        current_time = time.time()
        cpu_load = psutil.cpu_percent()
        gpu_load = GPUs[0].load
        mem_load = mem.used/total_mem
        results.append([current_time,cpu_load,gpu_load,mem_load])
        print(f'TIME: {current_time}, CPU: {cpu_load}, GPU: {gpu_load}, MEM: {mem_load}')
    
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()