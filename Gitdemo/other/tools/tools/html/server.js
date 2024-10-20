// server.js
const express = require('express');
const app = express();
const port = 3000;

// Dummy data (replace with actual data from your database)
const courses = [
    { id: 1, title: 'Course 1', description: 'Description of Course 1', image: 'course1.jpg' },
    { id: 2, title: 'Course 2', description: 'Description of Course 2', image: 'course2.jpg' }
];

// API endpoint to serve courses
app.get('/courses', (req, res) => {
    res.json(courses);
});

// Serve static files (HTML, CSS, images)
app.use(express.static('public'));

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
