let firstName = prompt("enter first name: ")
let lastName = prompt("enter last name: ")
let age = prompt("enter age: ")
let country = prompt("enter country: ")
let city  = prompt("enter city: ")

let profile = {
    "firstName": firstName,
    "lastName": lastName,
    "age": age,
    "country": country,
    "city": city
}

let strProfile = JSON.stringify(profile)

localStorage.setItem('profile', strProfile)

alert(localStorage.getItem('profile'))