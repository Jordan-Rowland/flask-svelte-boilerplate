<script>
	let rand = 0;

  const getRand = async () => {
		const res = await fetch("./rand");
		const jsonRes = await res.json();
		rand = jsonRes['random_number'];
	};

	let posts;

	let vStamp = Date.now()

	const getPosts = async () => {
		let res = await fetch("./posts");
		res = await res.json();
		posts = res['posts'];
	}

	let images;



	/* How to pass a value to an endpoint */
	// let sub;

	// const getImages = async () => {
		// let res = await fetch(`./images/${sub}`);
	// 	res = await res.json();
	// 	images = res['data'];
	// }



</script>

<main>
	<h1>Your number is {rand}</h1>
	<button on:click={getRand}>Get a random number</button>

	<button on:click={getPosts}>Fetch Posts</button>

	v{vStamp}

	{#if posts}
		{#each posts as post}
		  <p>
			  Username: {post['username']}
		  </p>
		  <p>
			  Message: {post['message']}
		  </p>
		{/each}
	{:else}
		<div>
			No posts
		</div>
	{/if}

</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

</style>
