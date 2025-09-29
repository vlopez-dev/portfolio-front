<script>
import DarkModeToggle from './Button.svelte';

import { onMount, onDestroy } from 'svelte';
	import { slide } from 'svelte/transition';

	let greetings = ['Hello my name is Victor','Hola mi nombre es Victor','Oi meu nome é Victor'];
	let index = 0;
	let roller;

	onMount(() => {
		roller = setInterval(() => {
			if (index === greetings.length - 1) index = 0;
			else index++;
		}, 3000);
	});

	onDestroy(() => {
		clearInterval(roller);
	});
  import Animate from './Animate.svelte';


</script>
<Animate>
<section class="hero is-fullheight hero-section">
    <div class="hero-body">
    <div class="columns mx-2 my-6 ">
      <div class="column is-full">
        
  {#key index}
	<p class="title custom-text"transition:slide>{greetings[index]}!</p>
  {/key}
        <p class="subtitle custom-text-color ">
         Back-end developer
        </p>
      </div>
   
    </div>
  </div>

  </section>
</Animate>
  <style>
   .hero-section {
  background-color: #FFF0F5;
  color: #2B2D42;
}

.hero-body {
  justify-content: center;
}

.title {
  font-family: 'Karla', sans-serif;
  font-size: 48px;
  text-align: center;
  color: #2B2D42;
}

.subtitle {
  font-family: 'Inconsolata', monospace;
  text-align: center;
  color: #FFB6B9;
}

/* Modo oscuro */
:global(body.dark-mode) .hero-section {
  background-color: #2B2D42;
  color: #F7F7F7;
}

:global(body.dark-mode) .title {
  color: #F7F7F7;
}

:global(body.dark-mode) .subtitle {
  color: #FFB6B9;
  text-shadow: 1px 1px 2px rgba(255, 182, 185, 0.6), 0 0 1em rgba(255, 182, 185, 0.6);
}


    
  </style>