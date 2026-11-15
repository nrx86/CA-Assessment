// let studentName: string = "Nikhil";
// let marks: number = 86;
// let passed: boolean = true;
// let subjectMarks: number[] = [86, 90, 78];

// let college = "SGT University";

// // Add another mark
// subjectMarks.push(95);

// // Print all variables
// console.log("Student Name:", studentName);
// console.log("Marks:", marks);
// console.log("Passed:", passed);
// console.log("Subject Marks:", subjectMarks);
// console.log("College:", college);

// const input= document.getElementById("noteInput")
// const addBtn= document.getElementById("addBtn")
// const clearBtn= document.getElementById("clearBtn")
// const count= document.getElementById("count")
// const list= document.getElementById("list")

// const items = document.querySelectorAll(".item")
// items.forEach(item => {
//   console.log(item.textContent)
// });
// const title = document.getElementById("title");
// title.style.color="crimson";
// title.style.backgroundColor="black";

// const title = document.getElementById("title");
// title.classList.add("highlight"); 

const academyTitle = document.getElementById("academyTitle");
academyTitle.textContent="NR86 Cricket Academy";

academyTitle.setAttribute("data-sport", "cricket")

const playerList=document.getElementById("playerList")
playerList.classList.add("squad");

const joinBtn=document.getElementById("joinBtn")
joinBtn.textContent="Register Now";

joinBtn.classList.add("primary");

joinBtn.style.backgroundColor="blue";

const firstPlayer = document.querySelector(".player");
firstPlayer.textContent="Virat Kohli - Captain";

const matchStatus=document.getElementById("matchStatus");
matchStatus.textContent="Match Day Ready";

matchStatus.style.color="green";

const allPlayers = document.querySelectorAll(".player");
allPlayers.forEach(item => {
  item.classList.add("selected")
});


