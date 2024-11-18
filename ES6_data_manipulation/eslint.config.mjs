import globals from "globals";
import js from "@eslint/js";
import typescriptEslintPlugin from "@typescript-eslint/eslint-plugin";
import typescriptEslintParser from "@typescript-eslint/parser";
import reactPlugin from "eslint-plugin-react";

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
  {
    files: ["**/*.js", "**/*.ts"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      parser: typescriptEslintParser,
      globals: {
        ...globals.browser,
        ...globals.node,
        es2021: true
      }
    },
    plugins: {
      "@typescript-eslint": typescriptEslintPlugin,
      react: reactPlugin
    },
    rules: {
      "@typescript-eslint/no-unused-expressions": "off",
      "react/react-in-jsx-scope": "off" // Exemple de règle React désactivée
    }
  }
];
