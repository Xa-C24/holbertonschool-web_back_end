import globals from 'globals';

export default [
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 2021, // Active les fonctionnalités modernes d'ECMAScript
      sourceType: 'commonjs', // Utilise CommonJS (require/module.exports)
      globals: {
        ...globals.node, // Définit les globales de Node.js, comme `require`, `module`, et `process`
      },
    },
    rules: {
      semi: ['error', 'always'], // Points-virgules obligatoires
      quotes: ['error', 'single'], // Guillemet simple obligatoire
      indent: ['error', 2], // Indentation de 2 espaces
      'no-unused-vars': ['error'], // Détecte les variables inutilisées
    },
  },
];
