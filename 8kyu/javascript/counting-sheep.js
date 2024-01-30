// Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

// For example,

// [True,  True,  True,  False,
//   True,  True,  True,  True ,
//   True,  False, True,  False,
//   True,  False, False, True ,
//   True,  True,  True,  True ,
//   False, False, True,  True]
// The correct answer would be 17.

// Hint: Don't forget to check for bad values like null/undefined



// My Solution
function countSheeps(sheep) {
    if (sheep === null || sheep === undefined) {
        return 0
    }
    const present = sheep.reduce((accumulator, currentValue) => {
        if (currentValue) {
            return accumulator + 1;
        } else {
            return accumulator
        }
    }, 0);
    return present
}