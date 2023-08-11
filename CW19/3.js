
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

let username = getUsername()

if(username == ""){
    const username = prompt("type username: ")
    document.cookie = `username=${username}; expires=${getDateString(7)}; path=/`;
}else{
    alert(username)
}
