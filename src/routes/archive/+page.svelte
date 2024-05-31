<script lang="ts">
	import Ellipsis from 'lucide-svelte/icons/ellipsis'

	import { Badge } from '$lib/components/ui/badge/index.js'
	import { Button } from '$lib/components/ui/button/index.js'
	import * as Card from '$lib/components/ui/card/index.js'
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu/index.js'
	import * as Table from '$lib/components/ui/table/index.js'
</script>

<div class="grid h-screen w-full">
	<div class="flex flex-col">
		<header
			class="sticky top-0 z-10 flex h-[57px] items-center gap-1 border-b bg-background px-4"
		>
			<h1 class="text-xl font-semibold">Anyknowledge</h1>
		</header>
		<main class="grid flex-1 gap-4 overflow-auto p-4">
			<div class="relative flex h-full min-h-[50vh] flex-col rounded-xl bg-muted/50 p-4">
				<Card.Root>
					<Card.Header>
						<Card.Title>Products</Card.Title>
						<Card.Description>
							Manage your products and view their sales performance.
						</Card.Description>
					</Card.Header>
					<Card.Content>
						<Table.Root>
							<Table.Header>
								<Table.Row>
									<Table.Head>Name</Table.Head>
									<Table.Head>Type</Table.Head>
									<Table.Head class="hidden md:table-cell">Docs</Table.Head>
									<Table.Head class="hidden md:table-cell">Size</Table.Head>
									<Table.Head class="hidden md:table-cell">Created at</Table.Head>
									<Table.Head>
										<span class="sr-only">Actions</span>
									</Table.Head>
								</Table.Row>
							</Table.Header>
							<Table.Body>
								<Table.Row>
									<Table.Cell class="font-medium"
										>Laser Lemonade Machine</Table.Cell
									>
									<Table.Cell>
										<Badge variant="outline">Draft</Badge>
									</Table.Cell>
									<Table.Cell class="hidden md:table-cell">
										<Badge variant="outline">Draft</Badge>
									</Table.Cell>
									<Table.Cell class="hidden md:table-cell">
										2023-07-12 10:42 AM
									</Table.Cell>
									<Table.Cell class="hidden md:table-cell">
										2023-07-12 10:42 AM
									</Table.Cell>
									<Table.Cell>
										<DropdownMenu.Root>
											<DropdownMenu.Trigger asChild let:builder>
												<Button
													aria-haspopup="true"
													size="icon"
													variant="ghost"
													builders={[builder]}
												>
													<Ellipsis class="size-6" />
													<span class="sr-only">Toggle menu</span>
												</Button>
											</DropdownMenu.Trigger>
											<DropdownMenu.Content align="end">
												<DropdownMenu.Item>Download</DropdownMenu.Item>
												<DropdownMenu.Item>Delete</DropdownMenu.Item>
											</DropdownMenu.Content>
										</DropdownMenu.Root>
									</Table.Cell>
								</Table.Row>
							</Table.Body>
						</Table.Root>
					</Card.Content>
					<Card.Footer>
						<div class="text-xs text-muted-foreground">
							Showing <strong>1-10</strong> of <strong>32</strong> products
						</div>
					</Card.Footer>
				</Card.Root>
			</div>
		</main>
	</div>
</div>
