const { test, expect } = require('@playwright/test');

test.beforeEach(async ({ page }) => {
  await page.goto('/example/index.html');
});

test('create node', async ({ page }) => {
  await page.click('#createNodeBtn');
  await expect(page.locator('#output')).toContainText('RequirementNode');
});

test('validate node', async ({ page }) => {
  await page.click('#validateNodeBtn');
  await expect(page.locator('#output')).toContainText('"valid": true');
});

test('create crosswalk', async ({ page }) => {
  await page.click('#createCrosswalkBtn');
  await expect(page.locator('#output')).toContainText('Standard-to-Standard');
});
