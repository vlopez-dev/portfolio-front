<script>
 import { page } from '$app/stores';
 import { currentSection } from '$lib/stores.js';
 import Nav from '$lib/Nav.svelte';
 import Footer from '$lib/Footer.svelte';
 import '../styles.css';
    
 // Mapear rutas a nombres de secciones
 const routeToSection = {
   '/': 'home',
   '/about': 'about', 
   '/projects': 'projects',
   '/contact': 'contact'
 };

// Actualizar la sección actual cuando cambie la ruta
 $: {
   const currentRoute = $page.route?.id || '/';
   const newSection = routeToSection[currentRoute] || 'home';
   currentSection.set(newSection);
 }

</script>
<Nav
item1="Home"
item2="About"
item3="Projects"
item4="Contact"


>
</Nav>


<slot></slot>
<Footer  >

</Footer>


<style>
 :global(body) {
    display: flex;
    color: #2B2D42;
    flex-direction: column;
    place-items: normal;
    background: linear-gradient(180deg, #FFF0F5 0%, #EDE7F6 25%, #E0F7FA 50%, #FFF9C4 100%);
    min-height: 100vh;
    font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    transition: all 0.3s ease;
    margin: 0;
    padding: 0;
  }

  :global(body.dark-mode) {
    display: flex;
    color: #F7F7F7;
    flex-direction: column;
    place-items: normal;
    background: linear-gradient(180deg, #2B2D42 0%, #3E3A4D 25%, #004D40 50%, #5D4037 100%);
    min-height: 100vh;
    margin: 0;
    padding: 0;
  }

  :global(*) {
    box-sizing: border-box;
  }

  :global(::selection) {
    background-color: #FFB6B9;
    color: white;
  }
</style>
