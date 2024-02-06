// When provided with a number between 0-9, return it in words.

// Input :: 1
// Output :: "One".

// If your language supports it, try using a switch statement.


//  My Solution
function switchItUp(number){
    const words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];

    if (number >= 0 && number <= 9) {
        return words[number];
    } 
}