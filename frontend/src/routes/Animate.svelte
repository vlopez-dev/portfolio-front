<script>
    import {slide} from 'svelte/transition'
</script>

<div transition:slide={{ delay: 150 }}>
    <slot />
</div>