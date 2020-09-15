function solution(n, edge) {
    let connect = Array.from(Array(n), () => [])
    for(let e of edge){
        connect[e[0]-1].push(e[1]-1)
        connect[e[1]-1].push(e[0]-1)
    }

    let distance = Array.from({length: n}, () => 20001);

    let q = [0]
    distance[0] = 0

    while(q.length !== 0){
        let now = q.pop()

        const nextD = distance[now] + 1

        for(let next of connect[now]){
            if(distance[next] > nextD){
                distance[next] = nextD

                q.push(next)
            }
        }
    }

    let maxD = 0
    let answer = 0;
    for(let d of distance){
        if(d > maxD) {
            maxD = d
            answer = 1
        } else if (d === maxD){
            answer++
        }
    }

    return answer;
}

// console.log(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
console.log(solution(5, [[1, 2], [1, 3], [2, 4], [4, 5], [3, 5]]))