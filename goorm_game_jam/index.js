
// Always doubt the input. The way you parse the input can lead to errors in the future.
// the number input can be more than 1 digit. So we need to use slice to get the last character!

const readline = require('readline');
const fs = require('fs');


const inputFilePath = 'case3.txt'; // Replace with the actual path to your input file
const readStream = fs.createReadStream(inputFilePath);
let rl = readline.createInterface({
    input: readStream,
});
let input;
let lineCount = 0;
let sideLength = -1;
const playerPosition = {
	x: 0,
	y: 0
}
const goormPosition = {
	x: 0,
	y: 0
}
const playerVisitInfo = []
const goormVisitInfo = []
const boardGameInfo = []


rl.on('line', (line) => {
	input = line;
	if(lineCount === 0){
		// We set the sideLength
		sideLength = Number(line);
		for (let i = 0; i < sideLength; i++) {
				playerVisitInfo.push([]);
				goormVisitInfo.push([]);
				for (let j = 0; j < sideLength; j++) {
						playerVisitInfo[i].push(false);
						goormVisitInfo[i].push(false);
				}
		}
	} else if (lineCount == 1){
		const position = line.split(" ")
		goormPosition.y = Number(position[0]) - 1;
		goormPosition.x = Number(position[1]) - 1;
		goormVisitInfo[goormPosition.y][goormPosition.x] = true;
	} else if (lineCount == 2){
		const position = line.split(" ")
		playerPosition.y = Number(position[0]) - 1;
		playerPosition.x = Number(position[1]) - 1;
		playerVisitInfo[playerPosition.y][playerPosition.x] = true;
	} else {
		const boardGameY = lineCount - 3;
		boardGameInfo.push([])
		const moveInfos = line.split(" ")
		for(let j = 0; j < moveInfos.length; j++){
			const moveInfo = moveInfos[j]
			const moveAmount = Number(moveInfo.slice(0,-1));
            // this was very important. I initially that of using moveInfo[0]. But that is not correct!
            // there can be numbers that are more than 1 digit. So we need to use slice
			const moveDirection = moveInfo.slice(-1);
            // slice(-1) means the last character!
			boardGameInfo[boardGameY].push({
				moveAmount,
				moveDirection
			})
		}

	}
	lineCount++;
	// if(lineCount === sideLength + 3){
	// 	rl.close();
	// }
});

rl.on('close', () => {
	let goormScore = 1;
	let playerScore = 1;
	let isGoormGameOver = false;
	let isPlayerGameOver = false;
	
	while(!isGoormGameOver){
		const command = boardGameInfo[goormPosition.y][goormPosition.x]
		const moveDirection = command.moveDirection;
		const moveAmount = command.moveAmount;
		for(let i = 0; i < moveAmount; i++){
			if(moveDirection === "L"){
				goormPosition.x = goormPosition.x - 1;
			} else if (moveDirection === "R"){
				goormPosition.x = goormPosition.x + 1;
			} else if (moveDirection === "U"){
				goormPosition.y = goormPosition.y - 1;
			} else if (moveDirection === "D"){
				goormPosition.y = goormPosition.y + 1;
			}
			if(goormPosition.x < 0){
				goormPosition.x = sideLength - 1;
			} else if (goormPosition.x > sideLength - 1){
				goormPosition.x = 0;
			}
				
			if(goormPosition.y < 0){
				goormPosition.y = sideLength -1;
			} else if (goormPosition.y > sideLength - 1){
				goormPosition.y = 0;
			}

			if(goormVisitInfo[goormPosition.y][goormPosition.x]){
				isGoormGameOver = true;
				break;
			} else {
				goormVisitInfo[goormPosition.y][goormPosition.x] = true
				goormScore = goormScore + 1;
			}
		}
		
		while(!isPlayerGameOver){
			const command = boardGameInfo[playerPosition.y][playerPosition.x]
			const moveDirection = command.moveDirection;
			const moveAmount = command.moveAmount;
			for(let i = 0; i < moveAmount; i++){
				if(moveDirection === "L"){
					playerPosition.x = playerPosition.x - 1;
				} else if (moveDirection === "R"){
					playerPosition.x = playerPosition.x + 1;
				} else if (moveDirection === "U"){
					playerPosition.y = playerPosition.y - 1;
				} else if (moveDirection === "D"){
					playerPosition.y = playerPosition.y + 1;
				}
				if(playerPosition.x < 0){
					playerPosition.x = sideLength - 1;
				} else if (playerPosition.x > sideLength - 1){
					playerPosition.x = 0;
				}

				if(playerPosition.y < 0){
					playerPosition.y = sideLength -1;
				} else if (playerPosition.y > sideLength - 1){
					playerPosition.y = 0;
				}

				if(playerVisitInfo[playerPosition.y][playerPosition.x]){
					isPlayerGameOver = true;
					break;
				} else {
					playerVisitInfo[playerPosition.y][playerPosition.x] = true
					playerScore = playerScore + 1;
				}
			}
		}
	}

	
	
	if(goormScore > playerScore){
		console.log(`goorm ${goormScore}`)
	} else {
		console.log(`player ${playerScore}`)
	}
})


// test case examples
/**
3
1 1
3 3
1L 2L 1D
2U 3R 1D
2R 2R 1U
*/

// answer: goorm 4

/**
4
4 2
2 4
1L 3D 3L 1U
2D 2L 4U 1U
2D 2L 4U 3L
4D 4D 1R 4R
*/

// answer: player 6


/**
3	
11
1 1
2 2
10R 1U 1U 1U 1U 1U 1U 1U 1U 1U 10D
1U 1U 1U 1U 1U 1U 1U 1U 1U 1U 1U
1U 1U 1U 1U 1U 1U 1U 1U 1U 1U 1U
1U 1U 1U 1U 1U 1U 1U 1U 1U 1U 1U
1U 1U 1U 1U 1U 1U 1U 1U 1U 1U 1U
1U 1U 1U 1U 1U 1U 1U 1U 1U 1U 1U
1U 1U 1U 1U 1U 1U 1U 1U 1U 1U 1U
1U 1U 1U 1U 1U 1U 1U 1U 1U 1U 1U
1U 1U 1U 1U 1U 1U 1U 1U 1U 1U 1U
1U 1U 1U 1U 1U 1U 1U 1U 1U 1U 1U
1U 1U 1U 1U 1U 1U 1U 1U 1U 1U 1D
 */

// answer: goorm 21