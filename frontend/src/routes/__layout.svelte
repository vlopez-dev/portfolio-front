<script>
    import Nav from "./Nav.svelte";
    import Footer from "./Footer.svelte";
  </script>
  
  <Nav
    item1="Home"
    item2="About"
    item3="Projects"
    item4="Contact"
  />
  
  <slot />
  
  <Footer />
  
<!-- Este archivo puede no estar en uso - los estilos están en +layout.svelte -->
