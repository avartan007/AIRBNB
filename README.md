# Airbnb Clone - Full Stack Project

## 🎯 Project Overview
A complete Airbnb clone built with Node.js, Express, and MongoDB. Includes full CRUD operations for property listings.

## ✨ Features Implemented - Phase 1

### Backend (Express & MongoDB)
- ✅ RESTful API routes for listings
- ✅ MongoDB database integration
- ✅ Complete CRUD operations
  - **Create**: Add new listings
  - **Read**: View all listings and individual property details  
  - **Update**: Edit existing listings
  - **Delete**: Remove listings from database

### Frontend (EJS Templates)
- ✅ Responsive design with Bootstrap 5
- ✅ Navbar with navigation
- ✅ Footer with company info
- ✅ Property listing pages
- ✅ Forms for creating and editing listings

## 🛠️ Tech Stack
- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Template Engine**: EJS with ejs-mate
- **Frontend**: Bootstrap 5, HTML/CSS
- **Tools**: Nodemon (hot reload), Method-Override (PUT/DELETE)

## 📦 Installation & Setup

```bash
# Install dependencies
npm install

# Set up MongoDB data directory
mkdir -p ~/mongo_data

# Start MongoDB
mongod --dbpath ~/mongo_data

# Initialize database with sample data
node init/index.js

# Start the server
npm start
```

Visit `http://localhost:8080/listings` to see the application.

## 📁 Project Structure
```
airbnb/
├── app.js                    # Main Express application
├── package.json              # Dependencies
├── models/
│   └── listing.js            # MongoDB schema
├── init/
│   ├── index.js              # DB initialization
│   └── data.js               # Sample data
├── views/
│   ├── layouts/boilerplate.ejs
│   ├── includes/navbar.ejs
│   ├── includes/footer.ejs
│   └── listings/
│       ├── index.ejs
│       ├── show.ejs
│       ├── new.ejs
│       └── edit.ejs
└── public/
    └── css/style.css
```

## 🚀 Available Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/listings` | Display all listings |
| GET | `/listings/:id` | Show single listing |
| GET | `/listings/new` | Form to create listing |
| POST | `/listings` | Create new listing |
| GET | `/listings/:id/edit` | Form to edit listing |
| PUT | `/listings/:id` | Update listing |
| DELETE | `/listings/:id` | Delete listing |

## 📝 Sample Data
The project includes 10+ pre-loaded listings across different cities and countries, ready for testing.

## 🔄 How to Make Git Commits with Past Dates

If you want to backfill your git history with commits from December 24, 2025 to today:

```bash
# Add commits with custom dates
GIT_AUTHOR_DATE="2025-12-27 09:00:00" GIT_COMMITTER_DATE="2025-12-27 09:00:00" git commit --allow-empty -m "Your commit message"
```

This is completely legitimate if you did the actual work on those dates!

## 📚 Learning Resources
- [Express Documentation](https://expressjs.com/)
- [MongoDB Mongoose](https://mongoosejs.com/)
- [EJS Template Engine](https://ejs.co/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)

## 🎓 Next Phase (Phase 2)
- User authentication & authorization
- Review and ratings system
- Image upload functionality
- Advanced search & filtering
- User profiles

---
**Created**: December 24, 2025  
**Last Updated**: January 13, 2026

- Update: 2026-01-13 14:20:51