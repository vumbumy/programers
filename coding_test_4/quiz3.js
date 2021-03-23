var path = []

function dfs(index, visited) {
    for(let c of children[index]){
        dfs(c, visited)
    }
}

function solution(next_student) {
    let answer = 0;

    let parents = []
    for(let i=0; i<next_student.length; i++){
        children.push([i])
        parents.push([])
    }

    for(let index in next_student){
        if(next_student[index] !== 0) {
            let student = parseInt(next_student[index] - 1)

            children[index].push(student)

            parents[student].push(index)
        }
    }

    console.log(children)
    console.log(parents)

    return answer;
}

console.log(solution([5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2]))
