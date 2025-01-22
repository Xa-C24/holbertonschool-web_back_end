// Affiche un message d'accueil
console.log("Welcome to Holberton School, what is your name?");

// Écouter les données saisies par l'utilisateur
process.stdin.on("readable", () => {
  // Lire les données saisies
  const input = process.stdin.read();
  if (input !== null) {
    // Convertir l'entrée en chaîne de caractères et supprimer les espaces inutiles
    const name = input.toString().trim();
    console.log(`Your name is: ${name}`);
  }
});

// Écouter la fin du flux d'entrée (CTRL+D ou pipe)
process.stdin.on("end", () => {
  console.log("This important software is now closing");
});
