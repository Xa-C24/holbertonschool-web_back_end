// Importation des fonctions nécessaires depuis leurs fichiers respectifs.
import { resolvePlugin } from '@babel/core';
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

// Fonction principale pour gérer l'inscription de l'utilisateur et l'upload de sa photo.
export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled (
    [signUpUser(firstName, lastName), uploadPhoto(fileName)]
  )
}
// return pending = en cours d'execution en attente
