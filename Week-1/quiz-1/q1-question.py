"""
Question:
Pick one IP from each region, find network latency from via the below code snippet
(ping 3 times), and finally sort the average latency by region.
http://ec2-reachability.amazonaws.com/
Expected Output for all 15 regions:
1. us-west-1 [50.18.56.1] - 100ms (Smallest average latency)
2. xx-xxxx-x [xx.xx.xx.xx] - 200ms
3. xx-xxxx-x [xx.xx.xx.xx] - 300ms
...
15. xx-xxxx-x [xx.xx.xx.xx] - 1000ms (Largest average latency)
"""
from __future__ import print_function
import subprocess


host = "yahoo.com"

ping = subprocess.Popen(
    ["ping", "-c", "3", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
print(out)
