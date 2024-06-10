<script context="module" lang="ts">
	import { z } from 'zod'

	export const formSchema = z.object({
		server_url: z.string().url(),
		username: z.string().min(2).max(50),
		avatar: z.string().url(),
		botavatar: z.string().url()
	})

	export type FormSchema = typeof formSchema
</script>

<script lang="ts">
	import { Input } from '$lib/components/ui/input'
	import { Separator } from '$lib/components/ui/separator'
	import * as Form from '$lib/components/ui/form'
	import { superForm } from 'sveltekit-superforms'
	import { zodClient } from 'sveltekit-superforms/adapters'
	import toast from 'svelte-french-toast'
	let defauledata = JSON.parse(localStorage.getItem('default') as string)
	const form = superForm(defauledata, {
		SPA: true,
		validators: zodClient(formSchema),
		resetForm: false,
		onSubmit() {
			localStorage.setItem('default', JSON.stringify($formData))
			toast.success('Saved', {
				position: 'top-right',
				style: 'background: var(--background); color: var(--foreground);'
			})
		}
	})
	const { form: formData, enhance } = form
</script>

<div>
	<h3 class="text-lg font-medium">Default</h3>
</div>
<Separator class="my-5" />

<form use:enhance>
	<Form.Field {form} name="server_url">
		<Form.Control let:attrs>
			<Form.Label>Server_url</Form.Label>
			<Input {...attrs} bind:value={$formData.server_url} />
		</Form.Control>
		<Form.Description>Anyknowledge server url</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="username">
		<Form.Control let:attrs>
			<Form.Label>Username</Form.Label>
			<Input {...attrs} bind:value={$formData.username} />
		</Form.Control>
		<Form.Description>name in display</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="avatar">
		<Form.Control let:attrs>
			<Form.Label>Avatar</Form.Label>
			<Input {...attrs} bind:value={$formData.avatar} />
		</Form.Control>
		<Form.Description>user image for display (only url)</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="botavatar">
		<Form.Control let:attrs>
			<Form.Label>BotAvatar</Form.Label>
			<Input {...attrs} bind:value={$formData.botavatar} />
		</Form.Control>
		<Form.Description>user image for display (only url)</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Button>Submit</Form.Button>
</form>
