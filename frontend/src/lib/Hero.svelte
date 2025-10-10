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
  background-color: var(--color-bg);
  color: var(--color-text);
  min-height: 100vh;
  transition: background-color 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.hero-body {
  justify-content: center;
}

.title {
  font-family: 'Karla', sans-serif;
  font-size: 48px;
  text-align: center;
  color: var(--color-text);
  margin-bottom: 1rem;
}

.subtitle {
  font-family: 'Inconsolata', monospace;
  text-align: center;
  color: var(--color-accent);
  font-size: 20px;
}

/* Modo oscuro */
  </style>
