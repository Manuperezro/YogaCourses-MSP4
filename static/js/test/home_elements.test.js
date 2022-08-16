/**
 * @jest-environment jsdom
 */

const { modulo, sum } = require('../home_elements');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});

test('modulo 2 from 5 to equal 1', () => {
    expect(modulo(5, 2)).toBe(1);
  });