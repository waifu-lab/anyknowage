<script lang="ts">
	import { Ellipsis } from 'lucide-svelte'
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu'
	import { Button } from '$lib/components/ui/button'
	import { mode } from 'mode-watcher'

	export let id: string
</script>

<DropdownMenu.Root>
	<DropdownMenu.Trigger asChild let:builder>
		<Button variant="ghost" builders={[builder]} size="icon" class="relative h-8 w-8 p-0">
			<span class="sr-only">Open menu</span>
			<Ellipsis class="h-4 w-4" />
		</Button>
	</DropdownMenu.Trigger>
	<DropdownMenu.Content>
		<DropdownMenu.Group>
			<DropdownMenu.Label>Actions</DropdownMenu.Label>
			{#if $mode === 'light'}
				<DropdownMenu.Item class=" bg-red-300 hover:bg-red-400" on:click={() => {}}
					>Delete File</DropdownMenu.Item
				>
			{:else if $mode === 'dark'}
				<DropdownMenu.Item class=" bg-red-500 hover:bg-red-600" on:click={() => {}}
					>Delete File</DropdownMenu.Item
				>
			{/if}
		</DropdownMenu.Group>
	</DropdownMenu.Content>
</DropdownMenu.Root>
