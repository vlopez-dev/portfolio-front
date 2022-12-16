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
        
        <a class="navbar-item" href="#/">{item1}</a>
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
}

</style>
