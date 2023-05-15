let loupeBtn=document.querySelector('.box6')
let closeBTN=document.querySelector('#closeBtn')
let sectionSearchBar=document.querySelector('.searchBar')
let isBtnLoupeOpen=false;

function searchOpen(){
    sectionSearchBar.style.display="flex"
}

function searchClose(){
    sectionSearchBar.style.display="none"
}

loupeBtn.addEventListener("click",searchOpen)
closeBTN.addEventListener("click",searchClose)

console.log(loupeBtn)


let partsBarShow=document.querySelector('.partsBar')
let partsMenu=document.querySelector('.menuBarParts')
let isPartsMoseOver=false

partsMenu.onmouseenter = function() {
partsBarShow.style.display = "flex";
}

partsBarShow.onmouseleave = function() {
partsBarShow.style.display = "none";
}


  

let aboutBarShow=document.querySelector('.aboutBar')
let aboutMenu=document.querySelector('.menuBarAbout')


aboutMenu.onmouseenter = function() {
    aboutBarShow.style.display = "flex";
}

aboutBarShow.onmouseleave = function() {
aboutBarShow.style.display = "none";
}
