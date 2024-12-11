const myList = [1, 2, 3, 2, 3]; 
function UniqueEle(num) {
  return num.length === new Set(num).size;
}
let Unique = UniqueEle(myList);
console.log(Unique); 