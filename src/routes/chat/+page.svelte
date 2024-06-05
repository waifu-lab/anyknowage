<script lang="ts">
	import CornerDownLeft from 'lucide-svelte/icons/corner-down-left'
	import { Badge } from '$lib/components/ui/badge/index.js'
	import { Button } from '$lib/components/ui/button/index.js'
	import { Textarea } from '$lib/components/ui/textarea/index.js'
	import { Label } from '$lib/components/ui/label/index.js'
	import Talkbox from '$lib/components/talkbox/talkbox.svelte'
	import { tick } from 'svelte'
	import toast from 'svelte-french-toast'
	let chatstr = ''
	export let data

	let defauledata = JSON.parse(localStorage.getItem('default') as string)

	let chatTrigger = 0
	let istinking = false
	let chatArea: HTMLElement

	let chats = []
	let chatPromise = data.chats(chatTrigger)

	$: if (chatPromise) {
		chatPromise.then((value) => {
			chats = value
			scrollToBottom(chatArea)
		})
	}

	const scrollToBottom = async (node: HTMLElement, smooth = false) => {
		if (!node) return
		await tick()
		if (smooth) {
			node.scroll({ top: node.scrollHeight, behavior: 'smooth' })
		} else {
			node.scrollTop = node.scrollHeight
		}
	}

	async function chat(message: string) {
		if (!message.trim()) return
		istinking = true
		scrollToBottom(chatArea, true)
		try {
			await data.chat(message)
		} catch (e) {
			toast.error('something wrong', {
				position: 'top-right',
				style: 'background: var(--background); color: var(--foreground);'
			})
		}
		chatTrigger += 1
		chatPromise = data.chats(chatTrigger)
		chatPromise.then(() => {
			istinking = false
		})
	}
</script>

<div class="grid h-screen w-full">
	<div class="flex flex-col">
		<header
			class="sticky top-0 z-10 flex h-[57px] items-center gap-1 border-b bg-background px-4"
		>
			<h1 class="text-xl font-semibold">Anyknowledge</h1>
		</header>
		<main class="grid flex-1 gap-4 overflow-auto p-4">
			<div class="relative flex h-full min-h-[50vh] flex-col rounded-xl bg-muted/50 p-4">
				<Badge variant="outline" class="absolute right-8 top-3">Chat</Badge>
				<div class="relative flex-1">
					<div
						class="absolute bottom-0 left-0 right-0 top-0 overflow-y-auto overflow-x-hidden scrollbar-none"
						bind:this={chatArea}
					>
						{#await chatPromise}
							<p class="text-center">Loading...</p>
						{:then value}
							{#if value.length === 0 && !istinking}
								<p class="text-center">you haven't chat yet</p>
							{:else}
								{#each value.reverse() as chat}
									<Talkbox
										name="User"
										messages={[chat.ask]}
										avatar={defauledata.avatar}
									/>
									<Talkbox
										name="Bot"
										messages={[chat.answer.answer]}
										avatar={defauledata.botavatar}
									/>
								{/each}
								{#if istinking}
									<Talkbox
										name="Bot"
										messages={['Thinking...']}
										avatar={defauledata.botavatar}
										isloading={true}
									/>
								{/if}
							{/if}
						{:catch error}
							<p class="text-center">{error.message}</p>
						{/await}
						<div class="h-6"></div>
					</div>
				</div>
				<form
					class="relative overflow-hidden rounded-lg border bg-background focus-within:ring-1 focus-within:ring-ring"
					on:submit={(e) => {
						e.preventDefault()
						chat(chatstr)
						chatstr = ''
					}}
				>
					<Label for="message" class="sr-only">Message</Label>
					<div class="flex max-h-32 items-start overflow-y-auto px-3 pt-0 scrollbar-thin">
						<Textarea
							id="message"
							placeholder="Type your message here..."
							class="h-[20px] min-h-4 resize-none border-0 p-3 shadow-none focus-visible:ring-0 focus-visible:ring-offset-0"
							bind:value={chatstr}
							on:keydown={(e) => {
								if (e.key === 'Enter' && !e.shiftKey) {
									e.preventDefault()
									chat(chatstr)
									chatstr = ''
								}
							}}
						/>
						<Button type="submit" size="sm" class="sticky top-[0.3rem] ml-auto gap-1.5">
							<CornerDownLeft class="size-3.5" />
						</Button>
					</div>
				</form>
			</div>
		</main>
	</div>
</div>
