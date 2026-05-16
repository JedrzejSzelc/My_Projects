/////////////////////////////////////////////////////////
/// Title:          Playwright frontend test          ///        
/// Subtitle:       Written in TypeScript             ///
/// Version:        20260516                          ///
/// Creator:        Jedrzej (Andrew) Szelc            ///
/// Maintainer:     Jedrzej (Andrew) Szelc            ///
/// GitHub:         https://github.com/JedrzejSzelc   ///
/////////////////////////////////////////////////////////

////////////////////////
///// Configuration ////
////////////////////////

// Import
import { test, expect } from '@playwright/test';

// Variables and config
var string_url_test_page = 'https://playwright.dev/'
var string_find_text_on_page = 'has title'
var string_find_link_on_page = 'Get started'

/////////////////
///// Hooks /////
/////////////////

// Before all
test.beforeAll(async () => {
  console.log('This is my BeforeAll hook!');
});

// Before Each
test.beforeEach(async () => {
  console.log('This is my BeforeEach hook!');
});

// After all
test.afterAll(async () => {
  console.log('This is my AfterAll hook!');
});

// After each
test.afterEach(async () => {
  console.log('This is my AfterEach hook!');
});

////////////////////////
///// Single Tests /////
////////////////////////

// Test - Find text on webpage
test('Find text on webpage.', async ({ page, browserName }) => {

  // Test label
  console.log('Test - Find text on webpage!');

  // Await webpage
  await page.goto(string_url_test_page);

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(string_find_text_on_page);
});

// Test - Find clickable link on webpage
test.skip('Get link on webpage.', async ({ page, browserName }) => {

  // Test label
  console.log('Test - Find on webpage!');

  // Await webpage
  await page.goto(string_url_test_page);

  // Click the get started link.
  await page.getByRole('link', { name: string_find_link_on_page}).click();

  // Expects page to have a heading with the name of Installation.
  await expect(page.getByRole('heading', { name: 'Installation' })).toBeVisible();
});

/////////////////////////
///// Test grouping /////
/////////////////////////

// Group 1
test.describe('Test group number 1.', () => {

  // Hook
  test.beforeAll(async () => {
    console.log('BeforeAll hook in test group 1.');
  });

  // Nested (grouped) test
  var string_test_name = 'Group 1 - Test 1.'
  test(string_test_name, async ({ page, browserName }) => {

    test.skip(browserName !== 'firefox', 'Only in FireFox');

    console.log(string_test_name);
  
  }); 

  // Nested (grouped) test
  var string_test_name = 'Group 1 - Test 2.'
  test.fixme(string_test_name, async ({ page, browserName }) => {

    test.skip(browserName !== 'chromium', 'Only in Chrome');

    console.log(string_test_name);
  
  }); 

});

// Group 2
test.describe('Test group number 2.', () => {

  // Nested (grouped) test
  var string_test_name = 'Group 2 - Test 1.'
  test(string_test_name, async ({ page, browserName }) => {

    test.skip(browserName !== 'firefox', 'Only in FireFox');

    console.log(string_test_name);
  
  }); 

  // Nested (grouped) test
  var string_test_name = 'Group 2 - Test 2.'
  test.fixme(string_test_name, async ({ page, browserName }) => {

    test.skip(browserName !== 'chromium', 'Only in Chrome');

    console.log(string_test_name);
  
  }); 

  // Hook
  test.afterAll(async () => {
    console.log('AfterAll hook in test group 2.');
  });

});

////////////////
///// Tags /////
////////////////

test.describe('Test group number 3.', {tag: '@tag_group_3'}, () => {

  // Nested (grouped) test
  var string_test_name = 'Group 3 - Test 1.'
  test(string_test_name, async ({ page, browserName }) => {

    test.skip(browserName !== 'firefox', 'Only in FireFox');

    console.log(string_test_name);
  
  }); 

  // Nested (grouped) test
  var string_test_name = 'Group 3 - Test 2.'
  test(string_test_name, {tag: '@tag_group_3_test_1'}, async ({ page, browserName }) => {

    test.skip(browserName !== 'chromium', 'Only in Chrome');

    console.log(string_test_name);
  
  }); 

  // Hook
  test.afterAll(async () => {
    console.log('AfterAll hook in test group 3.');
  });

});
