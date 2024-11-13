export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    // Déclaration de nouvelles variables pour le bloc if
    const innerTask = true;
    const innerTask2 = false;
    return [innerTask, innerTask2];
  }

  return [task, task2];
}
