<script>
    function toggle() {
        window.document.body.classList.toggle('dark-mode')
    }
</script>

<div class="container">
    <button on:click={toggle} class="dark-mode-toggle">
        <span class="sun-icon">☀️</span>
        
        <span class="moon-icon">🌙</span>
    </button>
</div>

<style>
    .container {
        
        width: 60px;

        margin: 0 auto;
    }

    .dark-mode-toggle {
        background-color: transparent;
        border: none;
        cursor: pointer;
        padding: 0;
        position: relative;
    }

    .sun-icon,
    .moon-icon {
        display: inline-block;
        font-size: 1.5rem;
        transition: opacity 0.3s ease, transform 0.3s ease;
        position: absolute;
        top: 0;
        left: 0;
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
    }
</style>
