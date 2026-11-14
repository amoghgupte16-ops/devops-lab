# 1. VARIABLES: a name that holds a value
team = "Wealth Platforms"
cpu_alert_threshold = 90

# 2. A LIST: an ordered collection, in square brackets
servers = ["app-01", "app-02", "db-01", "db-02"]

# 3. A DICTIONARY: key -> value pairs, in curly braces
cpu_usage = {
    "app-01": 45,
    "app-02": 92,
    "db-01": 78,
    "db-02": 85
}

print(f"Health report for {team}")
print(f"Checking {len(servers)} servers...\n")

# 4. A FOR LOOP: repeat for each item in the list
for server in servers:
    cpu = cpu_usage[server]          # look up a value by its key

    # 5. IF / ELSE: make a decision
    if cpu > cpu_alert_threshold:
        print(f"ALERT  {server}: CPU at {cpu}%")
    else:
        print(f"OK     {server}: CPU at {cpu}%")