const ProofOfWork = require("./proof-of-work");

test("Given hash length lower than number of digits, then false", () => {
  const isHashValid = ProofOfWork.hashEvaluator(2, 10)("1");
  expect(isHashValid).toBe(false);
});

test("Given the first 3 digits are bellow 100, then false", () => {
  const isHashValid = ProofOfWork.hashEvaluator(3, 100)("12345");
  expect(isHashValid).toBe(false);
});

test("Given the first 2 digits are bellow 40, then true", () => {
  const isHashValid = ProofOfWork.hashEvaluator(2, 40)("31fba2");
  expect(isHashValid).toBe(true);
});
