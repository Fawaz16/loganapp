let minidiv = document.querySelector(".minidiv");
let hamburger = document.querySelector(".hamburger");
let closebtn = document.querySelector(".close");
let btext=document.querySelector(".b-text p")
let ctext=document.querySelector(".c-text p")
let avatar=document.querySelector(".avatar")

hamburger.addEventListener("click", () => {
  minidiv.style.transform = "translateX(-0px)";
  if ((minidiv.style.transform = "translateX(-0px)")) {
    hamburger.style.display = "none";
    closebtn.style.display = "block";
    btext.style.display="none"
    ctext.style.display="none"
    avatar.style.display="none"
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



// /

var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action)
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}