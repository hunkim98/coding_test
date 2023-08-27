/**
 * 
 * 가장 먼 노드
    Description
    n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

    노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

    제한사항
    노드의 개수 n은 2 이상 20,000 이하입니다.
    간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
    vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
    입출력 예
    n	vertex	return
    6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
    입출력 예 설명
    예제의 그래프를 표현하면 아래 그림과 같고, 1번 노드에서 가장 멀리 떨어진 노드는 4,5,6번 노드입니다.

 * 
 * 
 */
function solution(n, edge) {
  var graphInfo = [new Set()];
  const distances = [0];
  const visited = [true];
  for (let i = 1; i < n; i++) {
    // initialize hash table for edges
    graphInfo.push(new Set());
    distances.push(Number.MAX_VALUE); // let us remember this
    // we can use visited array to check if we have visited the array
    visited.push(false);
    // and this, Number.MIN_VALUE;
  }

  for (let i = 0; i < edge.length; i++) {
    const [edgeStart, edgeEnd] = edge[i];
    graphInfo[edgeStart - 1].add(edgeEnd - 1);
    graphInfo[edgeEnd - 1].add(edgeStart - 1);
  }

  var longestDistance = -1;
  // we need to compare the distance starting from 2
  // return 0
  // Queue is very important for this BFS problem
  const queue = [0];
  // remind yourself that everytime we do bfs. the later values will have a bigger distance always
  // it is monotonic
  // However, we need a queue since, we need to visit the nodes in the order of distance!
  while (queue.length !== 0) {
    const nodeIndex = queue.shift();
    const nodeDistance = distances[nodeIndex];
    const visitableIndices = Array.from(graphInfo[nodeIndex].values());
    for (let i = 0; i < visitableIndices.length; i++) {
      const visitIndex = visitableIndices[i];
      if (visited[visitIndex]) {
        continue;
      }
      if (graphInfo[nodeIndex].has(visitIndex)) {
        if (distances[visitIndex] > nodeDistance + 1) {
          distances[visitIndex] = nodeDistance + 1;
          // we do not need to visit this again since the distance will
          // forever be longer in later iterations
          // this is possible since we used queue!!
          // if this was stack, we could not do this
          visited[visitIndex] = true;
          if (longestDistance < distances[visitIndex]) {
            longestDistance = distances[visitIndex];
          }
        }
      }
      queue.push(visitIndex);
    }
  }

  let longestCount = 0;
  for (let i = 0; i < n; i++) {
    const distance = distances[i];
    if (distance === longestDistance) {
      longestCount = longestCount + 1;
    }
  }

  return longestCount;

  // this was the first approach
  for (let i = 1; i < n; i++) {
    // BFS
    // our starting point is 0 (1)
    let distance = 0; // this is like level
    let isReached = false;
    const visitedNodeIndices = new Set([0]);
    const nodeIndicesToStartFrom = new Set([0]);
    while (!isReached) {
      const nodeIndicesToExplore = Array.from(nodeIndicesToStartFrom.values());
      for (let j = 0; j < nodeIndicesToExplore.length; j++) {
        const nodeIndex = nodeIndicesToExplore[j];
        visitedNodeIndices.add(nodeIndex);
        if (graphInfo[nodeIndex].has(i)) {
          isReached = true;
          break;
        }
      }
      if (isReached) {
        break;
      }
      nodeIndicesToStartFrom.clear();
      for (let j = 0; j < nodeIndicesToExplore.length; j++) {
        const nodeIndex = nodeIndicesToExplore[j];
        const candidateIndices = Array.from(graphInfo[nodeIndex].values());
        for (k = 0; k < candidateIndices.length; k++) {
          const candidateIndex = candidateIndices[k];
          if (visitedNodeIndices.has(candidateIndex)) {
            continue;
          }
          if (!nodeIndicesToStartFrom.has(candidateIndex)) {
            nodeIndicesToStartFrom.add(candidateIndex);
          }
        }
      }
      distance++;
    }
    distances.push(distance);

    if (longestDistance < distance) {
      longestDistance = distance;
    }
  }

  //     let longestCount = 0;
  //     for(let i = 0; i < distances.length; i++){
  //         const distance = distances[i]
  //         if(distance === longestDistance) {
  //             longestCount = longestCount + 1;
  //         }
  //     }

  //     return longestCount;
}

console.log(
  solution(6, [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2],
  ])
);

// answer: 3
