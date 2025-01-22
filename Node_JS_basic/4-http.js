const http = require('http');

// Créer un serveur HTTP
const app = http.createServer((req, res) => {
    // Configurer les en têtes HTTP
    res.writeHead(200, { 'Content-Type': 'text/plain'});

    // Envoyer la réponse
    res.end('Hello Holberton School!');
});

// Faire écouter le serveur sur le port 1245
app.listen(1245);

// Exporter le serveur
module.exports = app;
