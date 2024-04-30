<script lang="ts">
	import Triangle from 'lucide-svelte/icons/triangle'
	import SquareTerminal from 'lucide-svelte/icons/square-terminal'
	import Settings from 'lucide-svelte/icons/settings'
	import Paperclip from 'lucide-svelte/icons/paperclip'
	import Mic from 'lucide-svelte/icons/mic'
	import CornerDownLeft from 'lucide-svelte/icons/corner-down-left'
	import Archive from 'lucide-svelte/icons/Archive'
	import MessageCircleMore from 'lucide-svelte/icons/message-circle-more'

	import { Badge } from '$lib/components/ui/badge/index.js'
	import { Button } from '$lib/components/ui/button/index.js'
	import * as Tooltip from '$lib/components/ui/tooltip/index.js'
	import { Textarea } from '$lib/components/ui/textarea/index.js'
	import { Label } from '$lib/components/ui/label/index.js'
</script>

<div class="grid h-screen w-full pl-[53px]">
	<aside class="inset-y fixed left-0 z-20 flex h-full flex-col border-r">
		<div class="border-b p-2">
			<Button variant="outline" size="icon" aria-label="Home">
				<Triangle class="size-5 fill-foreground" />
			</Button>
		</div>
		<nav class="grid gap-1 p-2">
			<Tooltip.Root>
				<Tooltip.Trigger asChild let:builder>
					<Button
						variant="ghost"
						size="icon"
						class="rounded-lg bg-muted"
						aria-label="Playground"
						builders={[builder]}
					>
						<MessageCircleMore class="size-5" />
					</Button>
				</Tooltip.Trigger>
				<Tooltip.Content side="right" sideOffset={5}>Playground</Tooltip.Content>
			</Tooltip.Root>
			<Tooltip.Root>
				<Tooltip.Trigger asChild let:builder>
					<Button
						variant="ghost"
						size="icon"
						class="rounded-lg"
						aria-label="Models"
						builders={[builder]}
					>
						<Archive class="size-5" />
					</Button>
				</Tooltip.Trigger>
				<Tooltip.Content side="right" sideOffset={5}>Models</Tooltip.Content>
			</Tooltip.Root>
			<Tooltip.Root>
				<Tooltip.Trigger asChild let:builder>
					<Button
						variant="ghost"
						size="icon"
						class="rounded-lg"
						aria-label="API"
						builders={[builder]}
					>
						<SquareTerminal class="size-5" />
					</Button>
				</Tooltip.Trigger>
				<Tooltip.Content side="right" sideOffset={5}>API</Tooltip.Content>
			</Tooltip.Root>
		</nav>
		<nav class="mt-auto grid gap-1 p-2">
			<Tooltip.Root>
				<Tooltip.Trigger asChild let:builder>
					<Button
						variant="ghost"
						size="icon"
						class="mt-auto rounded-lg"
						aria-label="Account"
						builders={[builder]}
					>
						<Settings class="size-5" />
					</Button>
				</Tooltip.Trigger>
				<Tooltip.Content side="right" sideOffset={5}>Account</Tooltip.Content>
			</Tooltip.Root>
		</nav>
	</aside>
	<div class="flex flex-col">
		<header class="sticky top-0 z-10 flex h-[57px] items-center gap-1 border-b bg-background px-4">
			<h1 class="text-xl font-semibold">Anyknowledge</h1>
		</header>
		<main class="grid flex-1 gap-4 overflow-auto p-4 md:grid-cols-2 lg:grid-cols-3">
			<div
				class="relative flex h-full min-h-[50vh] flex-col rounded-xl bg-muted/50 p-4 lg:col-span-2"
			>
				<Badge variant="outline" class="absolute right-3 top-3">Output</Badge>
				<div class="flex-1" />
				<form
					class="relative overflow-hidden rounded-lg border bg-background focus-within:ring-1 focus-within:ring-ring"
				>
					<Label for="message" class="sr-only">Message</Label>
					<Textarea
						id="message"
						placeholder="Type your message here..."
						class="min-h-12 resize-none border-0 p-3 shadow-none focus-visible:ring-0"
					/>
					<div class="flex items-center p-3 pt-0">
						<Tooltip.Root>
							<Tooltip.Trigger asChild let:builder>
								<Button variant="ghost" size="icon" builders={[builder]}>
									<Paperclip class="size-4" />
									<span class="sr-only">Attach file</span>
								</Button>
							</Tooltip.Trigger>
							<Tooltip.Content side="top">Attach File</Tooltip.Content>
						</Tooltip.Root>
						<Tooltip.Root>
							<Tooltip.Trigger asChild let:builder>
								<Button variant="ghost" size="icon" builders={[builder]}>
									<Mic class="size-4" />
									<span class="sr-only">Use Microphone</span>
								</Button>
							</Tooltip.Trigger>
							<Tooltip.Content side="top">Use Microphone</Tooltip.Content>
						</Tooltip.Root>
						<Button type="submit" size="sm" class="ml-auto gap-1.5">
							Send Message
							<CornerDownLeft class="size-3.5" />
						</Button>
					</div>
				</form>
			</div>
		</main>
	</div>
</div>
