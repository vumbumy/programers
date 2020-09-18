function solution(user_id, banned_id) {
    let n = user_id.length
    let m = banned_id.length

    let answer = 1;
    for(let b of banned_id){
        let regExp = /[*]/gi

        b = b.replace(regExp, "\\w")

        let re = new RegExp('^' + b + '$')

        let count = 0;
        for(let j = 0; j < n; j++){
            if(re.test(user_id[j])){
                console.log(b, user_id[j])
                user_id[j] = ""

                count++;
            }
        }
        console.log(b, count)
        answer *= count
    }

    return answer
}

console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
console.log(solution(["frodo", "drodo", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "***do"]))