let burger = document.getElementById('burger'),
	 nav    = document.getElementById('main-header-nav')

burger.addEventListener('click', function(e){
	this.classList.toggle('is-open');
	nav.classList.toggle('is-open');
});