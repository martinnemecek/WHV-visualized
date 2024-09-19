import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import mime from 'mime';
import cors from 'cors'; // Import CORS

const app = express();
const port = 8080;

// For ES module, __dirname is not available, so we need to recreate it
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Enable CORS for all routes
app.use(cors());

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Serve index.html for the root route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Middleware to serve KMZ files with correct MIME type
app.get('/POA/:file', (req, res) => {
    const filePath = path.join(__dirname, 'public', 'POA', req.params.file);

    // Set MIME type explicitly for .kmz files
    if (path.extname(filePath) === '.kmz') {
        res.setHeader('Content-Type', 'application/vnd.google-earth.kmz');
    }

    res.sendFile(filePath, (err) => {
        if (err) {
            res.status(404).send('File not found');
        }
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
