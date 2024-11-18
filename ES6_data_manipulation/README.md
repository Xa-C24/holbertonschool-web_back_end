# **ES6 Data Manipulation**

## **Introduction**
ES6, also known as ECMAScript 2015, introduced several powerful features for data manipulation in JavaScript. This README provides an overview of key ES6 features that enhance data handling and manipulation capabilities.

---

## **Table of Contents**
1. [Destructuring](#destructuring)
2. [Spread Operator](#spread-operator)
3. [Rest Parameters](#rest-parameters)
4. [Arrow Functions](#arrow-functions)
5. [Template Literals](#template-literals)
6. [Enhanced Object Literals](#enhanced-object-literals)
7. [Array Methods](#array-methods)
8. [Map and Set](#map-and-set)

---

## **Destructuring**
Destructuring allows you to extract values from arrays or properties from objects into distinct variables.

```javascript
    // Array destructuring
    const [a, b] = [1, 2];

    // Object destructuring
    const { name, age } = { name: 'John', age: 30 };  

## **Spread Operator**  

The spread operator (...) allows an iterable to be expanded in places where zero or more arguments or elements are expected.  


    // Spread in arrays
    const arr1 = [1, 2, 3];
    const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]

    // Spread in objects
    const obj1 = { x: 1, y: 2 };
    const obj2 = { ...obj1, z: 3 }; // { x: 1, y: 2, z: 3 }  

## **Rest Parameters**  

Rest parameters allow you to represent an indefinite number of arguments as an array.  

    function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

## **Arrow Functions**  
Arrow functions provide a more concise syntax for writing function expressions.  

    const square = x => x * x;
    const add = (a, b) => a + b;


## **Template Literals**
Template literals allow embedded expressions and multi-line strings.  

    const name = 'Alice';
    const greeting = `Hello, ${name}!
    Welcome to ES6.`;

## **Enhanced Object Literals**  
ES6 provides shorthand syntax for defining object methods and properties.

    const x = 1, y = 2;
    const obj = {
      x,
      y,
      method() {
        return this.x + this.y;
      }
    };


## **Array Methods**  
ES6 introduced new array methods for easier data manipulation.

    const numbers = [1, 2, 3, 4, 5];

    // find
    const found = numbers.find(num => num > 3); // 4

    // findIndex
    const index = numbers.findIndex(num => num > 3); // 3

    // Array.from
    const arrayLike = { 0: 'a', 1: 'b', length: 2 };
    const arr = Array.from(arrayLike); // ['a', 'b']

## **Map and Set**  
Map and Set are new data structures introduced in ES6.  

    // Map
    const map = new Map();
    map.set('key', 'value');
    console.log(map.get('key')); // 'value'

    // Set
    const set = new Set([1, 2, 3, 3]);
    console.log(set.size); // 3 (duplicate values are removed)

## **Conclusion**
ES6 brought a range of new tools that significantly improve how we handle data in JavaScript. From destructuring and spread operators to modern array methods and new data structures like Map and Set, these features make JavaScript code cleaner, more readable, and more efficient.  
