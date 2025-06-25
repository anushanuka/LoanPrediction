#!/usr/bin/env python3
"""
Daily Date Logger Script
This script logs the current date and time to a log file.
"""

import os
from datetime import datetime

def log_daily_date():
    """Log the current date and time to a log file."""
    
    # Create logs directory if it doesn't exist
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    
    # Generate timestamp
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    date_only = current_time.strftime("%Y-%m-%d")
    
    # Log file path
    log_file = os.path.join(logs_dir, "daily_log.txt")
    
    # Write to log file
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Daily log entry for {date_only}\n")
    
    print(f"Successfully logged date: {timestamp}")
    print(f"Log file: {log_file}")

if __name__ == "__main__":
    log_daily_date() 