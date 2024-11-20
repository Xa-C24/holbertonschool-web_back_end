Arrays
Méthodes très courantes
1. Méthode concat()
2. Méthode includes()
3. Méthode indexOf()
4. Méthode join()
5. Méthode reverse()
Méthodes simples
1. Méthode fill()
2. Méthode find()
3. Méthode slice()
Méthodes complexes/avancées
1. Méthode copyWithin()
2. Méthode findIndex()
3. Méthode sort()
Map
Méthodes très courantes
1. Méthode set()
2. Méthode get()
3. Méthode has()
4. Méthode delete()
Méthodes simples
1. Méthode clear()
2. Méthode size()
Méthodes complexes/avancées
1. Méthode forEach()
Typed Arrays
Méthodes très courantes
1. Méthode find()
Méthodes simples
1. Méthode copyWithin()
2. Méthode subarray()
Méthodes complexes/avancées
1. Méthode set()
Objects
Méthodes très courantes
1. Méthode toString()
2. Méthode hasOwnProperty()
Méthodes simples
1. Méthode keys()
2. Méthode values()
Méthodes complexes/avancées
1. Méthode assign()
Arrays
Méthodes très courantes
1. Méthode concat()
But : Combine deux ou plusieurs tableaux.
Principe : Retourne un nouveau tableau contenant les éléments combinés.
let arr1 = [1, 2];
let arr2 = [3, 4];
let result = arr1.concat(arr2);  // result = [1, 2, 3, 4]
2. Méthode includes()
But : Vérifie si un élément existe dans le tableau.
Principe : Retourne true si l'élément est trouvé, sinon false.
let arr = [1, 2, 3];
arr.includes(2);  // Retourne true
3. Méthode indexOf()
But : Retourne l'index du premier élément trouvé dans le tableau.
Principe : Retourne -1 si l'élément n'est pas trouvé.
let arr = [1, 2, 3];
arr.indexOf(2);  // Retourne 1
4. Méthode join()
But : Combine tous les éléments du tableau en une seule chaîne.
Principe : Retourne une chaîne avec les éléments séparés par un délimiteur (par défaut une virgule).
let arr = [1, 2, 3];
arr.join('-');  // Retourne '1-2-3'
5. Méthode reverse()
But : Inverse l'ordre des éléments du tableau.
Principe : Modifie le tableau en place.
let arr = [1, 2, 3];
arr.reverse();  // arr = [3, 2, 1]
Méthodes simples
1. Méthode fill()
But : Remplir une portion du tableau avec une valeur donnée.
Principe : Modifie le tableau en place.
let arr = [1, 2, 3];
arr.fill(0, 1, 3);  // arr = [1, 0, 0]
2. Méthode find()
But : Retourne le premier élément du tableau qui satisfait une condition.
Principe : Retourne l'élément trouvé ou undefined si aucune correspondance n'est trouvée.
let arr = [1, 2, 3];
arr.find((el) => el > 1);  // Retourne 2
3. Méthode slice()
But : Extrait une portion du tableau.
Principe : Retourne un nouveau tableau sans modifier l'original.
let arr = [1, 2, 3, 4];
arr.slice(1, 3);  // Retourne [2, 3]
Méthodes complexes/avancées
1. Méthode copyWithin()
But : Copie une section du tableau dans une autre position.
Principe : Modifie le tableau en place.
let arr = [1, 2, 3, 4];
arr.copyWithin(0, 2);  // arr = [3, 4, 3, 4]
2. Méthode findIndex()
But : Retourne l'index du premier élément qui satisfait une condition.
Principe : Retourne -1 si aucun élément ne correspond.
let arr = [1, 2, 3];
arr.findIndex((el) => el > 1);  // Retourne 1
3. Méthode sort()
But : Trie les éléments du tableau.
Principe : Modifie le tableau en place.
let arr = [3, 1, 2];
arr.sort();  // arr = [1, 2, 3]
Map
Méthodes très courantes
1. Méthode set()
But : Ajoute ou met à jour une paire clé-valeur dans la Map.
Principe : Retourne la Map modifiée.
let map = new Map();
map.set('a', 1);  // map = Map { 'a' => 1 }
2. Méthode get()
But : Retourne la valeur associée à une clé.
Principe : Retourne undefined si la clé n'existe pas.
let map = new Map([['a', 1]]);
map.get('a');  // Retourne 1
3. Méthode has()
But : Vérifie si une clé existe dans la Map.
Principe : Retourne true ou false.
let map = new Map([['a', 1]]);
map.has('a');  // Retourne true
4. Méthode delete()
But : Supprime une paire clé-valeur de la Map.
Principe : Retourne true si la clé a été supprimée, sinon false.
let map = new Map([['a', 1]]);
map.delete('a');  // map = Map {}, retourne true
Méthodes simples
1. Méthode clear()
But : Supprime toutes les paires clé-valeur dans la Map.
Principe : Modifie la Map en place.
let map = new Map([['a', 1], ['b', 2]]);
map.clear();  // map = Map {}
2. Méthode size()
But : Retourne le nombre d'éléments dans la Map.
Principe : Retourne un entier représentant la taille de la Map.
let map = new Map([['a', 1], ['b', 2]]);
map.size;  // Retourne 2
Méthodes complexes/avancées
1. Méthode forEach()
But : Exécute une fonction pour chaque élément de la Map.
Principe : Ne retourne rien, sert uniquement à itérer sur les éléments.
let map = new Map([['a', 1], ['b', 2]]);
map.forEach((value, key) => console.log(key, value));  
// Affiche 'a 1' et 'b 2'
Typed Arrays
Méthodes très courantes
1. Méthode find()
But : Retourne le premier élément du tableau typé qui satisfait une condition donnée.
Principe : Retourne l'élément trouvé ou undefined si aucun élément ne correspond.
let arr = new Uint8Array([1, 2, 3]);
arr.find((el) => el > 1);  // Retourne 2
Méthodes simples
1. Méthode copyWithin()
But : Copie une section du tableau dans une autre position.
Principe : Modifie le tableau en place.
let arr = new Uint8Array([1, 2, 3, 4]);
arr.copyWithin(0, 2);  // arr = [3, 4, 3, 4]
2. Méthode subarray()
But : Retourne une section du tableau sous forme d'un nouveau tableau.
Principe : Ne modifie pas le tableau d'origine.
let arr = new Uint8Array([1, 2, 3, 4]);
let sub = arr.subarray(1, 3);  // sub = [2, 3]
Méthodes complexes/avancées
1. Méthode set()
But : Copie les éléments d'un autre tableau typé dans le tableau actuel.
Principe : Modifie le tableau en place.
let arr1 = new Uint8Array([1, 2, 3]);
let arr2 = new Uint8Array([4, 5]);
arr1.set(arr2, 1);  // arr1 = [1, 4, 5]
Objects
Méthodes très courantes
1. Méthode toString()
But : Retourne une chaîne représentant l'objet.
Principe : Renvoie une chaîne décrivant l'objet (par défaut, le nom de son constructeur).
let obj = { name: 'Alice', age: 25 };
obj.toString();  // Retourne '[object Object]'
2. Méthode hasOwnProperty()
But : Vérifie si un objet possède une propriété spécifique.
Principe : Retourne true si l'objet possède la propriété, sinon false.
let obj = { name: 'Alice' };
obj.hasOwnProperty('name');  // Retourne true
Méthodes simples
1. Méthode keys()
But : Retourne un tableau contenant toutes les clés de l'objet.
Principe : Retourne un objet Array des clés.
let obj = { name: 'Alice', age: 25 };
Object.keys(obj);  // Retourne ['name', 'age']
2. Méthode values()
But : Retourne un tableau contenant toutes les valeurs de l'objet.
Principe : Retourne un objet Array des valeurs.
let obj = { name: 'Alice', age: 25 };
Object.values(obj);  // Retourne ['Alice', 25]
Méthodes complexes/avancées
1. Méthode assign()
But : Copie les valeurs des propriétés d'un ou plusieurs objets dans un autre objet.
Principe : Modifie l'objet de destination et retourne cet objet.
let obj1 = { a: 1 };
let obj2 = { b: 2 };
Object.assign(obj1, obj2);  // obj1 = { a: 1, b: 2 }