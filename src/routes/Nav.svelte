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
  }
  .navbar {
    background-color: #fced73;
  }
  
  .navbar-menu{
    background-color: #fced73;
  }


</style>
