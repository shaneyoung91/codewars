// Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.


//  My Solution
function replace(s){
    const regex = /[aeiouAEIOU]/g;

    return s.replace(regex, '!')
}
