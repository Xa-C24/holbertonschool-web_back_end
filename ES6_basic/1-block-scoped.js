// 1-block-scoped.js

export default function taskBlock(trueOrFalse) {
    let task = false;
    let task2 = true;
  
    if (trueOrFalse) {
      let task = true; // portée limitée au bloc if
      let task2 = false; // portée limitée au bloc if
    }
  
    return [task, task2];
  }
  