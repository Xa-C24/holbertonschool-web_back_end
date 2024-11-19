export default function updateUniqueItems(items) {
  if (!(items instanceof Map)) {
    throw new Error("Cannot process");
  }
  // Parcourir la Map et mettre à jour les quantités
  items.forEach((value, key) => {
    if (value === 1) {
      items.set(key, 100);
    }
  })
}
