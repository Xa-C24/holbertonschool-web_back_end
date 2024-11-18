# ES6 Data Manipulation
Introduction
ES6, also known as ECMAScript 2015, introduced several powerful features for data manipulation in JavaScript. This README provides an overview of key ES6 features that enhance data handling and manipulation capabilities.
Table of Contents
Destructuring
Spread Operator
Rest Parameters
Arrow Functions
Template Literals
Enhanced Object Literals
Array Methods
Map and Set
Destructuring
Destructuring allows you to extract values from arrays or properties from objects into distinct variables1.
javascript
// Array destructuring
const [a, b] = [1, 2];

// Object destructuring
const { name, age } = { name: 'John', age: 30 };

Spread Operator
The spread operator (...) allows an iterable to be expanded in places where zero or more arguments or elements are expected1.
javascript
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]

const obj1 = { x: 1, y: 2 };
const obj2 = { ...obj1, z: 3 }; // { x: 1, y: 2, z: 3 }

Rest Parameters
Rest parameters allow you to represent an indefinite number of arguments as an array1.
javascript
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

Arrow Functions
Arrow functions provide a more concise syntax for writing function expressions1.
javascript
const square = x => x * x;
const add = (a, b) => a + b;

Template Literals
Template literals allow embedded expressions and multi-line strings1.
javascript
const name = 'Alice';
const greeting = `Hello, ${name}!
Welcome to ES6.`;

Enhanced Object Literals
ES6 provides shorthand syntax for defining object methods and properties1.
javascript
const x = 1, y = 2;
const obj = {
  x,
  y,
  method() {
    return this.x + this.y;
  }
};

Array Methods
ES6 introduced new array methods for easier data manipulation1.
javascript
const numbers = [1, 2, 3, 4, 5];

// find
const found = numbers.find(num => num > 3); // 4

// findIndex
const index = numbers.findIndex(num => num > 3); // 3

// Array.from
const arrayLike = { 0: 'a', 1: 'b', length: 2 };
const arr = Array.from(arrayLike); // ['a', 'b']

Map and Set
Map and Set are new data structures introduced in ES61.
javascript
// Map
const map = new Map();
map.set('key', 'value');
map.get('key'); // 'value'

// Set
const set = new Set([1, 2, 3, 3]);
set.size; // 3 (duplicate values are removed)