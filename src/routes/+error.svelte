<script>
	import { page } from '$app/stores'
</script>

<div>
	{#if $page?.error}
		<div class="mt-4 border-y-2 p-4">
			{#if $page?.status}
				<img src="https://http.cat/{$page?.status}" alt="HTTP status code" />
				<p>Page status: {$page?.status}</p>
			{/if}
			{#if $page?.error?.message}
				<p>Error message: {$page?.error?.message}</p>
			{/if}
		</div>
	{/if}
</div>
