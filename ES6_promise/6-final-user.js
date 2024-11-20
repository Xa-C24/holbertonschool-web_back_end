// Importation des fonctions nécessaires depuis leurs fichiers respectifs.
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

// Fonction principale pour gérer l'inscription de l'utilisateur et l'upload de sa photo.
export default function handleProfileSignup(firstName, lastName, fileName) {
  // Appel des fonctions pour retourner des Promises
  const signUpUserPromise = signUpUser(firstName, lastName); // Promise pour l'inscription
  const uploadPhotoPromise = uploadPhoto(fileName); // Promise pour l'upload de la photo

  // Utilisation de Promise.allSettled pour attendre que toutes les Promises soient "résolues" (fulfilled ou rejected)
  return Promise.allSettled([signUpUserPromise, uploadPhotoPromise])
    .then((results) => {
      // Transformation des résultats en un tableau structuré avec status et value/reason
      return results.map((result) => {
        if (result.status === 'fulfilled') {
          // Si la Promise est résolue avec succès
          return { status: result.status, value: result.value };
        }
        // Si la Promise est rejetée, inclure la raison
        return { status: result.status, value: result.reason };
      });
    });
}

// return pending = en cours d'execution en attente
