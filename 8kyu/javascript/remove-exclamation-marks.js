// Write function RemoveExclamationMarks which removes all exclamation marks from a given string.



// My Solution
function removeExclamationMarks(s) {
    const newS = s.replaceAll("!","");
    return newS; 
}