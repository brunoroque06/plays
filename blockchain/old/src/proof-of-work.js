exports.prove = digits => hash => {
  if (hash.length < digits) {
    return false;
  }
  return hash.substring(0, digits) === "0".repeat(digits);
};
