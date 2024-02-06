// Complete the solution so that it reverses the string passed into it.

// 'world'  =>  'dlrow'
// 'word'   =>  'drow'


//  My Solution
function solution(str){
    const splitStr = str.split("");
    const reverseStr = splitStr.reverse();
    const join = reverseStr.join("");
    return join
}