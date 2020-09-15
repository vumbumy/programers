function solution(tickets) {
    let countrySet = new Set()

    let connect = {}

    let index = 1

    for(let t of tickets){
        if(!connect.hasOwnProperty(t[0])) {
            connect[t[0]] = {}
        }

        connect[t[0]][t[1]] = index

        index += 1

        countrySet.add(t[0])
        countrySet.add(t[1])
    }
    
    var answer = [];
    return answer;
}

console.log(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
console.log(solution([["ICN","SFO"],["ICN","ATL"],["SFO","ATL"],["ATL","ICN"],["ATL","SFO"]]))