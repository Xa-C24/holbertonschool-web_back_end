# Arrays, Map, Typed Arrays, Objects - Méthodes en JavaScript

## Arrays

### Méthodes très courantes
- **concat()** : Combine deux ou plusieurs tableaux. Retourne un nouveau tableau contenant les éléments combinés.  
  Ex : `let result = [1, 2].concat([3, 4]); // [1, 2, 3, 4]`

- **includes()** : Vérifie si un élément existe dans le tableau. Retourne `true` si trouvé, sinon `false`.  
  Ex : `[1, 2, 3].includes(2); // true`

- **indexOf()** : Retourne l'index du premier élément trouvé, ou `-1` si absent.  
  Ex : `[1, 2, 3].indexOf(2); // 1`

- **join()** : Combine les éléments en une chaîne avec un délimiteur. Par défaut, une virgule.  
  Ex : `[1, 2, 3].join('-'); // '1-2-3'`

- **reverse()** : Inverse l'ordre des éléments. Modifie le tableau en place.  
  Ex : `[1, 2, 3].reverse(); // [3, 2, 1]`

### Méthodes simples
- **fill()** : Remplit une portion avec une valeur donnée. Modifie le tableau.  
  Ex : `[1, 2, 3].fill(0, 1, 3); // [1, 0, 0]`

- **find()** : Retourne le premier élément satisfaisant une condition.  
  Ex : `[1, 2, 3].find(el => el > 1); // 2`

- **slice()** : Extrait une portion, sans modifier l'original.  
  Ex : `[1, 2, 3, 4].slice(1, 3); // [2, 3]`

### Méthodes complexes/avancées
- **copyWithin()** : Copie une section à une autre position. Modifie le tableau.  
  Ex : `[1, 2, 3, 4].copyWithin(0, 2); // [3, 4, 3, 4]`

- **findIndex()** : Retourne l'index du premier élément satisfaisant une condition, ou `-1`.  
  Ex : `[1, 2, 3].findIndex(el => el > 1); // 1`

- **sort()** : Trie les éléments. Modifie le tableau.  
  Ex : `[3, 1, 2].sort(); // [1, 2, 3]`

---

## Map

### Méthodes très courantes
- **set()** : Ajoute ou met à jour une paire clé-valeur.  
  Ex : `new Map().set('a', 1); // Map { 'a' => 1 }`

- **get()** : Retourne la valeur associée à une clé.  
  Ex : `new Map([['a', 1]]).get('a'); // 1`

- **has()** : Vérifie si une clé existe.  
  Ex : `new Map([['a', 1]]).has('a'); // true`

- **delete()** : Supprime une clé. Retourne `true` si réussi, sinon `false`.  
  Ex : `new Map([['a', 1]]).delete('a'); // true`

### Méthodes simples
- **clear()** : Supprime toutes les paires clé-valeur.  
  Ex : `new Map([['a', 1]]).clear(); // Map {}`

- **size** : Retourne le nombre d'éléments.  
  Ex : `new Map([['a', 1], ['b', 2]]).size; // 2`

### Méthodes complexes/avancées
- **forEach()** : Exécute une fonction pour chaque paire clé-valeur.  
  Ex : `new Map([['a', 1]]).forEach((val, key) => console.log(key, val)); // 'a 1'`

---

## Typed Arrays

### Méthodes très courantes
- **find()** : Retourne le premier élément satisfaisant une condition.  
  Ex : `new Uint8Array([1, 2, 3]).find(el => el > 1); // 2`

### Méthodes simples
- **copyWithin()** : Copie une section à une autre position. Modifie le tableau.  
  Ex : `new Uint8Array([1, 2, 3, 4]).copyWithin(0, 2); // [3, 4, 3, 4]`

- **subarray()** : Retourne une section comme un nouveau tableau.  
  Ex : `new Uint8Array([1, 2, 3, 4]).subarray(1, 3); // [2, 3]`

### Méthodes complexes/avancées
- **set()** : Copie les éléments d'un autre tableau typé dans le tableau actuel.  
  Ex : `let arr1 = new Uint8Array([1, 2, 3]); arr1.set(new Uint8Array([4, 5]), 1); // [1, 4, 5]`

---

## Objects

### Méthodes très courantes
- **toString()** : Retourne une chaîne représentant l'objet.  
  Ex : `{ name: 'Alice' }.toString(); // '[object Object]'`

- **hasOwnProperty()** : Vérifie si l'objet possède une propriété spécifique.  
  Ex : `{ name: 'Alice' }.hasOwnProperty('name'); // true`

### Méthodes simples
- **keys()** : Retourne un tableau des clés de l'objet.  
  Ex : `Object.keys({ name: 'Alice', age: 25 }); // ['name', 'age']`

- **values()** : Retourne un tableau des valeurs de l'objet.  
  Ex : `Object.values({ name: 'Alice', age: 25 }); // ['Alice', 25]`

### Méthodes complexes/avancées
- **assign()** : Copie les propriétés d'un ou plusieurs objets dans un autre.  
  Ex : `Object.assign({ a: 1 }, { b: 2 }); // { a: 1, b: 2 }`
