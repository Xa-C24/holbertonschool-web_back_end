const fs = require('fs').promises;

async function countStudents(path) {
    try {
        // Lire le fichier de manière asynchrone
        const data = await fs.readFile(path, 'utf8');
        const lines = data.split('\n').filter((line) => line.trim() !== ''); // Supprimer les lignes vides

        // Vérifier si le fichier contient des données
        if (lines.length <= 1) {
            console.log('Number of students: 0');
            return;
        }

        const students = lines.slice(1); // Ignorer l'en-tête
        const fields = {}; // Pour stocker les étudiants par domaine

        students.forEach((line) => {
            const studentData = line.split(',');

            // Vérifier si la ligne contient les 4 colonnes attendues
            if (studentData.length >= 4) {
                const firstname = studentData[0].trim();
                const field = studentData[3].trim();

                // Ajouter l'étudiant au domaine correspondant
                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(firstname);
            }
        });

        // Afficher le nombre total d'étudiants
        console.log(`Number of students: ${students.length}`);

        // Afficher le nombre d'étudiants par domaine
        for (const [field, names] of Object.entries(fields)) {
            console.log(
                `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
            );
        }
    } catch (error) {
        // Gestion des erreurs
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
