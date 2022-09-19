<script>
  import Card from "./Card.svelte";
  import Nav from "./Nav.svelte";
  import Hero from "./Hero.svelte";
  import About from "./lib/About.svelte";
  import Projects from "./Projects.svelte";
  import Contact from "./lib/Contact.svelte";

</script>

  <Nav
  item1="Home"
  item2="About"
  item3="Projects"
  item4="Contact"
  >

  </Nav>

  <Hero
  hero_title="Titulo de Prueba"
  hero_subtitle="Subtitulo de prueba"
  >
  </Hero>

  <About>
   
  </About>

<Projects>

</Projects>
<Contact>
  
</Contact>
<style>
 :global(body) {
    display: flex;
    flex-direction: column;
    place-items:normal
	}
</style>