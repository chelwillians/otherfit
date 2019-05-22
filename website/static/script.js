const menuHamburguer = document.querySelector('#menuHamburguer');
const menu = document.querySelector('.menu');

menuHamburguer.onclick = function(){
    menuHamburguer.classList.toggle('ativo');
    menu.classList.toggle('ativo');
}