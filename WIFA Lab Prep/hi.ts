let studentName: string = "Nikhil";
let marks: number = 86;
let passed: boolean = true;
let subjectMarks: number[] = [86, 90, 78];

let college = "SGT University";

// Add another mark
subjectMarks.push(95);

// Print all variables
console.log("Student Name:", studentName);
console.log("Marks:", marks);
console.log("Passed:", passed);
console.log("Subject Marks:", subjectMarks);
console.log("College:", college);

// TypeScript error demonstration
subjectMarks.push("hello");