<div class="loader"></div>

<style>
	.loader {
		width: 40px;
		aspect-ratio: 1;
		display: grid;
		border: 4px solid #0000;
		border-radius: 50%;
		border-color: #ccc #0000;
		animation: l16 1s infinite linear;
	}
	.loader::before,
	.loader::after {
		content: '';
		grid-area: 1/1;
		margin: 2px;
		border: inherit;
		border-radius: 50%;
	}
	.loader::before {
		border-color: #f03355 #0000;
		animation: inherit;
		animation-duration: 0.5s;
		animation-direction: reverse;
	}
	.loader::after {
		margin: 8px;
	}
	@keyframes l16 {
		100% {
			transform: rotate(1turn);
		}
	}
</style>
