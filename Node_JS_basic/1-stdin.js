// Affiche un message d'accueil
process.stdout.write("Welcome to Holberton School, what is your name?\n");

// Écouter les données saisies par l'utilisateur
process.stdin.on("readable", () => {
  const input = process.stdin.read();
  if (input !== null) {
    const name = input.toString().trim();
    process.stdout.write(`Your name is: ${name}\n`);
  }
});

// Écouter la fin du flux d'entrée (CTRL+D ou pipe)
process.stdin.on("end", () => {
  process.stdout.write("This important software is now closing\n");
});
