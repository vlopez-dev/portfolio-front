<script>
    import {slide} from 'svelte/transition'
</script>

<div transition:slide={{ delay: 300 }}>
    <slot />
</div>