function solution(m, v) {
    let answer = [];

    for(let vv of v){
        let index = answer.findIndex(a => (m - a) < vv)
        // for(let i in answer){
        //     if(m - answer[i] >= vv)
        //         index = i
        //     else break
        // }

        if(index > 0)
            answer[index - 1] += vv
        else if(m - answer[0] >= vv){
            answer[0] += vv
        }else {
            answer.unshift(vv)
        }
    }

    return answer.length;
}


console.log(
    solution(4, [2,3,1])
)
