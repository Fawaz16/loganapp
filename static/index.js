let minidiv = document.querySelector(".minidiv");
let hamburger = document.querySelector(".hamburger");
let closebtn = document.querySelector(".close");
let btext=document.querySelector(".b-text p")
let ctext=document.querySelector(".c-text p")
let avatar=document.querySelector(".avatar")
let jtext=document.querySelector(".j2-text h3")
let ktext=document.querySelector(".shots")
let ytext=document.querySelector(".y-text ")

hamburger.addEventListener("click", () => {
  minidiv.style.transform = "translateX(-0px)";
  if ((minidiv.style.transform = "translateX(-0px)")) {
    hamburger.style.display = "none";
    closebtn.style.display = "block";
    btext.style.display="none"
    ctext.style.display="none"
    avatar.style.display="none"
    jtext.style.display="none"
    ktext.style.display="none"
    ytext.style.display="none"
  }
});
closebtn.addEventListener("click", () => {
  minidiv.style.transform = "translateX(768px)";
  if ((minidiv.style.transform = "translateX(768px)")) {
    hamburger.style.display = "block";
    closebtn.style.display = "none";
    btext.style.display="block"
    ctext.style.display="block"
    avatar.style.display="block"
    jtext.style.display="block"
    ktext.style.display="block"
    ytext.style.display="block"
  }
});

$(".bb-text").owlCarousel({
  margin: 10,
  loop: true,
  autoplay: true,
  autoplayTimeout: 7000,
  autoplayHoverPause: true,
  responsive: {
    0: {
      items: 1,
    },
    650: {
      items: 1,
    },
    
    1000: {
      items: 1,
    },
  },
});




// G// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
} 



$(document).ready(function(){
	$("#imageGallery").imagePopup({
    //overlay: "rgba(0, 100, 0, 0.5)"

    closeButton:{
        src: "images/close.png",
        width: "40px",
        height:"40px"
    },
    imageBorder: "15px solid #ffffff",
    borderRadius: "10px",
    imageWidth: "500px",
    imageHeight: "400px",
    imageCaption: {
        exist: true,
        color: "#ffffff",
        fontSize: "40px"
    },
    open: function(){
        console.log("opened");
    },
    close: function(){
        console.log("closed");
    }
});

});
