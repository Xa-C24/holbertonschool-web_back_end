module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
    jest: true,
  },
  extends: [
    'eslint:recommended',
    'airbnb-base',
    'plugin:jest/recommended',
  ],
  plugins: [
    'jest',
  ],
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module',
  },
  rules: {
    'no-unused-vars': 'warn',
    'no-console': 'off',
    'import/extensions': ['error', 'ignorePackages', { js: 'always' }],
    'jest/require-hook': 'warn',
    'max-len': ['error', { code: 120 }],
  },
};
