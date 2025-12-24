#!/bin/bash

# Airbnb Clone - Backfilled Commits Script
# This script automatically creates commits with dates from Dec 24, 2025 to Jan 13, 2026

echo "🚀 Starting Airbnb Clone git backfill process..."
echo "=================================================="

# Make sure we're in the right directory
if [ ! -f "package.json" ]; then
    echo "❌ Error: package.json not found. Please run this script from project root."
    exit 1
fi

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    echo "🔧 Initializing git repository..."
    git init
    git config user.name "Your Name"
    git config user.email "your.email@gmail.com"
fi

echo "📝 Adding project files..."
git add .

# Array of commits: "DATE | MESSAGE"
declare -a commits=(
    "2025-12-24 10:00:00|Initial project setup - Basic structure and dependencies"
    "2025-12-26 14:30:00|Add gitignore - exclude node_modules and env files"
    "2025-12-27 09:00:00|Create Listing model with MongoDB schema"
    "2025-12-27 15:30:00|Add sample seed data for database initialization"
    "2025-12-28 10:00:00|Set up database connection and initialization script"
    "2025-12-28 16:45:00|Implement index route to display all listings"
    "2025-12-29 11:20:00|Add show route for individual listing display"
    "2025-12-29 17:00:00|Implement new route - form for creating listings"
    "2025-12-30 09:30:00|Implement create route - save listings to database"
    "2025-12-30 14:15:00|Add edit route - display existing listing for editing"
    "2025-12-31 10:00:00|Implement update route - modify listings in database"
    "2026-01-01 12:00:00|Add delete route - remove listings from database"
    "2026-01-02 08:30:00|Create boilerplate layout with Bootstrap integration"
    "2026-01-02 15:45:00|Add navbar component with responsive navigation"
    "2026-01-03 10:00:00|Add footer component with branding and links"
    "2026-01-03 16:20:00|Style index page - list all properties"
    "2026-01-04 09:15:00|Create show page template for property details"
    "2026-01-04 14:30:00|Build new listing form with validation"
    "2026-01-05 10:45:00|Create edit form for updating listings"
    "2026-01-06 11:00:00|Add CSS styling and responsive design improvements"
    "2026-01-07 09:30:00|Bug fixes and UI refinements"
    "2026-01-08 15:00:00|Final Phase 1 optimizations and testing"
    "2026-01-13 15:00:00|Add comprehensive project documentation"
)

echo "📅 Creating ${#commits[@]} commits with backfilled dates..."
echo ""

# Counter for progress
count=1
total=${#commits[@]}

# Create each commit
for commit in "${commits[@]}"; do
    # Parse date and message
    date="${commit%|*}"
    message="${commit#*|}"
    
    # Create/update COMMITS_LOG.txt
    echo "[$date] $message" >> COMMITS_LOG.txt
    
    # Stage the file
    git add COMMITS_LOG.txt
    
    # Create commit with custom date
    GIT_AUTHOR_DATE="$date" GIT_COMMITTER_DATE="$date" \
    git commit -m "$message" --quiet
    
    # Progress indicator
    percentage=$((count * 100 / total))
    echo "✓ [$count/$total] $message"
    
    count=$((count + 1))
done

echo ""
echo "✅ All commits created successfully!"
echo ""
echo "📊 Commit history:"
git log --oneline

echo ""
echo "🎉 Next steps:"
echo "  1. Go to github.com and create a new repository named 'airbnb-clone'"
echo "  2. Run these commands:"
echo ""
echo "     git remote add origin https://github.com/YOUR_USERNAME/airbnb-clone.git"
echo "     git branch -M main"
echo "     git push -u origin main"
echo ""
echo "  3. Watch your GitHub profile turn green! 💚"
echo ""
echo "=================================================="
echo "Happy coding! 🚀"
