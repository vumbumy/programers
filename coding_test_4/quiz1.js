function solution(n, record) {
    let answer = [];

    let nickNamesEachServer = []
    for(let i=0; i<n; i++){
        nickNamesEachServer.push([])
    }

    for(let r of record){
        let info = r.split(" ")

        let sN = parseInt(info[0]) - 1
        let nN = info[1]

        if(!nickNamesEachServer[sN])
            nickNamesEachServer[sN] = [nN]
        else if(!nickNamesEachServer[sN].includes(nN)){
            if(nickNamesEachServer[sN].length >= 5){
                nickNamesEachServer[sN].shift()
            }

            nickNamesEachServer[sN].push(nN)
        }
    }

    for(let nickNames of nickNamesEachServer){
        answer = answer.concat(nickNames)
    }

    return answer;
}

// console.log(solution(1, ["1 fracta", "1 sina","1 hana","1 robel","1 abc", "1 sina", "1 lynn"]))
console.log(solution(4, ["1 a","1 b","1 abc","3 b","3 a","1 abcd","1 abc","1 aaa","1 a","1 z","1 q", "3 k", "3 q", "3 z", "3 m", "3 b"]))
