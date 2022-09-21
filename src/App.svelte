<script>
  import Card from "./routes/Card.svelte";
  import Nav from "./routes/Nav.svelte";
  import Hero from "./routes/Hero.svelte";
  import About from "./routes/About.svelte";
  import Projects from "./routes/Projects.svelte";
  import Contact from "./routes/Contact.svelte";
  </script>
  <Nav
  item1="Home"
  item2="About"
  item3="Projects"
  item4="Contact"
  >
  </Nav>

<Hero
hero_title="Titulo Principal"
></Hero>

<About
about_title="About title"
>
</About>



<style>
 :global(body) {
    display: flex;
    flex-direction: column;
    place-items:normal;
    background-color: transparent !important;
    
	}
</style>