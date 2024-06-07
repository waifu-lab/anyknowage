<script lang="ts">
	import { FolderUp, CornerDownLeft, X, Paperclip } from 'lucide-svelte'
	import { Badge } from '$lib/components/ui/badge/index.js'
	import { Button } from '$lib/components/ui/button/index.js'
	import * as Tooltip from '$lib/components/ui/tooltip/index.js'
	import { Textarea } from '$lib/components/ui/textarea/index.js'
	import { Label } from '$lib/components/ui/label/index.js'
	import Talkbox from '$lib/components/talkbox/talkbox.svelte'
	import { tick } from 'svelte'
	import { listen } from '@tauri-apps/api/event'
	import { open } from '@tauri-apps/api/dialog'
	import { readBinaryFile } from '@tauri-apps/api/fs'
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js'

	export let data
	const { posttext, addfile } = data
	let chatTrigger = 0
	let input = ''
	let fileInput: HTMLInputElement
	let chatArea: HTMLElement
	let posts = []
	let file: FileList
	let alertfile = false
	let dropfiles: string[]
	let defauledata = JSON.parse(localStorage.getItem('default') as string)

	const readTextFile = async () => {
		const openfile = await open({
			multiple: false,
			directory: false
		})
		console.log(openfile)
		if (!openfile) return
		const readfile = await readBinaryFile(openfile as string)
		let filename = typeof openfile === 'string' ? openfile.split('/') : ''
		if (filename.length === 1) {
			filename = typeof openfile === 'string' ? openfile.split('\\') : ''
		}
		addfile(readfile, filename.slice(-1) as string)
	}

	let chatPromise = data.posts(chatTrigger)

	$: if (chatPromise) {
		chatPromise.then((value) => {
			posts = value
			scrollToBottom(chatArea)
		})
	}
	$: dropfiles

	const scrollToBottom = async (node: HTMLElement, smooth = false) => {
		if (!node) return
		await tick()
		if (smooth) {
			node.scroll({ top: node.scrollHeight, behavior: 'smooth' })
		} else {
			node.scrollTop = node.scrollHeight
		}
	}

	const postdropfile = () => {
		dropfiles.forEach(async (element) => {
			const readfile = await readBinaryFile(element)
			addfile(readfile, element)
		})
	}

	let fileDropped = false
	listen('tauri://file-drop', async (event) => {
		console.log(event)
		fileDropped = false
		if (!event.payload) return
		alertfile = true
		dropfiles = event.payload as Array<string>
	})
	listen('tauri://file-drop-hover', (event) => {
		if ((event.payload as string[]).length === 0) return
		fileDropped = true
	})
	listen('tauri://file-drop-cancelled', (event) => {
		fileDropped = false
	})
</script>

{#if fileDropped}
	<div
		class="fixed left-1/2 top-1/2 z-50 w-[400px] -translate-x-1/2 -translate-y-1/2 transform rounded-lg border-2 bg-primary bg-opacity-90 p-6"
		id="dropzone"
	>
		<div class="text-center text-background">
			<FolderUp class="mx-auto h-20 w-20" />
			<h3 class="font-mediu mt-2 text-sm">
				<div class="relative cursor-pointer">
					<span>Drag and drop to upload</span>
				</div>
			</h3>
		</div>
	</div>
{/if}

<AlertDialog.Root bind:open={alertfile}>
	<AlertDialog.Content>
		<AlertDialog.Header>
			<AlertDialog.Title>Files</AlertDialog.Title>
			{#if dropfiles}
				{#each dropfiles as file, i (file)}
					<div class="flex items-center gap-2">
						<AlertDialog.Description>{file}</AlertDialog.Description>
						<Button
							variant="outline"
							size="icon"
							on:click={() => {
								dropfiles.splice(i, 1)
								dropfiles = dropfiles.slice()
								if (dropfiles.length === 0) {
									alertfile = false
								}
							}}
						>
							<X class="h-4 w-4" />
						</Button>
					</div>
				{/each}
			{/if}
		</AlertDialog.Header>
		<AlertDialog.Footer>
			<AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
			<AlertDialog.Action
				on:click={() => {
					postdropfile()
				}}>Upload</AlertDialog.Action
			>
		</AlertDialog.Footer>
	</AlertDialog.Content>
</AlertDialog.Root>

<div class="grid h-screen w-full">
	<div class="flex flex-col">
		<header
			class="sticky top-0 z-10 flex h-[57px] items-center gap-1 border-b bg-background px-4"
		>
			<h1 class="text-xl font-semibold">Anyknowledge</h1>
		</header>
		<main class="grid flex-1 gap-4 overflow-auto p-4">
			<div class="relative flex h-full min-h-[50vh] flex-col rounded-xl bg-muted/50 p-4">
				<Badge variant="outline" class="absolute right-8 top-3">Upload</Badge>
				<div class="relative flex-1">
					<div
						class="absolute bottom-0 left-0 right-0 top-0 overflow-y-auto overflow-x-hidden scrollbar-none"
						bind:this={chatArea}
					>
						{#await chatPromise}
							<p class="text-center">Loading...</p>
						{:then value}
							{#if value.length === 0}
								<p class="text-center">Nothing in knowledge</p>
							{:else}
								{#each value as post}
									<Talkbox
										file_id={post.file_id}
										name={defauledata.username}
										context={post.context}
										ext={post.ext}
										filename={post.name}
										avatar={defauledata.avatar}
										timestamp={post.time.$date}
									/>
								{/each}
								<div class="h-6"></div>
							{/if}
						{:catch error}
							<p class="text-center">{error.message}</p>
						{/await}
					</div>
				</div>
				<form
					class="relative overflow-hidden rounded-lg border bg-background focus-within:ring-1 focus-within:ring-ring"
				>
					<Label for="message" class="sr-only">Message</Label>
					<div class="flex max-h-32 items-start overflow-y-auto px-3 pt-0 scrollbar-thin">
						<div class="sticky top-0">
							<Tooltip.Root>
								<Tooltip.Trigger asChild let:builder>
									<input
										type="file"
										bind:this={fileInput}
										bind:files={file}
										style="display: none;"
									/>
									<Button
										variant="ghost"
										size="icon"
										builders={[builder]}
										on:click={readTextFile}
									>
										<Paperclip class="size-4" />
										<span class="sr-only">Attach file</span>
									</Button>
								</Tooltip.Trigger>
								<Tooltip.Content side="top">Attach File</Tooltip.Content>
							</Tooltip.Root>
						</div>
						<Textarea
							id="message"
							placeholder="Add to knowledge"
							class="h-[20px] min-h-4 resize-none border-0 p-3 shadow-none focus-visible:ring-0 focus-visible:ring-offset-0"
							bind:value={input}
							on:keydown={(e) => {
								if (e.key === 'Enter' && !e.shiftKey) {
									e.preventDefault()
									posttext(input)
									input = ''
								}
							}}
						/>
						<Button
							type="submit"
							size="sm"
							class="sticky top-[0.3rem] ml-auto  gap-1.5"
							on:click={() => {
								posttext(input)
								input = ''
							}}
						>
							<CornerDownLeft class="size-3.5" />
						</Button>
					</div>
				</form>
			</div>
		</main>
	</div>
</div>
