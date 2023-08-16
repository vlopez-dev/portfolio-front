<script>
  import Nav from "./routes/Nav.svelte";
  import Hero from "./routes/Hero.svelte";
  import About from "./routes/About.svelte";
  import Projects from "./routes/Projects.svelte";
  import Contact from "./routes/Contact.svelte";
  import Router from "svelte-spa-router"
  import Footer from "./routes/Footer.svelte";
    



  var _paq = window._paq = window._paq || [];
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="https://vicuy.matomo.cloud/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '1']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.async=true; g.src='//cdn.matomo.cloud/vicuy.matomo.cloud/matomo.js'; s.parentNode.insertBefore(g,s);
  })();

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




<Router {routes}></Router>
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