// Importer la classe Building depuis 5-building.js
import Building from './5-building.js';

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    // Appeler le constructeur parent pour définir sqft
    super(sqft);
    // Initialiser l’attribut _floors
    this._floors = floors;
  }

  // Getter pour sqft (hérité de la classe parente)
  get sqft() {
    return this._sqft;
  }

  // Getter pour floors
  get floors() {
    return this._floors;
  }

  // Redéfinir la méthode evacuationWarningMessage
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}

export default SkyHighBuilding;
