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
