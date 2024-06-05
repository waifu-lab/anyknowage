<script>
	import '../app.pcss'
	import './styles.css'
	import Sidebar from './Sidebar.svelte'
	import { ModeWatcher } from 'mode-watcher'
	import { onMount } from 'svelte'
	import io from '$lib/socketio'
	import { pushlog } from '$lib/log'
	import toast, { Toaster } from 'svelte-french-toast'
	onMount(() => {
		if (localStorage.getItem('default') === null) {
			localStorage.setItem(
				'default',
				JSON.stringify({
					username: 'user',
					avatar: 'https://cdn.discordapp.com/avatars/762484891945664542/a3d0e4d30b78ce30a2ed22b51bf80df4.png?size=1024',
					botavatar:
						'https://cdn.discordapp.com/avatars/762484891945664542/a3d0e4d30b78ce30a2ed22b51bf80df4.png?size=1024'
				})
			)
		}
		if (localStorage.getItem('chat') === null) {
			localStorage.setItem(
				'chat',
				JSON.stringify({
					model: 'gpt-4o',
					maxtoken: 2000,
					openaikey: ''
				})
			)
		}
		const sockst = io.get()
		if (sockst) {
			sockst.on('notify', (notify) => {
				console.log('notify')
				console.log(notify)
				if (notify.level === 'error') {
					toast.error(notify.message, {
						position: 'top-right',
						style: 'background: var(--background); color: var(--foreground);'
					})
				} else {
					toast.success(notify.message, {
						position: 'top-right',
						style: 'background: var(--background); color: var(--foreground);'
					})
				}
			})
			sockst.on('logger', (log) => {
				console.log(log)
				pushlog(log)
			})
		}
	})
</script>

<Toaster />
<div class="app">
	<ModeWatcher />
	<Sidebar />
	<main class="pl-[53px]">
		<slot></slot>
	</main>
</div>

<style>
</style>
