import time
import subprocess
import requests
import json

LOG_PATH = "/home/task/Desktop/cowrie/var/log/cowrie/cowrie.json"
SLACK_WEBHOOK = "https://hooks.slack.com/services/XXXX/XXXX/XXXX"
BANNED_IPS = set()

def tail_f(filename):
    with open(filename, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

def block_ip(ip):
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])

def notify_slack(ip, command):
    msg = {
        "text": f"Honeypot Alert\nAttacker IP: {ip}\nCommand: {command}"
    }
    try:
        requests.post(SLACK_WEBHOOK, json=msg)
    except:
        pass

def take_snapshot(ip):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    subprocess.run(["sudo", "cp", "/var/log/auth.log", f"/tmp/forensic_{ip}_{timestamp}.log"])

for line in tail_f(LOG_PATH):
    try:
        event = json.loads(line)
        if event.get('eventid') == 'cowrie.command.input':
            ip = event.get('src_ip')
            cmd = event.get('input')
            if ip and ip not in BANNED_IPS:
                block_ip(ip)
                notify_slack(ip, cmd)
                take_snapshot(ip)
                BANNED_IPS.add(ip)
    except json.JSONDecodeError:
        continue
