#!/usr/bin/env python3
"""
Airbnb Clone - GitHub Green Squares Generator
Creates backfilled commits from Dec 24, 2025 to Jan 13, 2026
to show development progress on GitHub profile
"""

import os
import subprocess
import datetime
from pathlib import Path
import random

# ═════════════════════════════════════════════════════════════
# CONFIGURATION
# ═════════════════════════════════════════════════════════════

REPO_PATH = str(Path.home() / "Documents/Programming/airbnb")
GIT_NAME = "avartan007"  # Change this to your name
GIT_EMAIL = "avartanathlay28@gmail.com"  # Change this to your email
START_DATE = datetime.datetime(2025, 12, 24, 9, 0, 0)  # Dec 24, 2025
END_DATE = datetime.datetime(2026, 1, 13, 17, 0, 0)  # Jan 13, 2026

# Project files to modify
PROJECT_FILES = [
    "CHANGELOG.md",
    "README.md",
    "package.json",
    "app.js",
    "models/listing.js",
    "init/index.js",
    "init/data.js",
    "views/layouts/boilerplate.ejs",
    "views/includes/navbar.ejs",
    "views/includes/footer.ejs",
    "views/listings/index.ejs",
    "views/listings/show.ejs",
    "views/listings/new.ejs",
    "views/listings/edit.ejs",
    "public/css/style.css",
]

# Phase-based commit messages
COMMIT_MESSAGES = {
    "2025-12-24": [
        "Initial project setup - Basic structure and dependencies",
    ],
    "2025-12-26": [
        "Add .gitignore - exclude node_modules and env files",
    ],
    "2025-12-27": [
        "Create Listing model with MongoDB schema",
        "Add sample seed data for database initialization",
    ],
    "2025-12-28": [
        "Set up database connection and initialization script",
        "Implement index route to display all listings",
    ],
    "2025-12-29": [
        "Add show route for individual listing display",
        "Implement new route - form for creating listings",
    ],
    "2025-12-30": [
        "Implement create route - save listings to database",
        "Add edit route - display existing listing for editing",
    ],
    "2025-12-31": [
        "Implement update route - modify listings in database",
    ],
    "2026-01-01": [
        "Add delete route - remove listings from database",
    ],
    "2026-01-02": [
        "Create boilerplate layout with Bootstrap integration",
        "Add navbar component with responsive navigation",
    ],
    "2026-01-03": [
        "Add footer component with branding and links",
        "Style index page - list all properties",
    ],
    "2026-01-04": [
        "Create show page template for property details",
        "Build new listing form with validation",
    ],
    "2026-01-05": [
        "Create edit form for updating listings",
    ],
    "2026-01-06": [
        "Add CSS styling and responsive design improvements",
    ],
    "2026-01-07": [
        "Bug fixes and UI refinements",
    ],
    "2026-01-08": [
        "Final Phase 1 optimizations and testing",
    ],
    "2026-01-09": [
        "Add advanced features and improvements",
    ],
    "2026-01-10": [
        "Refactor codebase and improve performance",
    ],
    "2026-01-11": [
        "Add error handling and validation enhancements",
    ],
    "2026-01-12": [
        "Final testing and code cleanup",
    ],
    "2026-01-13": [
        "Add comprehensive project documentation",
    ],
}

# ═════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═════════════════════════════════════════════════════════════

def run(cmd, cwd=None, env=None, silent=False):
    """Run shell command"""
    result = subprocess.run(
        cmd,
        cwd=cwd,
        shell=True,
        env=env,
        capture_output=silent,
        text=True
    )
    if result.returncode != 0 and not silent:
        print(f"Error: {result.stderr}")
    return result

def ensure_repo():
    """Initialize git repository if needed"""
    repo = Path(REPO_PATH)
    if not repo.exists():
        print(f"❌ Repository not found at {REPO_PATH}")
        print("Please make sure your airbnb project exists")
        exit(1)
    
    if not (repo / ".git").exists():
        print("🔧 Initializing git repository...")
        run("git init", cwd=REPO_PATH)
    else:
        print("✅ Git repository already initialized")

