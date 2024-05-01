<script>
	import '../app.pcss'
	import './styles.css'
	import Sidebar from './Sidebar.svelte'

</script>

<div class="app">
	<!-- <Header></Header> -->

	<Sidebar></Sidebar>
	<main class="pl-[53px]">
		<slot></slot>
	</main>

</div>

<style>
</style>
