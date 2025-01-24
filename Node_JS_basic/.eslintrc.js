module.exports = {
  env: {
    browser: false, // Désactiver l'environnement navigateur
    commonjs: true,
    es2021: true,
    node: true, // Activer les globales Node.js comme `process` et `require`
  },
  extends: 'eslint:recommended',
  parserOptions: {
    ecmaVersion: 12, // Activer les fonctionnalités modernes d'ECMAScript
  },
  rules: {
    semi: ['error', 'always'], // Points-virgules obligatoires
    quotes: ['error', 'single'], // Guillemet simple obligatoire
  },
};
