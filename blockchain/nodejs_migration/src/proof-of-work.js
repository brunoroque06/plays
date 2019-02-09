exports.prove = (digits, maxValue) => hash => {
  if (hash.length < digits) {
    return false;
  }
  // return hash.substring(0, digits) < maxValue;
  return hash.substring(0, 3) === "000";
};
