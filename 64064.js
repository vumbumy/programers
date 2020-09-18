var regExList = []
var n = 0;
var m = 0;

function recv(index, user_id) {
    if(m === index){
        console.log()
        return 1
    }

    let re = regExList[index]

    let count = 0;

    for(let j = 0;j<n;j++){
        if(re.test(user_id[j])){
            console.log(re, user_id[j])
            let temp = user_id[j]

            user_id[j] = ""

            count += recv(index + 1, user_id)

            user_id[j] = temp
        }
    }

    return count
}

function solution(user_id, banned_id) {
    n = user_id.length
    m = banned_id.length

    for(let b of banned_id){
        let regExp = /[*]/gi

        b = b.replace(regExp, "\\w")

        let re = new RegExp('^' + b + '$')

        regExList.push(re)
    }

    return recv(0, user_id);
}

console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))