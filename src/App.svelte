<script>
  import Card from "./routes/Card.svelte";
  import Nav from "./routes/Nav.svelte";
  import Hero from "./routes/Hero.svelte";
  import About from "./routes/About.svelte";
  import Projects from "./routes/Projects.svelte";
  import Contact from "./routes/Contact.svelte";
  import Router from "svelte-spa-router"
  let routes={
    "/":Hero,
    "/about":About,
    "/projects":Projects,
    "/Contact":Contact,

  }
  </script>

<Nav
item1="Home"
item2="About"
item3="Projects"
item4="Contact"
>


</Nav>









  <Router {routes}></Router>
  




<style>
 :global(body) {
    display: flex;
    color: white;
    flex-direction: column;
    place-items:normal;
    background-color: transparent !important;
    
	}
</style>