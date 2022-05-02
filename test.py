import psutil
import GPUtil
import pandas as pd
import time
import signal
import sys
import argparse

results = []
save_filename = 'test'

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    pd.DataFrame(results).to_csv(f'{save_filename}.csv', header=['time','cpu','gpu','mem'],index=None)
    sys.exit(0)

def main():
    # mem = psutil.virtual_memory()
    total_mem = psutil.virtual_memory().total

    while True:
        time.sleep(1)
        current_time = time.time()
        cpu_load = psutil.cpu_percent()
        mem_load = psutil.virtual_memory().used/total_mem
        # gpu_load = GPUtil.getGPUs()[0].load
        gpu_load = 0
        results.append([current_time,cpu_load,gpu_load,mem_load])
        print(f'TIME: {current_time}, CPU: {cpu_load}, GPU: {gpu_load}, MEM: {mem_load}')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--filename',help='filename',type=str)
    args = parser.parse_args()
    save_filename = args.filename
    signal.signal(signal.SIGINT, signal_handler)
    main()