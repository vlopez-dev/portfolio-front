<script>
 import { page } from '$app/stores';
 import { currentSection } from '$lib/stores.js';
 import Nav from '$lib/Nav.svelte';
 import Footer from '$lib/Footer.svelte';
 import '../styles.css';
 import 'bulma/css/bulma.min.css';
    
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
    color: var(--color-text);
    flex-direction: column;
    place-items: normal;
    background: linear-gradient(180deg, var(--grad-1) 0%, var(--grad-2) 25%, var(--grad-3) 50%, var(--grad-4) 100%);
    min-height: 100vh;
    font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    transition: all 0.3s ease;
    margin: 0;
    padding: 0;
  }

  :global(*) {
    box-sizing: border-box;
  }

  :global(::selection) {
    background-color: var(--color-accent);
    color: white;
  }
</style>
