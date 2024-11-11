# ES6 Basics

Welcome to the **ES6 Basics** guide! This document covers the fundamental features introduced in ES6 (ECMAScript 6), which greatly improve JavaScript's readability, functionality, and maintainability.

## Table of Contents

1. [Introduction](#introduction)
2. [Features of ES6](#features-of-es6)
   - [let and const](#let-and-const)
   - [Arrow Functions](#arrow-functions)
   - [Default Parameters](#default-parameters)
   - [Object and Array Destructuring](#object-and-array-destructuring)
   - [Template Literals](#template-literals)
   - [Classes](#classes)
   - [Modules (import/export)](#modules-importexport)
   - [Promises](#promises)
   - [Collections (Map, Set, WeakMap, WeakSet)](#collections-map-set-weakmap-weakset)
   - [Spread and Rest Operators](#spread-and-rest-operators)
3. [Conclusion](#conclusion)

## Introduction

ES6, also known as ECMAScript 2015, brought powerful enhancements to JavaScript. These changes make the language more efficient and adaptable for modern web development. This guide explores the core features of ES6, providing examples and use cases for each.

## Features of ES6

### 1. let and const

ES6 introduced `let` and `const` for declaring variables, allowing for block scope and better control over variable reassignment:

```javascript
let variable = 'Changeable';
const constant = 'Unchangeable';

1. Install Node.js 20.x.x and npm 9.x.x  
In my home directory, run the following commands to install Node.js:  

bash Copy the code      curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh  
                        sudo bash nodesource_setup.sh sudo apt install nodejs -y  

    Then check the installation:   
    bash Copy the code 
            nodejs -v # should display version 20.x.x  --> v20.18.0
            npm -v # should display version 9.x.x  --> 10.8.2

Install Jest, Babel, and ESLint  
In the project directory, install the necessary dependencies:  
bash Copy the code   
        npm install --save-dev jest # For testing  
        npm install --save-dev babel-jest @babel/core @babel/preset-env # For Babel  
        npm install --save-dev eslint # For linting  