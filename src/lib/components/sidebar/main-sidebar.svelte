<script lang="ts">
	import { cubicInOut } from 'svelte/easing'
	import { crossfade } from 'svelte/transition'
	import { cn } from '$lib/utils.js'
	import { page } from '$app/stores'
	import { Button } from '$lib/components/ui/button/index.js'
	import * as Tooltip from '$lib/components/ui/tooltip/index.js'
	import { FileUp, Archive, MessageCircleMore, SquareTerminal } from 'lucide-svelte'

	let className: string | undefined | null = undefined
	export let items: { href: string; svg: string; Tooltip: string }[]
	export { className as class }

	const [send, receive] = crossfade({
		duration: 250,
		easing: cubicInOut
	})
</script>

<nav class={cn('grid gap-1 p-2', className)}>
	{#each items as item}
		{@const isActive = $page.url.pathname === item.href}
		<Tooltip.Root>
			<Tooltip.Trigger asChild let:builder>
				<Button
					href={item.href}
					variant="ghost"
					size="icon"
					class={cn('relative rounded-lg')}
					aria-label="Talk"
					builders={[builder]}
				>
					{#if isActive}
						<div
							class="absolute inset-0 flex items-center justify-center rounded-md bg-muted"
							in:send={{ key: 'active-sidebar-tab' }}
							out:receive={{ key: 'active-sidebar-tab' }}
						></div>
					{/if}
					<div class="relative">
						<!-- IDK -->
						{#if item.svg === 'Archive'}
							<Archive class="size-5" />
						{:else if item.svg === 'SquareTerminal'}
							<SquareTerminal class="size-5" />
						{:else if item.svg === 'MessageCircleMore'}
							<MessageCircleMore class="size-5" />
						{:else if item.svg === 'FileUp'}
							<FileUp class="size-5" />
						{/if}
					</div>
				</Button>
			</Tooltip.Trigger>
			<Tooltip.Content side="right" sideOffset={5}>{item.Tooltip}</Tooltip.Content>
		</Tooltip.Root>
	{/each}
</nav>
