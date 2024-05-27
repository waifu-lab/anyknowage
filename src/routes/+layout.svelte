<script>
	import '../app.pcss'
	import './styles.css'
	import Sidebar from './Sidebar.svelte'
	import { ModeWatcher } from 'mode-watcher'
</script>

<div class="app">
	<!-- <Header></Header> -->
	<ModeWatcher />
	<Sidebar />
	<main class="pl-[53px]">
		<slot></slot>
	</main>
</div>

<style>
</style>