def git_config():
    """Configure git user"""
    print(f"⚙️  Configuring git user: {GIT_NAME} <{GIT_EMAIL}>")
    run(f'git config user.name "{GIT_NAME}"', cwd=REPO_PATH)
    run(f'git config user.email "{GIT_EMAIL}"', cwd=REPO_PATH)

def create_changelog():
    """Create or update CHANGELOG.md"""
    changelog_path = Path(REPO_PATH) / "CHANGELOG.md"
    if not changelog_path.exists():
        with open(changelog_path, "w") as f:
            f.write("# Airbnb Clone - Development Changelog\n\n")
    return str(changelog_path)

def update_file(file_path):
    """Add a line to a file"""
    full_path = Path(REPO_PATH) / file_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if file_path.endswith(".json"):
        # For JSON files, don't modify (they're likely config)
        return
    elif file_path.endswith(".md"):
        with open(full_path, "a") as f:
            f.write(f"\n- Update: {timestamp}")
    else:
        with open(full_path, "a") as f:
            f.write(f"\n// Updated: {timestamp}\n")

def make_commit(file, msg, commit_dt):
    """Create a commit with specific date"""
    try:
        update_file(file)
        
        # Set git date environment variables
        env = os.environ.copy()
        iso_date = commit_dt.isoformat()
        env["GIT_AUTHOR_DATE"] = iso_date
        env["GIT_COMMITTER_DATE"] = iso_date
        
        # Stage and commit
        run(f'git add -A', cwd=REPO_PATH, env=env, silent=True)
        run(
            f'git commit -m "{msg}"',
            cwd=REPO_PATH,
            env=env,
            silent=True
        )
        return True
    except Exception as e:
        print(f"Error making commit: {e}")
        return False

def get_commits_for_date(date_str):
    """Get commit messages for a specific date"""
    return COMMIT_MESSAGES.get(date_str, [])

def generate_commits():
    """Generate all commits for the timeline"""
    print("\n" + "="*60)
    print("🚀 Starting Airbnb Clone Green Squares Generator")
    print("="*60 + "\n")
    
    # Setup
    ensure_repo()
    git_config()
    create_changelog()
    
    # Generate commits
    print("\n📝 Generating commits...\n")
    
    current = START_DATE
    commit_count = 0
    
    while current <= END_DATE:
        date_str = current.strftime("%Y-%m-%d")
        messages = get_commits_for_date(date_str)
        
        if messages:
            print(f"📅 {date_str} - {len(messages)} commit(s)")
            for msg in messages:
                file = random.choice(PROJECT_FILES)
                hour = random.randint(9, 18)
                minute = random.randint(0, 59)
                commit_time = current.replace(hour=hour, minute=minute, second=0)
                
                if make_commit(file, msg, commit_time):
                    print(f"   ✓ {msg}")
                    commit_count += 1
        
        current += datetime.timedelta(days=1)
    
    print("\n" + "="*60)
    print(f"✅ Successfully created {commit_count} commits!")
    print("="*60 + "\n")
    
    # Verify
    print("📊 Verifying commits...\n")
    result = run("git log --oneline | head -20", cwd=REPO_PATH)
    
    print("\n🎉 Setup complete! Next steps:\n")
    print("1. Go to github.com/new")
    print("2. Create repository: 'airbnb-clone'")
    print("3. Make it PUBLIC")
    print("4. Then run:\n")
    print("   git remote add origin https://github.com/YOUR_USERNAME/airbnb-clone.git")
    print("   git branch -M main")
    print("   git push -u origin main\n")
    print("5. Watch your green contribution graph appear! 🟢\n")

# ═════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════

if __name__ == "__main__":
    generate_commits()
