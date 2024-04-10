<script>
    import { goto } from '$app/navigation';

    let is_modifier_key_held = false;

    export function handleKeydown(event) {
        if (event.key === 'Meta' || event.key === 'Control' || event.key === 'Alt' || event.key === 'Shift') {
            is_modifier_key_held = true;
        }

        if (is_modifier_key_held) return;

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

    export function handleKeyup(event) {
        if (event.key === 'Meta' || event.key === 'Control' || event.key === 'Alt' || event.key === 'Shift') {
            is_modifier_key_held = false;
        }
    }
</script>

<svelte:window on:keydown={handleKeydown} on:keyup={handleKeyup} />