// varibales 
let fruits = ["apple,mango, banana"]
console.log(fruits);


const pi = 33.4;
let person = "ricky";
let answer = "i am home ";
console.log(pi,person,answer)


let name = "monkey";
console.log(name )
// data type
let x;
x = 5;
x = "john";
console.log(x)


let p = 5;
let p2 ="monkey";
let p3 = "volvole";
console.log(p,p2,p3)

const persons = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
console.log(persons)

const persones = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
console.log(persones.firstName   +   "is"  +  persones.age   +   "years old.");


// functions 
function  number(p1,p2){
    return p1 +p2 
};
console.log(number(6,3))


const  y = num(6,7);
// const or let is all the same
function num(w,r){

    return w*r

};
console.log(y)


// conditions 
// 

let hour =12;
if ( hour < 18){
    greating = "good bye "
}
console.log (greating)


let hours =19;
if ( hours < 18){
    greating = "good bye ";
}
else{
    greating = "good evening";
}
console.log (greating)


let time =22;
if ( time < 18){
    greating = "good bye ";
}
else if(time <24){
    greating = "good day";
}

else{
    greating = "good evening";
}
console.log (greating)


                //    loops 
// loops{for,
// for in,
// for of,
// while,
// }

// arrays
const fruites = ["Banana", "Orange", "Apple", "Mango" ];

let length = fruites.length;
console.log("the legth is :",length );

const fruite = ["Banana", "Orange", "Apple", "Mango" ];
fruite.push = "lemon";  // adding an element
console.log(fruites)