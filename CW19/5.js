function getDateString(daysForward=0) {
    const date = new Date();
    date.setDate(date.getDate() + daysForward);
    return date.toUTCString();
}

function getUsername() {
    let Cookie = document.cookie.replace(
        /(?:(?:^|.*;\s*)username\s*=\s*([^;]*).*$)|^.*$/, "$1"
    );

    return Cookie;
}

function getPassword() {
    let Cookie = document.cookie.replace(
        /(?:(?:^|.*;\s*)password\s*=\s*([^;]*).*$)|^.*$/, "$1"
    );

    return Cookie;
}


function saveUser(){
    let check = document.getElementById("exampleCheck1").checked
    console.log(check)
    if (check){
        let password = document.getElementById("exampleInputPassword1").value
        let username = document.getElementById("exampleInputEmail1").value
        document.cookie = `username=${username}; expires=${getDateString(7)}; path=/`;
        document.cookie = `password=${password}; expires=${getDateString(7)}; path=/`;
    }
}

function getData(){
    if (getUsername() !== ""){
        document.getElementById("exampleInputPassword1").value = getPassword()
        document.getElementById("exampleInputEmail1").value = getUsername()
    }
}

document.addEventListener("DOMContentLoaded", getData);

