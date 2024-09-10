alert('Welcome..')
let side = prompt("Enter side: ")

let area = side * side
console.log(`Luar Persegi dengan sisi ${side} = ${area}`);
console.log('Luar Persegi dengan sisi '+ side + '=' + area);

var nama = 'Kazen'
nama = 'Ahmad'

var nama = 'Salma'
console.log(nama); 

let age = 10
age = 12

// let age = 15 // tidak bisa di deklarasikan ulang
console.log(age);

const pi = 3.14
// pi = 22/7
// tidak bisa diubah dan tidak bisa dideklarasikan ulang
console.log(pi);

let fruits = ['apple', 'banana', 'cherry', 'durian']
console.log(fruits);
console.log(fruits[1]);

let number = 13

if (number % 2 == 0) {
    console.log('Bilangan Genap');
} else {
    console.log('Bilangan Ganjil');
}

number - prompt('Enter number: ')

let mod = number % 2

switch (mod) {
    case 0:
        alert('Bilangan Genap')
        break;
    case 1:
        alert('Bilangan Ganjil')
        break;
       default:
        alert('Hanya Menerima Angka');
        break; 
}

for (let num = 0; num < 10; num++) {
    console.log(num);
}


for (let num in fruits) {
    console.log(fruits[num]);
}

for (let fruit of fruits){
    console.log("I like "+fruit);
}

let angka = 0

while (angka < 10) {
    console.log("Angka : "+angka);
    angka++
}

var animal = "Panda"
console.log(animal);

let hewan = "Singa"
console.log(hewan);

function greeting() {
    console.log("Hello.."+animal);
    console.log(hewan);
    let negara = "Indonesia"
    const g = 9.8
    console.log(negara);
    console.log(g)
}
// console.log(negara); let tidak bisa diakses diluar function
// console.log(g); const tidak bisa diakses diluar function

greeting()
greeting()
greeting()

function sayHello (name) {
    console.log(`Hello ${name}`);
}

sayHello("Budi")
sayHello("Kiki")