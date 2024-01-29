// You get an array of numbers, return the sum of all of the positives ones.

// Example [1,-4,7,12] => 1 + 7 + 12 = 20

// Note: if there is nothing to sum, the sum is default to 0.


// My Solution
function positiveSum(arr) {
    let posSum = 0
    let posNums = arr.filter((num) => num >= 0);
    for (let i = 0; i < posNums.length; i++) {
        posSum += posNums[i]
    }
    return posSum;
}