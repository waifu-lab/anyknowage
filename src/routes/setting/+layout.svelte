<script lang="ts">
	import SidebarNav from '$lib/components/sidebar/setting-sidebar.svelte'
	import { Separator } from '$lib/components/ui/separator'

	const sidebarNavItems = [
		{
			title: 'Default',
			href: '/setting'
		},
		{
			title: 'Chat',
			href: '/setting/chat'
		},
		{
			title: 'plugin',
			href: '/setting/plugin'
		},
		{
			title: 'About',
			href: '/setting/about'
		}
	]
</script>

<div class="block w-full space-y-6 p-10">
	<div class="space-y-0.5">
		<h2 class="text-2xl font-bold tracking-tight">Settings</h2>
		<p class="text-muted-foreground">Anyknowledge settings</p>
	</div>
	<Separator class="my-6" />
	<div class="flex flex-col space-y-8 lg:flex-row lg:space-x-12 lg:space-y-0">
		<aside class="-mx-4 lg:w-1/5">
			<SidebarNav items={sidebarNavItems} />
		</aside>
		<div class="flex-1 lg:max-w-2xl">
			<slot></slot>
		</div>
	</div>
</div>
