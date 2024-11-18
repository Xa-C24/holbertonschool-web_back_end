export default function cleanSet(set, startString) {
  // Vérifie que startString est une chaîne non vide
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  // Filtre les valeurs commençant par startString et génère une chaîne
  return Array.from(set)
    .filter((value) => typeof value === 'string' && value.startsWith(startString))
    .map((value) => value.slice(startString.length)) // Supprime startString
    .join('-'); // Joint les valeurs avec "-"
}
