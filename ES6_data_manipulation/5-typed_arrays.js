export default function createInt8TypedArray(lenght, position, value) {
  // Crée un nouveau ArrayBuffer avec la longueur spécifiée
  const buffer = new ArrayBuffer(lenght);

  // Crée une vue DataView pour manipuler le ArrayBuffer
  const dataViewInstance = new DataView(buffer);

  // Vérifie si la position est en dehors de la plage
  if (position < 0 || position >= lenght) {
    throw new Error('Position outside range');
  }

  // Définit la valeur Int8 à la position spécifiée
  dataViewInstance.setInt8(position, value);

  return dataViewInstance;
}
