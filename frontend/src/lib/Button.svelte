<script>
  import { onMount } from 'svelte';
  import { SunIcon, MoonIcon } from 'svelte-feather-icons';

  function toggle() {
    if (typeof window !== 'undefined') {
      window.document.body.classList.toggle('dark-mode');
    }
  }

  function setDarkMode() {
    if (typeof window !== 'undefined') {
      const hour = new Date().getHours();
      if (hour >= 20 || hour < 6) {
        // Si es de noche, activar modo oscuro
        window.document.body.classList.add('dark-mode');
      } else {
        // Si es de día, desactivar modo oscuro
        window.document.body.classList.remove('dark-mode');
      }
    }
  }

  onMount(() => {
    setDarkMode(); // Llamar a la función al cargar la página
  });
</script>

<div class="container">
  <button on:click={toggle} class="dark-mode-toggle">
    <span class="sun-icon">
      <SunIcon size="28" />
    </span>

    <span class="moon-icon">
      <MoonIcon size="28" />
    </span>
  </button>
</div>

<style>
  .container {
    width: 60px;
    margin: 0 auto;
  }

  .dark-mode-toggle {
    background-color: transparent;
    outline: none;
    border: none;
    cursor: pointer;
    padding: 0;
    position: relative;
  }

  .moon-icon {
    display: inline-block;
    font-size: 1.5rem;
    transition:
      opacity 0.3s ease,
      transform 0.3s ease;
    position: absolute;
    top: 0;
    left: 20px;
    color: transparent;
  }
  .sun-icon {
    display: inline-block;
    font-size: 1.5rem;
    transition:
      opacity 0.3s ease,
      transform 0.3s ease;
    position: absolute;
    top: 0;
    left: 20px;
    color: black;
  }

  :global(body.dark-mode) .sun-icon {
    opacity: 0;
    transform: scale(0.5);
    background-color: white;
    color: black;
  }

  :global(body.dark-mode) .moon-icon {
    opacity: 1;
    transform: scale(1);
    color: white;
  }
</style>
