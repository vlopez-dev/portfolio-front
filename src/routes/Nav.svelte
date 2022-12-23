<script>
  export let item1, item2, item3, item4;
  
window.onload=function(){
  const burgerIcon = document.querySelector('#burger')
  const navMenu =document.querySelector('#nav-links')

  burgerIcon.addEventListener('click', () => {
    navMenu.classList.toggle('is-active');
  });
}
 


</script>

<header>
  <nav class="navbar " role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="https://bulma.io">
        <img
          src="https://bulma.io/images/bulma-logo.png"
          alt="Bulma: a modern CSS framework based on Flexbox"
          width="112"
          height="28"
        />
      </a>
      <a id="burger" role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
        <span aria-hidden="true" />
        <span aria-hidden="true" />
        <span aria-hidden="true" />
      </a>
    </div>
    <div id="nav-links" class="navbar-menu">
      <div class="navbar-start " style="flex-grow: 1; justify-content: center;">
        
        <a class="navbar-item nav-link nav-link-ltr" href="#/">{item1}</a>
       <a class="navbar-item" href="#/about">{item2}</a>

        <a class="navbar-item" href="#/projects">{item3}</a>
        <a class="navbar-item" href="#/contact">{item4}</a>
      
      </div>
    </div>
  </nav>
</header>

<slot />

<style>
  header {
    width: 100%;
  }
  a {
    font-family: "Karla", sans-serif;
    color: #fffffe;
  }
  .navbar {
    background-color: #0f0e17;
  }
  
  .navbar-menu{
    background-color: #0f0e17;
  }
/* 
.navbar-item:hover{
  background-color: #ff8906;
  border-radius: 3px;
  color:#fffffe;
}
.nav.navbar a.active{
  background-color: #ff8906;
}

.navbar-item.is-active{
  background-color: red;
} */





a.navbar-item:focus, a.navbar-item:focus-within, a.navbar-item:hover, a.navbar-item.is-active, .navbar-link:focus, .navbar-link:focus-within, .navbar-link:hover, .navbar-link.is-active{
  background-color: #0f0e17;
}



.nav-link {
  font-weight: bold;
  font-size: 14px;
  text-transform: uppercase;
  text-decoration: none;
  color: #fffffe;
  padding: 20px 0px;
  margin: 0px 20px;
  display: inline-block;
  position: relative;
  opacity: 0.75;
}

.nav-link:hover {
  opacity: 1;
}

.nav-link::before {
  transition: 300ms;
  height: 5px;
  content: "";
  position: absolute;
  background-color: #ff8906;
}

.nav-link-ltr::before {
  width: 0%;
  bottom: 10px;
}

.nav-link-ltr:hover::before {
  width: 100%;
}

.nav-link-fade-up::before {
  width: 100%;
  bottom: 5px;
  opacity: 0;
}

.nav-link-fade-up:hover::before {
  bottom: 10px;
  opacity: 1;
}

.nav-link-grow-up::before {
  height: 0%;
  width: 100%;
  bottom: 0px;
}

.nav-link-grow-up:hover::before {
  height: 5px;
}










</style>
