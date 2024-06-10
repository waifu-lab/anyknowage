<script lang="ts">
	import { FileText } from 'lucide-svelte'
	import Loading from '$lib/components/loadingcircle.svelte'
	import * as Dialog from '$lib/components/ui/dialog/index.js'
	import axios from 'axios'
	import Markdown from 'svelte-exmarkdown'
	import type { Plugin } from 'svelte-exmarkdown'
	import rehypeHighlight from 'rehype-highlight'
	import 'highlight.js/styles/github.css'

	export let file_id: string | undefined = undefined
	export let avatar: string | undefined = undefined
	export let name: string = 'user'
	export let messages: string[] = []
	export let timestamp: number = Date.now()
	export let context: string | undefined = undefined
	export let ext: string | undefined = undefined
	export let filename: string | undefined = undefined
	export let isloading: boolean = false
	const server_url = JSON.parse(localStorage.getItem('default') as string).server_url

	const plugins: Plugin[] = [
		{
			rehypePlugin: [rehypeHighlight]
		}
	]
	const get_file_text = async () => {
		console.log(file_id)
		try {
			const data = await axios.get(server_url + '/file_text?file_id=' + file_id)
			return data.data.text
		} catch (e) {
			console.error(e)
			throw new Error(`Failed to get file text`)
		}
	}
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
				<Dialog.Root>
					<Dialog.Trigger>
						<div class=" flex items-center space-x-4 rounded-md border p-4">
							<FileText />
							<div class="flex-1 space-y-1">
								<p class="text-sm font-medium leading-none">{filename}</p>
							</div>
						</div></Dialog.Trigger
					>
					<Dialog.Content class="max-h-[100vh] w-[50vw] !max-w-5xl overflow-y-auto">
						{#await get_file_text()}
							<p>Loading...</p>
						{:then text}
							<div class="markdown">
								<Markdown md={text} {plugins} />
							</div>
						{:catch error}
							<p>{error.message}</p>
						{/await}
					</Dialog.Content>
				</Dialog.Root>
			{/if}
			{#if context != undefined}
				{#if new RegExp('(https?://(?:www.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9].[^s]{2,}|www.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9].[^s]{2,}|https?://(?:www.|(?!www))[a-zA-Z0-9]+.[^s]{2,}|www.[a-zA-Z0-9]+.[^s]{2,})').test(context)}
					<a href={context} target="_blank" class="hover:underline">{context}</a>
				{:else}
					<p>{@html context.replace(/\n/g, '<br>')}</p>
				{/if}
			{/if}
			<div class="flex items-center">
				{#if isloading}
					<div class="mr-4">
						<Loading />
					</div>
				{/if}
				{#each messages as message}
					<div class="talkbox_message">{message}</div>
				{/each}
			</div>
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
