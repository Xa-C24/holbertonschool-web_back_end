const http = require('http');
const fs = require('fs').promises;

// Fonction pour lire et traiter le fichier CSV
async function countStudents(path) {
    try {
        const data = await fs.readFile(path, 'utf8');
        const lines = data.split('\n').filter((line) => line.trim() !== ''); // Supprimer les lignes vides

        if (lines.length <= 1) {
            return 'No students found';
        }

        const students = lines.slice(1); // Ignorer l'en-tête
        const fields = {};

        students.forEach((line) => {
            const [firstname, , , field] = line.split(',');
            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstname);
        });

        let response = `Number of students: ${students.length}\n`;
        for (const [field, names] of Object.entries(fields)) {
            response += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
        }
        return response.trim();
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

// Créer le serveur HTTP
const app = http.createServer(async (req, res) => {
    const url = req.url;

    if (url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello Holberton School!');
    } else if (url === '/students') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.write('This is the list of our students\n');

        try {
            // Charger le fichier CSV
            const databasePath = process.argv[2];
            const studentData = await countStudents(databasePath);
            res.end(studentData);
        } catch (error) {
            res.end(error.message);
        }
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
});

// Faire écouter le serveur sur le port 1245
app.listen(1245);

// Exporter le serveur
module.exports = app;
