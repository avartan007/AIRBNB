const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const listingSchema = new Schema({
    title: {
        type: String,
        required: true,
    },
    description: String,
    image: {
        type: String,
        set: (v) => {
            // if seed provides an object like { filename, url }, use the url
            if (v && typeof v === "object" && typeof v.url === "string") return v.url;
            // if empty string, use default placeholder
            if (v === "") return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_QrTSimm7SqtWkXfKnrC1CYS3ISzOydLRlg&s";
            // otherwise keep the provided value (string or null/undefined)
            return v;
        },
    },
    price: Number,
    location: String,
    country: String,
});

const Listing = mongoose.model("Listing", listingSchema);
module.exports = Listing;

// Updated: 2026-01-13 14:20:51

// Updated: 2026-01-13 14:20:51

// Updated: 2026-01-13 14:24:37

// Updated: 2026-01-13 14:24:37

// Updated: 2026-01-13 14:24:37

// Updated: 2026-01-13 14:27:25
