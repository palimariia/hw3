
var nam = document.getElementById('id_name');
if (nam) {


    nam.addEventListener('input', function() {
        var inputName = this.value;
        var nameShow = document.getElementById('name_show');
        nameShow.innerText = inputName;
    });  
}

document.addEventListener('DOMContentLoaded', function() {
    var nam = document.getElementById('id_name');
    if (nam) {
        var inputName = nam.value;
        var nameShow = document.getElementById('name_show');
        nameShow.innerText = inputName;
    }
});


var bir = document.getElementById('id_birth');
if (bir) {
    
    bir.addEventListener('input', function() {
    var inputBirth = this.value;
    var birthShow = document.getElementById('birth_show');
    birthShow.innerText = inputBirth;
    });  
}

var about = document.getElementById('id_inf');
if (about) {
    
    about.addEventListener('input', function() {
    var inputInf = this.value;
    var aboutShow = document.getElementById('about_show');
    aboutShow.innerText = inputInf;
    });  
}

const nameInput = document.getElementById('id_name');
const nameErrorSpan = document.querySelector('.error');


nameInput.addEventListener('input', function() {

  const name = this.value;

  if (!/^[\u0400-\u04FF\s]+$/.test(name)) {
    this.classList.add('error-input');
    nameErrorSpan.classList.add('error-displayed');
  } else {
    this.classList.remove('error-input');
    nameErrorSpan.classList.remove('error-displayed');
  }
});

nameInput.addEventListener('focus', function() {
  this.classList.remove('error-input');
  nameErrorSpan.classList.remove('error-displayed');
});

const telegramInput = document.getElementById('id_telegram');
const telegramErrorSpan = document.querySelectorAll('.error'); 

telegramInput.addEventListener('input', function() {
  const username = this.value;

  if (!/^@[a-zA-Z]+$/.test(username)) {
    this.classList.add('error-input');
    telegramErrorSpan[0].classList.remove('hidden');
  } else {
    this.classList.remove('error-input');
    telegramErrorSpan[0].classList.add('hidden');
  }
});

telegramInput.addEventListener('focus', function() {
  this.classList.remove('error-input');
  telegramErrorSpan[0].classList.add('hidden');
});

const phoneInput = document.getElementById('id_phone');
const phoneErrorSpan = document.querySelector('#phone + .error');

phoneInput.addEventListener('input', function() {
  const phoneNumber = phoneInput.value;

  if (!/^[0-9+]+$/.test(phoneNumber)) {
    phoneInput.classList.add('error-input');
    phoneErrorSpan.forEach(errorSpan => errorSpan.classList.remove('hidden'));
  } else {
    phoneInput.classList.remove('error-input');
    phoneErrorSpan.forEach(errorSpan => errorSpan.classList.add('hidden'));
  }
});

phoneInput.addEventListener('focus', function() {
  this.classList.remove('error-input');
  phoneErrorSpan.classList.add('hidden');
});



const obrazovsSelect = document.myForm.obrazov;
const selection = document.getElementById("selection");
 
function changeOption(){
    const selectedOption = languagesSelect.options[obrazovsSelect.selectedIndex];
    selection.textContent = "Вы выбрали: " + selectedOption.text;
}
 
obrazovsSelect.addEventListener("change", changeOption);

