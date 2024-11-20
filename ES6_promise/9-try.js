export default function guardrail(mathFunction) {
  const queue = []; // Initialisation le tableau queue

  try {
     // Essayer d'exécuter mathFunction et ajouter son résultat au tableau
      const result = mathFunction();
      queue.push(result);
      // Si une erreur est levée, ajouter le message de l'erreur au tableau
  } catch (error) {
    queue.push(`Error: ${error.message}`);
  }

  queue.push('Guardrail was processed');

  return queue;
}
