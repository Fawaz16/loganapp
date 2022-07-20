let minidiv = document.querySelector(".minidiv");
let hamburger = document.querySelector(".hamburger");
let closebtn = document.querySelector(".close");
let btext=document.querySelector(".b-text p")
let ctext=document.querySelector(".c-text p")
let avatar=document.querySelector(".avatar")
let jtext=document.querySelector(".j2-text h3")
let ktext=document.querySelector(".shots")

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
  }
});
closebtn.addEventListener("click", () => {
  minidiv.style.transform = "translateX(-768px)";
  if ((minidiv.style.transform = "translateX(-768px)")) {
    hamburger.style.display = "block";
    closebtn.style.display = "none";
    btext.style.display="block"
    ctext.style.display="block"
    avatar.style.display="block"
    jtext.style.display="block"
    ktext.style.display="block"
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
