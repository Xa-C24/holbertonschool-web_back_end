
const fs = require('fs');

function countStudents(path) {
    try {
         // Lire le fichier synchroniquement
        const data = fs.readFileSync(path, 'utf-8');

        // Séparer les lignes et supprimer les lignes vides
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        // Vérifier si le fichier contient des données
        if (lines.length <= 1) {
            console.log('No valid data in the database');
            return;
        }

        // Enlever la première ligne (en-têtes)
        const students = lines.slice(1);

        // Initialiser un objet pour organiser les étudiants par domaine.
        const fields = {};

        // Parcourir chaque lignes des étudiants
        for (const student of students) {
            const [firstname, lastname, age, field] = student.split(',').map((value) => value.trim());

            if (!field) continue;  // Ignorer les entrées mal formatées

            // Ajouter l'étudiant au domaine correspondant
            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstname);
        }

        // Compter le nombre total d'étudiants
        console.log(`Number of students: ${students.length}`);

        // Trier les étudiants par domaine
        for (const [field, names] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }
    } catch (error) {
        // Lever une erreur si le fichier est introuvable
        throw new Error (`Cannot load the database`);
    }
}

module.exports = countStudents;
