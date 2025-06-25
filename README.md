# Daily Date Logger

A simple Python project that logs the current date and time daily using GitHub Actions.

## Features

- **Daily Logger Script**: Automatically logs the current date and time to a log file
- **GitHub Actions Automation**: Runs daily at 9:00 AM UTC
- **Automated Commits**: Commits log entries back to the repository

## Files

- `daily_logger.py`: Main Python script that logs dates
- `.github/workflows/daily-logger.yml`: GitHub Actions workflow
- `logs/daily_log.txt`: Log file (created automatically)

## Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. Run the script manually:
   ```bash
   python daily_logger.py
   ```

## GitHub Actions

The workflow runs automatically every day at 9:00 AM UTC and:
1. Runs the Python logger script
2. Commits any new log entries
3. Pushes changes back to the repository

You can also trigger the workflow manually from the GitHub Actions tab.

## Configuration

The GitHub Actions workflow is configured to commit with:
- User: anushanuka
- Email: anusha.nooka@gmail.com 