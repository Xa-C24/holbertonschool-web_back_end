# ES6 Promises

## Table of Contents
- [Introduction](#introduction)
- [What is a Promise?](#what-is-a-promise)
- [States of a Promise](#states-of-a-promise)
- [Creating a Promise](#creating-a-promise)
- [Using `.then()` and `.catch()`](#using-then-and-catch)
- [Using `.finally()`](#using-finally)
- [Chaining Promises](#chaining-promises)
- [Promise Static Methods](#promise-static-methods)
  - [Promise.all()](#promiseall)
  - [Promise.race()](#promiserace)
  - [Promise.any()](#promiseany)
  - [Promise.allSettled()](#promiseallsettled)
- [Error Handling in Promises](#error-handling-in-promises)
- [Async/Await](#asyncawait)
- [Conclusion](#conclusion)

---

## Introduction

**ES6 Promises** are a feature introduced in ECMAScript 2015 (ES6) to handle asynchronous operations more effectively. They provide a cleaner, more readable way to manage asynchronous code compared to traditional callbacks, reducing the likelihood of "callback hell."

---

## What is a Promise?

A **Promise** is an object representing the eventual completion (or failure) of an asynchronous operation. Promises provide a standard way to work with asynchronous code in JavaScript.

---

## States of a Promise

A Promise has three possible states:

1. **Pending**: The initial state, neither fulfilled nor rejected.
2. **Fulfilled**: The operation was successful, and the promise is resolved with a value.
3. **Rejected**: The operation failed, and the promise is rejected with a reason.

---

## Creating a Promise

You can create a Promise using the `Promise` constructor:

```javascript
const myPromise = new Promise((resolve, reject) => {
  const success = true;

  if (success) {
    resolve("Operation was successful!");
  } else {
    reject("Operation failed!");
  }
});

Conclusion
ES6 Promises simplify asynchronous programming by replacing traditional callbacks with a more structured and readable approach. Combined with async/await, Promises are a powerful tool for managing asynchronous operations in JavaScript.