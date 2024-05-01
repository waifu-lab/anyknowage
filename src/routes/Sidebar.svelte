<script lang="ts">
	import Triangle from 'lucide-svelte/icons/triangle'
	import SquareTerminal from 'lucide-svelte/icons/square-terminal'
	import Settings from 'lucide-svelte/icons/settings'
	import Archive from 'lucide-svelte/icons/Archive'
	import MessageCircleMore from 'lucide-svelte/icons/message-circle-more'

	import { Button } from '$lib/components/ui/button/index.js'
	import * as Tooltip from '$lib/components/ui/tooltip/index.js'
</script>

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
                    aria-label="Talk"
                    builders={[builder]}
                >
                    <MessageCircleMore class="size-5" />
                </Button>
            </Tooltip.Trigger>
            <Tooltip.Content side="right" sideOffset={5}>Talk</Tooltip.Content>
        </Tooltip.Root>
        <Tooltip.Root>
            <Tooltip.Trigger asChild let:builder>
                <Button
                    variant="ghost"
                    size="icon"
                    class="rounded-lg"
                    aria-label="Archive"
                    builders={[builder]}
                >
                    <Archive class="size-5" />
                </Button>
            </Tooltip.Trigger>
            <Tooltip.Content side="right" sideOffset={5}>Archive</Tooltip.Content>
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
                    aria-label="Setting"
                    builders={[builder]}
                >
                    <Settings class="size-5" />
                </Button>
            </Tooltip.Trigger>
            <Tooltip.Content side="right" sideOffset={5}>Setting</Tooltip.Content>
        </Tooltip.Root>
    </nav>
</aside>