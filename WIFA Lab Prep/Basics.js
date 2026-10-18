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

// function double(n) {
//     return n * 2;
// }
// console.log(double(5));


// function add(a,b) {
//     return a+b;
// }
// console.log(add(7,8));

// function isEven(n) {
//     return (n % 2 === 0);
// }
// console.log(isEven(8));

// const square = function (n) {
//     return n**2;
// }
// console.log(square(4));

// const scores = [30,60,80,100,45]
// const result = scores
// .filter(n => n>50)
// .map(n => n * 2)

// console.log(result)
//const prices = [100, 250, 80, 400, 150];
//const result = prices
//.filter (n => n>150)
//.map (n => n/2)
//console.log(result)

// const scores = [45, 70, 85, 30, 90, 60];
// const result = scores
// .filter (n => n>=60)
// .map (n => n + 5);

// console.log(result)
// console.log(scores)

// const runs = [10, 25, 40, 55, 70];
// const result = runs
// .filter (n => n>30)
// .map (n=> n*3)
// console.log(result)
// console.log(runs)

const nums = [4,10,7,12,9]
const result = nums
.filter (n=> n<10)
.map (n=> n*3)
console.log(result);
console.log(nums);