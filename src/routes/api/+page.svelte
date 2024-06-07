<script lang="ts">
	import { get_logs } from '$lib/log'
	import io from '$lib/socketio'
	import { message } from 'sveltekit-superforms'
	const sockst = io.get()

	let logs = get_logs()
	if (sockst) {
		sockst.on('logger', () => {
			logs = get_logs()
		})
	}
</script>

<div class="grid h-screen w-full">
	<div class="flex flex-col">
		<header
			class="sticky top-0 z-10 flex h-[57px] items-center gap-1 border-b bg-background px-4"
		>
			<h1 class="text-xl font-semibold">Anyknowledge</h1>
		</header>
		<main class="flex-1 overflow-auto p-4">
			{#each logs as log}
				{#if log.message.split('|')[1].trim() == 'INFO'}
					<span>{log.message.split('|')[0]}</span>
					<span class="text-green-500">{log.message.split('|')[1]}</span>
					<span>{log.message.split('|')[2]}</span>
					<br />
				{:else if log.message.split('|')[1].trim() == 'WARNING'}
					<span>{log.message.split('|')[0]}</span>
					<span class="text-orange-500">{log.message.split('|')[1]}</span>
					<span>{log.message.split('|')[2]}</span>
					<br />
				{:else if log.message.split('|')[1].trim() == 'ERROR'}
					<span>{log.message.split('|')[0]}</span>
					<span class="text-red-500">{log.message.split('|')[1]}</span>
					<span>{log.message.split('|')[2]}</span>
					<br />
				{:else}
					<p>{log.message}</p>
				{/if}
			{/each}
		</main>
	</div>
</div>
