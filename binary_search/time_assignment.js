function canReviewAll(n, times, providedTime) {
  let reviewableCount = 0;
  for (let i = 0; i < times.length; i++) {
    const time = times[i];
    reviewableCount += Math.floor(providedTime / time);
  }
  if (n <= reviewableCount) {
    return true;
  }
  return false;
}

function solution(n, times) {
  let answer = 0;
  const reviewerCount = times.length;
  const reviewerTurn = Array.from(Array(reviewerCount)).map((i) => 0);
  const sortedTimes = times.sort((a, b) => a - b);

  let a = 0;
  let b = sortedTimes.slice(-1) * n;
  while (a < b) {
    // a and b are times(minutes)
    const mid = a + Math.floor((b - a) / 2);
    const isValid = canReviewAll(n, times, mid);
    if (isValid) {
      // if isValid we shorten the range to find the maximum in the left
      // since we already looked at whether mid works, we do not need to search again
      b = mid;
    } else {
      // if not isValid we shorten the range to explore the right section
      // since we know that mid cannot work, we plus 1 to mid
      // Now because we add 1 to a every time, it will one day overwhelm b.
      // That is when while will break
      a = mid + 1;
    }
  }
  return a;
}

const answer = solution(6, [7, 10]);
console.log(answer); // 28
