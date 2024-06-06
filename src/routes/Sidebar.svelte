<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js'
	import { toggleMode } from 'mode-watcher'
	import * as Tooltip from '$lib/components/ui/tooltip/index.js'
	import { Box, Sun, Moon, Settings } from 'lucide-svelte'
	import MainSidebar from '$lib/components/sidebar/main-sidebar.svelte'

	const sidebarNavItems = [
		{
			svg: 'FileUp',
			href: '/',
			Tooltip: 'Upload'
		},
		{
			svg: 'MessageCircleMore',
			href: '/chat',
			Tooltip: 'Chat'
		},
		{
			svg: 'Archive',
			href: '/archive',
			Tooltip: 'Archive'
		},
		{
			svg: 'SquareTerminal',
			href: '/api',
			Tooltip: 'API'
		}
	]
</script>

<aside class="inset-y fixed left-0 z-20 flex h-full flex-col border-r">
	<div class="border-b p-2">
		<Button variant="outline" size="icon" aria-label="Home">
			<Box class="size-5 fill-foreground" />
		</Button>
	</div>
	<MainSidebar items={sidebarNavItems} />
	<nav class="mt-auto grid gap-1 p-2">
		<Tooltip.Root>
			<Tooltip.Trigger asChild let:builder>
				<Button on:click={toggleMode} variant="ghost" size="icon">
					<Sun
						class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
					/>
					<Moon
						class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
					/>
					<span class="sr-only">Toggle theme</span>
				</Button>
			</Tooltip.Trigger>
			<Tooltip.Content side="right" sideOffset={5}>Setting</Tooltip.Content>
		</Tooltip.Root>
		<Tooltip.Root>
			<Tooltip.Trigger asChild let:builder>
				<Button
					href="/setting"
					variant="ghost"
					size="icon"
					class="mt-auto rounded-lg"
					aria-label="Setting"
					builders={[builder]}
				>
					<Settings class="size-5" />
				</Button>
			</Tooltip.Trigger>
			<Tooltip.Content side="right" sideOffset={5}>Setting</Tooltip.Content>
		</Tooltip.Root>
	</nav>
</aside>
