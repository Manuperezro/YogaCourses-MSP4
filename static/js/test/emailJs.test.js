/**
 * @jest-environment jsdom
 */

const { Response }= require("../emailJs");

test('error message when email info is missing', () => {
  let response= "error";

  expect(Response(response)).toEqual("FAILED");
});