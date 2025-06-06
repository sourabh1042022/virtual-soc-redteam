# Virtual SOC with Red Team Attacks and Alert Scoring

## Overview
This project demonstrates the implementation of a local Virtual SOC using open-source tools to simulate, detect, and respond to red team attacks. It includes Atomic Red Team simulations, detection via Sysmon, Suricata, OSSEC, alert dashboards in Kibana, memory forensics using Volatility, and an SSH honeypot with live defensive scripting.

## Simulated Techniques
- T1059.001 – PowerShell Execution
- T1055 – Process Injection
- T1547 – Registry Persistence
- T1057 – Process Discovery
- T1047 – WMI Execution
- T1071.001 – HTTP C2 Communication

## Lab Setup
- Windows Server 2022: Sysmon, OSSEC Agent, FTK Imager, Elastic Agent
- Ubuntu VM: Suricata, OSSEC Manager, Volatility3, Cowrie Honeypot, ELK Stack
- Kali Linux: Evil-WinRM, Atomic Red Team

## Automation
- replay_attacks.py: Replays red team simulations
- mitre_simulation.yaml: GitHub Actions workflow to automate tests
- auto_defense.py: Watches Cowrie logs, blocks IPs, sends Slack alerts

## Scoring
See alert_scoring_table.csv for detection scoring.

## Memory Forensics
Memory dump analyzed using Volatility3 to detect:
- Hidden processes
- Injected shellcode
- Hooked APIs

## Honeypot Response
Cowrie triggers defensive script that:
- Blocks attacker IP via iptables
- Saves forensic snapshot
- Sends Slack alerts

## Deliverables
- Atomic Red Team simulation scripts
- Kibana dashboards
- Volatility results
- Honeypot logs and alerts
- Full technical report (all of these are in report/)

