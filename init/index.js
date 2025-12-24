const mongoose = require("mongoose");
const data = require("./data.js");
const Listing = require("../models/listing.js");

const MONGO_URL = "mongodb://127.0.0.1:27017/wanderlust";

async function main() {
  await mongoose.connect(MONGO_URL);
}

const initDB = async () => {
  const seed = Array.isArray(data) ? data : (data && Array.isArray(data.data) ? data.data : []);
  if (seed.length === 0) {
    console.log("No seed data found in init/data.js — nothing to insert.");
    return;
  }

  try {
    await Listing.deleteMany({});
    await Listing.insertMany(seed);
    console.log("DB initialized with sample data");
  } catch (err) {
    console.error("Error initializing DB:", err);
    throw err;
  }
};

main()
  .then(() => initDB())
  .then(() => mongoose.disconnect())
  .then(() => {
    console.log("Init complete, disconnected from DB.");
    process.exit(0);
  })
  .catch((err) => {
    console.error("Initialization failed:", err);
    process.exit(1);
  });
// Updated: 2026-01-13 14:20:51

// Updated: 2026-01-13 14:20:51

// Updated: 2026-01-13 14:20:51

// Updated: 2026-01-13 14:24:37

// Updated: 2026-01-13 14:24:37
