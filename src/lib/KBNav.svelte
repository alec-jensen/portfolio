<script>
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';

    function handleKeydown(event) {
        if (event.shiftKey || event.ctrlKey || event.altKey || event.metaKey) {
            return;
        }

        if (event.key === 'h') {
            goto('/');
        } else if (event.key === 'a') {
            goto('/about');
        } else if (event.key === 'p') {
            goto('/projects');
        } else if (event.key === 'c') {
            goto('/contact');
        }
    }
</script>

<svelte:window on:keydown={handleKeydown} />