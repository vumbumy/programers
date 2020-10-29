function isPalindrome(s) {
    let lo = 0, hi = s.length - 1

    while (lo < hi){
        if(s[lo++] !== s[hi--])
            return false
    }

    return true
}

function solution(s){
    if(s.length === 1)
        return 1

    for(let l = s.length; l >= 1;l--){
        for(let i = 0; i < s.length - l + 1; i++){
            let subStr = s.substring(i, i + l)
            if(isPalindrome(subStr))
                return l
        }
    }
    return 0
}

const assert = require('assert');

assert.equal(solution("abcdcba"), 7);
assert.equal(solution("abacde"), 3);
assert.equal(solution("abcabcdcbae"), 7);
assert.equal(solution("aaaa"), 4);
assert.equal(solution("abcde"), 1);
assert.equal(solution("a"), 1);
assert.equal(solution("abcbaqwertrewqq"), 9);
assert.equal(solution("abcbaqwqabcba") , 13);
assert.equal(solution("abba"), 4);
assert.equal(solution("abaabaaaaaaa"), 7);
