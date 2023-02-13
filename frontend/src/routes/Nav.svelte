<script>

  import { writable } from "svelte/store";
  import DarkModeToggle from './Button.svelte';


  export let item1, item2, item3, item4;
  
  window.onload = function() {
  const burgerIcon = document.querySelector("#burger");
  const navMenu = document.querySelector("#nav-links");
  const navLinks = document.querySelectorAll(".navbar-item");

  burgerIcon.addEventListener("click", () => {
    navMenu.classList.toggle("is-active");
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      setTimeout(() => {
        navMenu.classList.remove("is-active");
      }, 500);
    });
  });
};







</script>


<header>
  <nav class="navbar custom-component  " role="navigation" aria-label="main navigation ">
    <div class="navbar-brand custom-component">
     
      <a id="burger" role="button" class="navbar-burger custom-component" aria-label="menu" aria-expanded="false">
        <span aria-hidden="true" />
        <span aria-hidden="true" />
        <span aria-hidden="true" />
      </a>
    </div>
    <div id="nav-links" class="navbar-menu custom-component">
      <div class="navbar-start custom-component " style="flex-grow: 1; justify-content: center;">
        
        <a class="navbar-item nav-link nav-link-ltr custom-component" href="#/">{item1}</a>
       <a class="navbar-item nav-link nav-link-ltr custom-component " href="#/about">{item2}</a>

        <a class="navbar-item nav-link nav-link-ltr custom-component" href="#/projects">{item3}</a>
        <a class="navbar-item nav-link nav-link-ltr custom-component" href="#/contact">{item4}</a>
      
      </div>
    </div>
    <div class="navbar-end">
      <DarkModeToggle />
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






a.navbar-item:focus, a.navbar-item:focus-within, a.navbar-item:hover, a.navbar-item.is-active, .navbar-link:focus, .navbar-link:focus-within, .navbar-link:hover, .navbar-link.is-active{
  background-color: #0f0e17;
  color: white;
}




.nav-link {
  color: #fffffe;
  font-size: 16px;
  padding: 20px 0px;
  margin: 0px 20px;
  /* display: inline-block; */
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

.custom-component {
        background-color: #FFFFFF;
        color: #1f1235;
    }


:global(body.dark-mode) .custom-component {
        background-color: #0f0e17;
        color: #fffffe;
    }


</style>
