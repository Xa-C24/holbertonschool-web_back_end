// Importation des modules nécessaires
const express = require('express'); // Framework pour créer un serveur HTTP
const fs = require('fs').promises; // Module pour lire des fichiers de manière asynchrone

// Création de l'application Express
const app = express();
const PORT = 1245; // Port sur lequel le serveur écoutera les requêtes

// Fonction pour lire et traiter les données d'un fichier CSV
async function countStudents(path) {
  try {
    // Lecture du fichier CSV de manière asynchrone
    const data = await fs.readFile(path, 'utf8');

    // Suppression des lignes vides et division du fichier en lignes
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Suppression de l'en-tête (première ligne)
    const students = lines.slice(1);

    // Création d'un objet pour regrouper les étudiants par domaine
    const fields = {};

    // Parcours de chaque ligne (chaque étudiant)
    students.forEach((line) => {
      // Extraction des données : prénom, domaine, etc.
      const [firstname, , , field] = line.split(',');

      // Ajout de l'étudiant dans le domaine correspondant
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    // Création du résultat final à afficher
    let result = `Number of students: ${students.length}\n`;

    // Ajout des informations pour chaque domaine
    for (const [field, names] of Object.entries(fields)) {
      result += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }

    return result.trim(); // Retourne le résultat sans espaces inutiles

  } catch (error) {
    // Gestion des erreurs si le fichier ne peut pas être lu
    throw new Error('Cannot load the database');
  }
}

// Endpoint de base (/) : retourne un message simple
app.get('/', (req, res) => {
  res.send('Hello Holberton School!'); // Réponse envoyée au client
});

// Endpoint /students : retourne les informations sur les étudiants
app.get('/students', async (req, res) => {
  // Récupération du chemin du fichier CSV depuis les arguments de la ligne de commande
  const database = process.argv[2];

  // Vérification que le fichier a bien été fourni
  if (!database) {
    res.status(500).send('Database path is required');
    return;
  }

  // Envoi de l'entête de la réponse au client
  res.write('This is the list of our students\n');

  try {
    // Lecture et traitement des données du fichier CSV
    const studentsData = await countStudents(database);
    res.end(studentsData); // Envoi des données au client et fin de la réponse
  } catch {
    res.end('Cannot load the database');
  }
});

// Lancement du serveur sur le port spécifié
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`); // Message de confirmation dans la console
});

// Exportation de l'application Express (utile pour les tests ou l'importation dans d'autres fichiers)
module.exports = app;
