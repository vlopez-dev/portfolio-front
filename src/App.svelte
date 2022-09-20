<script>
  import Card from "./Card.svelte";
  import Nav from "./Nav.svelte";
  import Hero from "./Hero.svelte";
  import About from "./About.svelte";
  import Projects from "./Projects.svelte";
  import Contact from "./Contact.svelte";

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

  <About
  src="../src/aiony-haust-3TLl_97HNJo-unsplash.jpg"
  about_title="Titulo 1"
  about_description="Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "
  >
   
  </About>

<Projects>

</Projects>
<Contact>
  
</Contact>
<style>
 :global(body) {
    display: flex;
    flex-direction: column;
    place-items:normal;
    background-color: transparent !important;
    
	}
</style>