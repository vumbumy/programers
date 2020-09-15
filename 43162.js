function solution(n, computers) {
    var answer = 0;

    let visited = Array.from({length: n}, () => false);

    for(let i=0;i<n;i++){
        if(visited[i])
            continue;

        answer++

        let q = [i]

        while(q.length !== 0){
            let now = q.shift()

            visited[now] = true

            for(let next=0;next<n;next++){
                if(computers[now][next] === 1 && !visited[next]){
                    q.push(next)
                }
            }
        }
    }

    return answer;
}

console.log(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))