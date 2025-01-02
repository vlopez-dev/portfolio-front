<script>
 import Nav from '$lib/Nav.svelte';
 import Footer from '$lib/Footer.svelte';
 import Hero from '$lib/Hero.svelte';
import About from '$lib/About.svelte';
import Projects from '$lib/Projects.svelte';
import Contact from '$lib/Contact.svelte';
    

  let routes={
    
    "/":Hero,
    "/about":About,
    "/projects":Projects,
    "/Contact":Contact,

  }
  let darkMode = false

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
    color: white;
    flex-direction: column;
    place-items:normal;
    background-color: white;
	}
  :global(body.dark-mode) {
    display: flex;
    color: white;
    flex-direction: column;
    place-items:normal;
    background-color: #0f0e17;
	}
  
</style>