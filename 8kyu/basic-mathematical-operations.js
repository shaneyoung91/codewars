// Your task is to create a function that does four basic mathematical operations.

// The function should take three arguments - operation(string/char), value1(number), value2(number).
// The function should return result of numbers after applying the chosen operation.

// Examples(Operator, value1, value2) --> output
// ('+', 4, 7) --> 11
// ('-', 15, 18) --> -3
// ('*', 5, 5) --> 25
// ('/', 49, 7) --> 7


// My Solution
function basicOp(operation, value1, value2) {
    // Code
    // if statement contains specific operator, then do math accordingly
    let result = 0
    const mathSign = ['+','-', '*', '/'];
    if (operation === mathSign[0]) {
        result = value1 + value2
    } else if (operation === mathSign[1]) {
        result = value1 - value2
    } else if (operation === mathSign[2]) {
        result = value1 * value2
    } else if (operation === mathSign[3]) {
        result = value1 / value2
    }
    return result
}