<script lang="ts">
	import Table from './file-table.svelte'
	export let data
	const { posts } = data
</script>

<div class="grid h-screen w-full">
	<div class="flex flex-col">
		<header
			class="sticky top-0 z-10 flex h-[57px] items-center gap-1 border-b bg-background px-4"
		>
			<h1 class="text-xl font-semibold">Anyknowledge</h1>
		</header>
		<main class="grid flex-1 gap-4 overflow-auto p-4">
			{#await posts}
				<p>Loading...</p>
			{:then posts}
				<Table filelist={posts}></Table>
			{:catch error}
				<p>{error.message}</p>
			{/await}
			<!-- <Table filelist={}></Table> -->
		</main>
	</div>
</div>
