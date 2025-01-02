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
  
  <style>
    :global(body) {
      display: flex;
      color: white;
      flex-direction: column;
      place-items: normal;
      background-color: white;
    }
  
    :global(body.dark-mode) {
      display: flex;
      color: white;
      flex-direction: column;
      place-items: normal;
      background-color: #0f0e17;
    }
  </style>