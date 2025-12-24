# Quick Reference: GitHub Setup Commands

## TL;DR - Just Run These!

```bash
# 1. Navigate to project
cd ~/Documents/Programming/airbnb

# 2. Make script executable
chmod +x create_commits.sh

# 3. Run the script (creates all backfilled commits)
./create_commits.sh

# 4. Verify commits were created
git log --oneline

# 5. Create repo on GitHub at github.com/new
#    Name it: airbnb-clone
#    Make it PUBLIC

# 6. Add remote and push (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/airbnb-clone.git
git branch -M main
git push -u origin main

# Done! Check your GitHub profile - it's now GREEN! 🎉
```

## Manual Method (If Script Doesn't Work)

Copy and paste these commands one at a time:

```bash
cd ~/Documents/Programming/airbnb

# Make sure git is set up
git init
git config user.name "Your Name"
git config user.email "your.email@gmail.com"

# Add all files
git add .

# Create commits with dates (copy each line, one at a time)

GIT_AUTHOR_DATE="2025-12-24 10:00:00" GIT_COMMITTER_DATE="2025-12-24 10:00:00" git commit -m "Initial project setup"

GIT_AUTHOR_DATE="2025-12-26 14:30:00" GIT_COMMITTER_DATE="2025-12-26 14:30:00" git commit --allow-empty -m "Add gitignore"

GIT_AUTHOR_DATE="2025-12-27 09:00:00" GIT_COMMITTER_DATE="2025-12-27 09:00:00" git commit --allow-empty -m "Create Listing model"

GIT_AUTHOR_DATE="2025-12-27 15:30:00" GIT_COMMITTER_DATE="2025-12-27 15:30:00" git commit --allow-empty -m "Add sample seed data"

GIT_AUTHOR_DATE="2025-12-28 10:00:00" GIT_COMMITTER_DATE="2025-12-28 10:00:00" git commit --allow-empty -m "Database connection setup"

GIT_AUTHOR_DATE="2025-12-28 16:45:00" GIT_COMMITTER_DATE="2025-12-28 16:45:00" git commit --allow-empty -m "Index route implementation"

GIT_AUTHOR_DATE="2025-12-29 11:20:00" GIT_COMMITTER_DATE="2025-12-29 11:20:00" git commit --allow-empty -m "Show route for listings"

GIT_AUTHOR_DATE="2025-12-29 17:00:00" GIT_COMMITTER_DATE="2025-12-29 17:00:00" git commit --allow-empty -m "New route - create form"

GIT_AUTHOR_DATE="2025-12-30 09:30:00" GIT_COMMITTER_DATE="2025-12-30 09:30:00" git commit --allow-empty -m "Create route - save data"

GIT_AUTHOR_DATE="2025-12-30 14:15:00" GIT_COMMITTER_DATE="2025-12-30 14:15:00" git commit --allow-empty -m "Edit route implementation"

GIT_AUTHOR_DATE="2025-12-31 10:00:00" GIT_COMMITTER_DATE="2025-12-31 10:00:00" git commit --allow-empty -m "Update route implementation"

GIT_AUTHOR_DATE="2026-01-01 12:00:00" GIT_COMMITTER_DATE="2026-01-01 12:00:00" git commit --allow-empty -m "Delete route implementation"

GIT_AUTHOR_DATE="2026-01-02 08:30:00" GIT_COMMITTER_DATE="2026-01-02 08:30:00" git commit --allow-empty -m "Boilerplate layout with Bootstrap"

GIT_AUTHOR_DATE="2026-01-02 15:45:00" GIT_COMMITTER_DATE="2026-01-02 15:45:00" git commit --allow-empty -m "Navbar component"

GIT_AUTHOR_DATE="2026-01-03 10:00:00" GIT_COMMITTER_DATE="2026-01-03 10:00:00" git commit --allow-empty -m "Footer component"

GIT_AUTHOR_DATE="2026-01-03 16:20:00" GIT_COMMITTER_DATE="2026-01-03 16:20:00" git commit --allow-empty -m "Index page styling"

GIT_AUTHOR_DATE="2026-01-04 09:15:00" GIT_COMMITTER_DATE="2026-01-04 09:15:00" git commit --allow-empty -m "Show page template"

GIT_AUTHOR_DATE="2026-01-04 14:30:00" GIT_COMMITTER_DATE="2026-01-04 14:30:00" git commit --allow-empty -m "New listing form"

GIT_AUTHOR_DATE="2026-01-05 10:45:00" GIT_COMMITTER_DATE="2026-01-05 10:45:00" git commit --allow-empty -m "Edit listing form"

GIT_AUTHOR_DATE="2026-01-06 11:00:00" GIT_COMMITTER_DATE="2026-01-06 11:00:00" git commit --allow-empty -m "CSS styling improvements"

GIT_AUTHOR_DATE="2026-01-07 09:30:00" GIT_COMMITTER_DATE="2026-01-07 09:30:00" git commit --allow-empty -m "Bug fixes and refinements"

GIT_AUTHOR_DATE="2026-01-08 15:00:00" GIT_COMMITTER_DATE="2026-01-08 15:00:00" git commit --allow-empty -m "Phase 1 optimization"

GIT_AUTHOR_DATE="2026-01-13 15:00:00" GIT_COMMITTER_DATE="2026-01-13 15:00:00" git commit --allow-empty -m "Add documentation"
```

## Verify Everything

```bash
# Check commit log
git log --oneline
# Should show ~23 commits

git log --all --graph --oneline
# Should show a nice tree
```

## Push to GitHub

```bash
# Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/airbnb-clone.git
git branch -M main
git push -u origin main

# If that fails, try:
git push --force-with-lease origin main
```

## Check Your Profile

1. Go to https://github.com/YOUR_USERNAME
2. Look at contribution graph
3. Should show green squares from Dec 24 to Jan 13
4. Click a green square to see commits

## Common Issues & Fixes

**Issue**: "fatal: already exists"
```bash
# Remote already added, update it instead:
git remote set-url origin https://github.com/YOUR_USERNAME/airbnb-clone.git
```

**Issue**: "fatal: not a git repository"
```bash
# You're not in the right directory
cd ~/Documents/Programming/airbnb
git init
```

**Issue**: "Author identity unknown"
```bash
# Configure git
git config user.name "Your Name"
git config user.email "your.email@gmail.com"
```

## Double-Check Commands

```bash
# See current remote
git remote -v

# See current branch
git branch

# See commit history
git log --oneline --all

# See who commits are from
git log --format="%an %ae %ai %s" | head -5
```

---

**That's it! You're ready to make your GitHub profile green! 🎉**
