<script context="module" lang="ts">
	import { z } from 'zod'

	export const formSchema = z.object({
		model: z.string(),
		maxtoken: z.number().int().min(10).max(2000),
		apikey: z.string()
	})

	export type FormSchema = typeof formSchema
</script>

<script lang="ts">
	import { Input } from '$lib/components/ui/input'
	import { Separator } from '$lib/components/ui/separator'
	import * as Form from '$lib/components/ui/form'
	import { superForm } from 'sveltekit-superforms'
	import { zodClient } from 'sveltekit-superforms/adapters'
	import * as Select from '$lib/components/ui/select'
	let defauledata = JSON.parse(localStorage.getItem('chat') as string)
	const form = superForm(defauledata, {
		SPA: true,
		validators: zodClient(formSchema),
		resetForm: false,
		onSubmit() {
			localStorage.setItem('chat', JSON.stringify($formData))
		}
	})
	const { form: formData, enhance } = form
	$: selectedEmail = {
		label: $formData.model,
		value: $formData.model
	}
</script>

<div>
	<h3 class="text-lg font-medium">Chat</h3>
</div>
<Separator class="my-5" />

<form use:enhance>
	<Form.Field {form} name="model">
		<Form.Control let:attrs>
			<Form.Label>Model</Form.Label>
			<Select.Root
				selected={selectedEmail}
				onSelectedChange={(s) => {
					s && ($formData.model = s.value)
				}}
			>
				<Select.Trigger {...attrs}>
					<Select.Value />
				</Select.Trigger>
				<Select.Content>
					<Select.Item value="gpt-4" label="gpt-4" />
					<Select.Item value="gpt-3.5-turbo" label="pt-3.5-turbo" />
					<Select.Item value="gpt-3.5-turbo-0125" label="gpt-3.5-turbo-0125" />
					<Select.Item value="gpt-4-turbo" label="gpt-4-turbo" />
					<Select.Item value="gpt-4o" label="gpt-4o" />
					<Select.Item value="gpt-4-turbo-preview" label="gpt-4-turbo-preview" />
				</Select.Content>
			</Select.Root>
		</Form.Control>
		<Form.Description>Select a model to use</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="maxtoken">
		<Form.Control let:attrs>
			<Form.Label>MaxToken</Form.Label>
			<Input {...attrs} bind:value={$formData.maxtoken} />
		</Form.Control>
		<Form.Description>max token low: 10 max: 2000</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="apikey">
		<Form.Control let:attrs>
			<Form.Label>Apikey</Form.Label>
			<Input {...attrs} bind:value={$formData.apikey} />
		</Form.Control>
		<Form.Description>openai key</Form.Description>
		<Form.FieldErrors />
	</Form.Field>

	<Form.Button>Submit</Form.Button>
</form>
