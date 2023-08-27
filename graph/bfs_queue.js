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
