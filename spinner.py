import time
spinner = '|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|'
for i in spinner:
    print(f"\r{i}", end='', flush=True)
    time.sleep(0.2)
