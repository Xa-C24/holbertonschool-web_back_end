# Fundamental Project: Node.js

Welcome to this project on **Node.js**! 🌟 This project explores the basics of Node.js, a server-side JavaScript runtime environment. You will learn to create servers, read and write files, and manage asynchronous tasks. 🚀

---

## What is Node.js? 🤔

Node.js is a platform built on Google Chrome's **V8** JavaScript engine. It allows you to execute JavaScript code **outside a browser**. Node.js is ideal for fast and scalable applications, such as web servers, APIs, or CLI tools.

### Key Features of Node.js:
- **Asynchronous and Non-blocking**: Node.js uses an event loop to handle requests without blocking execution. ⏱️
- **Rich Ecosystem**: With **NPM (Node Package Manager)**, you have access to thousands of libraries. 📦
- **High Performance**: Thanks to the V8 engine and event-driven model. ⚡

---

## Installation 🛠️

1. Install **Node.js** from [nodejs.org](https://nodejs.org).
2. Verify the installation:
   ```bash
   node -v
   npm -v
   ```

3. Initialize a Node.js project:
   ```bash
   mkdir node-project
   cd node-project
   npm init -y
   ```

---

## Basic Examples 🎯

### 1. Create a Basic HTTP Server

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Welcome to my Node.js server!\n');
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
```

### 2. Read a File with `fs`

```javascript
const fs = require('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
```

---

## Key Concepts 🔑

### **Modules** 📁
Modules help structure your code. Example:
```javascript
// greet.js
module.exports = (name) => `Hello, ${name}!`;

// main.js
const greet = require('./greet');
console.log(greet('Holberton')); // Hello, Holberton!
```

### **Asynchronous Programming** ⏳
Node.js uses callbacks, Promises, or `async/await` to handle asynchronous tasks. Example with `async/await`:
```javascript
const fs = require('fs').promises;

async function readFile() {
    try {
        const data = await fs.readFile('example.txt', 'utf8');
        console.log(data);
    } catch (err) {
        console.error(err);
    }
}

readFile();
```

---

## Quick Start 🚀

1. Clone this repository:
   ```bash
   git clone https://github.com/username/node-project.git
   cd node-project
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the application:
   ```bash
   node app.js
   ```

---

## Useful Resources 📚

- [Official Node.js Documentation](https://nodejs.org/en/docs/)
- [Node.js Guide on MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Node.js)
- [NPM (Node Package Manager)](https://www.npmjs.com/)  



## Express.js - Résumé

- Express est un framework web minimaliste pour Node.js qui simplifie la création d'applications web et d'API. Il offre un ensemble riche de fonctionnalités pour gérer des requêtes HTTP, définir des routes, et ajouter des middlewares pour traiter les données entrantes et sortantes.

### Pourquoi utiliser Express ?

Simplifie le développement :

- Réduit le code nécessaire pour créer un serveur HTTP avec Node.js.

### Support des middlewares :

Permet d'ajouter des fonctions intermédiaires pour traiter les requêtes avant d'y répondre.

### Gestion facile des routes :

Offre une syntaxe claire pour gérer les différents endpoints (GET, POST, etc.).

### Flexibilité et extensibilité :

Supporte de nombreuses bibliothèques pour étendre ses fonctionnalités (par exemple : authentification, traitement des fichiers).

### Large écosystème :

Un des frameworks les plus populaires dans la communauté Node.js avec une large documentation et support.

### Fonctionnalités principales

## 1. Gestion des routes :

Permet de définir des endpoints pour chaque méthode HTTP (ég. GET, POST).

    const express = require('express');
    const app = express();

    // Route GET
    app.get('/', (req, res) => {
      res.send('Hello World!');
    });

    // Route POST
    app.post('/submit', (req, res) => {
      res.send('Form submitted!');
    });

    app.listen(3000, () => {
      console.log('Server running on port 3000');
    });

## 2. Middlewares :

Les middlewares sont des fonctions intermédiaires utilisées pour traiter les requêtes avant qu'elles n'atteignent la route.

    app.use((req, res, next) => {
      console.log(`Request received: ${req.method} ${req.url}`);
      next(); // Passe au middleware ou à la route suivante
    });

## 3. Support des fichiers statiques :

Permet de servir des fichiers CSS, images ou JavaScript.

    app.use(express.static('public'));

## 4. Paramètres de route :

Capture des parties dynamiques de l'URL.

    app.get('/user/:id', (req, res) => {
      res.send(`User ID: ${req.params.id}`);
    });

## 5. Gestion des erreurs :

Permet d'ajouter un middleware spécial pour gérer les erreurs.

    app.use((err, req, res, next) => {
      console.error(err.stack);
      res.status(500).send('Something broke!');
    });

### Quand utiliser Express ?

- Création d'API RESTful.

- Développement de petites applications web ou prototypes.

- Gestion des requêtes HTTP dans des projets backend.

- Exemple de projet simple avec Express

## Voici un exemple de serveur HTTP utilisant Express :

    const express = require('express');
    const app = express();
    const PORT = 3000;

    // Route de base
    app.get('/', (req, res) => {
      res.send('Welcome to my Express app!');
    });

    // Lancer le serveur
    app.listen(PORT, () => {
      console.log(`Server is running on http://localhost:${PORT}`);
    });

### Installation

Pour installer Express dans votre projet, utilisez la commande suivante :

    npm install express

## Conclusion

- Express est un outil puissant et facile à utiliser pour développer des applications backend avec Node.js. Il permet de se concentrer sur la logique métier sans gérer les détails complexes des requêtes HTTP. Avec son écosystème riche et sa communauté active, c'est un choix idéal pour tout projet backend.