let test, expect;
try {
  ({ test, expect } = require('@playwright/test'));
} catch (err) {
  console.warn('Playwright not installed, skipping demo E2E test.');
}

if (test) {
  // Simple placeholder test to ensure Playwright can run in CI
  test('E2E tests require Playwright', async ({ page }) => {
    // Minimal test to verify Playwright is working
    await page.goto('data:text/html,<h1>Test</h1>');
    await expect(page.locator('h1')).toHaveText('Test');
  });
}
