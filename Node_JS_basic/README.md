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

