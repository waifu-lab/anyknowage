<script lang="ts">
	import { FileText } from 'lucide-svelte'
	export let avatar: string | undefined = undefined
	export let name: string = 'user'
	export let messages: string[] = []
	export let timestamp: number = Date.now()
	export let context: string | undefined = undefined
	export let ext: string | undefined = undefined
	export let filename: string | undefined = undefined
</script>

<div class="talkbox">
	<div class="talkbox_main">
		<div class="talkbox_header">
			<img src={avatar} alt="avatar" class="talkbox_avatar" />
			<span class="talkbox_name">{name}</span>
			<span class="talkbox_timestamp">{new Date(timestamp).toLocaleTimeString()}</span>
		</div>
		<div class="talkbox_body">
			{#if ext != '.txt' && ext != undefined}
				<div class=" flex items-center space-x-4 rounded-md border p-4">
					<FileText />
					<div class="flex-1 space-y-1">
						<p class="text-sm font-medium leading-none">{filename}</p>
					</div>
				</div>
			{/if}
			{#if context != undefined}
				<p>{@html context.replace(/\n/g, '<br>')}</p>
			{/if}
			{#each messages as message}
				<div class="talkbox_message">{message}</div>
			{/each}
		</div>
	</div>
</div>

<style>
	.talkbox {
		position: relative;
		margin-top: 20px;
	}

	.talkbox_main {
		padding-left: 60px;
	}

	.talkbox_header {
		position: static;
	}

	.talkbox_avatar {
		position: absolute;
		left: 16px;
		width: 40px;
		height: 40px;
		border-radius: 50%;
	}

	.talkbox_name {
		font-size: 1.2rem;
		font-weight: 600;
		margin-left: 20px;
	}

	.talkbox_timestamp {
		font-size: 0.8rem;
		margin-left: 4px;
	}

	.talkbox_body {
		margin-top: 10px;
		margin-left: 20px;
	}

	.talkbox_message {
		border-radius: 10px;
	}
</style>
