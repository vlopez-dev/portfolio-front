<script>
  export let item1, item2, item3, item4;
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
      <a role="button" class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
      >
        <span aria-hidden="true" />
        <span aria-hidden="true" />
        <span aria-hidden="true" />
      </a>
    </div>
    <div class="navbar-menu ">
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

  nav.stroke ul li a,
  nav.fill ul li a {
    position: relative;
  }
  nav.stroke ul li a:after,
  nav.fill ul li a:after {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    width: 0%;
    content: ".";
    color: transparent;
    background: #aaa;
    height: 1px;
  }
  nav.stroke ul li a:hover:after {
    width: 100%;
  }

  nav.fill ul li a {
    transition: all 2s;
  }

  nav.fill ul li a:after {
    text-align: left;
    content: ".";
    margin: 0;
    opacity: 0;
  }
  nav.fill ul li a:hover {
    color: #fff;
    z-index: 1;
  }
  nav.fill ul li a:hover:after {
    z-index: -10;
    animation: fill 1s forwards;
    -webkit-animation: fill 1s forwards;
    -moz-animation: fill 1s forwards;
    opacity: 1;
  }
</style>
