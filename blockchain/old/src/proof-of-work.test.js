const ProofOfWork = require("./proof-of-work");

test("Given hash length lower than number of 0s, then false", () => {
  const isProved = ProofOfWork.prove(2)("1");
  expect(isProved).toBeFalsy();
});

test("Given the first 3 digits are not 0s, then false", () => {
  const isProved = ProofOfWork.prove(3)("12345");
  expect(isProved).toBeFalsy();
});

test("Given the first 2 digits are 0s, then true", () => {
  const isProved = ProofOfWork.prove(2)("00fba2");
  expect(isProved).toBeTruthy();
});
