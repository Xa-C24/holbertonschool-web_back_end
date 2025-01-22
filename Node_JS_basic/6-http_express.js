// Importation de Express
const express = require("express");

// Création de l'application Express
const app = express();

// Route pour l'endpoint /
app.get("/", (req, res) => {
  res.send("Hello Holberton School!");
});

// Configuration pour écouter sur le port 1245.
app.listen(1245, () => {
  console.log("Server is running on http://localhost:1245");
});

// Exportation de l'application Express
module.exports = app;
