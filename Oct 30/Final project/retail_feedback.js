
// Switch Database
use retail_feedback_db;

// Insert Sample Feedback Documents
db.feedback.insertMany([
  {
    product_id: 1,
    customer_name: "Amit Verma",
    feedback: "Laptop performance is great, but battery backup could be better.",
    rating: 4
  },
  {
    product_id: 2,
    customer_name: "Priya Nair",
    feedback: "Smartphone camera quality is outstanding!",
    rating: 5
  },
  {
    product_id: 3,
    customer_name: "Ravi Iyer",
    feedback: "Affordable and effective shampoo, good for daily use.",
    rating: 5
  }
]);

// Create Index for Quick Search by product_id
db.feedback.createIndex({ product_id: 1 });

// Verify Indexes
db.feedback.getIndexes();
