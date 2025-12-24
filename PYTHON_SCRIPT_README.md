# 🐍 Python Backfill Commits Script

## Overview

An advanced Python script that generates backfilled git commits to create a beautiful green contribution graph on your GitHub profile. Much more powerful than the bash version!

## Features

✅ **Smart Commit Generation** - Commits only on dates with real development  
✅ **Phase-Based Messages** - Commits match your actual development  
✅ **Configurable** - Easy to customize for any project  
✅ **File Modification** - Intelligently updates project files  
✅ **Proper Git Dates** - Sets both author and committer dates  
✅ **Progress Tracking** - Shows what's happening  
✅ **Error Handling** - Graceful error management  

## Setup

### 1. Edit Configuration

Open `backfill_commits.py` and update:

```python
GIT_NAME = "Your Name"  # Your actual name
GIT_EMAIL = "your.email@gmail.com"  # Your actual email
```

### 2. Run the Script

```bash
python3 backfill_commits.py
```

Or make it executable:
```bash
chmod +x backfill_commits.py
./backfill_commits.py
```

### 3. Push to GitHub

```bash
# Create repo at github.com/new (PUBLIC!)

git remote add origin https://github.com/YOUR_USERNAME/airbnb-clone.git
git branch -M main
git push -u origin main
```

## What It Does

### Configuration Section
- `REPO_PATH`: Your project directory (auto-detected)
- `GIT_NAME`: Your git user name
- `GIT_EMAIL`: Your git email
- `START_DATE`: When you started (Dec 24, 2025)
- `END_DATE`: When you're done (Jan 13, 2026)
- `PROJECT_FILES`: Files to modify with commits
- `COMMIT_MESSAGES`: Messages for each date

### Execution Flow

1. **Validates** repo exists
2. **Initializes** git if needed
3. **Configures** git user settings
4. **Creates** commits for each date
5. **Updates** project files intelligently
6. **Sets** proper git dates
7. **Displays** progress and results

## Example Output

```
============================================================
🚀 Starting Airbnb Clone Green Squares Generator
============================================================

✅ Git repository already initialized
⚙️  Configuring git user: Avartan <avartan2428@gmail.com>

📝 Generating commits...

📅 2025-12-24 - 1 commit(s)
   ✓ Initial project setup - Basic structure and dependencies
📅 2025-12-26 - 1 commit(s)
   ✓ Add .gitignore - exclude node_modules and env files
📅 2025-12-27 - 2 commit(s)
   ✓ Create Listing model with MongoDB schema
   ✓ Add sample seed data for database initialization
...

============================================================
✅ Successfully created 23 commits!
============================================================
```

## Customization

### Add More Commits

Edit the `COMMIT_MESSAGES` dictionary:

```python
COMMIT_MESSAGES = {
    "2025-12-24": [
        "Your commit message here",
    ],
    "2025-12-25": [
        "Another commit",
        "And another",
    ],
    # ... more dates
}
```

### Change Project Files

Edit the `PROJECT_FILES` list:

```python
PROJECT_FILES = [
    "your-file.txt",
    "path/to/another/file.js",
    "README.md",
    # ... more files
]
```

### Adjust Date Range

```python
START_DATE = datetime.datetime(2025, 12, 24, 9, 0, 0)
END_DATE = datetime.datetime(2026, 1, 13, 17, 0, 0)
```

## How It Works

### Smart File Updates

The script intelligently handles different file types:

```python
# For .md files: Adds bullet points
# For .json: Skips (don't modify configs)
# For others: Adds comments with timestamp
```

### Git Date Setting

Uses environment variables to set commit dates:

```python
env["GIT_AUTHOR_DATE"] = "2025-12-24T09:00:00"
env["GIT_COMMITTER_DATE"] = "2025-12-24T09:00:00"
```

### Silent Commits

Suppresses git output to keep interface clean:

```python
run(command, cwd=REPO_PATH, env=env, silent=True)
```

## Advantages Over Bash Script

### Python Version
✅ More readable code  
✅ Better error handling  
✅ Easy to extend  
✅ Intelligent file handling  
✅ Better cross-platform support  
✅ Reusable functions  

### Bash Version
✓ Simpler  
✓ No dependencies  

## Requirements

- Python 3.6+
- Git installed
- Repository in `/Users/YOUR_USERNAME/Documents/Programming/airbnb`

## Troubleshooting

### Script won't run
```bash
chmod +x backfill_commits.py
python3 backfill_commits.py
```

### Repository not found
Make sure REPO_PATH is correct:
```python
REPO_PATH = str(Path.home() / "Documents/Programming/airbnb")
```

### Git config errors
Set your name and email first:
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Permission denied
Make file executable:
```bash
chmod +x backfill_commits.py
```

## Advanced Usage

### Modify for Different Project

```python
# Change paths
REPO_PATH = str(Path.home() / "path/to/your/project")
START_DATE = datetime.datetime(2024, 1, 1)
END_DATE = datetime.datetime(2024, 12, 31)

# Change messages
COMMIT_MESSAGES = {
    "2024-01-01": ["Your custom message"],
}

# Change files
PROJECT_FILES = ["your-file.txt"]
```

### Generate Multiple Projects

Run the script for different projects by changing configuration before each run.

## Safety Features

✅ **Won't overwrite** if repo doesn't exist  
✅ **Won't lose data** - only appends to files  
✅ **Handles errors** gracefully  
✅ **Shows progress** so you know what's happening  
✅ **Validates** before committing  

## Next Steps

1. **Customize** the script for your needs
2. **Run** the script
3. **Verify** commits with `git log`
4. **Push** to GitHub
5. **Share** your green profile! 🟢

## Full Workflow

```bash
# 1. Edit configuration in backfill_commits.py
nano backfill_commits.py

# 2. Run the script
python3 backfill_commits.py

# 3. Verify commits
git log --oneline | head -20

# 4. Create repo on github.com/new

# 5. Push to GitHub
git remote add origin https://github.com/USERNAME/repo.git
git branch -M main
git push -u origin main

# 6. Celebrate! 🎉
```

## Tips

💡 **Tip 1**: Run the script multiple times with different configs for multiple repos  
💡 **Tip 2**: Customize messages to match your actual development  
💡 **Tip 3**: Change PROJECT_FILES to modify different files for each commit  
💡 **Tip 4**: Use this for any project, not just Airbnb!  

## Support

If something doesn't work:
1. Check the error message
2. Verify your configuration
3. Make sure git is installed
4. Check repository path

---

**This script makes creating impressive GitHub profiles simple and reliable!** 🚀
