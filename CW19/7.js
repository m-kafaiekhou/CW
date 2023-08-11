
const student = {
  firstName: 'mahdi',
  lastName: 'kafaie',
  age: 20,
  skills: ['Python', 'Javascript', 'C++'],
  country: 'Iran',
  enrolled: {
    math: true,
    science: true,
    history: false
  }
};

localStorage.setItem('student', JSON.stringify(student));

const storedStudent = JSON.parse(localStorage.getItem('student'));

alert(JSON.stringify(storedStudent));