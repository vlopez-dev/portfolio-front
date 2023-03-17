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
<section class="hero is-fullheight custom-component">
    <div class="hero-body">
    <div class="columns mx-2 my-6 ">
      <div class="column">
        
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
   
    .hero-body{
        justify-content: center;
    }
    .title{
      font-family: 'Karla', sans-serif;
      font-size: 80px;
    }
    .subtitle{
      font-family: 'Inconsolata', monospace;
        }

    .title{
      text-align: center;
      color: #fffffe;
    }
    





/* Componentes colors darkmode */
    .custom-component {
        background-color: #fffffe;
    }

:global(body.dark-mode) .custom-component {
        background-color: #0f0e17;
        color: #FFFFFF;
    }

/* Principal text  darkmode */
.custom-text {
        color: #1f1235;
}

:global(body.dark-mode) .custom-text {
        color: #FFFFFF;
}





/* subtitle  darkmode */
.custom-text-color{
color: #ff6e6c;

text-shadow: none;
text-align: center;
}
:global(body.dark-mode) .custom-text-color {
        color: #FFFFFF;
        text-shadow: 1px 1px 2px rgba(255, 146, 26, 0.8), 0 0 1em rgba(255, 146, 26, 0.8), 0 0 0.2em rgba(255, 146, 26, 0.8);
        text-align: center;

}
    
  </style>