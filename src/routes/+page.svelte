<script lang="ts">
	import Paperclip from 'lucide-svelte/icons/paperclip'
	import CornerDownLeft from 'lucide-svelte/icons/corner-down-left'

	import { Badge } from '$lib/components/ui/badge/index.js'
	import { Button } from '$lib/components/ui/button/index.js'
	import * as Tooltip from '$lib/components/ui/tooltip/index.js'
	import { Textarea } from '$lib/components/ui/textarea/index.js'
	import { Label } from '$lib/components/ui/label/index.js'
	import Talkbox from '$lib/components/talkbox/talkbox.svelte'
	export let data
	const { posts } = data
	console.log(posts)
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
				<Badge variant="outline" class="absolute right-8 top-3">Upload</Badge>
				<div class="relative flex-1">
					<div
						class="absolute bottom-0 left-0 right-0 top-0 overflow-y-auto overflow-x-hidden scrollbar-none"
					>
						{#await posts then value}
							{#if value.length === 0}
								<p class="text-center">Nothing in knowledge</p>
							{:else}
								{#each value as post}
									<Talkbox
										name="User"
										context={post.context}
										ext={post.ext}
										filename={post.name}
										avatar="https://cdn.discordapp.com/avatars/762484891945664542/a3d0e4d30b78ce30a2ed22b51bf80df4.png?size=1024"
										timestamp={post.time.$date}
									/>
								{/each}
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
					<div class="flex max-h-32 items-start overflow-y-auto p-3 pt-0 scrollbar-thin">
						<div class="sticky top-0">
							<Tooltip.Root>
								<Tooltip.Trigger asChild let:builder>
									<Button variant="ghost" size="icon" builders={[builder]}>
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
						/>
						<Button
							type="submit"
							size="sm"
							class="sticky top-[0.5rem] ml-auto  gap-1.5"
						>
							Send Message
							<CornerDownLeft class="size-3.5" />
						</Button>
					</div>
				</form>
			</div>
		</main>
	</div>
</div>
