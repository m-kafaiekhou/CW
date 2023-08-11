const input = +prompt("type somthing: ");



if( input >= 0 && input <= 10) {
    alert('child');
}else if( input > 10 && input <= 18) {
    alert('teenager');
}
else if( input > 18 && input <= 30) {
    alert('young person');
}
else if( input > 30) {
    alert('adult');
}
else {
    alert('Age is invalid');
}


