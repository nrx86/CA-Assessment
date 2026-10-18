// let runs = 75;
// const player = "Nikhil";

// runs = 90;

// console.log(runs);
// console.log(player);

// let runs = 75;
// let player = "Nikhil";
// let isPlaying = true;

// console.log(typeof runs);
// console.log(typeof player);
// console.log(typeof isPlaying);

// let player = "Nikhil";
// let runs = 75;

// console.log(player + runs);
// console.log(`${player} scored ${runs} runs`);
// console.log("2" + 3);
// console.log(2 + 3);


// const player = "Nikhil";
// let runs = 45;
// runs+=7;
// console.log(typeof runs);

// let result = runs >= 50 ? "Half-century" : "Keep playing"
// console.log(result);

// const player = "Nikhil";
// let runs = 42;
// let isOut = false;

// runs+=8;

// console.log(runs);
// console.log(typeof runs);

// let result = runs >=50 ? "Half-century" : "Keep playing";
// console.log(result);

// console.log(runs === 50);

// console.log(runs >= 50 && !isOut);

// let runs = 67;
// if (runs >=100) {
//     console.log("Century")
// } else if (runs >=50) {
//     console.log("Half-century")
// } else{
//     console.log("Keep practicing")
// }

// for(let i = 1; i<=6; i++) {
//     console.log(i)
// }

// for (let i = 1; i<=10; i++) {
//     if (i === 5) continue;
//     console.log(i);
// }

// for (let i = 1; i<=10; i++) {
//     if (i === 7) break;
//     console.log(i);
// }

// let lives = 3;

// while(lives>0) {
//     console.log("Playing..." + lives);
//     lives = lives - 1;
// }


// for (let i = 1; i<=15; i++) {
//     if (i % 3 === 0 && i % 5 === 0) {
//         console.log("FizzBuzz")
//     } else if (i % 3 === 0) {
//         console.log("Fizz")
//     } else if (i % 5 === 0) {
//         console.log("Buzz")
//     } else{
//         console.log(i)
//     }
// }

// let runs = 1;
// for (let i = 1; i<=10; i++) {
//     if (i % 3 === 0) {
//         console.log("Three")
//     } else if ( i % 2 === 0) {
//         console.log("Even")
//     } else {
//         console.log (i)
//     }
// }

// let n = 1;
// while (n<=10) {
//     if (n===6) break; 
//         console.log(n);
//         n++;
// }

// for (let i=1; i<=10; i++) {
//     if (i % 2 === 0) continue;
//     console.log(i)
// }

// for (let i = 1; i<=20; i++) {
//     if (i === 15) break;
//     else if (i % 3 === 0) {
//         console.log("Fizz")
//     } else if (i % 5 === 0) {
//         console.log("Buzz")
//     } else {
//         console.log(i)
//     }
// }

// for (let i = 10; i <= 20; i++) {
//     if (i === 13) continue;
//     else if (i % 2 === 0) {
//         console.log("Even")
//     } else if ( i % 3 === 0) {
//         console.log("Three")
//     } else{
//         console.log(i)
//     }
// }

function double(n) {
    return n * 2;
}
console.log(double(5));
