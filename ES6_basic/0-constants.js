// La fonction taskFirst utilise `const` pour déclarer une variable qui ne change pas.
export function taskFirst() {
    const task = 'I prefer const when I can.'; // Déclaration d'une constante.
    return task; // Retourne la valeur de la constante.
  }
  
  // La fonction getLast retourne une chaîne de caractères fixe.
  export function getLast() {
    return ' is okay'; // Retourne une chaîne de caractères.
  }
  
  // La fonction taskNext utilise `let` pour déclarer une variable modifiable.
  export function taskNext() {
    let combination = 'But sometimes let'; // Déclaration d'une variable avec `let`.
    combination += getLast(); // Ajoute la valeur retournée par getLast à la variable combination.
  
    return combination; // Retourne la chaîne de caractères combinée.
  }
  