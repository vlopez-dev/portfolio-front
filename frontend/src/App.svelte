<script>
  import Nav from "./routes/Nav.svelte";
  import Hero from "./routes/Hero.svelte";
  import About from "./routes/About.svelte";
  import Projects from "./routes/Projects.svelte";
  import Contact from "./routes/Contact.svelte";
  import Router from "svelte-spa-router"
  import Footer from "./routes/Footer.svelte";
  import Button from "./routes/Button.svelte";
  let routes={
    "/":Hero,
    "/about":About,
    "/projects":Projects,
    "/Contact":Contact,

  }
  </script>



<Button>
	Toggle
</Button>

<Nav
item1="Home"
item2="About"
item3="Projects"
item4="Contact"
>
</Nav>

<Router {routes}></Router>
<Footer>

</Footer>


<style>
 :global(body) {
    display: flex;
    color: white;
    flex-direction: column;
    place-items:normal;
    background-color: #0f0e17 !important;
    
	}

  :global(body.dark-mode ) {
		background-color: white !important;
		color: #bfc2c7;
	}
  :global(footer.dark-mode ) {
		background-color: white !important;
		color: #bfc2c7;
	}
  :global(.nav-links.dark-mode ) {
		background-color: white !important;
		color: #bfc2c7;
	}
  
</style>