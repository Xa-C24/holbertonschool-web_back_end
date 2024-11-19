module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
    jest: true,
  },
  globals: {
    'AudioWorkletGlobalScope ': 'readonly', // Remarquez l'espace à la fin
  },
  extends: 'eslint:recommended',
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
  },
};
