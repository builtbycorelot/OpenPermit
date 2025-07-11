#!/usr/bin/env node
/* eslint-disable no-console */
// Run Playwright tests if the package is installed. Otherwise skip gracefully.
const { execSync } = require('child_process');

function hasPlaywright() {
  try {
    require.resolve('@playwright/test');
    return true;
  } catch (err) {
    return false;
  }
}

if (!hasPlaywright()) {
  console.warn('Playwright not installed, skipping E2E tests.');
  process.exit(0);
}

execSync('node node_modules/@playwright/test/cli.js test', { stdio: 'inherit' });
