/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s = s.trim().replace(/\s+/g,' ');
    s = s.split(' ');
    s = s.pop();
    return s.length;
    
};