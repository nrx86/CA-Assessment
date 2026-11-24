// 1. What are variables
var number1 = 34;
var number2 = 86;
// console.log(number1+number2);

// 2. Data Types in JavaScript
//Numbers
var num1 = 18;
var num2 = 45.07;
//Strings
var str1 = "This is a string";
var str1 = 'This is also a string';

//Objects
var marks = {
    shivam: 56,
    atul: 87,
    nik: 100
}

//Booleans
var a = true;
var b = false;
// console.log(a,b)

//Undefined and null
var und = undefined;
// console.log(und);

var n = null;
// console.log(n);

//Arrays
var arr=[1,2,3,4,5]
// console.log(arr)

//Operators in JavaScript
//Arithmetic OPerators
var a = 34;
var b = 86;
// console.log("The value of a+b is: ", a+b);
// console.log("The value of a-b is: ", a-b);
// console.log("The value of a*b is: ", a*b);
// console.log("The value of a/b is: ", a/b);

//Assignment Operators
var c = b;
c +=2;
// c -=2;
// c *=2;
// c /=2;
//console.log(c);

//Comparison Operators
var x = 18
var y = 45
// console.log(x==y);
// console.log(x>=y);
// console.log(x<=y);
// console.log(x>y);
// console.log(x<y);

//Logical Operators
//Logical AND
// console.log(true && true)
// console.log(true && false)
// console.log(false && true)
// console.log(false && false)

//Logical OR
// console.log(true || true)
// console.log(true || false)
// console.log(false || true)
// console.log(false || false)

//Logical NOT
// console.log(!false);
// console.log(!true);

//Functions in JavaScript
function avg(a,b) {
    return (a+b)/2;
}
//DRY = Do not repeat yourself
c1=avg(4,6);
c2=avg(86,18);
// console.log(c1, c2);

//Conditionals in JavaScript
/*
var age = 19;
//Single if statement
// if (age > 18) {
//      console.log("You can drink rasna water");
// }
// If-Else Statement
// if (age > 18) {
//     console.log("You can drink rasna water");
// }
// else {
//     console.log("You can not drink rasna water");
// } 

//If-Else Ladder
if (age>32) {
    console.log("You are not a kid");
}
else if (age>26) {
    console.log("Bachhe nahi rahe");
} 
else if (age>22) {
    console.log("Yes, Bachhe nahi rahe");
} 
else if (age>18) {
    console.log("18 Bachhe nahi rahe");
} 
else {
    console.log("Bachhe rahe");
}
console.log("End of ladder")
*/

//Loops in JavaScript
var arr = [1,2,3,4,5,6,7]
// console.log(arr);
// for(var i =0; i<arr.length;i++){
//     if(i==2){
//         // break;
//         continue;
//     }
//     console.log(arr[i])
// }

// arr.forEach(function(element) {
//     console.log(element);
// })

// const xy = 0;
// xy++;
// xy = xy + 1;

let j = 0;
// while(j<arr.length){
//     console.log(arr[j]);
//     j++;
// }

//Arrays
let myArr =["Fan", "Camera", 43, null, true]
// console.log(myArr.length); #Array ki length batayega
// myArr.pop(); //last element Hatata hai array se
// myArr.push("Nikhil"); #last me push karega
// myArr.shift(); #array ke 1st element ko hatayega
// const newLen = myArr.unshift("Nikhil") # Nikhil ko as a first element treat karega
// console.log(newLen); #New Length print karega
// console.log(myArr); //Array k andar k elements print karvayega

//String Methods in JavaScript
let myLovelyString = "Nikhil is a better cricketer and a better student";
// console.log(myLovelyString.length)
// console.log(myLovelyString.indexOf("better"))
// console.log(myLovelyString.lastIndexOf("better"))
// console.log(myLovelyString.slice(1,4))
// console.log(myLovelyString.replace("student", "batter"))

