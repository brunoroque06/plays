const ProofOfWork = require("./proof-of-work");

test("Given hash length lower than number of digits, then false", () => {
  const isProved = ProofOfWork.prove(2, 10)("1");
  expect(isProved).toBeFalsy();
});

test("Given the first 3 digits are bellow 100, then false", () => {
  const isProved = ProofOfWork.prove(3, 100)("12345");
  expect(isProved).toBeFalsy();
});

test("Given the first 2 digits are bellow 40, then true", () => {
  const isProved = ProofOfWork.prove(2, 40)("31fba2");
  expect(isProved).toBeTruthy();
});
