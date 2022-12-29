<script>


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
<section class="hero is-fullheight">
    <div class="hero-body">
    <div class="columns ">
      <div class="column">
        
  {#key index}
	<p class="title"transition:slide>{greetings[index]}!</p>
  {/key}
        <p class="subtitle">
         Back-end developer
        </p>
      </div>
   
    </div>
  </div>

  </section>
</Animate>
  <style>
   .hero{
    background-color: #0f0e17;
   }
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
    .subtitle{
      text-align: center;
      color: #fffffe;
    }
  </style>