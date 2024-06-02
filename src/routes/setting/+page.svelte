<script context="module" lang="ts">
	import { z } from 'zod'

	export const formSchema = z.object({
		username: z.string().min(2).max(50),
		avatar: z.string().url()
	})

	export type FormSchema = typeof formSchema
</script>

<script lang="ts">
	import { Input } from '$lib/components/ui/input'
	import { Separator } from '$lib/components/ui/separator'
	import * as Form from '$lib/components/ui/form'
	import { superForm, defaults } from 'sveltekit-superforms'
	import { zodClient } from 'sveltekit-superforms/adapters'
	import SuperDebug from 'sveltekit-superforms'

	const initialData = {
		username: 'user',
		avatar: 'https://cdn.discordapp.com/avatars/762484891945664542/a3d0e4d30b78ce30a2ed22b51bf80df4.png?size=1024'
	}

	const form = superForm(defaults(initialData, zodClient(formSchema)), {
		SPA: true,
		validators: zodClient(formSchema),
		onSubmit() {
			localStorage.setItem('default', JSON.stringify($formData))
		}
	})
	const { form: formData, enhance } = form
</script>

<div>
	<h3 class="text-lg font-medium">Default</h3>
	<p class="text-sm text-muted-foreground">...</p>
</div>
<Separator class="my-5" />

<form method="POST" use:enhance>
	<Form.Field {form} name="username">
		<Form.Control let:attrs>
			<Form.Label>Username</Form.Label>
			<Input {...attrs} bind:value={$formData.username} />
		</Form.Control>
		<Form.Description>This is your public display name.</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="avatar">
		<Form.Control let:attrs>
			<Form.Label>Avatar</Form.Label>
			<Input {...attrs} bind:value={$formData.avatar} />
		</Form.Control>
		<Form.Description>This is your public display name.</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Button>Submit</Form.Button>
</form>
<SuperDebug data={$formData} />
