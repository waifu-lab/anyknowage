<script lang="ts">
	import { readable } from 'svelte/store'
	import { createTable, Render, Subscribe, createRender } from 'svelte-headless-table'
	import * as Table from '$lib/components/ui/table'
	import Fileaction from './file-table-action.svelte'
	import { addSelectedRows, addSortBy } from 'svelte-headless-table/plugins'
	import { ArrowUpDown } from 'lucide-svelte'
	import { Button } from '$lib/components/ui/button'
	import Clickbox from './file-table-click.svelte'

	type Filetype = {
		fileid: string
		filename: string
		time: Date
		size: number
	}

	export let filelist: Filetype[]

	function formatBytes(bytes: number, decimals = 2) {
		if (!+bytes) return '0 Bytes'

		const k = 1024
		const dm = decimals < 0 ? 0 : decimals
		const sizes = ['Bytes', 'KB', 'MB', 'GB']

		const i = Math.floor(Math.log(bytes) / Math.log(k))

		return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`
	}

	const table = createTable(readable(filelist), {
		sort: addSortBy(),
		select: addSelectedRows()
	})
	const columns = table.createColumns([
		table.column({
			accessor: 'fileid',
			header: (_, { pluginStates }) => {
				const { allPageRowsSelected } = pluginStates.select
				return createRender(Clickbox, {
					checked: allPageRowsSelected
				})
			},
			cell: ({ row }, { pluginStates }) => {
				const { getRowState } = pluginStates.select
				const { isSelected } = getRowState(row)

				return createRender(Clickbox, {
					checked: isSelected
				})
			}
		}),
		table.column({
			accessor: 'filename',
			header: 'Name'
		}),
		table.column({
			accessor: 'time',
			header: 'Time',
			cell: ({ value }) => value.toLocaleString()
		}),
		table.column({
			accessor: 'size',
			header: 'FileSize',
			cell: ({ value }) => formatBytes(value)
		}),
		table.column({
			accessor: ({ fileid }) => fileid,
			header: '',
			cell: ({ value }) => {
				return createRender(Fileaction, { id: value })
			}
		})
	])
	const { headerRows, pageRows, tableAttrs, tableBodyAttrs, pluginStates, rows } =
		table.createViewModel(columns)
	const { selectedDataIds } = pluginStates.select
</script>

<div class="rounded-md border">
	<Table.Root {...$tableAttrs}>
		<Table.Header>
			{#each $headerRows as headerRow}
				<Subscribe rowAttrs={headerRow.attrs()}>
					<Table.Row>
						{#each headerRow.cells as cell (cell.id)}
							<Subscribe
								attrs={cell.attrs()}
								let:attrs
								props={cell.props()}
								let:props
							>
								<Table.Head {...attrs}>
									{#if cell.id === 'filename'}
										<Button variant="ghost" on:click={props.sort.toggle}>
											<Render of={cell.render()} />
											<ArrowUpDown class={'ml-2 h-4 w-4'} />
										</Button>
									{:else if cell.id === 'time'}
										<Button variant="ghost" on:click={props.sort.toggle}>
											<Render of={cell.render()} />
											<ArrowUpDown class={'ml-2 h-4 w-4'} />
										</Button>
									{:else if cell.id === 'size'}
										<Button variant="ghost" on:click={props.sort.toggle}>
											<Render of={cell.render()} />
											<ArrowUpDown class={'ml-2 h-4 w-4'} />
										</Button>
									{:else}
										<Render of={cell.render()} />
									{/if}
								</Table.Head>
							</Subscribe>
						{/each}
					</Table.Row>
				</Subscribe>
			{/each}
		</Table.Header>
		<Table.Body {...$tableBodyAttrs}>
			{#each $pageRows as row (row.id)}
				<Subscribe rowAttrs={row.attrs()} let:rowAttrs>
					<Table.Row {...rowAttrs} data-state={$selectedDataIds[row.id] && 'selected'}>
						{#each row.cells as cell (cell.id)}
							<Subscribe attrs={cell.attrs()} let:attrs>
								<Table.Cell {...attrs}>
									<Render of={cell.render()} />
								</Table.Cell>
							</Subscribe>
						{/each}
					</Table.Row>
				</Subscribe>
			{/each}
		</Table.Body>
	</Table.Root>
</div>
