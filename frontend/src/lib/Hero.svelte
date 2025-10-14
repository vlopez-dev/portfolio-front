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
  <div class="bg-pattern" aria-hidden="true"></div>
  <div class="hero-body">
    <div class="columns mx-2 my-6 ">
      <div class="column is-full">
        
  {#key index}
	<p class="title custom-text title-accent" transition:slide><span class="title-text">{greetings[index]}!</span></p>
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
  position: relative;
  overflow: hidden;
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

.bg-pattern {
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0.06;
  background-image: radial-gradient(circle at 1px 1px, var(--color-text) 1px, transparent 1.5px);
  background-size: 18px 18px;
  mix-blend-mode: multiply;
}

.title-accent {
  display: block;
  text-align: center;
  margin-bottom: 28px; /* más espacio entre el subrayado y el subtítulo */
}

.title-text {
  position: relative;
  display: inline-block;
  padding-bottom: 8px; /* reserva espacio para el subrayado */
}

.title-text::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: 0;
  transform: translateX(-50%);
  width: 0%;
  height: 3px;
  background: var(--color-accent);
  border-radius: 999px;
  transition: width 600ms cubic-bezier(0.4, 0, 0.2, 1);
}

.title-text:hover::after {
  width: 60%;
}


@media (prefers-reduced-motion: reduce) {
  .title-text::after { transition: none; }
  .bg-pattern { opacity: 0.04; }
}
  </style>
