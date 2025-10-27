<script>
  import { onMount } from 'svelte';
  import DarkModeToggle from './Button.svelte';

  export let item1, item2, item3, item4;
  onMount(() => {
    const burgerIcon = document.querySelector('#burger');
    const navMenu = document.querySelector('#nav-links');
    const navLinks = document.querySelectorAll('.navbar-item');

    burgerIcon.addEventListener('click', () => {
      navMenu.classList.toggle('is-active');
    });

    navLinks.forEach((link) => {
      link.addEventListener('click', () => {
        setTimeout(() => {
          navMenu.classList.remove('is-active');
        }, 500);
      });
    });
  });
</script>

<header>
  <nav class="navbar custom-component" aria-label="main navigation">
    <div class="navbar-brand custom-component">
      <a
        id="burger"
        role="button"
        class="navbar-burger custom-component"
        aria-label="menu"
        aria-expanded="false"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div id="nav-links" class="navbar-menu custom-component">
      <div class="navbar-start custom-component" style="flex-grow: 1; justify-content: center;">
        <a
          class="navbar-item nav-link nav-link-ltr custom-navitem custom-nav-link"
          href="/"
          data-sveltekit-preload-data>{item1}</a
        >
        <a
          class="navbar-item nav-link nav-link-ltr custom-navitem custom-nav-link"
          href="/about"
          data-sveltekit-preload-data>{item2}</a
        >
        <a
          class="navbar-item nav-link nav-link-ltr custom-navitem custom-nav-link"
          href="/projects"
          data-sveltekit-preload-data>{item3}</a
        >
        <a
          class="navbar-item nav-link nav-link-ltr custom-navitem custom-nav-link"
          href="/contact"
          data-sveltekit-preload-data>{item4}</a
        >
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

  .nav-link {
    color: var(--color-text);
    font-size: 16px;
    padding: 20px 0px;
    margin: 0px 20px;
    position: relative;
    opacity: 0.85;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .nav-link:hover {
    opacity: 1;
    color: var(--color-accent);
  }

  .nav-link-ltr::before {
    width: 0%;
    bottom: 10px;
  }

  .nav-link-ltr:hover::before {
    width: 100%;
  }

  .custom-navitem {
    background-color: transparent;
    color: var(--color-text);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .custom-navitem:hover {
    color: var(--color-accent);
  }

  /* Removed duplicated styles - now using CSS variables */

  header {
    width: 100%;
  }

  .navbar {
    background-color: var(--color-bg);
    color: var(--color-text);
    box-shadow: none;
    backdrop-filter: none;
    border-bottom: none;
    position: relative;
    margin-bottom: 0;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .navbar-burger span {
    background-color: var(--color-text);
    transition: all 0.3s ease;
  }

  /* Ensure mobile menu uses theme colors (override Bulma defaults) */
  .navbar-menu {
    background-color: var(--color-bg);
    color: var(--color-text);
    box-shadow: none;
    border-top: 1px solid var(--color-border);
  }
  .navbar-item {
    background-color: transparent;
    color: var(--color-text);
  }
  .navbar-item:hover {
    background-color: color-mix(in srgb, var(--color-accent) 10%, transparent);
    color: var(--color-accent);
  }
  /* Cleaned up duplicate styles */

  .nav-link-ltr::before {
    width: 0%;
    bottom: 8px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    height: 3px;
    content: '';
    position: absolute;
    background-color: var(--color-accent);
    border-radius: 2px;
  }

  .nav-link-ltr:hover::before {
    width: 100%;
  }

  /* Dark mode styles now handled by CSS variables and reactivity */
</style>
